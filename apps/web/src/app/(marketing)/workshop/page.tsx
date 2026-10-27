import type { Metadata } from "next";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Download } from "lucide-react";
import { ProjectWorkshop } from "@/components/project-workshop";
import { getLocale } from "@/lib/locale";
import { translate } from "@/lib/translations";

export const metadata: Metadata = {
  title: "Bài thực hành mở / Open practice lesson",
  description:
    "Tạo một thư viện tài liệu dễ tìm cho lớp mình. Một bài thực hành CodingBuddy với tìm kiếm, chủ đề và hướng dẫn.",
};
export default async function WorkshopPage() {
  const locale = await getLocale();
  const t = (vi: string, en?: string) => translate(locale, vi, en);
  return (
    <div className="page-shell workshop-page">
      <Link href="/" className="back-link">
        <ArrowLeft size={16} aria-hidden="true" />
        {t("Về CodingBuddy", "Back to CodingBuddy")}
      </Link>
      <header className="workshop-page-heading">
        <div>
          <p className="section-label">
            {t(
              "Bài thực hành mở · Đọc và thử làm",
              "Open practice lesson · Read and try",
            )}
          </p>
          <h1>
            {t(
              "Làm một thư viện nhỏ\ncho lớp mình.",
              "Build a little library\nfor your classroom.",
            )}
          </h1>
        </div>
        <p>
          {t(
            "Một người bạn muốn học về biến nhưng không biết tìm tài liệu ở đâu. Hãy làm cho việc tìm kiếm đó dễ hơn.",
            "A classmate wants to learn about variables but can’t find the right note. Let’s make that search easier.",
          )}
        </p>
      </header>
      <ProjectWorkshop full />
      <div className="lesson-guide" id="start">
        <aside>
          <p className="section-label">
            {t("Cùng bắt đầu", "Let’s get started")}
          </p>
          <h2>
            {t(
              "Từ nhu cầu\nđến một lần thử.",
              "From a need\nto a first attempt.",
            )}
          </h2>
          <a
            className="studio-button secondary"
            href={`/downloads/resource-library-${locale}.html`}
            download
          >
            <Download size={17} aria-hidden="true" />
            {t("Tải mã nguồn", "Download the source")}
          </a>
          <p className="guide-note">
            {t(
              "Tệp HTML chạy ngay trong trình duyệt, không cần cài đặt thêm.",
              "An HTML file that opens in your browser. No installation needed.",
            )}
          </p>
        </aside>
        <div className="guide-content">
          <section>
            <h3>
              {t("1. Dùng thử như một người mới", "1. Try it as a new learner")}
            </h3>
            <p>
              {t(
                "Tìm “biến” hoặc “HTML”. Chọn một chủ đề. Thử một từ chưa có trong danh sách. Bạn có biết cần làm gì tiếp theo không?",
                "Search for “variables” or “HTML”. Choose a topic. Try a word that isn’t in the list. Is it clear what you can do next?",
              )}
            </p>
          </section>
          <section>
            <h3>
              {t(
                "2. Đọc cách chương trình tìm kiếm",
                "2. Read how the search works",
              )}
            </h3>
            <p>
              {t(
                "Ở tab “Cách lọc”, mỗi tài liệu được kiểm tra xem tiêu đề có chứa từ khóa hay không. Danh sách kết quả chỉ giữ lại những mục phù hợp. Đây là ý tưởng của filter trong JavaScript.",
                "In “The filter” tab, each resource is checked to see whether its title contains the keyword. The results keep only matching items. This is the idea behind JavaScript’s filter method.",
              )}
            </p>
          </section>
          <section>
            <h3>
              {t(
                "3. Thêm điều có ích cho một người bạn",
                "3. Add something useful for a friend",
              )}
            </h3>
            <p>
              {t(
                "Tải mã nguồn, mở bằng một trình soạn thảo và tìm danh sách resources. Thêm một tài liệu bạn thấy hữu ích. Lưu tệp, mở lại trên trình duyệt và thử tìm tài liệu vừa thêm.",
                "Download the source, open it in a text editor, and find the resources list. Add a note you find useful. Save the file, reopen it in your browser, and try finding your new note.",
              )}
            </p>
          </section>
          <section className="guide-reflection">
            <h3>
              {t(
                "Một câu hỏi trước khi kết thúc",
                "A question before you finish",
              )}
            </h3>
            <p>
              {t(
                "Nhờ một người bạn tìm một ghi chú mà không hướng dẫn họ trước. Họ gặp khó khăn ở đâu? Thay đổi một nhãn, một mô tả hoặc cách sắp xếp để giúp họ.",
                "Ask a friend to find a note without explaining the interface first. Where do they get stuck? Change a label, description, or the organization to help them.",
              )}
            </p>
          </section>
          <Link href="/courses" className="inline-link">
            {t("Xem tiếp lộ trình học", "Continue to the learning path")}{" "}
            <ArrowRight size={17} aria-hidden="true" />
          </Link>
        </div>
      </div>
    </div>
  );
}
