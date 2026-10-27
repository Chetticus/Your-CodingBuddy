# PY04 · Một danh sách, nhiều cuốn sách

Vietnamese spoken script + instructor directions · private rehearsal draft

Target edited length: 5–7 minutes. Speak quoted passages naturally; bracketed directions are not narration. Duration is an estimate, not subtitle timing.

## Before recording

- Copy starter.py to my-work.py in lesson 04. Preserve the original starter and solution.
- Start with two books and `print(books)`, as in the starter. Have solution.py ready to preview.
- Use the same editor/run command as earlier videos. Rehearse adding Mat Biec as a third item and a temporary fourth book, then restoring the three-book final version.
- Keep the indentation guide visible. The central demonstration is which lines repeat; do not introduce indexes or range yet.

## 1 · Show what scales — about 40 seconds

[SCREEN: Run solution.py to show three labeled book lines and a single total.]

> Chào bạn. Mình quay lại ý tưởng tủ sách nhé. Nếu có ba cuốn, mình có thể viết ba lệnh `print`. Nhưng mỗi lần thêm sách lại phải thêm một lệnh thì hơi bất tiện.
>
> Hôm nay mình sẽ lưu các tên sách trong một danh sách, rồi dùng một vòng lặp để hiển thị từng cuốn. Khi thêm sách vào dữ liệu, phần hiển thị sẽ tự xử lý thêm cuốn đó.

[ACTION: Switch to my-work.py with the two-book starter.]

## 2 · Read the list — about 60 seconds

```python
books = ["De Men Phieu Luu Ky", "The Little Prince"]
print(books)
```

> `books` là tên biến của danh sách. Cặp ngoặc vuông bao quanh các phần tử. Ở đây mỗi phần tử là một tên sách, và hai phần tử được ngăn bằng dấu phẩy.
>
> Mỗi tên có nhiều từ nhưng vẫn là một phần tử, vì toàn bộ tên đó nằm trong một cặp dấu nháy.

[ACTION: Save and run. Point to the raw list output.]

> `print(books)` cho mình thấy cả danh sách, gồm cả dấu ngoặc và dấu nháy. Nó hữu ích để kiểm tra dữ liệu. Nhưng nếu muốn người dùng đọc mỗi cuốn một dòng, mình cần một cách hiển thị khác.

## 3 · Handle each item — about 90 seconds

[REPLACE print(books) with the loop.]

```python
books = ["De Men Phieu Luu Ky", "The Little Prince"]
for title in books:
    print("Sach:", title)
```

> Mình đọc là: với mỗi tên sách trong `books`, thực hiện phần thụt vào bên dưới.
>
> `title` là tên mình chọn để gọi phần tử đang được xử lý. Lượt đầu nó nhận tên cuốn thứ nhất. Lượt tiếp theo nó nhận tên cuốn thứ hai. Python lần lượt lấy các phần tử từ danh sách cho mình.

[POINT to each list item, then to title in print.]

> Còn `books` vẫn là toàn bộ danh sách. Hai tên này không cùng nghĩa: một bên là danh sách, một bên là một phần tử trong từng lượt lặp.
>
> Bạn đoán dòng `print` này sẽ chạy mấy lần?

[PAUSE for 3 seconds. Save and run.]

> Hai lần, nên có hai dòng sách. Mình chỉ viết một lệnh `print` trong code, nhưng vòng lặp thực hiện nó một lần cho mỗi phần tử.

## 4 · Add a book without rewriting the display — about 45 seconds

[ACTION: Add the third list item, leaving the loop unchanged.]

```python
books = ["De Men Phieu Luu Ky", "The Little Prince", "Mat Biec"]
for title in books:
    print("Sach:", title)
```

> Mình thêm Mat Biec vào danh sách. Có dấu phẩy trước phần tử mới, còn phần vòng lặp mình giữ nguyên.
>
> Nếu chạy lại, bạn nghĩ cần viết thêm một lệnh `print` nữa không?

[PAUSE. Save and run.]

> Không cần. Danh sách có ba phần tử nên phần thân vòng lặp chạy ba lần. Đây là lý do mình tách phần dữ liệu ra khỏi cách hiển thị.

## 5 · Count once — about 60 seconds

[ADD the final line aligned with for, not with the inner print.]

```python
books = ["De Men Phieu Luu Ky", "The Little Prince", "Mat Biec"]
for title in books:
    print("Sach:", title)
print("So cuon sach:", len(books))
```

> `len(books)` cho mình số phần tử trong danh sách, ở đây là ba. Nó không đếm số chữ trong tên sách.
>
> Mình đặt dòng in tổng ra ngoài vòng lặp. Nghĩa là sau khi đã xử lý xong từng cuốn, chương trình mới in tổng một lần.

[ACTION: Save and run. Temporarily add a fourth book, save and rerun.]

> Khi thêm cuốn thứ tư, số dòng sách và tổng đều đổi thành bốn. Mình không gõ sẵn số ba vào thông báo, nên tổng đi theo dữ liệu.

[RESTORE the three-book list and save.]

## 6 · A mistake that still runs — about 60 seconds

> Mình sẽ cố tình đưa dòng tổng vào trong vòng lặp. Bạn thử đoán điều gì sẽ đổi.

[INDENT the final print by four spaces.]

```python
for title in books:
    print("Sach:", title)
    print("So cuon sach:", len(books))
```

[PAUSE. Save and run with the three-book list.]

> Bây giờ sau mỗi cuốn lại có một dòng tổng. Không có thông báo lỗi, nhưng kết quả không đúng điều mình muốn.
>
> Vì cả hai dòng đều thụt vào, cả hai đều thuộc phần lặp. Tổng vẫn là ba trong mỗi lượt vì danh sách vẫn có ba phần tử; đây không phải số cuốn đã xử lý đến lúc đó.

[ACTION: Move the total print back out of the loop. Save and rerun.]

> Mình đưa dòng tổng ra ngoài, và nó chỉ xuất hiện một lần. Khoảng thụt dòng trong Python quyết định phần nào thuộc vòng lặp, chứ không chỉ để trình bày cho đẹp.

## 7 · Student task — about 30 seconds

[SCREEN: Show the task and hide the solution.]

> Bạn bắt đầu từ danh sách hai sách trong file bài tập. Thêm một cuốn bạn chọn, hiển thị mỗi tên trên một dòng với nhãn “Sách”, rồi in tổng đúng một lần ở cuối.
>
> Sau đó thêm một cuốn nữa để kiểm tra: phần hiển thị và tổng có tự đổi không? Hãy đoán số dòng trước khi chạy. Tạm dừng video và thử nhé.

[PAUSE for 5 seconds; chapter boundary before the check.]

## 8 · Check and close — about 30 seconds

> Với ba phần tử, bạn cần thấy ba dòng sách và một dòng tổng bằng ba. Nếu tổng xuất hiện nhiều lần, hãy nhìn lại thụt dòng. Nếu thêm sách mà tổng không đổi, kiểm tra xem bạn có dùng `len(books)` hay đang in một số viết sẵn.
>
> Bây giờ mình đã xử lý được nhiều tên sách. Nhưng chỉ tên thôi chưa cho biết cuốn nào đang được mượn. Bài tiếp theo sẽ thêm mã và trạng thái cho từng cuốn.

## Instructor review

- Track title through both original items rather than saying only “it loops.”
- Show that the total counts list entries, not unique titles or words. Two copies with the same title would still count as two entries.
- Restore three books and place the total outside the loop; final code matches solution.py.
- Optional learner question, without a new demo requirement: what would an empty list make the loop do? Answer: zero iterations, then the outer total prints 0.
