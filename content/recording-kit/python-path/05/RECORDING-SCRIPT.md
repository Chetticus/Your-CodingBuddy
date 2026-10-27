# PY05 · Một cuốn sách có những thông tin gì?

Vietnamese spoken script + instructor directions · private rehearsal draft

Target edited length: 7–9 minutes. This lesson combines earlier conditions and loops with a new data structure; slow down at the nested indentation. Timings are estimates, not subtitle timestamps.

## Before recording

- Preserve starter.py and solution.py. Create my-work.py in lesson 05, starting with the single-book dictionary shown in section 2 rather than the complete list from the starter.
- Preview solution.py, then close its tab. Keep the same editor/run method as earlier videos.
- Prepare to distinguish three things on screen: list brackets `[]`, dictionary braces `{}`, and brackets used to look up a dictionary key, as in `book["title"]`.
- Use the exact sample data below. Rehearse changing the first borrowed value and swapping the two complete dictionary lines without changing their IDs.
- Do not add borrower identities, database terminology, JSON storage or loan actions yet. This lesson displays data; it does not implement borrowing.

## 1 · Give the data a purpose — about 40 seconds

[SCREEN: Run solution.py to show one available book and one borrowed book.]

> Chào bạn. Danh sách hôm trước cho biết có những tên sách nào. Nhưng nếu muốn mượn một cuốn, mình cần biết thêm: cuốn đó còn trống hay đang được mượn?
>
> Hôm nay mỗi cuốn sẽ có ba thông tin đi cùng nhau: mã sách, tên sách và trạng thái mượn. Mình sẽ lưu chúng bằng một cấu trúc trong Python gọi là dictionary.

[ACTION: Switch to the single-book working copy.]

## 2 · Describe one book — about 90 seconds

```python
book = {
    "id": 1,
    "title": "De Men Phieu Luu Ky",
    "borrowed": False,
}
print(book["title"])
```

> Trong cặp ngoặc nhọn này có các cặp khóa và giá trị. Khóa là tên thông tin mình muốn lấy. Ví dụ khóa `title` đi với tên sách, khóa `id` đi với mã số một.
>
> Dấu hai chấm nối khóa với giá trị của nó. Dấu phẩy ngăn các cặp thông tin. Dấu phẩy sau cặp cuối cũng được phép trong Python.

[POINT to borrowed and False.]

> `borrowed` có nghĩa là đang được mượn. Ở đây mình chọn `False`, tức là điều đó chưa đúng: sách chưa được mượn. Nếu đang được mượn, mình dùng `True`.
>
> `True` và `False` là hai giá trị boolean. Chúng viết hoa chữ đầu và không có dấu nháy. Đừng viết thành chuỗi chữ “False”, vì khi đó mình đã lưu một kiểu dữ liệu khác.

[POINT to book["title"]. Save and run.]

> Muốn lấy tên sách, mình dùng `book`, rồi khóa `title` trong ngoặc vuông. Ở đây dấu nháy là cần thiết: khóa mình đã dùng trong dictionary chính là đoạn chữ `title`.
>
> Dòng này chỉ in tên sách, thay vì in tất cả thông tin của cuốn đó.

## 3 · Put books into a list — about 75 seconds

[REPLACE the single-book example with the list and simple loop below.]

```python
books = [
    {"id": 1, "title": "De Men Phieu Luu Ky", "borrowed": False},
    {"id": 2, "title": "The Little Prince", "borrowed": True},
]
for book in books:
    print(book["title"])
```

> Để giữ nhiều cuốn, mình dùng lại danh sách ở bài trước. Nhưng mỗi phần tử bây giờ là một dictionary, thay vì chỉ là một tên sách.

[POINT to outer brackets, then each complete dictionary.]

> Cặp ngoặc vuông ngoài cùng chứa danh sách. Mỗi cặp ngoặc nhọn bên trong mô tả một cuốn. Mình viết mỗi cuốn trên một dòng cho dễ nhìn.
>
> Trong vòng lặp, biến `book` lần lượt nhận toàn bộ thông tin của từng cuốn. Vì vậy mình có thể lấy `book["title"]` để hiển thị tên của cuốn đang xử lý.

[ACTION: Save and run; point to each matching title.]

> Danh sách có hai cuốn nên vẫn có hai lượt lặp, giống bài trước. Điều thay đổi là mỗi lượt mình có nhiều thông tin hơn để dùng.

## 4 · Make the status readable — about 90 seconds

[REPLACE the loop body. Keep the list unchanged.]

```python
for book in books:
    if book["borrowed"]:
        status = "dang muon"
    else:
        status = "con trong"
    print(book["id"], book["title"], status)
```

> Mình dùng điều kiện đã học: nếu giá trị `borrowed` là đúng, tức `True`, thì trạng thái hiển thị là “đang mượn”. Nếu không, trạng thái là “còn trống”.
>
> Sau khi chọn được chữ để hiển thị, mình in mã, tên và trạng thái của cuốn đó.

[POINT carefully to indentation levels.]

> Có hai mức thụt dòng ở đây. `if`, `else` và dòng `print` đều nằm trong vòng lặp. Còn các dòng gán `status` nằm sâu hơn vì chúng thuộc từng nhánh điều kiện.
>
> Dòng `print` không nằm riêng trong nhánh `else`, vì mình muốn in cả sách đang mượn lẫn sách còn trống.

[ASK before running.]

> Cuốn mã một có `borrowed` bằng `False`, còn cuốn mã hai bằng `True`. Bạn đoán trạng thái nào sẽ hiện bên cạnh mỗi cuốn?

[PAUSE for 3 seconds. Save and run.]

> Mã một còn trống, mã hai đang mượn. Các chữ dễ đọc này được chọn từ dữ liệu boolean trong từng cuốn.

## 5 · Change the data, keep the rule — about 60 seconds

[ACTION: Change only book 1's borrowed value from False to True. Save and run.]

> Mình đổi trạng thái của cuốn mã một thành `True`, rồi chạy lại. Bây giờ cuốn đó cũng hiện đang mượn, dù phần hiển thị mình không sửa.
>
> Đây mới là mình chỉnh dữ liệu mẫu trực tiếp trong code. Chương trình chưa có thao tác cho người dùng mượn hoặc trả sách. Phần đó sẽ được xây khi mình làm dự án.

[RESTORE False. Swap the complete dictionary lines, retaining IDs. Save and run.]

> Mình thử đổi thứ tự hai cuốn. Cuốn mã hai được in trước, nhưng mã của nó vẫn là hai. Mã sách giúp mình nhận ra đúng cuốn, dù thứ tự hiển thị thay đổi.
>
> Nếu có hai bản sách cùng tên, mỗi bản có thể có mã riêng. Trong dự án này, mình cần giữ các mã không trùng nhau; Python chưa tự kiểm tra giúp mình việc đó ở đoạn code hiện tại.

[RESTORE original order and save.]

## 6 · Look up the wrong key — about 45 seconds

> Mình sẽ cố tình dùng sai một khóa để xem cách kiểm tra.

[ACTION: In the final print only, change book["title"] to book["name"]. Save and run.]

> Python báo `KeyError`, vì dictionary này không có khóa `name`. Dù “name” và “title” đều nghe có vẻ hợp lý, Python chỉ tìm đúng khóa mình đã đặt.

[POINT to the title key in the data; restore it in print, save and run.]

> Mình đối chiếu với dữ liệu, sửa lại thành `title`, rồi chạy lại. Khi gặp lỗi kiểu này, trước hết hãy xem khóa đang dùng có thực sự tồn tại và viết đúng không.

## 7 · Student task — about 30 seconds

[SCREEN: Show the task, not the final code.]

> Với hai sách trong file bài tập, hãy hiển thị mỗi cuốn trên một dòng gồm mã, tên và trạng thái dễ đọc. Sau đó đổi `borrowed` của cuốn thứ nhất và dự đoán kết quả trước khi chạy.
>
> Nếu muốn thử thêm, bạn đổi thứ tự hai cuốn nhưng giữ nguyên mã. Hãy kiểm tra rằng thông tin của mỗi cuốn vẫn đi cùng nhau. Tạm dừng video để làm nhé.

[PAUSE for 5 seconds. Insert a chapter boundary before the check.]

## 8 · Check and close — about 30 seconds

> Ban đầu, mã một cần hiện còn trống, mã hai hiện đang mượn. Khi chỉ đổi trạng thái của cuốn thứ nhất, chỉ trạng thái của cuốn đó nên thay đổi.
>
> Hôm nay mình đã dùng danh sách để giữ nhiều cuốn và dictionary để giữ các thông tin của từng cuốn. Ở bài tiếp theo, mình sẽ gom một công việc vào hàm để có thể dùng lại, bắt đầu từ việc tìm tên sách.

## Instructor review

- Explain the single dictionary before the list of dictionaries.
- Distinguish a string key such as "title" from the variable name book; this builds on video 02 rather than contradicting it.
- Point to nested indentation and ensure print runs for both statuses.
- Restore False for ID 1, True for ID 2, original order and the title key. Final code matches solution.py.
- Do not suggest IDs are automatically unique or that editing borrowed implements a complete borrowing system.
