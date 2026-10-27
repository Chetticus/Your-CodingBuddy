# Final project: a classroom book exchange

## Student brief / Đề bài

Một bạn muốn tìm sách còn có thể mượn. Hãy làm một công cụ chạy trên máy tính để xem sách, tìm theo tên, mượn, trả và giữ lại trạng thái sau khi đóng chương trình. Dùng sách mẫu; chưa cần thông tin cá nhân hay tài khoản.

Build a local tool for browsing available books, searching titles, recording loans and returns, and saving state between runs. Use invented data. An online multi-user service is outside this first project.

## Submit

- Your Python file and a small sample dataset.
- A short README: how to run it, what it does, and one limitation.
- A completed test table with actual results.
- A before/after note describing one improvement you made yourself.
- A 1–2 minute explanation, spoken or written: follow one action from input to changed data.

## Acceptance checks

| Try this | Expected behavior | Your result |
|---|---|---|
| Find with an empty keyword | All available books, excluding borrowed ones | |
| Find ` DE MEN ` | Same result as `de men` | |
| Search for a nonexistent title | A helpful no-results message | |
| Borrow ID 1 | Status changes once; book disappears from available results | |
| Borrow ID 1 again | Does not falsely report a new successful loan | |
| Return ID 1 | Book becomes available again | |
| Enter `abc` for an ID | Explains the problem without crashing | |
| Enter ID 99 | Explains that the action could not be completed | |
| Quit and restart after borrowing | Borrowed status survives | |
| Use a damaged copy of the data file | Explains the read problem; does not silently overwrite it | |

## Review rubric

For each area mark **Needs work / Meets the brief / Goes further**, with one concrete piece of evidence. These are teaching criteria, not an external certification.

| Area | Meets the brief | Goes further |
|---|---|---|
| Useful behavior | Search, borrow, return and save work | A justified feature makes the tool more useful |
| Understanding | Explains list, dictionary, function and stored file in own words | Can predict how a code change affects behavior |
| Reliability | Handles missing IDs and non-number input | Investigates and handles an additional failure case |
| Usability | Clear prompts and results | Improves a confusing interaction after a real test |
| Reflection | States local-only limitation and describes one change | Connects feedback to a specific design decision |

Use one extension: display all books with status; add a category filter; or add a new book with a unique ID. Define its expected behavior before coding. Do not require all extensions to finish the course.
