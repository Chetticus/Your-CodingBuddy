# PY03 · Đúng, sai hay chưa trả lời?

Vietnamese spoken script + instructor directions · private rehearsal draft

Target edited length: 6–8 minutes. Timing is an estimate, not subtitle timing. Speak the quoted passages in your own words; bracketed cues are instructor actions.

## Before recording

- Use the same editor, terminal and run command as videos 01–02. Work on a copy named my-work.py in lesson 03, keeping starter.py and solution.py unchanged.
- Start the working copy with only `answer = input("Ham nao hien thi chu trong Python? ")`.
- Rehearse five inputs: `print`, `loop`, Enter alone, ` PRINT `, and spaces alone. Type these answers without quotation marks.
- Have solution.py ready for the result preview; close its tab afterward. Run the working copy with `python my-work.py`, or the tested alternative used in earlier videos.
- Ensure four-space indentation is visible. Do not introduce nested conditions, scoring or multiple questions yet.

## 1 · Show the problem — about 40 seconds

[SCREEN: Run solution.py with print, then run again with loop. Keep both responses visible.]

> Chào bạn. Hôm trước, chương trình đã nhận được câu trả lời của mình. Nhưng nếu làm một câu đố, chỉ nhận câu trả lời thôi chưa đủ. Mình muốn trả lời đúng thì có một phản hồi, trả lời sai thì có một gợi ý.
>
> Bạn thấy hai lần chạy này: mình dùng cùng một chương trình, nhưng kết quả khác nhau vì câu trả lời khác nhau. Hôm nay mình sẽ viết phần quyết định đó bằng điều kiện.

[ACTION: Switch to the working copy containing just the input line.]

> Câu hỏi của mình là: hàm nào dùng để hiển thị chữ trong Python? Mình đã dùng hàm này từ bài đầu: `print`.

## 2 · Add the first decision — about 90 seconds

[TYPE the following below the existing input.]

```python
if answer == "print":
    print("Dung roi!")
```

> Mình đọc dòng này như sau: nếu câu trả lời bằng đoạn chữ “print”, thì hiển thị “Đúng rồi”.
>
> Ở bài trước, một dấu bằng dùng để gán giá trị cho biến. Ở đây là hai dấu bằng, dùng để so sánh. Mình đang kiểm tra xem giá trị của `answer` có bằng đoạn văn bản bên phải hay không.

[POINT to the colon, then the indented print.]

> Cuối dòng `if` có dấu hai chấm. Dòng bên dưới được thụt vào để cho biết nó thuộc phần sẽ thực hiện khi điều kiện đúng. Trong ví dụ này, mình dùng bốn khoảng trắng. Trình soạn thảo thường giúp mình thụt vào tự động.

[ACTION: Save and run with print. Then run with loop.]

> Với `print`, thông báo xuất hiện. Với `loop`, chương trình kết thúc mà chưa có phản hồi nào, vì mình mới viết phần dành cho câu trả lời đúng.

## 3 · Handle the other case — about 45 seconds

[ADD else aligned with if.]

```python
answer = input("Ham nao hien thi chu trong Python? ")
if answer == "print":
    print("Dung roi!")
else:
    print("Chua dung. Goi y: ham minh dung o bai 1.")
```

> `else` là phần còn lại: khi điều kiện phía trên không đúng, mình đưa ra gợi ý. Chữ `else` nằm cùng mức với `if`, còn nội dung của mỗi nhánh thụt vào bên dưới.
>
> Bạn đoán nếu nhập `loop`, chương trình sẽ hiện một thông báo hay cả hai?

[PAUSE for 3 seconds. Save, run, enter loop.]

> Chỉ có gợi ý. Trong cấu trúc này, chương trình chọn một nhánh để thực hiện, chứ không chạy cả hai.

## 4 · Make the comparison fair — about 75 seconds

[ACTION: Run the current version with uppercase PRINT.]

> Mình vừa nhập đúng tên hàm nhưng viết hoa, và chương trình vẫn nói chưa đúng. Đây không phải lỗi làm chương trình dừng. Nó chạy được, nhưng cách so sánh chưa đúng ý mình.
>
> Trong câu đố này, mình muốn chấp nhận cả chữ hoa và khoảng trắng thừa ở hai đầu. Mình sẽ xử lý câu trả lời trước khi kiểm tra.

[REPLACE the first line only.]

```python
answer = input("Ham nao hien thi chu trong Python? ").strip().lower()
```

> `strip` bỏ khoảng trắng ở đầu và cuối. `lower` chuyển chữ hoa thành chữ thường. Kết quả sau hai bước đó mới được gán vào `answer`.
>
> Những bước này không sửa mọi lỗi gõ. Nếu bạn nhập sai tên hàm hoặc chèn khoảng trắng vào giữa tên, nó vẫn khác đáp án.

[ACTION: Save, run with space-PRINT-space. Show the accepted result.]

> Bây giờ câu trả lời này được xử lý thành `print`, nên được chấp nhận. Mình đã kiểm tra chính trường hợp vừa làm chương trình phản hồi chưa hợp lý.

## 5 · Distinguish an empty answer — about 60 seconds

[ACTION: Run and press Enter without typing. It currently gives the wrong-answer hint.]

> Nếu chưa nhập gì, mình muốn nhắc người dùng trả lời, thay vì đưa gợi ý như khi họ đã thử. Mình thêm một trường hợp ở giữa.

[INSERT elif before else. Show the complete version.]

```python
answer = input("Ham nao hien thi chu trong Python? ").strip().lower()
if answer == "print":
    print("Dung roi!")
elif answer == "":
    print("Ban chua nhap cau tra loi.")
else:
    print("Chua dung. Goi y: ham minh dung o bai 1.")
```

> `elif` nghĩa là: nếu điều kiện trước chưa đúng, kiểm tra thêm điều kiện này. Hai dấu nháy không có gì ở giữa biểu diễn một chuỗi rỗng.
>
> Chương trình kiểm tra từ trên xuống. Gặp nhánh đúng thì thực hiện nhánh đó. Nếu không nhánh nào phía trước đúng, nó dùng `else`.

[ACTION: Save and test Enter alone, then spaces alone.]

> Cả hai đều được nhắc nhập câu trả lời. Với trường hợp chỉ có khoảng trắng, `strip` đã bỏ chúng đi nên phần còn lại cũng là chuỗi rỗng.

## 6 · Read one syntax error — about 40 seconds

> Mình sẽ cố tình bỏ một dấu để cùng đọc lỗi.

[ACTION: Remove the colon after the first if. Save and run. The syntax error happens before any question is asked.]

> Python báo lỗi cú pháp trước khi chạy được câu hỏi. Mình nhìn dòng được chỉ ra: cuối điều kiện đang thiếu dấu hai chấm.

[RESTORE the colon. Save and run with print.]

> Mình thêm lại rồi chạy để kiểm tra. Lỗi này khác với lúc nhập chữ hoa: khi đó chương trình vẫn chạy nhưng kết quả chưa đúng ý; còn lần này cú pháp chưa hợp lệ nên nó không chạy được.

## 7 · Pause and try — about 30 seconds

[SCREEN: Keep the task visible, hide the solution.]

> Bạn hãy hoàn thành câu đố có ba phản hồi: đúng, chưa đúng và chưa nhập gì. Sau đó thử `print`, `loop`, Enter trống và ` PRINT ` có khoảng trắng ở hai đầu.
>
> Trước mỗi lần chạy, ghi hoặc nói nhánh bạn nghĩ sẽ được chọn. Bạn có thể đổi lời phản hồi thành cách nói của mình. Tạm dừng video để thử nhé.

[PAUSE for 5 seconds. Add a chapter boundary before the check.]

## 8 · Check and close — about 30 seconds

> Nếu `print` và phiên bản viết hoa có khoảng trắng đều được chấp nhận, `loop` nhận gợi ý, còn bỏ trống được nhắc trả lời, thì chương trình đã làm đúng các trường hợp mình đặt ra.
>
> Điều quan trọng hôm nay là biết diễn đạt: khi nào chương trình nên làm việc nào. Ở bài tiếp theo, mình sẽ quay lại tủ sách và xử lý nhiều tên sách bằng danh sách và vòng lặp.

## Instructor review

- Show `=` versus `==`, the colon, and indentation without introducing extra syntax.
- Make clear that normalization is your chosen quiz behavior, not a universal rule for all inputs.
- Restore the deliberate syntax error; final code should match solution.py.
- Actually test all branches. Do not claim success after testing only the correct answer.
