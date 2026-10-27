/** Add the authored project lessons to the isolated review DB. No production seed. */
import 'dotenv/config';
import { readFile, mkdir, copyFile, stat } from 'node:fs/promises';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { PrismaPg } from '@prisma/adapter-pg';
import {
  PrismaClient,
  CourseLevel,
  CourseStatus,
  LessonType,
  StorageProvider,
  EnrollmentStatus,
  EnrollmentSource,
} from '../src/generated/prisma/client.js';
import { PG_SESSION_OPTIONS } from '../src/prisma/pg-session.js';
import { buildSearchText } from '../src/catalog/search-text.js';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '../../..');
const connectionString = process.env.DATABASE_URL ?? '';
const target = new URL(connectionString);
if (
  process.env.NODE_ENV === 'production' ||
  target.hostname !== '127.0.0.1' ||
  target.port !== '55435' ||
  target.pathname !== '/template1'
) {
  throw new Error(
    'This script only writes to the isolated CodingBuddy review database.',
  );
}
type Project = {
  slug: string;
  title: { vi: string; en: string };
  subtitle: { vi: string; en: string };
  categoryName: string;
  categorySlug: string;
  outcomes: string[];
  requirements: string[];
  section: string;
  lessons: { title: string; file: string }[];
  downloads: string[];
};
const projects = JSON.parse(
  await readFile(
    resolve(root, 'apps/web/src/content/project-courses.json'),
    'utf8',
  ),
) as Project[];
const prisma = new PrismaClient({
  adapter: new PrismaPg({ connectionString, ...PG_SESSION_OPTIONS }),
});
const storageRoot = resolve(
  process.cwd(),
  process.env.STORAGE_LOCAL_DIR ?? '.storage',
);
try {
  for (const project of projects) {
    const category = await prisma.category.upsert({
      where: { slug: project.categorySlug },
      create: {
        slug: project.categorySlug,
        name: project.categoryName,
        position: 9,
      },
      update: {},
    });
    const description = `## Bạn sẽ làm được gì?\n\n${project.subtitle.vi}\n\nĐây là khóa học bằng bài đọc và thực hành, gồm ${project.lessons.length} bài có ví dụ, giải thích, bài tập và lời giải để tự kiểm tra. Bạn có thể hoàn thành khóa bằng các bài đọc hiện có, không cần chờ video.\n\n## Cách học\n\nĐọc một phần, chạy thử đoạn code nhỏ rồi làm bài tập trước khi xem mã hoàn chỉnh. Các ví dụ và dữ liệu dùng để học, chưa phải dự án đã được triển khai trong cộng đồng.\n\n## Tệp dự án\n\n${project.downloads.map((file) => `- [${file}](/downloads/projects/${file})`).join('\n')}`;
    const data = {
      title: project.title.vi,
      subtitle: project.subtitle.vi,
      description,
      searchText: buildSearchText(
        project.title.vi + ' ' + project.title.en.replace(/-/g, ' '),
        project.subtitle.vi + ' ' + project.subtitle.en,
      ),
      categoryId: category.id,
      level: CourseLevel.BEGINNER,
      language: 'vi',
      learningOutcomes: project.outcomes,
      requirements: project.requirements,
      targetAudience: [
        'Bạn 10–15 tuổi muốn làm một dự án nhỏ có ích',
        'Người học muốn thực hành và giải thích được điều mình viết',
      ],
      priceVnd: 0,
      compareAtPriceVnd: null,
      status: CourseStatus.PUBLISHED,
      lessonCount: project.lessons.length,
      totalDurationSeconds: 0,
      ratingAverage: null,
      ratingCount: 0,
      demoStats: false,
    };
    const course = await prisma.course.upsert({
      where: { slug: project.slug },
      create: { slug: project.slug, ...data, publishedAt: new Date() },
      update: data,
    });
    const section = await prisma.section.upsert({
      where: { courseId_position: { courseId: course.id, position: 1 } },
      create: { courseId: course.id, position: 1, title: project.section },
      update: { title: project.section },
    });
    for (const [index, entry] of project.lessons.entries()) {
      const content = await readFile(
        resolve(root, 'content/project-lessons', entry.file),
        'utf8',
      );
      const lessonData = {
        title: entry.title,
        type: LessonType.ARTICLE,
        content,
        isPreview: true,
        durationSeconds: 0,
      };
      const lesson = await prisma.lesson.upsert({
        where: {
          sectionId_position: { sectionId: section.id, position: index + 1 },
        },
        create: { sectionId: section.id, position: index + 1, ...lessonData },
        update: lessonData,
      });
      if (index !== project.lessons.length - 1) continue;
      for (const [position, file] of project.downloads.entries()) {
        const source = resolve(
          root,
          'apps/web/public/downloads/projects',
          file,
        );
        const objectKey = `lessons/${lesson.id}/resources/${file}`;
        const destination = resolve(storageRoot, objectKey);
        await mkdir(dirname(destination), { recursive: true });
        await copyFile(source, destination);
        const contentType = file.endsWith('.html')
          ? 'text/html'
          : file.endsWith('.csv')
            ? 'text/csv'
            : 'text/plain';
        const resource = {
          storage: StorageProvider.DEMO,
          objectKey,
          filename: file,
          contentType,
          sizeBytes: (await stat(source)).size,
        };
        await prisma.lessonResource.upsert({
          where: {
            lessonId_position: { lessonId: lesson.id, position: position + 1 },
          },
          create: { lessonId: lesson.id, position: position + 1, ...resource },
          update: resource,
        });
      }
    }
    // Like seed-learning.ts: review fixtures are not a real admin action.
    // Preserve existing progress; give the documented demo learner full access.
    const student = await prisma.user.findUnique({
      where: { email: 'student1@elearning.local' },
    });
    const admin = await prisma.user.findUnique({
      where: { email: 'admin@elearning.local' },
    });
    if (student && admin) {
      await prisma.enrollment.upsert({
        where: { userId_courseId: { userId: student.id, courseId: course.id } },
        create: {
          userId: student.id,
          courseId: course.id,
          status: EnrollmentStatus.ACTIVE,
          source: EnrollmentSource.MANUAL_GRANT,
          grantedById: admin.id,
        },
        update: {},
      });
      await prisma.course.update({
        where: { id: course.id },
        data: {
          enrollmentCount: await prisma.enrollment.count({
            where: { courseId: course.id, status: EnrollmentStatus.ACTIVE },
          }),
        },
      });
    }
    console.log(
      `Local written course ready: ${project.slug} (${project.lessons.length} lessons)`,
    );
  }
} finally {
  await prisma.$disconnect();
}
