import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { EnrollCta } from "@/components/catalog/enroll-cta";
import { projectCourses } from "./project-courses";

describe("project catalog access and readiness", () => {
  it("offers exactly one public trial and nine paid project outlines", () => {
    const trials = projectCourses.filter((course) => course.publicTrial);
    const paid = projectCourses.filter((course) => !course.publicTrial);
    expect(trials).toHaveLength(1);
    expect(trials[0].priceVnd).toBe(0);
    expect(trials[0].lessons).toHaveLength(4);
    expect(new Set(trials[0].lessons.map((lesson) => lesson.video)).size).toBe(
      4,
    );
    expect(paid).toHaveLength(9);
    for (const course of paid) {
      expect([100000, 150000, 200000]).toContain(course.priceVnd);
      expect(course.availability).toBe("planned");
      expect(course.lessons).toHaveLength(0);
      expect(course.milestones?.length).toBeGreaterThanOrEqual(3);
    }
  });

  it("lets a guest open the whole book trial without authentication", () => {
    const html = renderToStaticMarkup(
      createElement(EnrollCta, {
        courseId: "book-trial",
        slug: "python-tu-sach-lop-minh",
        priceVnd: 0,
        archived: false,
      }),
    );
    expect(html).toContain('href="/workshop"');
    expect(html).not.toContain("/login");
    expect(html).not.toContain("/checkout");
  });

  it("shows a project inquiry rather than selling unfinished lessons", () => {
    const course = projectCourses.find((item) => item.priceVnd === 200000)!;
    const html = renderToStaticMarkup(
      createElement(EnrollCta, {
        courseId: "planned",
        slug: course.slug,
        priceVnd: course.priceVnd,
        archived: false,
      }),
    );
    expect(html).toContain("Hỏi Nam về dự án");
    expect(html).toContain("Chưa mở đăng ký học");
    expect(html).not.toContain("/learn/");
    expect(html).not.toContain("Liên hệ đăng ký học");
  });
});
