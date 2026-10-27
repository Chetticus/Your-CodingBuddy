# PY05 · Dictionary: mô tả một cuốn sách

## Bạn sẽ làm được gì?

Gom mã, tên và trạng thái của mỗi cuốn trong một dictionary.

Sao chép starter.py thành my-work.py, rồi chạy bằng `python my-work.py` trong thư mục bài học. Xem [hướng dẫn bắt đầu](../../STUDENT-START.md) nếu chưa chạy được Python.

## Tự làm trước khi xem lời giải

Hiển thị mỗi sách trên một dòng gồm mã, tên và con trong/dang muon. Đổi borrowed của sách 1 rồi chạy lại.

## Kiểm tra

Sách 1 ban đầu còn trống, sách 2 đang mượn; đổi boolean làm đổi đúng trạng thái tương ứng.

Ghi một đầu vào, kết quả mong đợi và kết quả thực tế. Nếu khác nhau, ghi thay đổi bạn đã thử.

## Gợi ý từng bước

1. Duyệt bằng for book in books.
2. Dùng if book["borrowed"] thay vì so sánh với chuỗi "True".

## Đối chiếu lời giải

Mở solution.py sau khi đã thử. Chạy cùng đầu vào với bản của bạn. Giải thích một khác biệt thay vì chép lại cả file. Lời giải là một cách làm, không phải cách duy nhất.

## Nghĩ thêm

Tại sao mã sách không nên phụ thuộc vào vị trí trong danh sách?

## English summary

Represent each book with an ID, title, and boolean loan status. Keep stable IDs when reordering the list. Dictionary keys must match exactly.
