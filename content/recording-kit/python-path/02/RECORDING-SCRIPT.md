# PY02 · Để chương trình hỏi và nhận câu trả lời

Vietnamese spoken script + instructor directions · draft for Nam to rehearse

Estimated edited length: 6–8 minutes, depending on typing and pauses. These are pacing suggestions, not subtitle timestamps. Read only the quoted passages aloud; adapt their wording naturally.

## Before the take

- Use the same editor, text size, layout and Python command as video 01.
- Work in the lesson 02 folder. Copy starter.py to my-work.py, then replace the working copy with `print("Ban muon chia se cuon sach nao?")` for the opening build. Preserve the original files.
- Keep solution.py ready for the first demonstration. Close its tab after showing it.
- Demo answers: first run `BanA` / `Mat Biec`; second run `BanB` / `The Little Prince`. Use these consistently so the changed output is obvious.
- Rehearse input in the terminal: an answer is typed while the program is running, not at a new shell prompt or inside the source file.

## 1 · Show the difference — approximately 40 seconds

[SCREEN: Run solution.py. Enter BanA and Mat Biec. Leave the result visible.]

> Bài trước, chương trình của mình chỉ hiện những câu đã viết sẵn. Hôm nay, nó sẽ hỏi biệt danh và tên một cuốn sách, rồi dùng chính câu trả lời đó để tạo một thông báo.
>
> Bạn thấy ở đây: mình nhập BanA và Mat Biec, nên chương trình hiện “BanA muốn chia sẻ Mat Biec”. Nếu người khác nhập câu trả lời khác, thông báo cũng cần đổi theo.

[ACTION: Switch to my-work.py containing the single print line.]

> Mình bắt đầu từ câu hỏi ở bài trước. `print` chỉ hiện câu này ra rồi kết thúc. Muốn chờ người dùng gõ câu trả lời, mình sẽ dùng `input`.

## 2 · Ask one question — approximately 90 seconds

[ACTION: Replace the old line with the following.]

```python
nickname = input("Biet danh cua ban: ")
```

> Mình dùng `nickname` làm tên biến cho biệt danh. Bên phải dấu bằng là `input`, với câu hỏi nằm trong dấu nháy.
>
> Khi chạy dòng này, Python gọi `input` trước: hiện câu hỏi và chờ mình nhập. Sau khi mình nhấn Enter, câu trả lời được gán cho tên `nickname` để mình dùng ở những dòng tiếp theo.

[ACTION: Save and run. Before entering anything, point to the waiting cursor.]

> Chương trình đang chờ ở đây, chứ không bị treo. Mình bấm vào terminal, gõ BanA, rồi nhấn Enter.

[ACTION: Enter BanA. The program exits without printing the answer again.]

> Chương trình đã nhận câu trả lời, nhưng mình chưa yêu cầu nó hiển thị lại. Mình thêm một dòng nữa.

```python
nickname = input("Biet danh cua ban: ")
print(nickname)
```

[ACTION: Save, run, enter BanA again.]

> Lần này `print` dùng giá trị đang gắn với tên `nickname`, nên kết quả là BanA.
>
> Dấu bằng trong dòng đầu là phép gán: lấy kết quả bên phải và gắn với tên bên trái. Nó không phải câu hỏi xem hai bên có bằng nhau hay không. Phần so sánh mình sẽ học sau.

## 3 · A name versus literal text — approximately 45 seconds

[ACTION: Temporarily add `print("nickname")` below `print(nickname)`.]

> Mình thử thêm một dòng gần giống hệt. Dòng này có dấu nháy quanh `nickname`. Bạn đoán hai dòng có hiện giống nhau không?

[PAUSE for 3 seconds. Run with BanA.]

> Dòng không có dấu nháy hiện BanA, là giá trị của biến. Dòng có dấu nháy hiện nguyên chữ nickname, vì mình đã yêu cầu Python in đúng đoạn văn bản đó.
>
> Khi muốn dùng câu trả lời của người dùng, mình viết tên biến không có dấu nháy.

[ACTION: Remove the temporary `print("nickname")` line.]

## 4 · Ask about a book and combine the answers — approximately 90 seconds

[ACTION: Add the book input between nickname input and print. Replace the print line as below.]

```python
nickname = input("Biet danh cua ban: ")
book = input("Cuon sach ban muon chia se: ")
print(nickname, "muon chia se", book)
```

> Mình cần một câu trả lời nữa, nên tạo biến `book` để giữ tên sách.
>
> Ở dòng cuối, mình đưa ba phần cho `print`: biệt danh người dùng, đoạn chữ “muốn chia sẻ”, rồi tên sách. Các phần được ngăn bằng dấu phẩy. Với cách dùng mặc định này, `print` thêm khoảng trắng giữa các phần.
>
> Hai câu trả lời cần hai tên biến khác nhau. Nếu mình gán tên sách vào `nickname` lần nữa, giá trị trước đó gắn với tên này sẽ bị thay thế.

[ACTION: Save and run; enter BanA / Mat Biec. Point to how each answer appears in the final sentence.]

> Đây là biệt danh ở câu hỏi đầu, còn đây là tên sách ở câu hỏi thứ hai. Phần chữ ở giữa giữ nguyên vì mình viết sẵn nó trong dấu nháy.

[ACTION: Run again without editing the source; enter BanB / The Little Prince.]

> Lần này mình không sửa code. Chỉ thay câu trả lời, và kết quả đã thay đổi. Tên sách có nhiều từ vẫn được nhận đầy đủ, vì `input` đọc nội dung mình gõ cho đến khi nhấn Enter.
>
> Ở bài này, những câu trả lời đó đều là văn bản. Chương trình cũng chưa lưu chúng vào file; mỗi lần chạy lại mình sẽ nhập lại. Mình sẽ học phần lưu dữ liệu khi làm dự án tủ sách.

## 5 · A deliberate variable-name mistake — approximately 60 seconds

> Mình sẽ cố tình đổi một chữ để xem lỗi nào xuất hiện.

[ACTION: Change only book to Book in the final print. Keep the assignment lowercase.]

```python
print(nickname, "muon chia se", Book)
```

[ACTION: Save, run and answer BOTH prompts before the error appears.]

> Hai câu hỏi vẫn chạy. Nhưng đến dòng cuối, Python không tìm thấy tên `Book` viết hoa, nên báo `NameError`.
>
> Mình đã gán câu trả lời cho `book` viết thường. Trong Python, `book` và `Book` là hai tên khác nhau. Mình nhìn tên trong dòng gán rồi đối chiếu với tên trong dòng đang lỗi.

[ACTION: Restore lowercase book; save, rerun, answer both questions and show the working result.]

> Mình sửa cho hai tên khớp nhau và chạy lại. Đây là cách kiểm tra lỗi này: tìm nơi tạo biến, rồi xem nơi sử dụng có viết đúng tên không.

## 6 · Your turn — approximately 30 seconds

[SCREEN: Show the exercise. Leave the solution out of view.]

> Bạn hãy tự làm một chương trình hỏi biệt danh và tên sách, rồi in một câu chứa cả hai câu trả lời. Dùng cách diễn đạt của bạn cũng được.
>
> Chạy hai lần với hai bộ câu trả lời khác nhau, và thử ít nhất một tên sách có nhiều từ. Mục tiêu là kết quả đổi theo câu trả lời mà bạn không phải sửa code giữa hai lần chạy.
>
> Bạn tạm dừng video ở đây và thử nhé. Nếu cần, phần bài tập có gợi ý để bạn xem từng bước.

[PAUSE for 5 seconds. Add a chapter/edit boundary before the check.]

## 7 · Check understanding and close — approximately 40 seconds

> Để kiểm tra, bạn nhìn xem chương trình có chờ ở cả hai câu hỏi không, và câu cuối có dùng đúng cả hai câu trả lời không.
>
> Một câu hỏi thêm: `print(book)` và `print("book")` khác nhau thế nào?

[PAUSE for 3 seconds.]

> Dòng đầu dùng giá trị của biến `book`. Dòng sau chỉ hiện nguyên chữ book.
>
> Bây giờ chương trình của mình đã có thể nhận thông tin và dùng lại nó. Nhưng nó vẫn chấp nhận cả câu trả lời trống. Ở bài tiếp theo, mình sẽ bắt đầu dùng điều kiện để phản hồi khác nhau tùy câu trả lời.

[END: Leave the three correct code lines and final output visible.]

## Instructor check after the take

- Did the viewer see exactly where to type answers?
- Did you explain why the program pauses at input?
- Did you run the same code with two different sets of answers?
- Did you distinguish assignment from comparison, and variable names from quoted text?
- Did you restore lowercase book and remove the temporary print line?
- Did you avoid claiming that input saves data permanently or validates it automatically?
