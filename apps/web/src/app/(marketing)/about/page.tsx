import type { Metadata } from "next";
import Link from "next/link";
import Image from "next/image";
import { ArrowRight } from "lucide-react";
import { getLocale } from "@/lib/locale";
import { translate } from "@/lib/translations";
export const metadata: Metadata = { title: "Câu chuyện / Our story" };
export default async function AboutPage() {
  const locale = await getLocale();
  const t = (vi: string, en?: string) => translate(locale, vi, en);
  return (
    <div className="page-shell">
      <section className="about-intro">
        <div>
          <p className="section-label">
            {t("Câu chuyện của CodingBuddy", "The story of CodingBuddy")}
          </p>
          <h1>
            {t(
              "Mình là Nam.\nRất vui được học cùng bạn.",
              "I’m Nam.\nGood to be learning with you.",
            )}
          </h1>
          <p>
            {t(
              "Mình thích lập trình, robot và cảm giác tìm ra lời giải sau nhiều lần thử. CodingBuddy bắt đầu từ mong muốn chia sẻ cách học đó với những bạn nhỏ hơn.",
              "I like code, robots, and finding a solution after a few attempts. CodingBuddy began with a wish to share that way of learning with younger students.",
            )}
          </p>
          <Link className="inline-link" href="/workshop">
            {t("Cùng thử một bài học", "Try a lesson together")}
            <ArrowRight size={17} aria-hidden="true" />
          </Link>
        </div>
        <aside className="about-note">
          <Image
            src="/images/hai-nam.jpg"
            alt={t("Nguyễn Hải Nam bên robot của mình", "Nguyễn Hải Nam beside his robot")}
            width={1365}
            height={2048}
            sizes="(max-width: 900px) 100vw, 420px"
            priority
            className="about-portrait"
          />
          <h2>
            {t(
              "Hiểu vì sao nó chạy.\nTự tin thử cách khác.",
              "Understand why it works.\nFeel confident trying another way.",
            )}
          </h2>
          <p>
            Nguyễn Hải Nam ·{" "}
            {t("Người sáng lập & người dạy", "Founder & tutor")}
          </p>
        </aside>
      </section>
      <section className="about-reading">
        <h2>
          {t("Cách mình muốn\ncùng bạn học.", "How I’d like\nus to learn.")}
        </h2>
        <div>
          <p>
            {t(
              "Một dự án không cần phải lớn để có ý nghĩa. Có thể chỉ là danh sách giúp một bạn tìm tài liệu, một trang hướng dẫn dễ đọc hơn, hay một công cụ nhỏ tiết kiệm thao tác.",
              "A project doesn’t need to be large to mean something. It might be a list that helps a classmate find a resource, a more readable guide, or a small tool that saves a few steps.",
            )}
          </p>
          <p>
            {t(
              "Chúng mình bắt đầu bằng một nhu cầu, học những kiến thức cần thiết, rồi làm thử. Gặp lỗi là một phần của quá trình. Hỏi người khác dùng có dễ không cũng là một phần của việc học lập trình.",
              "We start with a need, learn the skills we need, and make a first attempt. Bugs are part of the process. Asking someone whether it is easy to use is part of learning to code, too.",
            )}
          </p>
        </div>
      </section>
      <section className="about-reading">
        <h2>{t("Những điều đang\nđược xây dựng.", "What’s\ntaking shape.")}</h2>
        <div>
          <p>
            {t(
              "Mình đang chuẩn bị chuỗi video trực tiếp hướng dẫn làm dự án và các tài liệu kiến thức nền tảng. Trong lúc đó, bài thực hành mở là nơi bạn có thể dùng thử, đọc và sửa code ngay hôm nay.",
              "I’m preparing a series of project-building videos and materials on the fundamentals. Meanwhile, the open practice lesson is a place to try, read, and change code today.",
            )}
          </p>
          <p>
            {t(
              "Về lâu dài, CodingBuddy hướng tới việc mở rộng cơ hội học công nghệ cho trẻ em ở cộng đồng dân tộc thiểu số. Mình muốn cách dạy và các dự án ở đây cùng hướng về việc giúp ích cho người khác.",
              "Over time, CodingBuddy aims to widen access to technology learning for children in ethnic minority communities. I want the teaching and projects here to share that purpose of helping someone.",
            )}
          </p>
          <Link href="/contact" className="studio-button secondary">
            {t("Trao đổi với mình", "Get in touch")}
            <ArrowRight size={17} aria-hidden="true" />
          </Link>
        </div>
      </section>
    </div>
  );
}
