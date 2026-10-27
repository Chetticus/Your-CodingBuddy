# BK01 · Tủ sách chia sẻ: làm phiên bản đầu dùng được

Video 07 in the full path · first lesson of the book-exchange project course

Vietnamese spoken script + instructor directions · private rehearsal draft

Target edited length: 7–9 minutes. These are pacing estimates, not subtitle timestamps. Speak the quoted passages; bracketed directions are for you.

## Before recording

- Copy lesson 07's starter.py to my-work.py. It contains the two-book display from video 05; use it as the starting point rather than typing that entire lesson again.
- Keep starter.py and solution.py unchanged. Use the same editor, terminal and run command as earlier videos.
- Preview the completed solution, then close its tab. Have a short note ready on screen: `Ma sach / Ten sach / Trang thai` and `Xem danh sach → Tim va muon/tra → Luu du lieu → Thu va cai thien`.
- Prepare a third book: ID 3, Mat Biec, borrowed False. Rehearse moving the existing loop into show_books(items), preserving its nested indentation.
- This lesson intentionally revisits familiar code. Its new work is defining a small project, organizing the display into a function, and testing the data assumptions. It does not yet implement search, loans, accounts or file storage.

## 1 · Start with the person using it — about 50 seconds

[SCREEN: Run solution.py; show the three book records and readable statuses.]

> Chào bạn. Từ bài này, mình bắt đầu làm dự án tủ sách chia sẻ. Mình chọn một tình huống đơn giản: một bạn muốn mượn sách nhưng chưa biết có những cuốn nào và cuốn nào còn trống.
>
> Phiên bản đầu sẽ giúp xem danh sách như bạn đang thấy ở đây. Sau đó mình mới thêm tìm kiếm, ghi nhận mượn trả và lưu dữ liệu.
>
> Đây là dữ liệu mẫu để học, chưa phải một hệ thống đang được cả lớp sử dụng. Mình sẽ làm cho từng phần chạy đúng rồi thử xem nó có giúp người dùng thực hiện việc cần làm không.

[ACTION: Switch to the short scope note.]

## 2 · Decide what the first version needs — about 60 seconds

> Với mỗi cuốn, mình cần mã để phân biệt, tên để nhận ra và trạng thái để biết đang được mượn chưa. Ba thông tin này là đủ cho mục tiêu đầu tiên.
>
> Mình chưa cần thêm tài khoản hay thông tin liên hệ người mượn. Chương trình này cũng mới chạy trên một máy, chưa phải website để nhiều người dùng cùng lúc.

[POINT to the four planned stages, then underline only the first.]

> Lộ trình của dự án là: xem danh sách; tìm và mượn trả; lưu lại; rồi kiểm tra và cải thiện. Hôm nay mình chỉ hoàn thành phần đầu.
>
> Nếu bạn chọn một chủ đề khác, ví dụ dụng cụ lớp học, cách nghĩ vẫn tương tự: ai sẽ dùng, họ cần làm việc gì, và phiên bản nhỏ nhất cần giữ thông tin nào?

## 3 · Reuse what we already understand — about 60 seconds

[SCREEN: Open my-work.py with the existing two-book data and display loop. Run it once.]

> Đoạn này quen thuộc từ bài dictionary: một danh sách chứa hai cuốn, rồi vòng lặp chọn chữ để hiển thị trạng thái. Mình giữ lại phần đã hiểu và đã chạy được, thay vì viết lại từ đầu.

[ADD the third dictionary, preserving commas and brackets.]

```python
books = [
    {"id": 1, "title": "De Men Phieu Luu Ky", "borrowed": False},
    {"id": 2, "title": "The Little Prince", "borrowed": True},
    {"id": 3, "title": "Mat Biec", "borrowed": False},
]
```

> Mình thêm cuốn thứ ba với mã ba. Trước khi chạy, bạn đoán cuốn này sẽ hiện còn trống hay đang mượn?

[PAUSE for 3 seconds. Save and run.]

> Nó hiện còn trống vì `borrowed` là `False`. Vòng lặp cũ đã xử lý được cuốn mới mà mình không phải viết thêm phần hiển thị riêng.

## 4 · Turn the display into a reusable job — about 90 seconds

[ACTION: Add def show_books(items), move the existing loop inside it, and replace for book in books with for book in items. Leave the call absent temporarily.]

```python
def show_books(items):
    for book in items:
        if book["borrowed"]:
            status = "dang muon"
        else:
            status = "con trong"
        print(book["id"], book["title"], status)
```

> Mình đặt công việc hiển thị vào hàm `show_books`. Tham số `items` là danh sách được đưa vào khi gọi hàm. Bên trong, mình duyệt `items` thay vì lấy trực tiếp danh sách `books` bên ngoài.
>
> Nhờ vậy mình có thể dùng cùng cách hiển thị cho danh sách khác, miễn là mỗi phần tử có các thông tin mà hàm cần: `id`, `title` và `borrowed`.

[POINT to indentation levels: def, for, if/else, status.]

> Khi chuyển vào hàm, cả khối vòng lặp được thụt thêm một mức. Dòng `print` vẫn thuộc vòng lặp, nhưng nằm ngoài hai nhánh `if` và `else`, để cuốn nào cũng được hiển thị.

[ACTION: Save and run before adding the call.]

> Chưa có kết quả, vì mình mới định nghĩa hàm. Bạn có nhớ cần thêm bước nào không?

[PAUSE; ADD below the function, with no indentation.]

```python
show_books(books)
```

[ACTION: Save and run.]

> Mình gọi hàm và đưa danh sách `books` vào. Trong lần gọi này, `items` nhận danh sách đó. Cách hiển thị giống lúc trước, nhưng bây giờ công việc đã được đặt tên để dùng lại.

## 5 · Why this function prints — about 45 seconds

> Ở bài tìm kiếm, hàm dùng `return` để đưa danh sách kết quả về, rồi mình quyết định hiển thị nó ở ngoài. Còn mục đích của `show_books` chính là hiển thị, nên nó gọi `print` bên trong.
>
> Hai hàm có hai nhiệm vụ khác nhau. Mình không cần viết `print(show_books(books))`; chỉ gọi `show_books(books)` là đủ.

[OPTIONAL instructor demonstration: only if needed, show that wrapping the call in print produces the book lines and then None. Explain that a function with no explicit return value returns None, then restore the direct call. Otherwise do not add this extra concept to the recording.]

## 6 · Check the meaning of an ID — about 75 seconds

> Bây giờ mình thử một vấn đề về dữ liệu. Mình sẽ cố tình cho cuốn thứ ba dùng lại mã một.

[ACTION: Change only the third id from 3 to 1. Save and run.]

> Chương trình vẫn in được. Nhưng có hai cuốn mang mã một. Nếu sau này người dùng yêu cầu mượn cuốn mã một, mình sẽ không phân biệt được họ muốn cuốn nào.
>
> Đây là một quy tắc của dự án: mỗi bản sách cần một mã riêng. Python không tự biết quy tắc đó chỉ vì mình gọi trường này là `id`.

[RESTORE id 3. Then swap the complete first and third dictionary lines, keeping each record intact. Save and run.]

> Mình đổi thứ tự hiển thị, nhưng mã của từng cuốn vẫn giữ nguyên. Mã không phải vị trí hiện tại trong danh sách. Nó giúp mình tham chiếu đúng cuốn ngay cả khi sắp xếp lại.

[RESTORE original order and save.]

> Hôm nay mình kiểm tra mã bằng mắt với ba cuốn mẫu. Ở phần kiểm thử cuối dự án, mình sẽ thêm cách phát hiện mã trùng tự động. Hiện tại chương trình chưa có kiểm tra đó.

## 7 · Check this version against its goal — about 45 seconds

[SCREEN: Keep the output and scope note side by side if readable; otherwise alternate between them.]

> Mình quay lại mục tiêu đầu: xem được mã, tên và trạng thái. Có ba cuốn, ba mã khác nhau; cuốn thứ hai đang mượn, hai cuốn còn lại còn trống.
>
> Mình thử đổi riêng trạng thái của cuốn thứ ba, rồi chạy lại để kiểm tra xem chỉ thông tin đó thay đổi đúng không.

[ACTION: Change book 3 to True, save, run, compare. Restore False and save.]

> Đúng như mong đợi. Đây là kiểm tra nhỏ nhưng cụ thể: mình biết đã đổi dữ liệu gì và kết quả nào cần đổi theo.

## 8 · Student task — about 30 seconds

[SCREEN: Show the task, hide the completed function.]

> Bạn hãy thêm cuốn thứ ba với mã riêng, rồi đưa phần hiển thị vào hàm `show_books(items)` và gọi hàm với danh sách của bạn. Đổi ít nhất một tên sách thành cuốn bạn chọn.
>
> Chạy thử để xem đủ ba dòng và đúng trạng thái. Sau đó đổi thứ tự hai cuốn, giữ nguyên mã, rồi kiểm tra lại. Tạm dừng video để làm nhé.

[PAUSE for 5 seconds. Separate the task from the closing check with a chapter boundary.]

## 9 · Close with the next missing ability — about 30 seconds

> Khi giải thích bài của mình, hãy chỉ ra danh sách dữ liệu ở đâu, hàm hiển thị ở đâu và dòng nào gọi hàm. Nếu chạy mà không thấy gì, trước hết kiểm tra xem đã gọi hàm chưa.
>
> Phiên bản đầu đã cho mình xem tủ sách. Bài tiếp theo sẽ thêm việc tìm sách còn trống và thay đổi trạng thái khi mượn hoặc trả, để người dùng bắt đầu thao tác với chương trình.

## Instructor review

- Avoid presenting this as a second dictionary introduction: emphasize scope, reuse and explicit checks.
- Explain items versus books and show the function call outside the definition.
- Final code should match solution.py except for intentionally personalized titles.
- Restore IDs 1/2/3, original order and borrowed values False/True/False.
- Describe duplicate-ID rejection as future work, not a feature already implemented.
- Never present the sample shelf or imagined user as an actual classroom deployment.
