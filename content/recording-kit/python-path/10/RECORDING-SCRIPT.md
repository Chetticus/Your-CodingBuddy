# BK04 · Kiểm thử, nhờ người dùng thử và cải thiện

Video 10 · Vietnamese spoken script + instructor directions · private rehearsal draft

Target edited length: 8–11 minutes, plus optional footage from an actual pilot. Timings are estimates, not subtitle timestamps. Do not invent tester feedback or imply a rehearsal is a real student session.

## Before recording

- Copy starter.py to my-work.py in a disposable lesson 10 folder. It is the completed lesson 09 program, without duplicate-ID validation.
- Open [the project brief and test table](../../PROJECT-BRIEF.md) and [pilot feedback sheet](../../PILOT-FEEDBACK.md).
- Prepare clean sample data with IDs 1/2/3 and borrowed values False/True/False. Keep a known-good backup. Quit before changing a data file manually.
- Use solution.py as the reference for the three duplicate-ID changes. Rehearse the broken-data test before filming.
- Plan one small usability change, such as explaining the menu choices in Vietnamese. Label it an instructor-proposed improvement unless a real tester actually suggested it.
- If no tester is available, record the rehearsal version in section 6 and leave real feedback for later. The lesson can still teach how to conduct a test.

## 1 · A working demo is the beginning of a check — about 40 seconds

[SCREEN: Show the running project and an unfilled test table.]

> Chào bạn. Chương trình của mình đã tìm, mượn, trả và lưu được dữ liệu. Nhưng chạy thành công một lần chưa cho biết các tình huống khác có làm đúng không.
>
> Hôm nay mình sẽ ghi rõ điều mong đợi, thử từng trường hợp, sửa một vấn đề về mã sách, rồi chuẩn bị cho một người khác dùng thử. Mục tiêu là biết chương trình làm được gì và còn thiếu gì, thay vì chỉ nói “chạy được rồi”.

## 2 · Write the expectation before running — about 90 seconds

[SCREEN: Project test table. Point to input, expected behavior and actual result.]

> Với mỗi lần kiểm tra, mình ghi đầu vào, kết quả mong đợi và kết quả thực tế. Mình viết điều mong đợi trước khi chạy, để không vô tình coi bất kỳ kết quả nào hiện ra cũng là đúng.

[ACTION: Starting from clean sample data, run the following. Fill the table with actual observations, not prefilled “pass” labels.]

| Trial | Expectation |
|---|---|
| f, blank | IDs 1 and 3; exclude borrowed ID 2 |
| f, ` DE MEN ` | ID 1 despite case and surrounding spaces |
| f, missing | Clear no-match message |
| b, 1; b, 1 again | First action changes state; second does not report a new success |
| b, abc; b, 99 | Helpful messages; no crash or false success |
| q; restart; f, De Men | ID 1 is still unavailable |
| r, 1; q; restart; f, De Men | ID 1 is available again |

> Một số kiểm tra phụ thuộc trạng thái từ bước trước. Ví dụ sau khi mượn mã một, mình không còn mong nó xuất hiện trong kết quả sách trống. Vì vậy mình ghi cả trạng thái bắt đầu và thứ tự thao tác, để có thể làm lại cùng bài thử.
>
> Nếu kết quả khác dự đoán, mình ghi lại đầu vào và thông báo thực tế trước khi sửa. Dữ liệu đó sẽ giúp tìm lỗi.

## 3 · Find the duplicate-ID problem — about one minute

[ACTION: Quit. Back up the valid file. In the disposable books.json, change the third book's id to 1 while retaining the first book's id 1. Run the starter-based program and find with a blank keyword.]

> Mình cố tình cho hai sách cùng mã một, giống vấn đề đã nói ở bài đầu dự án. Phiên bản hiện tại vẫn đọc được file vì kiểu dữ liệu của mã vẫn là số nguyên.
>
> Nhưng khi yêu cầu đổi trạng thái mã một, hàm sẽ gặp cuốn đầu tiên có mã đó rồi kết thúc. Nó không thể biết người dùng định chọn cuốn nào trong hai cuốn trùng mã.
>
> Thay vì chọn một cuốn tùy theo thứ tự, mình muốn từ chối dữ liệu này và báo vấn đề ngay lúc đọc file.

[ACTION: Quit before editing code. Keep this duplicate-data copy for verifying the fix.]

## 4 · Add a check for IDs already seen — about two minutes

[SCREEN: Show load_books in the working copy. Make exactly these changes from lesson 10 solution.py.]

1. Add `ids = set()` after the list-type check and before `for book in books:`.
2. Add `or book["id"] in ids` as the last condition in the existing invalid-entry test. Keep earlier structure/type checks in their original order.
3. Change the error message to `Invalid or duplicate book entry.` and add `ids.add(book["id"])` after the validation block, inside the loop.

```python
ids = set()
for book in books:
    if (not isinstance(book, dict)
            or type(book.get("id")) is not int
            or not isinstance(book.get("title"), str)
            or not book["title"].strip()
            or type(book.get("borrowed")) is not bool
            or book["id"] in ids):
        raise ValueError("Invalid or duplicate book entry.")
    ids.add(book["id"])
```

> `set` là một tập hợp. Ở đây mình dùng nó để ghi nhớ các mã đã gặp. Trước khi kiểm tra sách đầu tiên, tập hợp đang rỗng.
>
> Với mỗi cuốn, nếu mã đã nằm trong tập hợp thì mình đã thấy mã đó ở một cuốn trước: dữ liệu bị trùng. Nếu cuốn hợp lệ, mình thêm mã vào tập hợp bằng `add`, rồi mới xét cuốn tiếp theo.

[TRACE IDs 1, 2, 1 with the cursor or a short note.]

> Gặp một thì ghi nhớ một. Gặp hai thì ghi nhớ thêm hai. Gặp một lần nữa thì phát hiện đã có. Mình kiểm tra trước khi thêm, chứ không thêm xong rồi mới hỏi mã có trong tập hợp chưa.
>
> Các kiểm tra cấu trúc từ bài trước vẫn được giữ. Mình không bỏ chúng chỉ vì đã thêm kiểm tra mã trùng.

[ACTION: Save and run against the duplicate-ID file. Show the read error, then reopen the file to confirm it remains unchanged.]

> Giờ chương trình báo dữ liệu không hợp lệ và chưa vào menu. Nó không tự sửa mã hay xóa cuốn bị trùng. Người quản lý dữ liệu cần xem lại mã nào đúng.

[RESTORE the known-good sample file. Run again.]

## 5 · Check that the fix did not break normal use — about 60 seconds

> Mình vừa chứng minh bản sửa từ chối mã trùng. Nhưng còn phải kiểm tra dữ liệu đúng vẫn dùng được.

[ACTION: With restored valid data, run find → borrow 1 → quit → restart → find → return 1. Check the test table again.]

> Tìm kiếm vẫn đúng, trạng thái vẫn giữ qua lần chạy và trả sách vẫn hoạt động. Mình đánh dấu kết quả dựa trên lần chạy này.

[ACTION: Briefly repeat the malformed-JSON test from lesson 09 using a disposable copy, then restore it; or refer to a separately recorded test result, clearly labeled with its actual run.]

> Phần kiểm tra file hỏng cũng cần giữ: báo lỗi rõ ràng và không âm thầm ghi đè. Khi sửa một phần, mình kiểm tra lại những hành vi quan trọng có thể bị ảnh hưởng.

## 6 · Ask another person to use it — about 90 seconds

[SCREEN: Show the pilot sheet. If no tester is present, use the rehearsal narration below.]

> Tiếp theo mình muốn biết một người chưa nhìn code có hiểu cách dùng không. Mình chuẩn bị một yêu cầu: “Hãy tìm một cuốn còn trống, mượn nó, rồi trả lại.”
>
> Nếu đang tự thử như mình trong đoạn này, đây mới là diễn tập. Khi có người thử thật, mình sẽ đưa yêu cầu đó và quan sát, không chỉ họ từng phím ngay từ đầu.
>
> Mình ghi họ dừng ở đâu, hiểu thông báo thế nào và lúc nào cần hỏi. Nếu mình phải giúp, mình cũng ghi lại. Những điểm đó cho biết phần nào cần giải thích rõ hơn.

[OPTIONAL actual-pilot footage: use only with appropriate permission. Anonymous notes are sufficient; no face or voice recording is required. Use these questions without inventing responses.]

> Bạn nghĩ thông báo vừa rồi nghĩa là gì?
>
> Bạn muốn làm gì tiếp theo nhưng chưa biết cách?
>
> Chỗ nào bạn phải đọc lại?

> Mình không hỏi “Dễ dùng đúng không?”, vì câu đó dễ khiến người thử chỉ đồng ý. Mình cần biết họ đã làm gì và gặp vướng mắc cụ thể nào.

## 7 · Make one small, honest improvement — about 60 seconds

[ACTION: Save a separate experiment.py copy for this optional variation, preserving the reference-matching my-work.py. Replace only the menu prompt text, not command letters or logic.]

```python
action = input("f: tim sach | b: muon | r: tra | q: thoat > ").strip().lower()
```

> Một cải tiến mình đề xuất là giải thích lựa chọn menu bằng tiếng Việt rõ hơn. Đây là ý tưởng của mình để thử, chưa phải kết luận rằng người dùng đã thích hơn.
>
> Mình đổi phần hướng dẫn nhưng giữ các phím và logic. Sau đó mình cần chạy lại để kiểm tra các lựa chọn vẫn hoạt động. Nếu có người thử, mình có thể nhờ họ làm lại cùng nhiệm vụ và quan sát xem có còn vướng ở menu không.

[ACTION: Run the experiment with f, b, r and q. Record what actually happens. If a real observation suggests a different improvement, replace this section with that observation and change rather than inventing feedback to justify this example.]

## 8 · Student task and project submission — about 60 seconds

[SCREEN: Show the submission checklist from PROJECT-BRIEF.md.]

> Đến lượt bạn: thêm kiểm tra mã trùng, hoàn thành bảng thử và chọn một cải tiến riêng. Có thể là hướng dẫn rõ hơn, cách hiển thị dễ đọc hơn, hoặc một tính năng nhỏ bạn giải thích được lý do cần có.
>
> Bản nộp gồm code, dữ liệu mẫu, hướng dẫn chạy, kết quả kiểm tra và một ghi chú trước–sau về thay đổi của bạn. Kèm một đoạn giải thích ngắn: theo một lượt mượn từ đầu vào, qua thay đổi trạng thái, đến lúc lưu file.
>
> Tạm dừng video để làm từng phần. Nếu chưa có người dùng thử, hãy ghi rõ chưa thử với người khác; đừng tự điền phản hồi thay họ.

[PAUSE for 5 seconds, then clear closing boundary.]

## 9 · Close the first project — about 40 seconds

> Từ những lệnh in đầu tiên, bạn đã nối dữ liệu, điều kiện, vòng lặp, hàm và file thành một công cụ nhỏ. Điều mình muốn bạn giữ lại là cách chọn một việc cụ thể, làm phiên bản nhỏ, thử và sửa dựa trên kết quả.
>
> Công cụ này chạy trên một máy, chưa xử lý nhiều người dùng đồng thời và chưa xác minh ai được phép mượn. Đó là giới hạn cần nói rõ khi giới thiệu dự án.
>
> Bạn hãy chọn một điểm mình tự thay đổi và giải thích vì sao. Một phiên bản nhỏ mà bạn hiểu và kiểm tra được là kết quả đáng để tiếp tục phát triển.

## Instructor review

- Show the bug before the fix, then show both invalid and valid data after the fix.
- Keep the optional usability experiment separate from the canonical reference solution.
- Record actual test results; leave unknown pilot outcomes blank.
- Describe the project as a local learning tool, not proven classroom impact or a finished multi-user product.
- End with restored valid sample data, no deliberate corruptions, and a clear next action for learners.
