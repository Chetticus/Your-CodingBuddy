# PY06 · Viết một hàm tìm sách, rồi thử xem nó có làm đúng không

Vietnamese spoken script + instructor directions · private rehearsal draft

Target edited length: 8–10 minutes. These are pacing estimates, not subtitle timestamps. Speak quoted passages naturally. Bracketed cues are actions for the instructor.

## Before recording

- Work in lesson 06. Copy starter.py to my-work.py; keep the original starter and solution unchanged.
- Begin with the starter function returning an empty list. Remove its demonstration print temporarily for section 2; restore calls as directed.
- Keep the same editor, terminal and Python command as earlier videos. Preview solution.py, then close that tab.
- Rehearse searches for ` DE MEN `, `Mat`, `missing` and the empty string. Also rehearse the deliberate early-return bug using Mat, not just the first book.
- This lesson deliberately uses a list of title strings, not the dictionaries from video 05. Explain that simplification. Do not add available-book filtering yet.

## 1 · A job we will need more than once — about 40 seconds

[SCREEN: Run solution.py. Point to the matching list and the empty result.]

> Chào bạn. Khi tủ sách có nhiều cuốn, mình muốn tìm bằng một phần tên thay vì đọc hết danh sách. Mình cũng muốn tìm nhiều lần với các từ khóa khác nhau mà không phải chép lại đoạn code tìm kiếm.
>
> Hôm nay mình sẽ đặt công việc đó vào một hàm: đưa danh sách và từ khóa vào, rồi nhận lại những tên phù hợp.
>
> Bài trước mình đã có cả mã và trạng thái của sách. Trong bài này, mình tạm dùng danh sách chỉ có tên để tập trung vào cách viết hàm. Khi làm dự án, mình sẽ dùng lại ý tưởng tìm kiếm với dữ liệu đầy đủ hơn.

## 2 · Name the job and its inputs — about 75 seconds

[SCREEN: Show this incomplete but runnable function. Keep the title list below it; no function call yet.]

```python
def find_titles(titles, keyword):
    matches = []
    return matches


titles = ["De Men Phieu Luu Ky", "The Little Prince", "Mat Biec"]
```

> `def` bắt đầu phần định nghĩa hàm. Mình đặt tên là `find_titles`, nghĩa là tìm tên sách. Hai tên trong ngoặc là hai tham số: danh sách tên cần tìm trong đó, và từ khóa cần tìm.
>
> Các dòng thụt vào bên dưới là công việc của hàm. Hiện tại mình mới tạo một danh sách rỗng tên là `matches`, rồi trả danh sách đó về bằng `return`. Phần tìm kiếm chưa được viết.

[ACTION: Save and run. No output appears.]

> Chưa có gì hiện ra. Mình mới định nghĩa hàm, chưa gọi nó. Python biết hàm này là gì, nhưng phần thân không tự chạy chỉ vì mình đã viết nó.

[ADD below the title list.]

```python
result = find_titles(titles, "De Men")
print(result)
```

> Đây là lời gọi hàm. Mình đưa danh sách vào vị trí đầu, từ khóa vào vị trí thứ hai. Kết quả hàm trả về được gán cho `result`, rồi mình in kết quả đó.

[ACTION: Save and run; point to [].]

> Danh sách đang rỗng vì hàm chưa thêm kết quả nào. Bây giờ mình sẽ viết phần còn thiếu.

## 3 · Look through the titles — about 90 seconds

[UPDATE only the function to the simple case-sensitive version.]

```python
def find_titles(titles, keyword):
    matches = []
    for title in titles:
        if keyword in title:
            matches.append(title)
    return matches
```

> Mình duyệt từng tên bằng vòng lặp đã học. Trong dòng `if`, `keyword in title` kiểm tra xem từ khóa có xuất hiện bên trong tên sách hay không.
>
> Chữ `in` ở đây dùng để kiểm tra một phần văn bản nằm trong một văn bản khác. Còn ở dòng `for`, nó nằm trong cú pháp duyệt danh sách. Mình nhìn cả dòng để hiểu công việc đang làm.

[POINT to matches.append(title).]

> Nếu tên phù hợp, `append` thêm tên đó vào cuối danh sách kết quả. Nếu không phù hợp, mình bỏ qua tên đó và tiếp tục vòng lặp.

[TRACE the three titles with the cursor.]

> Với từ khóa De Men, cuốn đầu được thêm vào. Hai cuốn sau không khớp. Khi vòng lặp kết thúc, `return` trả lại danh sách đã tìm được.

[ACTION: Save and run; show the one-item result.]

> Mình giữ kết quả ở dạng danh sách vì một từ khóa có thể khớp nhiều tên. Nếu không khớp tên nào, danh sách sẽ rỗng.

## 4 · Handle case and extra spaces — about 60 seconds

[ACTION: Change the call's query to ` DE MEN `, save and run; show the empty result before fixing.]

> Tên có trong danh sách, nhưng chữ hoa và khoảng trắng làm phép so sánh hiện tại không khớp. Mình sẽ xử lý hai phía trước khi kiểm tra.

[REPLACE the if line.]

```python
if keyword.strip().casefold() in title.casefold():
    matches.append(title)
```

> `strip` bỏ khoảng trắng ở hai đầu từ khóa. `casefold` giúp đưa chữ về dạng phù hợp để so sánh không phân biệt hoa thường. Ở ví dụ này, bạn có thể hiểu mục đích của nó gần với `lower` mình đã dùng ở bài câu đố.
>
> Mình xử lý cả từ khóa và tên sách, nhưng vẫn thêm tên gốc vào kết quả, nên cách viết tên sách khi hiển thị không bị đổi.

[ACTION: Save and rerun the same query.]

> Lần này tìm thấy sách. Lưu ý cách này không bỏ dấu tiếng Việt và không tự sửa tên gõ sai. Mình chỉ đang xử lý chữ hoa thường và khoảng trắng hai đầu từ khóa.

## 5 · Return is different from print — about 45 seconds

[SCREEN: Keep `result = find_titles(...)` and `print(result)` visible. Point to return inside the function, then the separate print.]

> `return` đưa kết quả về nơi gọi hàm và kết thúc lần gọi đó. Nó không tự hiển thị kết quả trong file chương trình này. `print` mới là phần mình dùng để hiện nó ra terminal.
>
> Nhờ tách hai việc, sau này mình có thể lấy danh sách kết quả để đếm hoặc hiển thị theo cách khác, mà không phải viết lại phần tìm kiếm.

[ACTION: Temporarily comment out print(result), run to show no output, then restore it.]

> Hàm vẫn được gọi, nhưng khi bỏ dòng `print`, mình không thấy kết quả trên màn hình. Không thấy chữ xuất hiện chưa chắc có nghĩa là hàm không chạy.

## 6 · Catch a function that stops too soon — about 90 seconds

> Mình sẽ cố tình đặt `return` sai vị trí. Đây là lỗi có thể bị bỏ sót nếu mình chỉ thử một trường hợp.

[ACTION: Indent return matches one level so it is inside for but outside if.]

```python
def find_titles(titles, keyword):
    matches = []
    for title in titles:
        if keyword.strip().casefold() in title.casefold():
            matches.append(title)
        return matches
```

[ACTION: Run with De Men: it appears to work. Then change the query to Mat and rerun: [].]

> Tìm cuốn đầu thì có vẻ đúng. Nhưng tìm Mat Biec ở cuối lại không thấy. Mình lần theo chương trình: xử lý cuốn thứ nhất, rồi gặp `return`, nên hàm kết thúc ngay. Nó chưa kịp nhìn đến hai cuốn còn lại.
>
> Mình cần trả kết quả sau khi duyệt xong tất cả tên. Vì vậy `return` phải ra ngoài vòng lặp, nhưng vẫn nằm trong hàm.

[ACTION: Restore return to four-space indentation. Run with Mat and confirm the final book is found.]

> Giờ đã tìm được cuốn cuối. Khi sửa lỗi, mình chạy lại chính đầu vào từng làm sai để kiểm tra thay đổi có giải quyết được vấn đề không.

## 7 · Test more than one happy case — about 60 seconds

[ACTION: Temporarily use these four calls under the title list.]

```python
print(find_titles(titles, " DE MEN "))
print(find_titles(titles, "Mat"))
print(find_titles(titles, "missing"))
print(find_titles(titles, ""))
```

> Mình kiểm tra tên đầu, tên cuối, từ khóa không có và từ khóa rỗng. Bạn thử đoán kết quả cuối cùng.

[PAUSE for 3 seconds. Save and run.]

> Từ khóa rỗng trả về cả ba tên. Trong Python, chuỗi rỗng được coi là nằm trong mọi chuỗi. Với công cụ này, mình có thể dùng hành vi đó để cho xem tất cả tên. Ở một sản phẩm khác, mình có thể chọn nhắc người dùng nhập từ khóa thay vì làm như vậy.

## 8 · Student task and close — about 45 seconds

[SCREEN: Show the task; hide the completed function.]

> Bạn hãy hoàn thành `find_titles` trong file bài tập. Nó cần trả về những tên khớp từ khóa, không phân biệt hoa thường và bỏ qua khoảng trắng hai đầu từ khóa. Nếu không có tên phù hợp, trả danh sách rỗng.
>
> Hãy thử cả cuốn đầu và cuốn cuối, không chỉ một trường hợp. Tạm dừng video để làm trước khi xem lời giải.

[PAUSE for 5 seconds; clear chapter boundary before closing check.]

> Khi tự kiểm tra, hãy giải thích được hai điều: vì sao `return` nằm sau vòng lặp, và vì sao mình in kết quả ở ngoài hàm. Bạn không cần nhớ từng dòng để hiểu được hai ý đó.
>
> Đây là bài cuối của phần nền tảng Python đầu tiên. Tiếp theo mình sẽ ghép danh sách, dictionary, điều kiện, vòng lặp và hàm thành phiên bản đầu của tủ sách chia sẻ.

## Final code and instructor checks

Restore the two demonstration calls from solution.py, removing temporary result/print calls and extra tests from the final working copy. Keep the four test cases in the recording or student notes, not as an unexplained change to the reference file.

- Check the final function matches solution.py and return is outside for.
- Say that this searches titles only; it does not filter loan status.
- Show that the deliberate bug fails on a later item, then verify the fix on that item.
- Do not imply casefold removes Vietnamese accents.
- Allow the longer runtime if needed; the distinction between defining, calling, returning and printing deserves visible examples.
