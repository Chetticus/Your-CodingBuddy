from pathlib import Path
import json, shutil, textwrap, zipfile

root = Path(__file__).resolve().parents[1]
lessons = root / 'content/project-lessons'
downloads = root / 'apps/web/public/downloads/projects'
def write(path, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(body).strip()+'\n', encoding='utf-8')

theory = [
'''Một chương trình là các hướng dẫn được viết theo cú pháp mà Python hiểu. Bạn lưu hướng dẫn trong file `.py`; khi chạy file, Python thực hiện chúng. Trình soạn thảo là nơi viết, còn terminal là nơi chạy và đọc kết quả. Đừng gõ lệnh chạy vào giữa code Python.

Trong `print("Xin chao!")`, `print` là hàm hiển thị. Cặp ngoặc bao quanh thông tin được đưa vào hàm; cặp dấu nháy đánh dấu văn bản. Dấu nháy không xuất hiện trong kết quả. Mỗi lần gọi `print` như ví dụ sẽ kết thúc bằng xuống dòng. Ba lệnh nằm liên tiếp được thực hiện từ trên xuống.

Lưu file rồi chạy `python my-work.py` trong thư mục chứa file; tùy máy, lệnh đã được cài có thể là `py` hoặc `python3`. Nếu báo không tìm thấy file, kiểm tra thư mục hiện tại và tên file, đừng sửa code để chữa lỗi đường dẫn. Nếu máy chưa có Python, dùng bản cài từ trang chính thức python.org và nhờ người hỗ trợ khi cần.

Thử thay nội dung trong dấu nháy, lưu và chạy lại. Nhìn phần kết quả mới nhất vì terminal có thể giữ cả đầu ra cũ. Một câu hỏi được in bằng `print` chưa khiến chương trình chờ trả lời; bài sau sẽ thêm khả năng đó.

Nếu bỏ dấu nháy đóng, Python báo lỗi cú pháp. Đọc tên lỗi, xem dòng được chỉ ra, sửa một chỗ rồi chạy lại. Thông báo lỗi là thông tin để điều tra, không phải đánh giá khả năng của bạn.''',
'''Một chương trình tương tác cần nhận thông tin mới mỗi lần chạy. `input("Biet danh cua ban: ")` hiển thị lời nhắc và chờ bạn gõ trong terminal. Nhấn Enter để hoàn tất câu trả lời. Trong file chương trình này, `input` trả về một chuỗi văn bản.

`nickname = input(...)` thực hiện phần bên phải trước, rồi gán kết quả cho tên `nickname`. Một dấu `=` là phép gán, không phải phép so sánh. Biến là tên để dùng lại giá trị; khi gán giá trị mới cho cùng tên, giá trị được tham chiếu bởi tên đó thay đổi.

`print(nickname)` lấy giá trị của biến. `print("nickname")` in nguyên chữ nickname. Đây là khác biệt quan trọng giữa tên dùng trong chương trình và văn bản viết sẵn. Trong ví dụ cuối, biệt danh và tên sách không có dấu nháy ở dòng in, còn cụm `"muon chia se"` có dấu nháy vì nó là phần cố định.

Hai câu hỏi dùng hai biến để tránh ghi đè nhau. `print` nhận nhiều phần ngăn bằng dấu phẩy và mặc định thêm khoảng trắng giữa chúng. Tên sách có nhiều từ vẫn được nhận đầy đủ đến khi bạn nhấn Enter.

Python phân biệt hoa thường: `Book` không phải `book`. Nếu gặp `NameError`, tìm nơi gán biến rồi đối chiếu tên đang sử dụng. Ở bài này câu trả lời chưa được kiểm tra và chưa được lưu thành file; chạy lại thì bạn nhập lại. Đó là giới hạn của phiên bản hiện tại, không phải máy bị quên một file đã lưu.''',
'''Điều kiện giúp chương trình chọn hành động theo dữ liệu. Một câu đố cần phân biệt đúng, sai và chưa trả lời. `answer == "print"` so sánh giá trị, khác với dấu `=` dùng để gán. Phép so sánh cho kết quả đúng hoặc sai.

Trong chuỗi `if / elif / else`, Python xét từ trên xuống và thực hiện nhánh đầu tiên thỏa điều kiện. `else` nhận các trường hợp còn lại. Dấu hai chấm bắt đầu khối lệnh; phần thụt vào bên dưới thuộc nhánh đó. Các chữ `if`, `elif`, `else` phải cùng mức thụt dòng.

Hai dấu nháy liền nhau `""` là chuỗi rỗng. Nó khác với một chuỗi chứa dấu cách. Ví dụ dùng `strip()` để bỏ khoảng trắng hai đầu, rồi `lower()` chuyển chữ hoa thành chữ thường trước khi gán kết quả vào `answer`. Vì vậy câu trả lời chỉ chứa khoảng trắng trở thành rỗng.

Đây là lựa chọn thiết kế cho câu đố: chấp nhận PRINT như print. Không phải dữ liệu nào cũng nên chuyển chữ thường. Cách này cũng không sửa chữ gõ sai hoặc khoảng trắng ở giữa tên hàm.

Hãy phân biệt hai kiểu vấn đề. Thiếu dấu hai chấm có thể khiến chương trình không chạy vì cú pháp sai. Chưa xử lý chữ hoa có thể khiến chương trình vẫn chạy nhưng phản hồi không đúng mục tiêu. Vì vậy việc không có thông báo lỗi chưa chứng minh bài làm đã đúng; bạn cần thử nhiều đầu vào.''',
'''Danh sách (`list`) giữ nhiều giá trị theo thứ tự. Trong ví dụ, mỗi tên sách là một chuỗi; ngoặc vuông chứa danh sách và dấu phẩy phân cách các phần tử. Một tên có nhiều từ vẫn là một phần tử. Hai phần tử có cùng tên vẫn được tính là hai mục riêng.

`for title in books:` lần lượt gán từng phần tử vào tên `title`, rồi thực hiện khối thụt vào. `books` là cả danh sách; `title` là giá trị đang được xử lý trong mỗi lượt. Bạn có thể đặt tên biến vòng lặp khác, miễn dùng nhất quán.

`len(books)` đếm phần tử trong danh sách, không đếm chữ trong tên sách và không tự loại mục trùng. Đặt dòng in tổng ngoài vòng lặp để nó chỉ chạy một lần sau khi duyệt xong. Nếu đặt trong vòng lặp, tổng sẽ lặp lại sau mỗi cuốn dù con số có thể vẫn đúng.

Thêm một mục vào dữ liệu rồi giữ nguyên vòng lặp. Chương trình tự có thêm một lượt xử lý, nên không cần chép thêm lệnh hiển thị. Đây là bước đầu tách dữ liệu khỏi logic làm việc với dữ liệu.

Với danh sách rỗng `[]`, vòng lặp không chạy lượt nào. Dòng in tổng bên ngoài vẫn chạy và hiện 0. Hãy thử điều này trên bản sao để hiểu thụt dòng thay vì ghi nhớ một mẫu. Nếu thêm sách mà kết quả không đổi, hãy kiểm tra đã lưu file và có đang in một con số cố định thay vì dùng `len` không.''',
'''Một tên sách chưa đủ để biết cuốn đó có thể được mượn. Dictionary giữ các cặp khóa–giá trị, chẳng hạn khóa `title` đi với tên sách. Cặp ngoặc nhọn bao quanh dictionary; dấu hai chấm nối khóa với giá trị; dấu phẩy ngăn các cặp.

Trong ví dụ, `id` là số nguyên, `title` là văn bản và `borrowed` là boolean. `True` nghĩa là đang mượn; `False` nghĩa là chưa mượn. Hai giá trị này viết hoa chữ đầu và không có dấu nháy. Chuỗi `"False"` là văn bản khác kiểu, không phải giá trị boolean False.

`book["title"]` lấy giá trị theo khóa. Khóa phải có trong dictionary và viết đúng; `book["name"]` gây `KeyError` nếu chỉ có khóa title. Khác với biến book, khóa trong ví dụ là một chuỗi nên có dấu nháy khi tra cứu.

Danh sách `books` chứa nhiều dictionary. Mỗi lượt vòng lặp, `book` nhận một dictionary; điều kiện bên trong chọn chữ hiển thị dựa trên borrowed. Dòng print nằm trong vòng lặp nhưng ngoài hai nhánh điều kiện, để cả hai loại trạng thái đều được in.

Mã sách ổn định dù thứ tự danh sách thay đổi. Hai bản sách cùng tên có thể có hai mã khác nhau. Python chưa tự bảo đảm mã duy nhất trong đoạn này; đó là quy tắc mình sẽ kiểm tra trong dự án. Thay borrowed trực tiếp trong dữ liệu mẫu chỉ là một thí nghiệm, chưa phải chức năng mượn trả cho người dùng.''',
'''Hàm gom một công việc thành phần có tên để gọi lại. `def find_titles(titles, keyword)` định nghĩa hàm nhận hai tham số: danh sách tên và từ khóa. Phần thân chỉ chạy khi hàm được gọi. Các dữ liệu bạn đưa lúc gọi được dùng qua tên tham số bên trong.

Ở bài này ta dùng lại danh sách chuỗi để tập trung vào hàm. `matches = []` tạo kết quả rỗng. Vòng lặp xét từng tên; phép `keyword in title` kiểm tra một chuỗi có nằm trong chuỗi khác không. Khi khớp, `append` thêm tên vào cuối danh sách kết quả.

`strip` bỏ khoảng trắng hai đầu từ khóa và `casefold` hỗ trợ so sánh không phân biệt hoa thường. Nó không loại dấu tiếng Việt. Hàm giữ tên gốc khi thêm vào kết quả nên cách viết tên không bị đổi. Từ khóa rỗng khớp mọi tên theo quy tắc chuỗi của Python; ở đây ta chấp nhận nó như cách xem tất cả tên.

`return` đưa kết quả về nơi gọi và kết thúc lần gọi hàm. `print` hiển thị thông tin. Tách hai việc giúp sau này bạn có thể đếm hoặc trình bày kết quả khác đi mà không sửa phần tìm kiếm. Bạn có thể viết `result = find_titles(titles, "Mat")` rồi `print(result)` để quan sát rõ hai bước.

Nếu đặt return bên trong vòng lặp, hàm có thể kết thúc ngay sau tên đầu. Tìm cuốn đầu có vẻ đúng nhưng tìm cuốn cuối thất bại. Vì vậy hãy thử đầu, cuối, không có kết quả và từ khóa rỗng. Một lần chạy thành công chưa chứng minh mọi trường hợp hoạt động.'''
]
titles = ['Chạy chương trình và đọc kết quả','Nhận câu trả lời bằng biến và input','Điều kiện: đúng, sai và bỏ trống','Danh sách và vòng lặp','Dictionary: thông tin đi cùng nhau','Hàm tìm kiếm và cách kiểm thử']
for i, explanation in enumerate(theory,1):
    pack=root/'content/recording-kit/python-path'/f'{i:02}'
    student=(pack/'STUDENT.md').read_text(encoding='utf-8')
    student=student[student.index('## Tự làm trước'):student.index('## English summary')]
    student=student.replace('solution.py',f'python-{i:02}-solution.py').replace('starter.py',f'python-{i:02}-starter.py')
    for kind in ('starter','solution'):
        shutil.copyfile(pack/f'{kind}.py', downloads/f'python-{i:02}-{kind}.py')
    code=(pack/'solution.py').read_text(encoding='utf-8').strip()
    write(lessons/f'python-{i:02}.md',f'''## {titles[i-1]}

**Cách học:** bài đọc và thực hành độc lập, không cần video. Dự kiến 25–40 phút gồm thời gian tự làm; tốc độ của bạn có thể khác. {'Bắt đầu với máy tính có Python 3 và trình soạn thảo; không cần thư viện ngoài.' if i==1 else 'Hoàn thành bài trước hoặc tự giải thích được ví dụ của bài đó.'}

### Sau bài này

{(pack/'TEACHER.md').read_text(encoding='utf-8').split('**Mục tiêu:** ')[1].split('\n')[0]}

## Hiểu từng bước

{explanation}

## Chạy một ví dụ hoàn chỉnh

Đọc và dự đoán đầu ra trước khi chạy. Tạo file riêng cho bài này để không ghi đè bài trước.

```python
{code}
```

## Tài liệu để tự làm

[Tệp bắt đầu](/downloads/projects/python-{i:02}-starter.py) · [Lời giải đối chiếu](/downloads/projects/python-{i:02}-solution.py). Lưu bản bắt đầu thành `my-work.py`, chạy `python my-work.py` trong thư mục đó. Nếu liên kết mở nội dung trong trình duyệt, dùng Lưu liên kết thành để giữ file `.py`.

{student}

## Trước khi đánh dấu hoàn thành

Bạn cần chạy được bản của mình, giải thích một dòng bằng lời riêng và thử thêm một đầu vào hoặc thay đổi khác ví dụ. Ghi lại một lỗi đã gặp, cách bạn kiểm tra và kết quả sau khi sửa. Việc xem lời giải không thay cho việc tự chạy và giải thích.
''')

web = [
('Một trang có cấu trúc', '''Bạn sẽ tạo một trang thông tin tủ sách bằng HTML. HTML mô tả ý nghĩa của nội dung; nó không phải ảnh chụp của một trang. Thẻ mở và thẻ đóng bao quanh nội dung, chẳng hạn `<p>...</p>` là một đoạn văn. Một số thẻ như meta không có thẻ đóng.

`head` giữ thông tin về tài liệu: title xuất hiện ở tab trình duyệt, charset giúp đọc chữ tiếng Việt. `body` chứa nội dung người đọc thấy. `lang="vi"` khai báo ngôn ngữ. `h1` là tiêu đề chính, còn `h2` chia các mục; chọn cấp tiêu đề theo cấu trúc, không chỉ theo cỡ chữ.

Tạo thư mục `tu-sach`, mở trình soạn thảo văn bản, lưu ví dụ thành `index.html` với UTF-8. Mở file bằng trình duyệt. Sau mỗi thay đổi, lưu trong trình soạn thảo rồi tải lại trình duyệt. Không cần máy chủ hoặc tài khoản để làm bài này. Nếu trình duyệt hiện code như văn bản, kiểm tra tên file có bị thành index.html.txt không.

Danh sách có thứ tự `ol` phù hợp với các bước cần làm lần lượt; mỗi bước nằm trong li. Thay vì gõ số bằng tay trong nhiều đoạn, cấu trúc danh sách giúp trình duyệt giữ thứ tự và công cụ hỗ trợ đọc nhận ra các bước.''', '''<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Tủ sách lớp mình</title>
</head>
<body>
  <main>
    <h1>Mượn sách từ tủ sách lớp</h1>
    <p>Trang mẫu hướng dẫn ba bước để tìm một cuốn sách.</p>
    <h2>Cách bắt đầu</h2>
    <ol>
      <li>Xem danh sách sách còn trống.</li>
      <li>Hỏi người phụ trách trước khi lấy sách.</li>
      <li>Ghi lại thời điểm trả đã thống nhất.</li>
    </ol>
  </main>
</body>
</html>''', 'Đổi trang thành hướng dẫn sử dụng một tài nguyên lớp học do bạn chọn. Viết một lời giới thiệu và ba bước. Thêm mục h2 giải thích người đọc có thể hỏi ai khi cần giúp.', 'Tab trình duyệt có title riêng; trang có một h1 và các bước đánh số. Lưu, tải lại và kiểm tra câu mới đã xuất hiện.', 'Đặt h2 và một p bên trong main sau ol. Nội dung giúp người đọc biết hành động tiếp theo; không cần JavaScript. Ví dụ: <h2>Khi cần giúp</h2><p>Hỏi người phụ trách tủ sách của lớp.</p>'),
('Liên kết và hình ảnh có mục đích', '''Bài này thêm cách di chuyển giữa các mục. Thuộc tính id gắn tên duy nhất cho một phần của trang. Liên kết `href="#steps"` đi tới phần có `id="steps"` trong cùng tài liệu. Nếu hai giá trị không khớp, người đọc không đến đúng phần. Dùng chữ mô tả đích đến, chẳng hạn “Các bước mượn sách”, thay cho nhiều liên kết chỉ ghi “Bấm đây”.

Ảnh cần giúp hiểu nội dung, không chỉ lấp khoảng trống. Thuộc tính src chỉ nơi file ảnh nằm; đường dẫn tương đối được tính từ vị trí tài liệu. Nếu index.html nằm cạnh thư mục images, ảnh có thể dùng `images/shelf.jpg`. Hãy dùng ảnh bạn có quyền sử dụng; bài mẫu bên dưới không cần ảnh để chạy.

Với ảnh có thông tin, alt mô tả điều người đọc cần biết nếu không nhìn được ảnh. Với ảnh chỉ trang trí, alt rỗng tránh đọc thông tin thừa. Một sơ đồ có chữ không nên dùng mô tả chung “hình ảnh”; hãy giữ phần giải thích quan trọng bằng văn bản trong trang.

Điều hướng nằm trong nav để diễn đạt đây là nhóm liên kết. Dùng bàn phím Tab đến từng liên kết rồi Enter để kích hoạt. Giữ đường viền focus mặc định nếu chưa có kiểu thay thế rõ ràng. Không cần mở mọi liên kết trong tab mới.''', '''<!doctype html>
<html lang="vi">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Hướng dẫn tủ sách</title></head>
<body><main>
  <h1>Tủ sách lớp mình</h1>
  <nav aria-label="Trong trang"><a href="#steps">Các bước mượn</a> · <a href="#help">Khi cần giúp</a></nav>
  <h2 id="steps">Các bước mượn</h2>
  <ol><li>Tìm sách còn trống.</li><li>Hỏi người phụ trách.</li><li>Ghi lại ngày trả.</li></ol>
  <h2 id="help">Khi cần giúp</h2>
  <p>Hỏi người phụ trách nếu chưa biết cuốn sách có thể được mượn không.</p>
</main></body></html>''', 'Thêm mục quy định với id="rules" và một liên kết điều hướng đến nó. Nếu có ảnh phù hợp, thêm ảnh với src và alt; nếu chưa có, hoàn thành bài bằng chữ và liên kết trước.', 'Các liên kết tới đúng mục; mỗi id chỉ dùng một lần. Dùng được Tab và Enter. Nếu dùng ảnh, thử đổi sai đường dẫn rồi quan sát alt, sau đó sửa lại.', 'Liên kết là <a href="#rules">Quy định</a> và đích là <h2 id="rules">Quy định</h2>. Dấu # chỉ nằm trong href, không nằm trong giá trị id.'),
('CSS: làm nội dung dễ đọc', '''CSS chọn phần tử rồi đặt quy tắc trình bày. Trong `p { line-height: 1.7; }`, p là bộ chọn, line-height là thuộc tính và 1.7 là giá trị. Các thuộc tính ngăn bằng dấu chấm phẩy. Quy tắc nằm trong style trong head hoặc một file CSS được liên kết. Bài này dùng style để bạn chỉ quản lý một file.

`max-width` giới hạn dòng văn bản trên màn hình lớn; `margin: auto` chia khoảng trống hai bên. Padding tạo khoảng cách bên trong vùng nội dung. Line-height không có đơn vị là hệ số theo cỡ chữ, giúp dòng cách nhau khi thay đổi kích thước chữ.

Màu chữ và nền cần đủ tương phản. Đừng chỉ dùng màu để phân biệt hành động: liên kết nên có gạch chân và focus rõ. Tránh xóa outline chỉ vì nó không hợp thẩm mỹ. Người dùng bàn phím cần biết đang ở đâu.

CSS không thay thế cấu trúc HTML. Nếu tạm bỏ style, nội dung vẫn phải theo thứ tự có nghĩa. Bạn có thể đặt cùng class cho nhiều phần cần cách trình bày giống nhau; đừng sao chép một kiểu inline dài vào mọi phần tử.

Khi quy tắc không áp dụng, kiểm tra bộ chọn có đúng phần tử, dấu ngoặc nhọn có khép và file đã lưu chưa. Nếu dùng CSS riêng, kiểm tra đường dẫn href trước khi đổi hàng loạt thuộc tính.''', '''/* Đặt bên trong thẻ style trong head của trang bài trước. */
* { box-sizing: border-box; }
body { margin: 0; background: #f3f1e8; color: #242520; font: 18px/1.7 system-ui, sans-serif; }
main { max-width: 720px; margin: auto; padding: 32px 24px; }
h1, h2 { line-height: 1.25; }
li { margin-block: 12px; }
a { color: #71351f; text-underline-offset: 4px; }
a:focus-visible { outline: 3px solid #71351f; outline-offset: 4px; }''', 'Áp dụng CSS cho trang trước. Tạo class .note cho một lưu ý, với border-left và padding. Tạm bỏ style để kiểm tra thứ tự nội dung vẫn hợp lý.', 'Nội dung có khoảng thở, không chạy dài toàn màn hình; liên kết rõ và có focus khi Tab. Không có mục bị mất chỉ vì đổi style.', 'Thêm .note { border-left: 4px solid #71351f; padding-left: 16px; } và <p class="note">Hỏi trước khi lấy sách.</p>. Class nối HTML với CSS; dấu chấm chỉ dùng ở bộ chọn CSS.'),
('Trang đọc được trên màn hình nhỏ', '''Một trang cần thích nghi với chiều rộng khác nhau. Metadata viewport trong head cho trình duyệt di động dùng chiều rộng thiết bị. Với main có max-width, nội dung có thể nhỏ lại thay vì giữ cứng một chiều rộng lớn. Tránh đặt width:900px lên vùng đọc chính.

Ảnh có thể tràn nếu kích thước tự nhiên lớn. Dùng max-width:100% và height:auto để ảnh không rộng hơn vùng chứa mà vẫn giữ tỉ lệ. Với đoạn văn bản dài không có khoảng trắng, overflow-wrap:anywhere cho phép xuống dòng khi cần. Đừng chữa tràn bằng cách thu tất cả chữ xuống rất nhỏ.

Media query chỉ thêm quy tắc khi điều kiện khớp. Ví dụ ở màn hình hẹp có thể giảm padding. Không phải mọi trang đều cần nhiều điểm ngắt; trước hết thử bố cục linh hoạt đơn giản.

Kiểm tra bằng việc thu cửa sổ, phóng to chữ và dùng bàn phím. Mô phỏng chiều rộng trên máy tính hữu ích nhưng chưa thay thế hoàn toàn thiết bị thật. Nếu chưa thử trên điện thoại, ghi đúng thiết bị đã thử thay vì đánh dấu hoàn tất mọi nền tảng.

Khi đưa trang cho người khác, hỏi họ thực hiện một nhiệm vụ cụ thể: tìm hướng dẫn hoặc giải thích bước đầu. Ghi quan sát và sửa một điểm; đừng chỉ hỏi trang có đẹp không. Một bản hoàn chỉnh có nội dung rõ, đường dẫn hoạt động và ghi chú về giới hạn.''', '''/* Thêm vào cuối style đã có. */
img { max-width: 100%; height: auto; }
p, a, code { overflow-wrap: anywhere; }
@media (max-width: 480px) {
  main { padding: 24px 16px; }
}
''', 'Hoàn thiện trang tủ sách. Kiểm tra ở cửa sổ hẹp khoảng 360px, rộng khoảng 1200px và zoom 200%. Thử Tab/Enter. Ghi một vấn đề đã sửa và lưu phiên bản cuối.', 'Không phải kéo ngang để đọc đoạn văn; nội dung không bị cắt; liên kết vẫn đến đúng mục. Nộp index.html và ghi chú trước/sau một thay đổi.', 'Nếu main có width cố định, đổi sang max-width và giữ padding. Nếu ảnh tràn, thêm quy tắc img. Đừng bỏ nội dung để làm kết quả kiểm tra có vẻ đạt.')
]
base_html=web[1][2]
css=web[2][2]+'\n'+web[3][2]
final_html=base_html.replace('</head>',f'<style>\n{css}\n</style></head>')
write(downloads/'web-foundations.html', final_html)
for i,(title,body,code,task,check,answer) in enumerate(web,1):
    lang='html' if i<3 else 'css'
    write(lessons/f'web-{i:02}.md',f'''## {title}

**Mục tiêu:** {title.lower()} bằng một trang hướng dẫn tủ sách. **Thời gian thực hành dự kiến:** 30–45 phút. {'Không cần biết code trước; cần trình duyệt và trình soạn thảo văn bản.' if i==1 else 'Dùng file index.html từ bài trước. Giữ một bản sao trước khi sửa.'} Đây là bài học bằng chữ, không cần chờ video.

## Giải thích và làm từng bước

{body}

## Ví dụ để chạy

{'Tạo file index.html với toàn bộ nội dung sau.' if i<3 else 'Giữ HTML bài trước; chèn các quy tắc sau vào style trong head, không dán CSS trực tiếp vào body.'}

```{lang}
{code}
```

## Tự làm trước khi xem lời giải

{task}

## Kiểm tra kết quả

{check}

Ghi hành động bạn thử, kết quả mong muốn và kết quả thực tế. Nếu khác nhau, lưu lại ví dụ nhỏ nhất còn gây lỗi để tìm nguyên nhân.

## Gợi ý và lời giải có giải thích

{answer}

Một lời giải tham khảo hoàn chỉnh nằm trong [web-foundations.html](/downloads/projects/web-foundations.html). Mở để xem kết quả hoặc lưu file rồi đọc bằng trình soạn thảo. Chỉ đối chiếu sau khi tự làm; câu chữ và thiết kế của bạn có thể khác mà vẫn đáp ứng yêu cầu.

## Tự đánh giá

Bạn có thể giải thích vai trò của phần mới thêm mà không đọc lại hướng dẫn không? Đổi một nội dung rồi kiểm tra lại. Bài hoàn thành khi bạn hiểu thay đổi, không chỉ khi ảnh chụp giống ví dụ.
''')

# Keep existing project lesson identifiers/positions and core content; add authored teaching sections.
extras={
'books-01':('35–45','Thiết kế dữ liệu và hiển thị ba sách có mã ổn định.', '''Hãy tưởng tượng bạn chỉ nhận một danh sách tên. Bạn không biết cuốn nào đang được mượn, và hai bản cùng tên rất khó phân biệt. Vì vậy mỗi bản sách có một id riêng; title dành cho người đọc; borrowed là trạng thái. Mã không cần bằng vị trí trong danh sách.

List là nhóm các cuốn; dictionary là nhóm thông tin của một cuốn. Khi vòng lặp đi qua books, biến book nhận từng dictionary. `book["title"]` lấy giá trị theo khóa văn bản title. Viết sai thành name sẽ gây KeyError nếu khóa đó không tồn tại.

Hai boolean True/False không có dấu nháy. Chuỗi "False" vẫn là văn bản không rỗng; dùng nó trong if sẽ cho hành vi khác False. Hãy kiểm tra kiểu dữ liệu ngay từ bản mẫu, thay vì sửa cách hiển thị để che lỗi.

Đoạn ví dụ đầu dùng biểu thức điều kiện ngắn để chọn status. Bạn có thể viết thành if/else quen thuộc: nếu borrowed thì status = "dang muon", ngược lại status = "con trong". Hai cách đều phải in đúng cả hai trạng thái.''', 'Thêm sách mã 3 tên Mat Biec, chưa mượn. Sau đó chuyển toàn bộ khối for thành hàm show_books(items) và gọi với books.', '''```python
def show_books(items):
    for book in items:
        if book["borrowed"]:
            status = "dang muon"
        else:
            status = "con trong"
        print(book["id"], book["title"], status)

show_books(books)
```

Hàm nhận danh sách qua items nên không cần biết tên biến bên ngoài. Lời gọi nằm sau phần định nghĩa và không thụt vào trong hàm. Nếu chỉ định nghĩa mà chưa gọi, không có bảng sách xuất hiện.''', 'Đổi thứ tự hai dictionary: mã và trạng thái vẫn đi cùng đúng tên. Đổi riêng borrowed của mã 3: chỉ trạng thái đó thay đổi. Viết một câu giải thích tại sao mã trùng sẽ gây khó khăn khi mượn sách.'),
'books-02':('40–55','Tìm sách còn trống, mượn và trả đúng cuốn.', '''Tìm kiếm có hai điều kiện: tên khớp và sách chưa được mượn. Từ and yêu cầu cả hai đúng. not borrowed đảo trạng thái boolean, nên cuốn có borrowed=True bị loại. Từ khóa được strip và casefold để chấp nhận khoảng trắng hai đầu và hoa/thường; dấu tiếng Việt vẫn giữ nguyên.

Biểu thức trong ngoặc vuông ở ví dụ đầu là list comprehension: cách viết gọn một vòng lặp xây danh sách. Nếu chưa quen, tạo matches=[], duyệt từng book, nếu thỏa điều kiện thì matches.append(book), cuối cùng return matches. Kết quả chứa dictionary chứ không chỉ tên, để bạn vẫn biết mã của cuốn đó.

Hàm borrow trả True khi có thay đổi mới và False khi không thể thực hiện yêu cầu. Không nên hiểu True là “đang mượn” trong mọi hàm: hàm trả sách thành công cũng trả True dù trạng thái mới là False. Tên hàm và ý nghĩa giá trị trả về cần được giải thích rõ.

Từ khóa rỗng khớp mọi tên, nhưng điều kiện chưa mượn vẫn áp dụng. Một sách không xuất hiện có thể do đã được mượn, không nhất thiết do sai tên. Thử cả đầu vào hợp lệ và không có kết quả trước khi kết luận tìm kiếm bị lỗi.''', 'Viết return_book, kiểm tra trả một sách đang mượn, trả lại lần nữa và trả mã không tồn tại. Sau đó tìm lại cuốn vừa trả.', '''```python
def return_book(books, book_id):
    for book in books:
        if book["id"] == book_id and book["borrowed"]:
            book["borrowed"] = False
            return True
    return False
```

Với dữ liệu ban đầu, return_book(books, 2) là True; gọi lại là False; mã 99 cũng False. Đặt return False sau vòng lặp để không dừng trước khi xét sách thứ hai. Trong file hoàn chỉnh, set_loan gộp mượn và trả bằng một tham số trạng thái; đó là cách giảm lặp logic, không phải yêu cầu bạn phải dùng ngay.''', 'Ghi kết quả trước/sau cho một chuỗi tìm → mượn → tìm → trả → tìm. Không báo thành công cho mã 99. Giải thích vì sao chỉ thử sách đầu có thể bỏ sót lỗi return nằm sai vị trí.'),
'books-03':('45–60','Lưu trạng thái qua lần chạy và bàn giao một dự án có kiểm thử.', '''Dữ liệu trong biến sống trong phiên chạy; file lưu trạng thái để phiên sau đọc lại. json.dumps tạo văn bản JSON; write_text ghi văn bản. read_text đọc văn bản và json.loads chuyển nó về dữ liệu Python. JSON dùng true/false chữ thường, Python dùng True/False; thư viện xử lý chuyển đổi.

File hoàn chỉnh chỉ dùng dữ liệu mẫu khi file chưa tồn tại. Nếu file có nhưng sai, chương trình báo lỗi và dừng thay vì giả vờ đó là lần chạy đầu. Việc đọc JSON thành công chưa chứng minh cấu trúc đúng; load_books kiểm tra danh sách, từng trường và mã trùng.

Menu là khung hỗ trợ: while lặp, q dùng break để thoát; input trả văn bản và int thử chuyển mã thành số. Nếu nhập abc, except ValueError hiện lời nhắc và continue quay lại menu. Bạn không cần học thuộc toàn bộ khung mới có thể giải thích đường đi của một lượt mượn.

Sau thay đổi thành công, save_books được gọi. Nếu ghi lỗi, dữ liệu trong bộ nhớ đã đổi nhưng file có thể chưa được cập nhật; chương trình nói rõ điều đó. Đây chưa phải hệ thống cơ sở dữ liệu có giao dịch, sao lưu tự động hay hỗ trợ nhiều máy sửa cùng lúc.''', 'Tạo một thư mục thử riêng, lưu source và chạy chuỗi mượn → thoát → mở lại → trả. Sao lưu dữ liệu trước khi cố tình sửa hỏng JSON trong bản thử. Viết README ngắn cho người khác chạy.', '''README tham khảo: “Cần Python 3. Chạy python book-sharing.py trong thư mục dự án. f tìm sách còn trống; b mượn bằng mã; r trả bằng mã; q thoát. Trạng thái lưu trong books.json cạnh chương trình. Đây là công cụ một máy, dùng sách mẫu và chưa xác minh người mượn.”

Khi file JSON hỏng, khôi phục từ bản sao hợp lệ sau khi kiểm tra, không xóa file thật để che lỗi. Với file có hai sách cùng mã, bản hoàn chỉnh phải từ chối đọc. Mã mới cho sách cần được chọn có chủ đích, không thay ngẫu nhiên lúc khởi động.''', 'Nộp file Python, dữ liệu mẫu, README và bảng thử có đầu vào/kết quả thực tế. Nhờ một người thử tìm và mượn; ghi một điểm khó hiểu và một thay đổi. Nếu chưa có người thử, ghi đúng là tự kiểm tra.'),
'guide-01':('30–40','Viết một bản hướng dẫn có người đọc, mục tiêu và các bước rõ.', '''Một hướng dẫn tốt bắt đầu từ việc người đọc cần làm, không từ danh sách tính năng của trang. Viết câu “Người đọc là..., đang muốn..., nhưng đang gặp...” để giới hạn phạm vi. Ví dụ: người mới nhận tin nhắn yêu cầu đăng nhập, chưa biết nên phản ứng thế nào.

Chia yêu cầu thành những hành động nhìn thấy được. “Cẩn thận” không cho biết phải làm gì; “Tự mở ứng dụng chính thức đã biết thay vì làm theo đường dẫn trong tin nhắn” rõ hơn. Tránh hứa xác định an toàn tuyệt đối từ một dấu hiệu đơn lẻ.

Mỗi bước nên có một hành động chính. Đặt thông tin cần trước ở trên, giải thích thêm phía sau. Một khối cảnh báo dài đặt trước mọi nội dung có thể làm người đọc bỏ qua cả hướng dẫn; chọn lưu ý có liên quan trực tiếp đến bước hiện tại.

Với ví dụ địa chỉ, dùng tên miền .example chỉ để minh họa và hiển thị bằng chữ, không yêu cầu người học thử vào liên kết nghi ngờ. Bài này dạy thiết kế nội dung và web; nó không tạo một công cụ tự đánh giá đường dẫn.''', 'Viết một tiêu đề, câu mô tả người đọc, bốn bước hành động và một giới hạn. Gạch bỏ từ nào người mới chưa chắc hiểu hoặc giải thích nó ngay bên cạnh.', '''Một bản nháp có thể là: 1. Dừng lại khi tin nhắn tạo cảm giác phải làm ngay. 2. Đọc xem ai gửi và họ đang yêu cầu gì. 3. Tự mở ứng dụng hoặc địa chỉ chính thức đã biết để kiểm tra. 4. Hỏi người lớn/người phụ trách nếu vẫn chưa chắc. Giới hạn: hướng dẫn không tự xác nhận một trang là an toàn.

Đáp án không nằm ở việc dùng đúng bốn câu này. Bạn có thể chọn cách tổ chức khác miễn người đọc biết hành động tiếp theo và không bị hướng đến một thử nghiệm rủi ro.''', 'Đọc bản nháp như người chưa biết chủ đề. Với mỗi bước, chỉ ra một hành động có thể làm. Nộp bản chữ trước khi thêm CSS; giữ bản này để so sánh với phiên bản sau thử nghiệm.'),
'guide-02':('40–55','Chuyển bản nháp thành HTML dễ đọc, có ví dụ và đáp án.', '''Bắt đầu bằng nội dung trước khi chọn màu. h1 đặt tên công việc; phần giới thiệu cho biết khi nào cần dùng; ol giữ các bước theo thứ tự. h2 chia mục ví dụ và giới hạn. Không dùng h2 chỉ vì muốn chữ to; ý nghĩa cấu trúc giúp cả người đọc lẫn công cụ hỗ trợ.

CSS trong style chỉ tác động trình bày. max-width giới hạn độ dài dòng, padding tạo khoảng trống, line-height tạo khoảng cách giữa dòng. Nếu nội dung vẫn đúng khi bỏ CSS, cấu trúc cơ bản của bạn đang tốt hơn một trang chỉ có các hộp trang trí.

details và summary cho một câu hỏi mở/đóng mà không cần JavaScript. summary phải diễn đạt câu hỏi thực sự, không chỉ ghi “xem thêm”. Đáp án nên giải thích lý do, không chỉ hiện chữ đúng hoặc sai. Người học có thể dự đoán trước khi mở.

Khi thêm ví dụ, phân biệt nội dung hướng dẫn thật và bài tập. Địa chỉ mẫu chỉ dùng làm dữ liệu đọc, đặt trong code; đừng biến thành nút truy cập. Nếu đổi sang một kỹ năng khác, kiểm tra các bước trên thiết bị mà bạn mô tả.''', 'Thêm một h2 cho ví dụ, một câu hỏi trong summary và câu trả lời có lý do. Thêm một liên kết nội bộ từ đầu trang tới mục ví dụ.', '''```html
<a href="#example">Thử một ví dụ</a>
<h2 id="example">Một tin nhắn yêu cầu làm ngay</h2>
<details>
  <summary>Có nên nhập mật khẩu theo đường dẫn vừa nhận không?</summary>
  <p>Hãy tự mở ứng dụng hoặc địa chỉ chính thức đã biết để kiểm tra trước. Cảm giác khẩn cấp trong tin nhắn không xác nhận người gửi là đáng tin.</p>
</details>
```

href có # còn id không có. details có thể đóng/mở bằng bàn phím. Đây là một ví dụ về cách tổ chức câu hỏi, không phải một bài kiểm tra tự động ghi điểm.''', 'Lưu file, mở bằng trình duyệt và dùng Tab/Enter để đến câu hỏi. Tạm bỏ CSS: tiêu đề, bước và đáp án vẫn theo thứ tự có nghĩa. Nộp file HTML có nội dung của riêng bạn.'),
'guide-03':('35–50','Kiểm tra trang và ghi lại một cải tiến có bằng chứng.', '''Kiểm tra kỹ thuật và thử với người đọc trả lời hai câu hỏi khác nhau. Trang có thể không tràn nhưng lời hướng dẫn vẫn khó hiểu. Người đọc có thể thích màu nhưng không biết bước tiếp theo. Vì vậy cần quan sát cả cách trang hiển thị và cách người dùng thực hiện nhiệm vụ.

Tạo một bảng gồm thiết bị/chiều rộng, hành động, điều mong đợi, kết quả và việc sửa. Kiểm tra hẹp khoảng 360px, rộng khoảng 1200px, zoom 200% và bàn phím. Nếu không có điện thoại thật, ghi là kiểm tra cửa sổ hẹp trên máy tính, không tự đánh dấu đã thử thiết bị.

Đưa một yêu cầu cụ thể: “Đọc tình huống và cho biết bạn sẽ làm gì tiếp theo.” Chờ người thử thao tác, ghi nơi họ dừng hoặc hỏi. Nếu bạn giúp, ghi lại đã giúp gì. Không ép người thử nói trang tốt và không điền lời khen giả vào báo cáo.

Chọn một thay đổi đủ nhỏ để biết tác dụng: viết lại một bước, thay nhãn liên kết, tăng khoảng cách, sửa tràn. Đừng đổi mọi thứ cùng lúc rồi kết luận một màu mới làm người dùng hiểu hơn. Nếu chưa có người thử, tự kiểm tra vẫn hữu ích nhưng cần gọi đúng tên.''', 'Hoàn thành bảng kiểm và ghi một thay đổi trước/sau. Viết 3–5 câu giới thiệu dự án: ai dùng, giúp làm gì, điều bạn sửa và một giới hạn.', '''Ví dụ báo cáo minh họa, không phải kết quả người dùng thật: “Trước: liên kết chỉ ghi Xem. Sau: đổi thành Các bước kiểm tra tin nhắn để chỉ rõ đích đến. Tự kiểm tra: liên kết đi đúng mục bằng Enter. Chưa thử với người khác.”

Nếu ảnh hoặc chữ dài gây tràn, xử lý phần tử đó bằng max-width hoặc overflow-wrap thay vì thu nhỏ mọi chữ. Giữ focus nhìn thấy được. Khi người dùng không hiểu một câu, sửa từ ngữ trước khi thêm hiệu ứng.''', 'Nộp HTML hoàn chỉnh và ghi chú kiểm thử. Có thể hoàn thành bằng một lần tự kiểm tra trung thực; phần thử người khác bổ sung khi có người tự nguyện. Không mô tả trang như công cụ xác nhận liên kết an toàn.'),
'waste-01':('30–45','Đọc CSV và giải thích ý nghĩa của dữ liệu trước khi tính.', '''CSV là văn bản có các giá trị phân cách bằng dấu phẩy. Dòng đầu đặt tên cột; mỗi dòng sau là một quan sát. Trong file này, một dòng là khối lượng một loại thức ăn của một ngày, không phải một học sinh. Đơn vị grams là gram, nên không cộng với kilogram nếu chưa đổi đơn vị.

DictReader dùng tên cột làm khóa dictionary. Dù ô nhìn như số, giá trị đọc ban đầu vẫn là văn bản. Vì vậy "120" + "80" tạo "12080", không phải 200. Cần chuyển kiểu trước khi tính, đồng thời có cách xử lý ô không thể chuyển.

with mở file trong một phạm vi rồi đóng nó khi xong. newline="" giúp bộ đọc CSV xử lý xuống dòng; utf-8-sig chấp nhận cả dấu đánh dấu mã hóa có thể có trong file xuất từ phần mềm bảng tính. Path(__file__).with_name giữ đường dẫn cạnh script.

Đặt câu hỏi có thể trả lời từ cột hiện có: ngày nào có tổng lượng ghi nhận cao nhất? Bảng chưa có số suất ăn, khẩu phần hoặc lý do bỏ lại. Vì vậy chưa thể kết luận món nào bị ghét hay hoạt động nào đã giảm lãng phí.''', 'Giải thích một dòng bằng lời, in kiểu dữ liệu của grams, rồi thử tổng hai giá trị có và không chuyển float. Thực hiện trên bản sao.', '''```python
print("120" + "80")       # 12080
print(float("120") + float("80"))  # 200.0
```

Trong vòng lặp CSV, dùng print(type(row["grams"]).__name__) sẽ thấy str. float tạo số mới; nó không tự thay giá trị trong row. Không dùng phép cộng chuỗi để tính khối lượng. Khi thử unknown, ValueError cho biết cần nhánh xử lý dữ liệu lỗi trong bài sau.''', 'Nói rõ mỗi dòng biểu diễn gì, đơn vị nào được dùng và điều bảng chưa cho biết. File mẫu có sáu quan sát thuộc ba ngày; không gọi đó là sáu ngày.'),
'waste-02':('40–55','Nhóm số đo hợp lệ theo ngày và báo số dòng bỏ qua.', '''Tổng theo ngày là một dictionary: khóa là day, giá trị là tổng gram. totals.get(day, 0) lấy tổng hiện có, hoặc 0 nếu ngày chưa xuất hiện. Cộng từng số đo hợp lệ vào tổng, không thay tổng bằng số đo mới nhất.

Phần kiểm tra chia hai loại: chuyển sang số thất bại, hoặc chuyển được nhưng không phải số đo chấp nhận được. Giá trị âm, NaN và vô hạn không hợp lệ trong bài. Dòng không có ngày hoặc tên loại thức ăn cũng bị bỏ qua. Đếm skipped để người đọc biết không phải mọi dòng đều được dùng.

continue kết thúc lượt hiện tại rồi chuyển dòng tiếp theo. Vì vậy câu cập nhật totals phải nằm sau các kiểm tra; nếu đặt trước, dữ liệu lỗi có thể đã ảnh hưởng tổng. Nếu bắt lỗi quá rộng rồi bỏ qua im lặng, bạn có thể che cả lỗi lập trình; ở đây chỉ xử lý các kiểu lỗi chuyển số dự kiến.

Các đoạn minh họa dùng reader từ khối mở file ở bài trước. Để chạy một chương trình hoàn chỉnh, dùng food-waste.py đính kèm; hàm read_totals còn kiểm tra tên cột trước khi duyệt. Bạn có thể gọi hàm với một đường dẫn thử để kiểm tra mà không sửa file gốc.''', 'Trong bản sao CSV, thêm dòng âm, unknown và một ô grams trống. Chạy chương trình hoàn chỉnh rồi so sánh tổng và skipped với bản gốc.', '''Ba dòng mẫu có thể là Thursday,rice,-10; Thursday,rice,unknown; Thursday,rice, (kết thúc bằng dấu phẩy). Khi thêm vào sáu dòng gốc, tổng vẫn là 580 và skipped là 3. Thursday không được đưa vào totals vì không có số đo hợp lệ.

Monday bắt đầu 0, cộng 120 thành 120, rồi cộng 80 thành 200. Đây là cách kiểm tra bằng tay một nhóm trước khi tin toàn bộ báo cáo. Nếu Monday chỉ còn 80, có thể bạn đã gán grams trực tiếp thay vì cộng vào tổng cũ.''', 'Đối chiếu bằng tay một ngày và kiểm tra số dòng lỗi. Nêu được vì sao báo số dòng bỏ qua quan trọng khi đọc báo cáo; tổng từ phần dữ liệu hợp lệ không nhất thiết đại diện đầy đủ cho mọi ngày.'),
'waste-03':('40–55','Tạo biểu đồ đơn giản và kết luận đúng giới hạn của mẫu.', '''Một biểu đồ cần đơn vị và tỉ lệ rõ. Ta có thể in thanh bằng ký tự #, mỗi ký tự đại diện 10 gram, kèm số chính xác bên cạnh. Độ dài thanh là số nguyên nên có thể làm tròn xuống; con số kèm theo giúp tránh hiểu thanh là phép đo chính xác tới từng gram.

Trung bình trong ví dụ là tổng chia số ngày có ít nhất một quan sát hợp lệ. Nó không phải trung bình trên sáu dòng, không phải trên mỗi suất ăn và không tự tính các ngày thiếu là 0. Nếu không còn ngày hợp lệ, chương trình thông báo thay vì chia cho 0.

Từ một bảng nhỏ, hãy viết riêng ba phần: quan sát, giới hạn và câu hỏi tiếp theo. “Wednesday có tổng lớn nhất trong mẫu” là quan sát. “Món ăn kém nên bị bỏ nhiều” là suy đoán cần dữ liệu khác. Không biến số liệu học tập thành bằng chứng về một trường thật.

Nếu muốn thu dữ liệu riêng, thống nhất đơn vị, thời điểm đo, phạm vi và người phụ trách. Cùng một ngày có nhiều dòng loại thức ăn nên cột số suất, nếu bổ sung, không được cộng lặp trên từng dòng một cách tùy tiện.''', 'Sau khi có totals hợp lệ, in biểu đồ chữ và viết một quan sát, một giới hạn, một câu hỏi. Sau đó thử thêm Thursday 40g và 60g trên bản sao.', '''```python
for day, grams in totals.items():
    bar = "#" * int(grams / 10)
    print(f"{day}: {bar} ({grams:g} g)")
print("Moi # bieu dien 10 g; thanh duoc lam tron xuong.")
```

Đặt đoạn này trong main của file hoàn chỉnh sau kiểm tra totals không rỗng. Mẫu gốc cho thanh dài 20, 15 và 23 ký tự. Bản thêm Thursday cho tổng 680 trên 4 ngày, trung bình 170g. Câu kết luận mẫu: “Wednesday cao nhất trong ba ngày mẫu. Chưa biết số suất ăn nên chưa so sánh theo mỗi suất. Cần thu thêm số suất theo ngày bằng một quy tắc nhất quán.”''', 'Nộp Python, CSV mẫu hoặc dữ liệu có nguồn rõ, kết quả chạy và ba câu báo cáo. Thử file chỉ có tiêu đề và file sai tên cột. Nếu dùng dữ liệu mẫu, giữ nhãn dữ liệu dựng để học trong sản phẩm cuối.')
}
for slug,(minutes,goal,body,task,answer,check) in extras.items():
    path=lessons/f'{slug}.md'
    original=path.read_text(encoding='utf-8').split('\n<!-- expanded-lesson -->')[0].strip()
    # Idempotent: keep original base content and replace authored expansion on re-run.
    write(path,original+f'''\n\n<!-- expanded-lesson -->
## Học sâu hơn: mục tiêu và cách làm

**Mục tiêu:** {goal} **Thời gian thực hành dự kiến:** {minutes} phút. Bạn có thể dừng giữa các phần; bài học này hoàn thành được bằng chữ và code, không phụ thuộc video.

{body}

## Bài thực hành có hướng dẫn

{task}

Hãy làm trước khi đọc phần đối chiếu. Ghi đầu vào và kết quả mong đợi; chỉ thay một điều mỗi lần để dễ hiểu tác động.

## Lời giải đối chiếu và lý do

{answer}

## Điều kiện hoàn thành

{check}

Nếu chưa đạt, chỉ ra bước nhỏ nhất chưa hoạt động, kiểm tra dữ liệu đầu vào và đọc thông báo lỗi. Một bài hoàn thành gồm kết quả chạy được và lời giải thích của bạn, không chỉ bản code giống ví dụ.
''')

manifest=root/'apps/web/src/content/project-courses.json'
courses=json.loads(manifest.read_text(encoding='utf-8'))
courses=[c for c in courses if c['slug'] not in ('python-nen-tang','web-nen-tang')]
for slug,vi,en,subtitle,english,theme,category,catname,files,names,assets,req in [
('python-nen-tang','Python: những chương trình hữu ích đầu tiên','Python: your first useful programs','Từ dòng chữ đầu tiên đến hàm tìm kiếm: sáu bài đọc, mã nguồn và bài tập tự kiểm tra.','From your first output to a search function: six written lessons with code and exercises.','slate','python-thuc-hanh','Python & giải quyết vấn đề',[f'python-{i:02}.md' for i in range(1,7)],titles,[f'python-{i:02}-{kind}.py' for i in range(1,7) for kind in ('starter','solution')],['Máy tính có Python 3 và trình soạn thảo','Không cần biết lập trình trước; không cần thư viện ngoài']),
('web-nen-tang','Web: trang đầu tiên của bạn','Web: your first website','Tạo một trang hướng dẫn từ HTML và CSS, rồi kiểm tra bằng bàn phím và trên màn hình nhỏ.','Build a useful page with HTML and CSS, then test keyboard use and small screens.','lime','lap-trinh-web','Lập trình web',[f'web-{i:02}.md' for i in range(1,5)],[r[0] for r in web],['web-foundations.html'],['Máy tính có trình duyệt và trình soạn thảo văn bản','Không cần biết lập trình trước'])]:
    courses.append(dict(slug=slug,title=dict(vi=vi,en=en),subtitle=dict(vi=subtitle,en=english),categoryName=catname,categorySlug=category,theme=theme,coverLabel=('Python' if theme=='slate' else 'HTML + CSS')+' / Nền tảng',outcomes=names[-3:],requirements=req,section='Đọc, làm thử và tự kiểm tra',lessons=[dict(title=f'{i:02} · {name}',file=file) for i,(name,file) in enumerate(zip(names,files),1)],downloads=assets))
write(manifest,json.dumps(courses,ensure_ascii=False,indent=2))
print(f'Prepared {sum(len(c["lessons"]) for c in courses)} lessons across {len(courses)} written courses.')
