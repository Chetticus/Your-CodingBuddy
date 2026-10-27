# PY01 · Chương trình đầu tiên: cho máy tính hiển thị điều mình muốn

Vietnamese spoken script + instructor directions · draft for Nam to rehearse

Estimated edited length: 5–7 minutes, depending on typing and pauses. Section timings are pacing suggestions, not subtitle timestamps. Read the quoted passages aloud in your own voice; bracketed directions are for you only.

## Before the take

- Use the editor and Python runner you have already tested. This script assumes an editor above a terminal, running `python my-work.py` from the lesson folder. If your machine uses `py`, say and show that consistently instead.
- Copy starter.py to my-work.py. For the on-screen build, replace the working copy with a blank file before recording. Keep starter.py and solution.py untouched.
- Keep solution.py ready for the opening demonstration, then close its tab to avoid running the wrong file.
- Students should have completed [the setup guide](../../STUDENT-START.md). This video teaches running and editing, not installation.
- Use large editor and terminal text. Keep these notes outside the recorded window.

## 1 · A small result first — approximately 30 seconds

[SCREEN: Run solution.py once. Let the three output lines remain visible. Optional: show your face for the opening sentence, then switch to the code.]

> Chào bạn, mình là Nam. Trong loạt bài này, mình sẽ cùng bạn làm một công cụ nhỏ để tìm sách và ghi lại sách đang được mượn.
>
> Nhưng mình sẽ bắt đầu từ một việc đơn giản hơn: làm cho máy tính hiện ra điều mình muốn. Ba dòng bạn đang thấy ở đây đều do một chương trình Python tạo ra. Cuối bài này, bạn sẽ tự viết và thay đổi được những dòng như vậy.
>
> Bạn hãy mở trình soạn thảo và Python đã chuẩn bị ở phần hướng dẫn bắt đầu. Nếu chưa chạy được Python, mình khuyên bạn làm phần đó trước rồi quay lại đây.

[ACTION: Switch to the blank my-work.py. Point once to the code area and once to the terminal.]

> Phía trên là nơi mình viết và lưu chương trình. Phía dưới là terminal, nơi mình chạy chương trình và đọc kết quả. Mình sẽ dùng cả hai phần này.

## 2 · Write and run one line — approximately 60–90 seconds

[TYPE slowly. Leave the complete line visible before explaining it.]

```python
print("Xin chao! Minh la Nam.")
```

> Mình gõ `print`, mở ngoặc, rồi đặt câu muốn hiển thị trong dấu nháy. Sau đó mình đóng dấu nháy và đóng ngoặc.
>
> Ở đây, `print` dùng để đưa nội dung ra màn hình. Phần nằm trong hai dấu nháy là văn bản mình muốn hiện ra. Bạn có thể đổi Nam thành một biệt danh bạn thích.
>
> Trong các ví dụ đầu, mình gõ tiếng Việt không dấu để dễ theo dõi trên nhiều máy. Python vẫn có thể hiển thị tiếng Việt có dấu.

[ACTION: Save visibly. Click the terminal. Type `python my-work.py`, then press Enter. Do not narrate a command different from the one you actually use.]

> Mình lưu file, rồi chạy file `my-work.py`. Và đây là câu vừa viết. Dấu nháy giúp Python nhận ra phần văn bản; chúng không xuất hiện trong kết quả.
>
> Nếu máy bạn dùng lệnh `py` hoặc `python3`, hãy dùng đúng lệnh đã chạy được trong phần chuẩn bị. Điều cần kiểm tra là mình đang chạy đúng file vừa lưu.

## 3 · Change something and predict — approximately 45 seconds

[ACTION: Replace only the text inside the quotes.]

```python
print("Xin chao! Minh la BanA.")
```

> Bây giờ mình chỉ đổi phần trong dấu nháy. Bạn đoán lần chạy tiếp theo sẽ hiện Nam hay BanA?

[PAUSE for 3 seconds. Save and rerun.]

> Là BanA. Cách gọi `print` vẫn giữ nguyên, nhưng nội dung mình đưa cho nó đã đổi.
>
> Nếu bạn sửa code mà vẫn thấy câu cũ, hãy kiểm tra hai việc trước: đã lưu chưa, và có đang chạy đúng file không. Bạn cũng cần nhìn kết quả của lần chạy mới nhất, vì terminal có thể vẫn giữ dòng cũ ở phía trên.

## 4 · Add two more lines — approximately 60 seconds

[ACTION: Restore Nam, then type the other two lines.]

```python
print("Xin chao! Minh la Nam.")
print("Minh dang hoc Python de lam mot tu sach chia se.")
print("Ban muon chia se cuon sach nao?")
```

> Mình thêm một dòng nói chương trình này hướng tới việc gì, rồi một câu hỏi.
>
> Trước khi chạy, bạn đoán câu hỏi sẽ xuất hiện trước hay sau lời chào?

[PAUSE. Save and run. Point to each output line in order.]

> Python thực hiện ba lệnh này theo thứ tự từ trên xuống. Mỗi lần gọi `print` như thế này sẽ hiện nội dung rồi xuống dòng.
>
> Có một điểm cần để ý: câu cuối trông giống câu hỏi, nhưng chương trình chưa chờ mình trả lời. Nó mới chỉ in một câu ra thôi. Ở bài sau, mình sẽ thêm phần nhận câu trả lời.

[ACTION: Briefly move the third line above the first, save and run. Then restore the original order and save.]

> Khi mình đổi thứ tự lệnh, thứ tự kết quả cũng đổi theo. Máy làm theo những gì mình viết; nó không tự quyết định câu nào nên đứng trước.

## 5 · Deliberately break one thing — approximately 60 seconds

> Mình sẽ cố tình làm sai một chỗ để xem Python báo thế nào.

[ACTION: In the working copy only, remove the closing quote from the first line. Save and run.]

```python
print("Xin chao! Minh la Nam.)
```

> Mình vừa bỏ dấu nháy đóng. Thay vì chạy bình thường, Python báo lỗi cú pháp, thường có tên là `SyntaxError`.
>
> Bạn chưa cần hiểu toàn bộ thông báo. Mình đọc tên lỗi và nhìn dòng được chỉ ra trước. Ở đây có dấu nháy mở nhưng không có dấu nháy đóng, nên phần văn bản chưa được viết đúng.

[ACTION: Restore the quote. Save and rerun all three lines.]

> Mình thêm lại dấu nháy và chạy lại để kiểm tra. Ba dòng đã hiện ra như trước. Khi gặp lỗi, hãy thử sửa một điểm rồi chạy lại, thay vì đổi nhiều chỗ cùng lúc và không biết điều gì đã giúp.

## 6 · Student task — approximately 30 seconds

[SCREEN: Show these three requirements as text, or point students to STUDENT.md.]

> Đến lượt bạn. Hãy viết ba dòng: một lời chào, một thứ bạn muốn làm bằng Python, và một câu hỏi bạn muốn chương trình hiển thị.
>
> Bạn không cần dùng tủ sách giống mình. Có thể là một câu đố về chủ đề bạn thích, hoặc một danh sách đồ cần chuẩn bị.
>
> Sau khi chạy được, đổi thứ tự hai dòng. Hãy đoán kết quả trước khi chạy lại. Bạn có thể tạm dừng video ở đây để thử.

[PAUSE for 5 seconds. Place a clear edit/chapter boundary before the check below. Do not immediately replace the task with an answer.]

## 7 · Check and close — approximately 30 seconds

> Để tự kiểm tra, bạn hãy nhìn ba việc: có đủ ba dòng không, nội dung có đúng phần bạn viết trong dấu nháy không, và thứ tự có đúng không.
>
> Hôm nay bạn đã viết, chạy, thay đổi và sửa một lỗi trong chương trình đầu tiên. Ở bài tiếp theo, mình sẽ dùng `input` để chương trình hỏi và thực sự nhận câu trả lời của người dùng.

[END: Keep the working code and output visible for a few seconds. No claim that the next video is already published.]

## Instructor check after the take

- Did you actually show Save → Run → new output?
- Did you explain that the printed question does not accept input yet?
- Did you restore the deliberate bug and the line order?
- Does the saved final working copy match solution.py, apart from intentionally personalized text?
- Can a viewer read the terminal when the video is displayed small?
