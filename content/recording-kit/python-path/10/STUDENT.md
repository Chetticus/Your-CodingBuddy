# BK04 · Thử với người dùng và cải thiện

## Bạn sẽ làm được gì?

Ghi kết quả kiểm thử và thêm kiểm tra mã sách trùng.

Sao chép starter.py thành my-work.py, rồi chạy bằng `python my-work.py` trong thư mục bài học. Xem [hướng dẫn bắt đầu](../../STUDENT-START.md) nếu chưa chạy được Python.

## Tự làm trước khi xem lời giải

Bổ sung kiểm tra mã trùng từ solution, hoàn thành bảng kiểm và chọn một cải tiến riêng. Nhờ một người thử tìm và mượn sách, ghi lại một điểm khó hiểu rồi sửa.

## Kiểm tra

Dữ liệu mã trùng bị từ chối; dữ liệu hợp lệ vẫn chạy. Nộp code, hướng dẫn, kết quả kiểm tra và một ghi chú thay đổi có bằng chứng.

Ghi một đầu vào, kết quả mong đợi và kết quả thực tế. Nếu khác nhau, ghi thay đổi bạn đã thử.

## Gợi ý từng bước

1. Tạo ids = set() trước vòng lặp kiểm tra dữ liệu.
2. Kiểm tra book["id"] in ids rồi mới ids.add(book["id"]).
3. Chỉ thử với bản sao dữ liệu. Bảng kiểm ở ../../PROJECT-BRIEF.md.

## Đối chiếu lời giải

Mở solution.py sau khi đã thử. Chạy cùng đầu vào với bản của bạn. Giải thích một khác biệt thay vì chép lại cả file. Lời giải là một cách làm, không phải cách duy nhất.

## Nghĩ thêm

Người thử đã làm gì khác với điều bạn dự đoán? Bạn sửa điều gì vì quan sát đó?

## English summary

Test expected behavior, reject duplicate IDs, and improve one interaction based on observed feedback. State the local-only limitation and describe your own contribution.
