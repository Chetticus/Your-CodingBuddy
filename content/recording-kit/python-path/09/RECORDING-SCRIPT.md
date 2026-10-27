# BK03 · Đóng chương trình rồi mở lại: dữ liệu còn không?

Video 09 · Vietnamese spoken script + instructor directions · private rehearsal draft

Target edited length: 10–14 minutes. Possible split: saving/reloading first, handling unreadable files second. Timing is an estimate, not subtitle timing.

## Before recording

- Copy starter.py to my-work.py in a disposable lesson 09 practice folder. This starter is the previous lesson's non-persistent menu. Preserve the supplied files.
- Have lesson 09's solution.py ready as the storage scaffold. Do not use lesson 10's duplicate-ID check yet.
- Use only sample data. A previous take may have created books.json: move that practice file aside before starting a fresh take, rather than resetting anyone's real data.
- Rehearse writing a file, opening it, quitting, restarting, and restoring a deliberately damaged copy. Stop the program before manually editing JSON.
- Keep a known-good backup outside the working filename, for example books-backup.json. Only books.json is loaded by the program.

## 1 · Reproduce the missing behavior — about 60 seconds

[SCREEN: Run starter-based my-work.py. Borrow 1, quit, restart, find De Men.]

> Chào bạn. Mình vừa mượn cuốn mã một, nhưng đóng chương trình rồi mở lại thì nó lại còn trống. Phần mượn đã đổi dữ liệu trong bộ nhớ, nhưng lần chạy mới lại bắt đầu từ dữ liệu mẫu.
>
> Hôm nay mình muốn trạng thái được giữ lại qua các lần chạy. Mình sẽ ghi dữ liệu vào một file, rồi đọc file đó khi chương trình bắt đầu.
>
> Mình vẫn làm trên một máy với dữ liệu mẫu. Việc thêm file chưa biến chương trình thành một hệ thống cho nhiều người dùng cùng lúc.

## 2 · Where the data will live — about 75 seconds

[ADD imports at the top and DATA after the existing core functions, matching solution.py.]

```python
import json
from pathlib import Path

DATA = Path(__file__).with_name("books.json")
```

> Mình dùng hai công cụ có sẵn trong Python. `json` giúp chuyển dữ liệu thành văn bản theo một định dạng có cấu trúc, rồi đọc lại. `Path` giúp làm việc với đường dẫn file.
>
> Dòng `DATA` chọn file tên `books.json` nằm cạnh file chương trình đang chạy. Nhờ vậy vị trí dữ liệu không phụ thuộc vào việc terminal ban đầu mở ở thư mục nào.
>
> Bạn chưa cần học thuộc cách viết đường dẫn này. Điều cần biết là file nào đang được dùng và nó nằm ở đâu, để không vô tình đọc dữ liệu của một bài thử khác.

## 3 · Write the saving function — about 90 seconds

[ADD the supplied function; type the body while explaining the two operations.]

```python
def save_books(books, path=DATA):
    path.write_text(json.dumps(books, ensure_ascii=False, indent=2), encoding="utf-8")
```

> Hàm nhận danh sách sách. `path=DATA` đặt đường dẫn mặc định: nếu mình không đưa đường dẫn khác khi gọi, nó dùng file đã chọn ở trên.
>
> `json.dumps` tạo văn bản JSON từ danh sách. `ensure_ascii=False` cho phép giữ ký tự như chữ tiếng Việt ở dạng dễ đọc; `indent=2` thêm cách xuống dòng và thụt dòng để mình dễ nhìn file.
>
> `write_text` ghi văn bản đó vào file với mã hóa UTF-8. Nếu file đã có, nội dung cũ sẽ được thay bằng dữ liệu đang lưu. Vì vậy mình cần chắc đang dùng đúng file và dữ liệu đã được đọc thành công trước khi sửa rồi lưu lại.

[Do not call this function blindly against an unknown existing file. Continue into the load scaffold first.]

## 4 · Read before opening the menu — about two minutes

[ACTION: Bring in the complete load_books function from lesson 09 solution.py. Show its top portion first.]

```python
def load_books(path=DATA):
    if not path.exists():
        return [book.copy() for book in STARTER]
    books = json.loads(path.read_text(encoding="utf-8"))
```

> Khi chưa có file, mình trả về các bản sao của sách mẫu, giống phiên bản trước. Khi đã có file, mình đọc văn bản rồi dùng `json.loads` để chuyển nó về dữ liệu Python.
>
> Chú ý tên hai thao tác: `dumps` tạo văn bản để ghi, còn `loads` đọc văn bản để lấy lại dữ liệu.

[SCROLL through the validation block in the supplied function.]

> Đọc được JSON chưa chắc có nghĩa là dữ liệu đúng cho tủ sách. Một file có thể chứa văn bản hoặc một đối tượng khác, trong khi mình cần một danh sách các cuốn sách.
>
> Phần kiểm tra này xác nhận có danh sách, mỗi phần tử là dictionary, mã là số nguyên, tên là văn bản không rỗng và trạng thái là boolean. Nếu không đúng, `raise ValueError` báo rằng dữ liệu không phù hợp.
>
> Đây là đoạn hỗ trợ dài hơn, mình cung cấp sẵn để bạn đọc theo từng yêu cầu. Bạn không cần tự nhớ toàn bộ cú pháp kiểm tra kiểu dữ liệu trong bài này. Nhưng hãy hiểu vì sao mình không tin mọi file chỉ vì tên của nó là books.json.

[POINT to the final return books.]

> Sau khi kiểm tra xong, hàm mới trả danh sách cho chương trình sử dụng. Phiên bản này chưa kiểm tra mã trùng; mình sẽ bổ sung ở bài cuối.

## 5 · Connect reading and saving to the right moments — about two minutes

[REPLACE main's original sample-copy assignment with this block.]

```python
try:
    books = load_books()
except (OSError, ValueError) as error:
    print("Could not read books.json:", error)
    return
```

> Mình đọc dữ liệu trước khi vào menu. Nếu có lỗi truy cập file hoặc dữ liệu không đọc được theo yêu cầu, chương trình thông báo và dừng lần gọi `main`.
>
> Nó không tự thay file lỗi bằng sách mẫu, vì làm vậy có thể khiến mình mất dữ liệu cũ mà không biết. Chưa có file và có file nhưng file lỗi là hai trường hợp khác nhau.

[REPLACE only the success body after set_loan. Keep the existing failure branch.]

```python
if set_loan(books, book_id, action == "b"):
    try:
        save_books(books)
        print("Saved.")
    except OSError as error:
        print("Change is in memory but could not be saved:", error)
else:
    print("Unknown book, or its status already matches.")
```

> Khi một lượt mượn hoặc trả thực sự thay đổi trạng thái, mình lưu ngay, không đợi đến lúc người dùng thoát. Thông báo “Saved” chỉ xuất hiện sau khi thao tác ghi hoàn thành.
>
> Nếu không ghi được, trạng thái trong bộ nhớ vẫn đã đổi, nhưng chương trình phải nói rõ chưa lưu thành công. Không nên hiểu một thay đổi trên màn hình là chắc chắn đã nằm trong file.

## 6 · Prove it survives a restart — about 90 seconds

[ACTION: Save the code. In the fresh practice folder, run, borrow 1 and confirm Saved. Open the created books.json without changing it.]

> Đây là file vừa được tạo. Mình tìm cuốn mã một và thấy trạng thái đã đổi. Trong JSON, boolean viết là `true` và `false` bằng chữ thường; trong Python là `True` và `False`. Thư viện json xử lý sự chuyển đổi đó cho mình.

[ACTION: Quit; restart; find De Men. Expected: no available match. Then return 1; quit; restart; find again.]

> Lần này đóng rồi mở lại, sách vẫn đang mượn. Sau khi trả và khởi động lại, nó xuất hiện trong sách trống. Mình đã kiểm tra cả hai chiều, thay vì chỉ nhìn thấy file rồi cho rằng phần lưu hoạt động đúng.
>
> Trong phiên bản này, nếu chưa có thay đổi nào thì chưa nhất thiết có file mới. File được tạo khi mình lưu một thay đổi thành công.

## 7 · Do not hide damaged data — about 75 seconds

[ACTION: Quit. Copy the valid books.json to books-backup.json. In the disposable books.json only, remove the final closing bracket. Save and run.]

> Mình cố tình làm hỏng một bản dữ liệu thử bằng cách bỏ dấu ngoặc đóng. Chương trình báo lỗi đọc và không mở menu.

[ACTION: Reopen the damaged file and show the missing bracket is still missing.]

> File vẫn giữ nguyên bản lỗi, không bị âm thầm thay bằng dữ liệu mẫu. Mình còn cơ hội kiểm tra hoặc khôi phục từ bản sao.

[ACTION: Restore books.json from the known-good backup, then rerun and find books.]

> Mình khôi phục bản đã sao lưu và kiểm tra lại. Với dữ liệu thật, đừng xóa file chỉ để thông báo lỗi biến mất. Trước hết cần hiểu vấn đề và giữ lại bản gốc.

## 8 · Student task and close — about 45 seconds

[SCREEN: Show task, hide the finished code.]

> Bạn dùng khung đọc và lưu được cung cấp để nâng cấp chương trình trước. Kiểm tra mượn, thoát, mở lại, rồi trả và mở lại lần nữa. Mở file để chỉ đúng trạng thái đã đổi.
>
> Sau đó thử lỗi đọc trên một bản dữ liệu riêng có bản sao dự phòng. Tạm dừng video để làm từng bước. Không cần làm tất cả trong một lần.

[PAUSE for 5 seconds, then closing check.]

> Nếu giải thích được dữ liệu đang ở bộ nhớ hay ở file, lúc nào chương trình đọc và lúc nào nó lưu, bạn đã nắm được phần chính. Bài cuối mình sẽ kiểm thử có hệ thống và chọn một điểm để cải thiện.

## Instructor review

- Show actual save/restart evidence, not only the presence of a file.
- Keep the syntax error demonstration in a disposable copy, and restore the good data before ending.
- Use the complete validation scaffold from solution.py, not only its abbreviated opening shown in section 4.
- Do not promise crash-proof storage, automatic backups or simultaneous multi-user support. This is a small local-file implementation.
- Final code matches lesson 09 solution.py. Never silently reuse a books.json from another take.
