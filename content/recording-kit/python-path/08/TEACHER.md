# BK02 · Tìm sách, mượn và trả

Private recording draft · Vietnamese narration · planned, not recorded

**Mục tiêu:** Tìm sách còn trống và thay đổi đúng trạng thái qua menu.

**Chuẩn bị:** Hoàn thành bài 07; giải thích được kết quả của bài trước. Mở starter.py và solution.py ở hai tab; chỉ chiếu tab đang dạy. Làm trên bản sao my-work.py. Không sửa bản gốc khi ghi hình.

**Thời lượng dự kiến:** 10–14; có thể tách thành hai video phút video; dành thêm 15–25 phút cho học sinh thực hành. Đây là ước lượng để diễn tập, không phải thời lượng công bố.

## 1. Mở bài — nói bằng giọng của bạn (khoảng 30 giây)

> Một danh sách chỉ để nhìn chưa đủ. Mình muốn tìm sách còn trống, mượn một cuốn, rồi tìm lại để biết trạng thái đã thay đổi.

Cho xem kết quả đích trong solution.py, sau đó quay về starter.py. Không cần đọc lời mở nguyên văn.

## 2. Dạy trên màn hình (phần chính)

1. Viết find_available bằng vòng lặp quen thuộc: tên khớp và chưa mượn mới thêm vào matches. Chạy với từ khóa rỗng.
2. Viết set_loan: tìm đúng id, từ chối trạng thái đã giống yêu cầu, cập nhật rồi return True; không tìm thấy trả False.
3. Đọc menu chuẩn bị sẵn trong solution từng phần: while lặp đến q; int chuyển mã; try/except bắt ValueError; continue quay lại menu. Cho học sinh dự đoán b và r truyền boolean nào.

Sau mỗi thay đổi: hỏi “Bạn đoán lần chạy này sẽ hiện gì?”, dừng ngắn, chạy thử, giải thích sự khác nhau. Nói lý do trước khi đọc cú pháp.

## 3. Một lỗi để cùng sửa (khoảng 1 phút)

Trong bản thử, bỏ điều kiện not book["borrowed"] để sách đang mượn vẫn được tìm thấy. Kiểm tra trước/sau khi mượn và khôi phục điều kiện.

## 4. Dừng video và tự làm

> Xây find_available và set_loan trước. Sau đó nối với menu mẫu. Thử tìm → mượn 1 → tìm lại → trả 1. Thử abc, 99 và mượn hai lần.

Hiện yêu cầu trên màn hình và nhắc người học tạm dừng. Gợi ý và lời giải nằm trong STUDENT.md và solution.py. Nếu quay lời giải, đặt sau điểm dừng hoặc tách thành đoạn tùy chọn.

## 5. Kiểm tra và kết bài

Mượn làm mất sách khỏi kết quả sách trống; trả đưa sách trở lại. Mã lỗi không gây crash. Thoát rồi chạy lại vẫn mất thay đổi: bài sau sẽ giải quyết.

Hỏi: “Tại sao không được báo thành công nếu người dùng nhập mã không tồn tại?”

Kết bài: “Nếu bạn giải thích được vì sao kết quả thay đổi, hãy thử một đầu vào khác trước khi sang bài tiếp theo.” Không hứa bài tiếp theo đã có video khi chưa xuất bản.

## Ghi chú riêng trước khi quay

- Cách mình sẽ nói lại lời mở: ____
- Điểm mình chưa giải thích tự tin: ____
- Chi tiết thật mình muốn kể, nếu có: ____
- Timestamp cần quay lại: ____

## English lesson summary

Combine available-book search with borrow/return actions. Read the supplied menu scaffold and handle non-numeric IDs. Data still resets after exit in this version.

Translate captions from the actual final take. This summary is not a timed subtitle track.
