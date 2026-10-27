# BK02 · Tìm sách, mượn và trả

Video 08 · Vietnamese spoken script + instructor directions · private rehearsal draft

Target edited length: 11–15 minutes. This lesson has more new syntax than earlier lessons. If rehearsal feels rushed, split after section 4 into “Search and change status” and “Connect the menu.” Timings are estimates, not subtitle timestamps. Speak quoted passages; bracketed directions are actions.

## Before recording

- Copy starter.py to my-work.py in lesson 08. Keep starter.py and solution.py unchanged. Use the same editor and run command as earlier recordings.
- The starter contains the previous book display. Begin by adding functions below show_books and replacing its final call with the temporary test calls in this script.
- Keep solution.py ready for the opening demonstration and later menu scaffold. Tell students when using supplied code; do not imply they should already know while, try/except or the main guard.
- For the final menu version, use the STARTER data and main function from this lesson's solution.py. This version does not save files. Do not accidentally use lesson 09's menu.
- Rehearse the full interaction: f → blank; b → 1; f → De Men; r → 1; f → De Men; q. Each arrow means enter the response and press Enter.

## 1 · Show an interaction — about 45 seconds

[SCREEN: Run solution.py. Find available books, borrow ID 1, search De Men again, then return ID 1 and search again. Quit.]

> Chào bạn. Hôm trước mình đã xem được tủ sách. Hôm nay mình muốn người dùng làm được ba việc: tìm sách còn trống, ghi nhận một lượt mượn và trả lại sách.
>
> Bạn thấy cuốn mã một xuất hiện lúc đầu. Sau khi mượn, nó không còn trong kết quả sách trống. Khi trả, nó xuất hiện lại. Mình sẽ xây từng phần rồi nối chúng với một menu nhỏ.

[ACTION: Switch to the working copy.]

## 2 · Search only available books — about 90 seconds

[TYPE this function below show_books.]

```python
def find_available(books, keyword):
    matches = []
    keyword = keyword.strip().casefold()
    for book in books:
        if not book["borrowed"] and keyword in book["title"].casefold():
            matches.append(book)
    return matches
```

> Cách tìm này giống bài hàm, nhưng mỗi phần tử bây giờ là một dictionary. Mình lấy tên qua khóa `title`, rồi kiểm tra từ khóa có nằm trong tên không.
>
> Có thêm điều kiện `not book["borrowed"]`: cuốn đó chưa được mượn. Từ `and` nối hai yêu cầu, nghĩa là cả hai đều phải đúng. Tên phù hợp nhưng sách đang được mượn thì chưa được thêm vào kết quả.
>
> Mình thêm cả thông tin cuốn sách vào `matches`, không chỉ tên. Như vậy kết quả vẫn có mã và trạng thái để mình dùng tiếp. `return` nằm sau vòng lặp, giống điều mình đã kiểm tra ở bài sáu.

[REPLACE the previous final show_books call with these tests, placed after the function definitions.]

```python
show_books(find_available(books, ""))
show_books(find_available(books, " DE MEN "))
```

[ACTION: Save and run. Point out IDs 1 and 3 in the first result, only 1 in the second.]

> Từ khóa rỗng khớp mọi tên, nhưng điều kiện chưa mượn vẫn được giữ. Vì vậy lần đầu chỉ có mã một và ba; mã hai đang được mượn nên không xuất hiện.

## 3 · Change exactly one book — about two minutes

[ADD this function before the temporary test calls.]

```python
def set_loan(books, book_id, borrowed):
    for book in books:
        if book["id"] == book_id:
            if book["borrowed"] == borrowed:
                return False
            book["borrowed"] = borrowed
            return True
    return False
```

> Hàm này nhận danh sách, mã cuốn cần đổi và trạng thái muốn đặt. Muốn mượn thì truyền `True`; muốn trả thì truyền `False`.
>
> Mình tìm cuốn có mã khớp. Nếu trạng thái đã giống yêu cầu thì không có thay đổi mới, nên trả về `False`. Nếu khác, mình cập nhật trạng thái rồi trả về `True`.

[POINT to the last return False, outside for.]

> Nếu duyệt hết mà không tìm được mã, hàm cũng trả về `False`. Ở đây giá trị trả về cho biết có thay đổi thành công hay không. Nó không phải trạng thái mượn mới của cuốn sách.
>
> Điều đó có nghĩa là trả sách thành công vẫn trả về `True`, dù trạng thái `borrowed` vừa được đặt thành `False`.

[REPLACE temporary test calls with the following. Run from fresh sample data.]

```python
print(set_loan(books, 1, True))
print(set_loan(books, 1, True))
print(set_loan(books, 99, True))
print(set_loan(books, 1, False))
```

[PAUSE for prediction before running. Expected: True, False, False, True.]

> Lần đầu mượn mã một có thay đổi. Mượn lại ngay thì không. Mã chín mươi chín không tồn tại. Lần cuối trả mã một có thay đổi nên kết quả là `True`.
>
> Mình dùng mã riêng cho mỗi cuốn như đã thống nhất. Hàm này chưa kiểm tra dữ liệu có mã trùng; mình sẽ bổ sung kiểm tra đó ở bài cuối.

## 4 · A search that accidentally shows borrowed books — about one minute

> Mình thử cố tình bỏ phần kiểm tra trạng thái trong hàm tìm kiếm.

[ACTION: Temporarily change the if in find_available to only `if keyword in book["title"].casefold():`. Replace test calls with the following.]

```python
set_loan(books, 1, True)
show_books(find_available(books, "De Men"))
```

[ACTION: Save and run. The borrowed book incorrectly appears, labeled dang muon.]

> Tên vẫn khớp nên cuốn đang mượn vẫn xuất hiện. Code chạy được, nhưng đã vi phạm mục tiêu: kết quả phải là sách còn trống.

[RESTORE the complete condition; rerun. There is no book output.]

> Khi khôi phục điều kiện, không còn cuốn phù hợp. Hiện hàm hiển thị không in gì khi danh sách rỗng. Trong menu, mình sẽ thêm thông báo để người dùng hiểu chuyện gì xảy ra.

[OPTIONAL split point. End the first part with the two functions working; start the second with a short recap.]

## 5 · Connect the supplied menu — about two minutes

[ACTION: Remove temporary calls. Move to the final structure in lesson 08's solution: STARTER sample data, the two functions just taught, and the supplied main function and bottom guard. Copy the main scaffold in a visible step. The old show_books is not used by this menu and may be removed from the working copy to match the reference.]

> Phần menu có một số cú pháp mới, nên mình chuẩn bị sẵn khung để cùng đọc. Bạn không cần tự nhớ hết khung này trước khi làm bài. Mục tiêu chính là hiểu nó gọi hai hàm vừa viết lúc nào và dùng kết quả ra sao.

[POINT to the start of main.]

```python
books = [book.copy() for book in STARTER]
```

> Dòng đầu tạo danh sách làm việc từ dữ liệu mẫu, sao chép từng dictionary sách. Đây là cách viết gọn của việc duyệt các sách mẫu rồi thêm từng bản sao vào danh sách mới. Với dữ liệu đơn giản hiện tại, mình có thể đổi trạng thái mà không đổi trực tiếp các dictionary mẫu.

[POINT to while True, input and the q branch.]

> `while True` giữ menu lặp lại. Mỗi lượt, chương trình hỏi mình muốn làm gì. Nhập `q` thì `break` thoát vòng lặp. Các lựa chọn còn lại là `f` để tìm, `b` để mượn và `r` để trả.

[POINT to the f branch, its call to find_available, and if not matches.]

> Khi chọn tìm, menu hỏi từ khóa, gọi `find_available`, rồi in mã và tên của từng kết quả. Nếu danh sách rỗng, `if not matches` giúp hiện thông báo không có sách trống phù hợp, thay vì im lặng.

[POINT to `elif action in ("b", "r")`.]

> Nhánh này xử lý chung hai lựa chọn mượn và trả. Phần trong ngoặc chứa hai giá trị được chấp nhận; phép kiểm tra hỏi xem lựa chọn có nằm trong hai giá trị đó không.

## 6 · Read and validate a book ID — about 90 seconds

[HIGHLIGHT this existing section of the scaffold.]

```python
try:
    book_id = int(input("Book ID: "))
except ValueError:
    print("Use a whole-number book ID.")
    continue
```

> `input` trả về văn bản, còn mã trong dữ liệu là số nguyên. `int` thử chuyển câu trả lời thành số nguyên để so sánh đúng kiểu.
>
> Nếu nhập `abc`, việc chuyển đổi gây `ValueError`. Phần `except` xử lý lỗi này bằng một lời nhắc. `continue` bỏ qua phần còn lại của lượt menu hiện tại và quay về hỏi lựa chọn tiếp theo.

[POINT to the set_loan call.]

```python
if set_loan(books, book_id, action == "b"):
    print("Changed for this session.")
else:
    print("Unknown book, or its status already matches.")
```

> `action == "b"` tạo ra `True` khi mượn và `False` khi trả. Giá trị đó được đưa vào hàm. Nếu hàm báo đã thay đổi, menu thông báo thành công trong phiên chạy này. Nếu không, nó báo mã không tồn tại hoặc trạng thái đã giống yêu cầu.
>
> Thông báo chung này còn có thể rõ hơn. Mình sẽ giữ nó đơn giản trước và ghi lại để cải thiện khi thử với người dùng.

[POINT briefly to the bottom guard.]

> Đoạn cuối `if __name__ == "__main__"` gọi `main` khi mình chạy trực tiếp file này. Đây là phần khởi động được cung cấp trong khung; hôm nay bạn chỉ cần biết nó đưa mình vào menu.

## 7 · Run a complete session — about 90 seconds

[ACTION: Save, run and narrate the following sequence. Do not run the temporary mutation tests before starting this menu.]

| Inputs | Expected result |
|---|---|
| f, then blank | IDs 1 and 3 |
| b, then 1 | Changed for this session |
| f, then De Men | No available books match |
| b, then 1 | No new successful change |
| b, then abc | Whole-number prompt, menu continues |
| b, then 99 | Unknown/already-matching message |
| r, then 1; f, then De Men | ID 1 appears again |
| b, then 1; q; restart; f, then De Men | ID 1 appears again because state was not saved |

> Mình thử cả hành động đúng lẫn đầu vào không phù hợp. Điểm quan trọng là thông báo phải phản ánh việc chương trình thực sự làm được, không báo thành công cho mọi yêu cầu.
>
> Cuối cùng mình mượn sách, thoát rồi chạy lại. Sách lại còn trống, vì dữ liệu vừa thay đổi mới nằm trong bộ nhớ của lần chạy trước. Bài tiếp theo sẽ xử lý việc giữ lại dữ liệu.

## 8 · Student task and close — about 40 seconds

[SHOW the task and pause point.]

> Bạn hãy hoàn thành hai hàm tìm sách trống và thay đổi trạng thái, rồi nối với menu mẫu. Thử tìm, mượn, tìm lại, trả, rồi thử mã không tồn tại và một câu trả lời không phải số.
>
> Trước mỗi lần thử, nói kết quả bạn mong đợi. Tạm dừng video để làm từng bước; bạn có thể hoàn thành phần tìm kiếm trước rồi mới nối menu.

[PAUSE for 5 seconds; separate the closing check.]

> Khi giải thích bài, hãy theo một lượt mượn từ lựa chọn `b`, tới mã sách, tới dictionary được đổi và cuối cùng là thông báo. Nếu hiểu được đường đi đó, bạn đã hiểu cách các phần phối hợp, thay vì chỉ chạy một file có sẵn.

## Instructor review

- Use lesson 08's non-persistent menu; no books.json should be created.
- Explain set_loan's success boolean separately from borrowed status.
- Restore the availability filter and remove temporary mutation calls.
- Final working code should match solution.py, with the supplied scaffold clearly identified.
- Give this lesson room. Splitting is preferable if menu syntax overwhelms the core task.
