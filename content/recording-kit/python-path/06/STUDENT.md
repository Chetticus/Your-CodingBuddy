# PY06 · Hàm và cách tìm lỗi

## Bạn sẽ làm được gì?

Viết hàm trả về danh sách tên khớp một từ khóa.

Sao chép starter.py thành my-work.py, rồi chạy bằng `python my-work.py` trong thư mục bài học. Xem [hướng dẫn bắt đầu](../../STUDENT-START.md) nếu chưa chạy được Python.

## Tự làm trước khi xem lời giải

Hoàn thành find_titles, tìm đúng khi có khoảng trắng ở hai đầu và khác chữ hoa. Trả về list rỗng khi không có kết quả.

## Kiểm tra

" DE MEN " trả một tên, missing trả [], từ khóa rỗng trả cả ba tên.

Ghi một đầu vào, kết quả mong đợi và kết quả thực tế. Nếu khác nhau, ghi thay đổi bạn đã thử.

## Gợi ý từng bước

1. Chuẩn hóa cả từ khóa và title bằng casefold; strip chỉ cần cho từ khóa.
2. append chạy trong if; return chạy sau vòng lặp.

## Đối chiếu lời giải

Mở solution.py sau khi đã thử. Chạy cùng đầu vào với bản của bạn. Giải thích một khác biệt thay vì chép lại cả file. Lời giải là một cách làm, không phải cách duy nhất.

## Nghĩ thêm

Vì sao chỉ thử sách đầu tiên có thể bỏ sót lỗi?

## English summary

Define a reusable search function that returns a list. Test first, last, absent, and blank queries. Returning inside the loop can stop the search too early.
