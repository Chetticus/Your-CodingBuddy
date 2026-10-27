"use client";
import { UiText } from "@/components/language-provider";
import Link from "next/link";
import { useEffect, useState } from "react";
import type { Paginated } from "@/lib/catalog";
import type { EnrollmentItem } from "@/lib/learning";
import { whoAmI } from "@/lib/viewer";
import { buttonClass } from "@/components/ui/button";
import { Alert } from "@/components/ui/feedback";

type Audience = "unknown" | "guest" | "signed-in" | "enrolled" | "started";

/** Only an ACTIVE enrollment in this course changes the learning CTA. */
export async function audienceOf(courseId: string): Promise<Audience> {
  const user = await whoAmI();
  if (!user) return "guest";
  try {
    const response = await fetch(
      `/api/v1/enrollments/me?courseId=${courseId}&pageSize=1`,
      { credentials: "include", cache: "no-store" },
    );
    if (!response.ok) return "signed-in";
    const [enrollment] = ((await response.json()) as Paginated<EnrollmentItem>)
      .items;
    if (enrollment?.status !== "ACTIVE") return "signed-in";
    return enrollment.progress.completedLessons > 0 ? "started" : "enrolled";
  } catch {
    return "signed-in";
  }
}

/** Paid enrollment is arranged with the tutor; this component creates no order. */
export function EnrollCta({
  courseId,
  slug,
  priceVnd,
  archived,
}: {
  courseId: string;
  slug: string;
  priceVnd: number;
  archived: boolean;
}) {
  const [audience, setAudience] = useState<Audience>("unknown");
  useEffect(() => {
    let active = true;
    audienceOf(courseId).then((result) => {
      if (active) setAudience(result);
    });
    return () => {
      active = false;
    };
  }, [courseId]);

  if (audience === "enrolled" || audience === "started")
    return (
      <div className="min-h-12">
        <Link
          href={`/learn/${slug}`}
          className={buttonClass("primary", "lg", "w-full")}
        >
          <UiText
            value={audience === "started" ? "Tiếp tục học" : "Vào học"}
            en={audience === "started" ? "Continue learning" : "Start learning"}
          />
        </Link>
      </div>
    );
  if (archived)
    return (
      <div className="grid gap-3">
        <span
          aria-disabled="true"
          className={
            buttonClass("outline", "lg") + " pointer-events-none opacity-60"
          }
        >
          <UiText value="Khóa học đã ngừng nhận học viên" />
        </span>
        <Alert variant="info" title="Khóa học đã lưu trữ">
          <UiText value="Khóa học này không còn nhận học viên mới. Người đã có quyền học vẫn học bình thường." />
        </Alert>
      </div>
    );
  if (priceVnd > 0)
    return (
      <div className="grid gap-3">
        <Link
          href={`/checkout/${slug}`}
          className={buttonClass("accent", "lg", "w-full")}
        >
          <UiText value="Liên hệ đăng ký học" en="Contact Nam to enroll" />
        </Link>
        <p className="text-xs leading-relaxed text-muted-foreground">
          <UiText
            value="Trao đổi học phí và cách tham gia trực tiếp với Nam qua Zalo hoặc thông tin liên hệ."
            en="Discuss the fee and how to join directly with Nam through Zalo or the contact details."
          />
        </p>
      </div>
    );
  return (
    <div className="grid gap-3">
      <Link
        href={
          audience === "signed-in"
            ? `/learn/${slug}`
            : `/login?next=${encodeURIComponent("/courses/" + slug)}`
        }
        className={buttonClass("accent", "lg", "w-full")}
      >
        <UiText
          value={
            audience === "signed-in"
              ? "Đọc khóa học miễn phí"
              : "Đăng nhập để đọc bài"
          }
          en={
            audience === "signed-in" ? "Read the free course" : "Log in to read"
          }
        />
      </Link>
      {audience === "signed-in" && (
        <p className="text-xs text-muted-foreground">
          <UiText
            value="Bài đọc mở sau đăng nhập. Tiến độ được lưu khi bạn có quyền học."
            en="Written lessons are open after login. Progress is saved when you have an enrollment."
          />
        </p>
      )}
    </div>
  );
}
