# BK03 · Giữ dữ liệu sau khi đóng chương trình

## Bạn sẽ làm được gì?

Lưu JSON và đọc lại trạng thái ở lần chạy tiếp theo.

Sao chép starter.py thành my-work.py, rồi chạy bằng `python my-work.py` trong thư mục bài học. Xem [hướng dẫn bắt đầu](../../STUDENT-START.md) nếu chưa chạy được Python.

## Tự làm trước khi xem lời giải

Thêm lưu/đọc vào phiên bản trước bằng khung hỗ trợ. Chứng minh một lượt mượn còn nguyên qua hai lần chạy. Mở books.json và chỉ đúng trường đã đổi.

## Kiểm tra

Mượn 1 → thoát → mở lại: mã 1 không còn trong sách trống. Trả 1 → mở lại: xuất hiện. File hỏng được giữ nguyên cùng thông báo lỗi.

Ghi một đầu vào, kết quả mong đợi và kết quả thực tế. Nếu khác nhau, ghi thay đổi bạn đã thử.

## Gợi ý từng bước

1. Lưu sau set_loan thành công, không chỉ lúc thoát.
2. Giữ các hàm xử lý file được cung cấp. Phần kiểm tra cấu trúc dài là mã hỗ trợ để đọc, không phải yêu cầu học thuộc.
3. Hãy dùng thư mục khác cho mỗi thí nghiệm để tránh dùng nhầm books.json.

## Đối chiếu lời giải

Mở solution.py sau khi đã thử. Chạy cùng đầu vào với bản của bạn. Giải thích một khác biệt thay vì chép lại cả file. Lời giải là một cách làm, không phải cách duy nhất.

## Nghĩ thêm

Một thay đổi trong bộ nhớ có đồng nghĩa với việc đã lưu thành công không?

## English summary

Persist book state in a local JSON file. Save after successful changes and load on startup. Explain missing versus damaged files and do not overwrite unreadable data silently.
