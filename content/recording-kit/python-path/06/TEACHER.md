# PY06 · Hàm và cách tìm lỗi

Private recording draft · Vietnamese narration · planned, not recorded

**Mục tiêu:** Viết hàm trả về danh sách tên khớp một từ khóa.

**Chuẩn bị:** Hoàn thành bài 05; giải thích được kết quả của bài trước. Mở starter.py và solution.py ở hai tab; chỉ chiếu tab đang dạy. Làm trên bản sao my-work.py. Không sửa bản gốc khi ghi hình.

**Thời lượng dự kiến:** 7–10 phút video; dành thêm 15–25 phút cho học sinh thực hành. Đây là ước lượng để diễn tập, không phải thời lượng công bố.

## 1. Mở bài — nói bằng giọng của bạn (khoảng 30 giây)

> Mình sẽ cần tìm sách nhiều lần. Thay vì chép lại đoạn tìm kiếm, mình đặt nó vào một hàm, đưa dữ liệu vào và nhận kết quả ra.

Cho xem kết quả đích trong solution.py, sau đó quay về starter.py. Không cần đọc lời mở nguyên văn.

## 2. Dạy trên màn hình (phần chính)

1. Giải thích def, hai tham số titles/keyword, list matches và return. Hàm chỉ chạy khi được gọi.
2. Duyệt từng title; dùng in để kiểm tra chuỗi con, append để thêm kết quả. casefold so sánh không phân biệt hoa/thường, không bỏ dấu.
3. Gọi hàm với " DE MEN ", missing và chuỗi rỗng. In kết quả bên ngoài hàm để phân biệt return với print.

Sau mỗi thay đổi: hỏi “Bạn đoán lần chạy này sẽ hiện gì?”, dừng ngắn, chạy thử, giải thích sự khác nhau. Nói lý do trước khi đọc cú pháp.

## 3. Một lỗi để cùng sửa (khoảng 1 phút)

Đặt return matches trong for để chương trình dừng quá sớm. Tìm Mat Biec ở cuối danh sách để phát hiện; đưa return ra ngoài vòng lặp.

## 4. Dừng video và tự làm

> Hoàn thành find_titles, tìm đúng khi có khoảng trắng ở hai đầu và khác chữ hoa. Trả về list rỗng khi không có kết quả.

Hiện yêu cầu trên màn hình và nhắc người học tạm dừng. Gợi ý và lời giải nằm trong STUDENT.md và solution.py. Nếu quay lời giải, đặt sau điểm dừng hoặc tách thành đoạn tùy chọn.

## 5. Kiểm tra và kết bài

" DE MEN " trả một tên, missing trả [], từ khóa rỗng trả cả ba tên.

Hỏi: “Vì sao chỉ thử sách đầu tiên có thể bỏ sót lỗi?”

Kết bài: “Nếu bạn giải thích được vì sao kết quả thay đổi, hãy thử một đầu vào khác trước khi sang bài tiếp theo.” Không hứa bài tiếp theo đã có video khi chưa xuất bản.

## Ghi chú riêng trước khi quay

- Cách mình sẽ nói lại lời mở: ____
- Điểm mình chưa giải thích tự tin: ____
- Chi tiết thật mình muốn kể, nếu có: ____
- Timestamp cần quay lại: ____

## English lesson summary

Define a reusable search function that returns a list. Test first, last, absent, and blank queries. Returning inside the loop can stop the search too early.

Translate captions from the actual final take. This summary is not a timed subtitle track.
