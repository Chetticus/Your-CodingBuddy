import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { ArrowDown, ArrowUpRight } from "lucide-react";
import content from "@/content/community-work.json";
import { getLocale } from "@/lib/locale";
import { translate } from "@/lib/translations";

export const metadata: Metadata = {
  title: "Cộng đồng / Community",
  description: "CodingBuddy — learning, sharing and community activities.",
  robots: content.isDraft ? { index: false, follow: false } : undefined,
};

export default async function CommunityPage() {
  const locale = await getLocale();
  const t = (vi: string, en: string) => translate(locale, vi, en);
  return (
    <div className="page-shell community-page">
      {content.isDraft && (
        <aside className="community-draft">
          <strong>{t("BẢN XEM TRƯỚC", "PREVIEW DRAFT")}</strong>
          <span>
            {t(
              "Các câu chuyện và hình minh họa bên dưới là nội dung mẫu. Thông tin, hình ảnh và kết quả thực tế sẽ được bổ sung sau.",
              "The stories and illustrations below are placeholders. Actual details, photos and outcomes will be added later.",
            )}
          </span>
        </aside>
      )}
      <section className="community-hero">
        <div>
          <p className="section-label">
            {t(
              "CODINGBUDDY / CÙNG CỘNG ĐỒNG",
              "CODINGBUDDY / WITH OUR COMMUNITY",
            )}
          </p>
          <h1>
            {t("Từ lớp học,", "From learning,")}
            <br />
            <span>{t("đến cơ hội mới.", "to new possibilities.")}</span>
          </h1>
          <p className="community-lead">
            {t(
              "CodingBuddy hướng tới việc dùng nguồn lực từ hoạt động dạy học để mở rộng cơ hội học công nghệ cho trẻ em ở cộng đồng dân tộc thiểu số.",
              "CodingBuddy aims to use resources from teaching to widen access to technology learning for children in ethnic minority communities.",
            )}
          </p>
          <a href="#activities" className="studio-button secondary">
            {t("Xem nhật ký hoạt động", "Explore the activity journal")}
            <ArrowDown size={17} aria-hidden="true" />
          </a>
        </div>
        <aside className="community-note">
          <span className="section-label">
            {t("ĐIỀU MÌNH MUỐN GIỮ", "WHAT MATTERS HERE")}
          </span>
          <h2>
            {t(
              "Giúp ích bắt đầu từ việc lắng nghe.",
              "Useful help starts with listening.",
            )}
          </h2>
          <p>
            {t(
              "Một thiết bị phù hợp. Một buổi học vừa sức. Một tài liệu có thể dùng lại. Mỗi hoạt động cần bắt đầu từ nhu cầu thực tế và có người đồng hành sau đó.",
              "A suitable device. An approachable lesson. A resource someone can use again. Each activity should start with a real need and include support afterward.",
            )}
          </p>
          <span className="community-signature">Hải Nam / The CodingBuddy</span>
        </aside>
      </section>
      <section id="activities" className="community-journal">
        <div className="community-section-heading">
          <div>
            <p className="section-label">{t("NHẬT KÝ / 01", "JOURNAL / 01")}</p>
            <h2>{t("Những việc cùng làm.", "Things we do together.")}</h2>
          </div>
          <p>
            {t(
              "Mỗi câu chuyện dành chỗ cho nhu cầu, việc đã làm và điều cần tiếp tục.",
              "Each story makes room for the need, the work and what comes next.",
            )}
          </p>
        </div>
        <div className="community-story-grid">
          {content.stories.map((story, index) => (
            <article key={story.id} className="community-story" id={story.id}>
              <div className="community-image">
                <Image
                  src={story.image}
                  width={800}
                  height={500}
                  alt={
                    t("Hình minh họa mẫu — ", "Placeholder illustration — ") +
                    story.category[locale]
                  }
                />
                {content.isDraft && (
                  <span>
                    {t("HÌNH MINH HỌA MẪU", "PLACEHOLDER ILLUSTRATION")}
                  </span>
                )}
              </div>
              <div className="community-story-body">
                <p className="community-category">
                  0{index + 1} / {story.category[locale]}
                </p>
                <h3>{story.title[locale]}</h3>
                <p>{story.summary[locale]}</p>
                <p className="community-location">
                  {t(
                    "Địa điểm & thời gian: sẽ bổ sung",
                    "Location & date: to be added",
                  )}
                </p>
                <details>
                  <summary>
                    {t("Mở ghi chép hoạt động", "Open activity notes")}
                    <span aria-hidden="true">+</span>
                  </summary>
                  <dl>
                    {(
                      [
                        [t("Nhu cầu ban đầu", "The initial need"), story.need],
                        [
                          t("Việc đã thực hiện", "The work carried out"),
                          story.work,
                        ],
                        [t("Sau hoạt động", "Following up"), story.followUp],
                      ] as const
                    ).map(([label, copy]) => (
                      <div key={label}>
                        <dt>{label}</dt>
                        <dd>{copy[locale]}</dd>
                      </div>
                    ))}
                  </dl>
                </details>
              </div>
            </article>
          ))}
        </div>
      </section>
      <section className="community-records">
        <div>
          <p className="section-label">{t("GHI NHẬN / 02", "RECORDS / 02")}</p>
          <h2>
            {t(
              "Câu chuyện đi cùng thông tin rõ ràng.",
              "The story, with clear records.",
            )}
          </h2>
          <p>
            {t(
              "Phần này sẽ ghi lại nguồn đóng góp, cách sử dụng và tài liệu đối chiếu cho từng hoạt động.",
              "This section will document contributions, their use and supporting records for each activity.",
            )}
          </p>
        </div>
        <dl>
          {[
            [
              t("Nguồn lực đóng góp", "Resources contributed"),
              t(
                "Chờ bổ sung nguồn và số liệu xác nhận",
                "Awaiting confirmed sources and figures",
              ),
            ],
            [
              t("Thiết bị & hoạt động", "Equipment & activities"),
              t(
                "Chờ cập nhật danh sách và thời điểm thực hiện",
                "Awaiting activity lists and dates",
              ),
            ],
            [
              t("Hình ảnh & ghi nhận", "Photos & documentation"),
              t(
                "Chờ hình ảnh được phép chia sẻ và tài liệu đối chiếu",
                "Awaiting approved photos and supporting records",
              ),
            ],
          ].map(([title, value]) => (
            <div key={title}>
              <dt>{title}</dt>
              <dd>{value}</dd>
            </div>
          ))}
        </dl>
      </section>
      <section className="community-outro">
        <div>
          <h2>
            {t(
              "Có một việc mình có thể cùng làm?",
              "Something we could work on together?",
            )}
          </h2>
          <p>
            {t(
              "Nếu bạn có nhu cầu học tập hoặc ý tưởng phù hợp, hãy bắt đầu bằng một cuộc trò chuyện.",
              "If you have a learning need or a suitable idea, let’s start with a conversation.",
            )}
          </p>
        </div>
        <Link href="/contact" className="studio-button primary">
          {t("Trao đổi với Nam", "Talk with Nam")}
          <ArrowUpRight size={18} aria-hidden="true" />
        </Link>
      </section>
    </div>
  );
}
