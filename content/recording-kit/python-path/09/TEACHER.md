# BK03 · Giữ dữ liệu sau khi đóng chương trình

Private recording draft · Vietnamese narration · planned, not recorded

**Mục tiêu:** Lưu JSON và đọc lại trạng thái ở lần chạy tiếp theo.

**Chuẩn bị:** Hoàn thành bài 08; giải thích được kết quả của bài trước. Mở starter.py và solution.py ở hai tab; chỉ chiếu tab đang dạy. Làm trên bản sao my-work.py. Không sửa bản gốc khi ghi hình.

**Thời lượng dự kiến:** 10–14; có thể tách thành hai video phút video; dành thêm 15–25 phút cho học sinh thực hành. Đây là ước lượng để diễn tập, không phải thời lượng công bố.

## 1. Mở bài — nói bằng giọng của bạn (khoảng 30 giây)

> Hôm trước mình mượn sách rồi đóng chương trình, nhưng mở lại thì sách lại còn trống. Hôm nay mình tách dữ liệu đang nằm trong bộ nhớ và dữ liệu được lưu thành file.

Cho xem kết quả đích trong solution.py, sau đó quay về starter.py. Không cần đọc lời mở nguyên văn.

## 2. Dạy trên màn hình (phần chính)

1. Mở starter (bản chưa lưu), mượn 1, thoát và chạy lại để thấy vấn đề. Dùng thư mục thử riêng.
2. Giải thích json.dumps/json.loads và read_text/write_text. Path(__file__).with_name đặt file cạnh script. Đọc trước khi vào menu, lưu sau thay đổi thành công.
3. Dùng khung load_books/save_books trong solution; giải thích trường hợp chưa có file, file hợp lệ, file lỗi. Mượn, thoát, chạy lại và tìm; sau đó trả.

Sau mỗi thay đổi: hỏi “Bạn đoán lần chạy này sẽ hiện gì?”, dừng ngắn, chạy thử, giải thích sự khác nhau. Nói lý do trước khi đọc cú pháp.

## 3. Một lỗi để cùng sửa (khoảng 1 phút)

Trong bản sao dữ liệu thử, làm sai cú pháp JSON. Chạy lại và cho thấy lỗi đọc cùng việc file không bị ghi đè. Khôi phục từ bản sao, không xóa dữ liệu để che lỗi.

## 4. Dừng video và tự làm

> Thêm lưu/đọc vào phiên bản trước bằng khung hỗ trợ. Chứng minh một lượt mượn còn nguyên qua hai lần chạy. Mở books.json và chỉ đúng trường đã đổi.

Hiện yêu cầu trên màn hình và nhắc người học tạm dừng. Gợi ý và lời giải nằm trong STUDENT.md và solution.py. Nếu quay lời giải, đặt sau điểm dừng hoặc tách thành đoạn tùy chọn.

## 5. Kiểm tra và kết bài

Mượn 1 → thoát → mở lại: mã 1 không còn trong sách trống. Trả 1 → mở lại: xuất hiện. File hỏng được giữ nguyên cùng thông báo lỗi.

Hỏi: “Một thay đổi trong bộ nhớ có đồng nghĩa với việc đã lưu thành công không?”

Kết bài: “Nếu bạn giải thích được vì sao kết quả thay đổi, hãy thử một đầu vào khác trước khi sang bài tiếp theo.” Không hứa bài tiếp theo đã có video khi chưa xuất bản.

## Ghi chú riêng trước khi quay

- Cách mình sẽ nói lại lời mở: ____
- Điểm mình chưa giải thích tự tin: ____
- Chi tiết thật mình muốn kể, nếu có: ____
- Timestamp cần quay lại: ____

## English lesson summary

Persist book state in a local JSON file. Save after successful changes and load on startup. Explain missing versus damaged files and do not overwrite unreadable data silently.

Translate captions from the actual final take. This summary is not a timed subtitle track.
