import courses from "@/content/project-courses.json";
import type { Locale } from "./translations";

/** Editorial presentation only; the API still owns IDs, access, prices and progress. */
export const projectCourses = courses;
export function projectCourse(slug?: string) {
  return courses.find((course) => course.slug === slug);
}
export function projectCopy(slug: string, locale: Locale) {
  const project = projectCourse(slug);
  return project
    ? { title: project.title[locale], subtitle: project.subtitle[locale] }
    : null;
}
