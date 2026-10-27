# BK02 · Tìm sách, mượn và trả

## Bạn sẽ làm được gì?

Tìm sách còn trống và thay đổi đúng trạng thái qua menu.

Sao chép starter.py thành my-work.py, rồi chạy bằng `python my-work.py` trong thư mục bài học. Xem [hướng dẫn bắt đầu](../../STUDENT-START.md) nếu chưa chạy được Python.

## Tự làm trước khi xem lời giải

Xây find_available và set_loan trước. Sau đó nối với menu mẫu. Thử tìm → mượn 1 → tìm lại → trả 1. Thử abc, 99 và mượn hai lần.

## Kiểm tra

Mượn làm mất sách khỏi kết quả sách trống; trả đưa sách trở lại. Mã lỗi không gây crash. Thoát rồi chạy lại vẫn mất thay đổi: bài sau sẽ giải quyết.

Ghi một đầu vào, kết quả mong đợi và kết quả thực tế. Nếu khác nhau, ghi thay đổi bạn đã thử.

## Gợi ý từng bước

1. set_loan nhận True để mượn, False để trả.
2. int("abc") gây ValueError; phần except giúp quay lại menu thay vì dừng chương trình.
3. Menu là khung được cung cấp; không yêu cầu thuộc lòng mọi dòng mới của bài này.

## Đối chiếu lời giải

Mở solution.py sau khi đã thử. Chạy cùng đầu vào với bản của bạn. Giải thích một khác biệt thay vì chép lại cả file. Lời giải là một cách làm, không phải cách duy nhất.

## Nghĩ thêm

Tại sao không được báo thành công nếu người dùng nhập mã không tồn tại?

## English summary

Combine available-book search with borrow/return actions. Read the supplied menu scaffold and handle non-numeric IDs. Data still resets after exit in this version.
