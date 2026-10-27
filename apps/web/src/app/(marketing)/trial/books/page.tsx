import type { Metadata } from "next";
import Link from "next/link";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { ArrowLeft, ArrowRight, BookOpen, Download } from "lucide-react";
import { Prose } from "@/components/catalog/sections";
import { getLocale } from "@/lib/locale";
import { projectCourse } from "@/lib/project-courses";

export const metadata: Metadata = {
  title: "Tủ sách chia sẻ · Học thử miễn phí / Free book project",
  description:
    "Bốn video làm dự án tủ sách bằng Python. Miễn phí, không cần tài khoản.",
  alternates: { canonical: "/trial/books" },
};

/** Explicitly public material. Paid lessons continue through the authenticated player. */
export default async function BookTrialPage() {
  const project = projectCourse("python-tu-sach-lop-minh")!;
  const locale = await getLocale();
  const t = (vi: string, en: string) => (locale === "vi" ? vi : en);
  const notes = await Promise.all(
    project.lessons.map((lesson) =>
      readFile(
        resolve(process.cwd(), "../../content/project-lessons", lesson.file),
        "utf8",
      ),
    ),
  );
  return (
    <div className="page-shell book-trial">
      <Link href="/courses" className="inline-link">
        <ArrowLeft size={17} aria-hidden="true" />
        {t("Về các dự án", "Back to projects")}
      </Link>
      <header className="trial-intro">
        <p className="section-label">
          01 / {t("DỰ ÁN HỌC THỬ MIỄN PHÍ", "FREE TRIAL PROJECT")}
        </p>
        <h1>{t("Tủ sách của lớp mình.", "Your class, sharing books.")}</h1>
        <p>
          {t(
            "Cùng Nam làm một công cụ tìm sách, mượn/trả và lưu dữ liệu bằng Python. Bốn video, bài đọc và mã tham khảo — mở cho mọi người, không cần tài khoản.",
            "Build a Python tool with Nam to find books, record loans and returns, and save your data. Four videos, written notes, and reference code — open to everyone, with no account required.",
          )}
        </p>
        <div className="trial-facts">
          <span>{t("Miễn phí", "Free")}</span>
          <span>4 {t("video", "videos")}</span>
          <span>Python 3</span>
          <span>
            {t("Âm thanh & bài đọc: tiếng Việt", "Audio & notes: Vietnamese")}
          </span>
        </div>
        <a
          href="/downloads/projects/book-sharing.py"
          download
          className="inline-link"
        >
          <Download size={17} aria-hidden="true" />
          {t("Tải mã tham khảo", "Download reference code")}
        </a>
      </header>
      <nav
        aria-label={t("Bốn bài học", "Four lessons")}
        className="trial-chapters"
      >
        {project.lessons.map((lesson, index) => (
          <a href={`#lesson-${index + 1}`} key={lesson.title}>
            <span>0{index + 1}</span>
            {lesson.title.slice(5)}
          </a>
        ))}
      </nav>
      <div className="trial-lessons">
        {project.lessons.map((lesson, index) => (
          <section
            id={`lesson-${index + 1}`}
            key={lesson.title}
            className="trial-lesson"
            aria-labelledby={`lesson-title-${index + 1}`}
          >
            <header>
              <p className="section-label">
                {t("BÀI", "LESSON")} 0{index + 1}
              </p>
              <h2 id={`lesson-title-${index + 1}`}>{lesson.title.slice(5)}</h2>
            </header>
            <video
              controls
              playsInline
              preload="metadata"
              aria-label={lesson.title}
              src={lesson.video}
            >
              {t(
                "Trình duyệt của bạn chưa hỗ trợ video này.",
                "Your browser does not support this video.",
              )}
            </video>
            <p className="trial-video-help">
              {t(
                "Dừng video để tự làm trước khi xem tiếp. Có thể chọn tốc độ phát trong trình đơn của trình phát. Video hiện chưa có phụ đề.",
                "Pause to try each step yourself. Playback speed is available in the player menu. Captions are not available yet.",
              )}
            </p>
            <details className="panel trial-notes">
              <summary>
                <BookOpen size={18} aria-hidden="true" />
                {t("Bài đọc & thực hành", "Written notes & practice")}
              </summary>
              <Prose source={notes[index]} />
            </details>
          </section>
        ))}
      </div>
      <section className="trial-next">
        <p className="section-label">
          {t("SAU TỦ SÁCH", "AFTER THE BOOK PROJECT")}
        </p>
        <h2>
          {t(
            "Một vấn đề khác. Một dự án mới.",
            "Another problem. A new project.",
          )}
        </h2>
        <p>
          {t(
            "Chín dự án Python tiếp theo đang được chuẩn bị, với mức học phí từ 300.000₫ đến 500.000₫. Xem phạm vi dự kiến trước khi chọn hướng bạn muốn học tiếp.",
            "Nine more Python projects are in preparation, priced from 300,000₫ to 500,000₫. Explore their planned scope to choose what you want to build next.",
          )}
        </p>
        <Link href="/courses" className="studio-button">
          {t("Khám phá các dự án", "Explore projects")}
          <ArrowRight size={18} aria-hidden="true" />
        </Link>
      </section>
    </div>
  );
}
