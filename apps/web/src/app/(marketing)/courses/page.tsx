import type { Metadata } from "next";
import Link from "next/link";
import { ArrowUpRight, BookOpen } from "lucide-react";
import { CourseGrid } from "@/components/catalog/course-card";
import { CourseFilters } from "@/components/catalog/filters";
import { SortSelect } from "@/components/catalog/sort-select";
import { Pagination } from "@/components/catalog/pagination";
import {
  COURSE_QUERY_KEYS,
  firstValue,
  valueList,
  publicFetch,
  toQuery,
  type Category,
  type CourseCard,
  type Paginated,
} from "@/lib/catalog";
import { getLocale } from "@/lib/locale";
import { translate } from "@/lib/translations";
export const metadata: Metadata = { title: "Khóa học / Courses" };
type Search = Record<string, string | string[] | undefined>;
export default async function CoursesPage({
  searchParams,
}: {
  searchParams: Promise<Search>;
}) {
  const [params, locale] = await Promise.all([searchParams, getLocale()]);
  const t = (vi: string, en?: string) => translate(locale, vi, en);
  const state = {
    q: firstValue(params.q),
    category: valueList(params.category),
    level: valueList(params.level),
    priceVndMin: firstValue(params.priceVndMin),
    priceVndMax: firstValue(params.priceVndMax),
    sort: firstValue(params.sort) ?? "publishedAt:desc",
  };
  const [courses, categories] = await Promise.all([
    publicFetch<Paginated<CourseCard>>(
      "/courses" + toQuery({ ...params, sort: state.sort }, COURSE_QUERY_KEYS),
      60,
    ).catch(() => null),
    publicFetch<{ items: Category[] }>("/categories", 60).catch(() => ({
      items: [],
    })),
  ]);
  const visibleCategories = categories.items.filter(
    (category) =>
      category.courseCount > 0 || state.category.includes(category.slug),
  );
  const hasFilters = Boolean(
    state.q ||
    state.category.length ||
    state.level.length ||
    state.priceVndMin ||
    state.priceVndMax,
  );
  return (
    <div className="page-shell">
      <header className="catalog-hero">
        <p className="section-label">
          <span className="context-dot" />
          01 / {t("TỪ KIẾN THỨC ĐẾN ỨNG DỤNG", "FROM KNOWING TO MAKING")}
        </p>
        <h1 tabIndex={-1}>
          {t("Từ bài học nhỏ", "From small lessons")}
          <br />
          {t("đến", "to")} <em>{t("dự án có ích.", "useful projects.")}</em>
        </h1>
        <p>
          {t(
            "Học kiến thức nền tảng, làm theo từng bước và thử một dự án của riêng mình. Có bài đọc, bài tập và mã nguồn để bạn thực sự bắt tay vào làm.",
            "Learn the fundamentals, follow the steps, and build a project of your own. Written lessons, exercises, and source files help you put it into practice.",
          )}
        </p>
        <div className="catalog-hero-bottom">
          <span>
            {t(
              "Python · Web · Tư duy giải quyết vấn đề",
              "Python · Web · Problem solving",
            )}
          </span>
          <Link href="/workshop" className="inline-link">
            {t(
              "Chưa biết bắt đầu? Thử bài mở",
              "Not sure where to start? Try the open lesson",
            )}{" "}
            <ArrowUpRight size={17} aria-hidden="true" />
          </Link>
        </div>
      </header>
      <section className="course-catalog" aria-labelledby="catalog-title">
        <aside
          className="catalog-filters"
          aria-label={t("Bộ lọc khóa học", "Course filters")}
        >
          <h2>{t("Tìm một khóa học", "Find your course")}</h2>
          <CourseFilters
            action="/courses"
            categories={visibleCategories}
            state={state}
            locale={locale}
          />
        </aside>
        <div className="catalog-results">
          <header className="catalog-results-heading">
            <div>
              <h2 id="catalog-title">
                {t("Thư viện khóa học", "Course library")}
              </h2>
              <p>
                {courses
                  ? courses.total +
                    " " +
                    t("khóa học", courses.total === 1 ? "course" : "courses")
                  : t("Đang kết nối thư viện", "Connecting to the library")}
              </p>
            </div>
            <SortSelect value={state.sort} basePath="/courses" query={params} />
          </header>
          {hasFilters && (
            <Link className="inline-link mb-5" href="/courses">
              {t("Xóa bộ lọc", "Clear filters")}
            </Link>
          )}
          {courses?.items.length ? (
            <>
              <CourseGrid courses={courses.items} />
              <Pagination
                basePath="/courses"
                query={params}
                page={courses.page}
                totalPages={courses.totalPages}
                total={courses.total}
              />
            </>
          ) : (
            <div className="catalog-empty">
              <BookOpen size={25} aria-hidden="true" />
              <h3>
                {courses
                  ? t("Chưa có khóa học phù hợp", "No matching courses")
                  : t(
                      "Chưa kết nối được thư viện",
                      "The course library is unavailable",
                    )}
              </h3>
              <p>
                {courses
                  ? t(
                      "Thử từ khóa ngắn hơn hoặc xóa bộ lọc để xem toàn bộ khóa học.",
                      "Try a shorter keyword or clear the filters to see all courses.",
                    )
                  : t(
                      "Bạn có thể thử bài thực hành mở trong lúc kết nối lại.",
                      "You can try the open practice project while the connection is restored.",
                    )}
              </p>
              <Link
                href={courses ? "/courses" : "/workshop"}
                className="studio-button"
              >
                {courses
                  ? t("Xem tất cả khóa học", "Show all courses")
                  : t("Mở bài thực hành", "Open practice")}
              </Link>
            </div>
          )}
          <p className="course-format-note">
            {t(
              "Các khóa dự án mới: bài đọc + thực hành, mã nguồn có sẵn. Video hướng dẫn đang chuẩn bị. Nội dung mẫu của hệ thống được đánh dấu riêng.",
              "New project courses: written lessons, practice, and source files. Teaching videos are in preparation. Inherited sample courses are labeled separately.",
            )}
          </p>
        </div>
      </section>
    </div>
  );
}
