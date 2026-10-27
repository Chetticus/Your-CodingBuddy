# PY05 · Dictionary: mô tả một cuốn sách

Private recording draft · Vietnamese narration · planned, not recorded

**Mục tiêu:** Gom mã, tên và trạng thái của mỗi cuốn trong một dictionary.

**Chuẩn bị:** Hoàn thành bài 04; giải thích được kết quả của bài trước. Mở starter.py và solution.py ở hai tab; chỉ chiếu tab đang dạy. Làm trên bản sao my-work.py. Không sửa bản gốc khi ghi hình.

**Thời lượng dự kiến:** 5–8 phút video; dành thêm 15–25 phút cho học sinh thực hành. Đây là ước lượng để diễn tập, không phải thời lượng công bố.

## 1. Mở bài — nói bằng giọng của bạn (khoảng 30 giây)

> Tên sách thôi chưa đủ: mình còn cần biết sách đang được mượn chưa. Mỗi cuốn sẽ có một nhóm thông tin đi cùng nhau.

Cho xem kết quả đích trong solution.py, sau đó quay về starter.py. Không cần đọc lời mở nguyên văn.

## 2. Dạy trên màn hình (phần chính)

1. Chỉ ba trường id, title, borrowed của một book, rồi cho thấy books là list chứa nhiều book.
2. Duyệt books và truy cập book["title"]. Giải thích False chưa mượn, True đang mượn.
3. Viết if để đổi boolean thành chữ dễ đọc. In id, title và status; đổi thứ tự sách và chỉ ra id vẫn giữ nguyên.

Sau mỗi thay đổi: hỏi “Bạn đoán lần chạy này sẽ hiện gì?”, dừng ngắn, chạy thử, giải thích sự khác nhau. Nói lý do trước khi đọc cú pháp.

## 3. Một lỗi để cùng sửa (khoảng 1 phút)

Truy cập book["name"] khi dữ liệu chỉ có title. Dùng KeyError để tìm lại tên khóa chính xác.

## 4. Dừng video và tự làm

> Hiển thị mỗi sách trên một dòng gồm mã, tên và con trong/dang muon. Đổi borrowed của sách 1 rồi chạy lại.

Hiện yêu cầu trên màn hình và nhắc người học tạm dừng. Gợi ý và lời giải nằm trong STUDENT.md và solution.py. Nếu quay lời giải, đặt sau điểm dừng hoặc tách thành đoạn tùy chọn.

## 5. Kiểm tra và kết bài

Sách 1 ban đầu còn trống, sách 2 đang mượn; đổi boolean làm đổi đúng trạng thái tương ứng.

Hỏi: “Tại sao mã sách không nên phụ thuộc vào vị trí trong danh sách?”

Kết bài: “Nếu bạn giải thích được vì sao kết quả thay đổi, hãy thử một đầu vào khác trước khi sang bài tiếp theo.” Không hứa bài tiếp theo đã có video khi chưa xuất bản.

## Ghi chú riêng trước khi quay

- Cách mình sẽ nói lại lời mở: ____
- Điểm mình chưa giải thích tự tin: ____
- Chi tiết thật mình muốn kể, nếu có: ____
- Timestamp cần quay lại: ____

## English lesson summary

Represent each book with an ID, title, and boolean loan status. Keep stable IDs when reordering the list. Dictionary keys must match exactly.

Translate captions from the actual final take. This summary is not a timed subtitle track.
