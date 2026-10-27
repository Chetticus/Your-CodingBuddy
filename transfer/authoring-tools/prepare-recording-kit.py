from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / 'content' / 'recording-kit'

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(value).strip() + '\n', encoding='utf-8')

solutions = {
1: '''
print("Xin chao! Minh la Nam.")
print("Minh dang hoc Python de lam mot tu sach chia se.")
print("Ban muon chia se cuon sach nao?")
''',
2: '''
nickname = input("Biet danh cua ban: ")
book = input("Cuon sach ban muon chia se: ")
print(nickname, "muon chia se", book)
''',
3: '''
answer = input("Ham nao hien thi chu trong Python? ").strip().lower()
if answer == "print":
    print("Dung roi!")
elif answer == "":
    print("Ban chua nhap cau tra loi.")
else:
    print("Chua dung. Goi y: ham minh dung o bai 1.")
''',
4: '''
books = ["De Men Phieu Luu Ky", "The Little Prince", "Mat Biec"]
for title in books:
    print("Sach:", title)
print("So cuon sach:", len(books))
''',
5: '''
books = [
    {"id": 1, "title": "De Men Phieu Luu Ky", "borrowed": False},
    {"id": 2, "title": "The Little Prince", "borrowed": True},
]
for book in books:
    if book["borrowed"]:
        status = "dang muon"
    else:
        status = "con trong"
    print(book["id"], book["title"], status)
''',
6: '''
def find_titles(titles, keyword):
    matches = []
    for title in titles:
        if keyword.strip().casefold() in title.casefold():
            matches.append(title)
    return matches


titles = ["De Men Phieu Luu Ky", "The Little Prince", "Mat Biec"]
print(find_titles(titles, " DE MEN "))
print(find_titles(titles, "missing"))
''',
7: '''
books = [
    {"id": 1, "title": "De Men Phieu Luu Ky", "borrowed": False},
    {"id": 2, "title": "The Little Prince", "borrowed": True},
    {"id": 3, "title": "Mat Biec", "borrowed": False},
]


def show_books(items):
    for book in items:
        if book["borrowed"]:
            status = "dang muon"
        else:
            status = "con trong"
        print(book["id"], book["title"], status)


show_books(books)
''',
}

core = '''
STARTER = [
    {"id": 1, "title": "De Men Phieu Luu Ky", "borrowed": False},
    {"id": 2, "title": "The Little Prince", "borrowed": True},
    {"id": 3, "title": "Mat Biec", "borrowed": False},
]


def find_available(books, keyword):
    matches = []
    keyword = keyword.strip().casefold()
    for book in books:
        if not book["borrowed"] and keyword in book["title"].casefold():
            matches.append(book)
    return matches


def set_loan(books, book_id, borrowed):
    for book in books:
        if book["id"] == book_id:
            if book["borrowed"] == borrowed:
                return False
            book["borrowed"] = borrowed
            return True
    return False
'''
menu = '''
def main():
    books = [book.copy() for book in STARTER]
    while True:
        action = input("[f]ind, [b]orrow, [r]eturn, [q]uit: ").strip().lower()
        if action == "q":
            break
        if action == "f":
            matches = find_available(books, input("Title keyword: "))
            for book in matches:
                print(book["id"], book["title"])
            if not matches:
                print("No available books match.")
        elif action in ("b", "r"):
            try:
                book_id = int(input("Book ID: "))
            except ValueError:
                print("Use a whole-number book ID.")
                continue
            if set_loan(books, book_id, action == "b"):
                print("Changed for this session.")
            else:
                print("Unknown book, or its status already matches.")
        else:
            print("Choose f, b, r or q.")


if __name__ == "__main__":
    main()
'''
solutions[8] = core + '\n' + menu
storage = '''
DATA = Path(__file__).with_name("books.json")


def load_books(path=DATA):
    if not path.exists():
        return [book.copy() for book in STARTER]
    books = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(books, list):
        raise ValueError("Expected a list of books.")
    for book in books:
        if (not isinstance(book, dict)
                or type(book.get("id")) is not int
                or not isinstance(book.get("title"), str)
                or not book["title"].strip()
                or type(book.get("borrowed")) is not bool):
            raise ValueError("Invalid book entry.")
    return books


def save_books(books, path=DATA):
    path.write_text(json.dumps(books, ensure_ascii=False, indent=2), encoding="utf-8")
'''
load_block = '''    try:
        books = load_books()
    except (OSError, ValueError) as error:
        print("Could not read books.json:", error)
        return'''
save_block = '''                try:
                    save_books(books)
                    print("Saved.")
                except OSError as error:
                    print("Change is in memory but could not be saved:", error)'''
solutions[9] = 'import json\nfrom pathlib import Path\n\n' + core + storage + menu.replace('    books = [book.copy() for book in STARTER]', load_block).replace('                print("Changed for this session.")', save_block)
solutions[10] = solutions[9].replace('    for book in books:\n        if (not isinstance(book, dict)', '    ids = set()\n    for book in books:\n        if (not isinstance(book, dict)').replace('or type(book.get("borrowed")) is not bool):', 'or type(book.get("borrowed")) is not bool\n                or book["id"] in ids):').replace('raise ValueError("Invalid book entry.")', 'raise ValueError("Invalid or duplicate book entry.")\n        ids.add(book["id"])')

starters = {
1: '# Them mot loi chao va mot dieu ban muon tao bang Python.\nprint("Xin chao!")\n',
2: 'nickname = input("Biet danh cua ban: ")\n# TODO: hoi ten sach, sau do in ca biet danh va ten sach.\nprint(nickname)\n',
3: 'answer = input("Ham nao hien thi chu trong Python? ")\n# TODO: so sanh cau tra loi va hien thi phan hoi.\nprint("Ban da nhap:", answer)\n',
4: 'books = ["De Men Phieu Luu Ky", "The Little Prince"]\n# TODO: them mot sach, in tung sach, sau do in so luong.\nprint(books)\n',
5: 'books = [\n    {"id": 1, "title": "De Men Phieu Luu Ky", "borrowed": False},\n    {"id": 2, "title": "The Little Prince", "borrowed": True},\n]\n# TODO: in ma, ten va trang thai de doc cua tung cuon.\nprint(books)\n',
6: 'def find_titles(titles, keyword):\n    matches = []\n    # TODO: tim ten sach phu hop, them vao matches, tra ve ket qua.\n    return matches\n\n\ntitles = ["De Men Phieu Luu Ky", "The Little Prince", "Mat Biec"]\nprint(find_titles(titles, " DE MEN "))\n',
7: solutions[5] + '\n# TODO: them sach ma 3 va dua phan hien thi vao ham show_books.\n',
8: solutions[7] + '\n# TODO: them tim kiem, muon/tra va menu. Xem STUDENT.md.\n',
9: solutions[8],
10: solutions[9],
}

# title, outcome, opening, demo steps, deliberate bug, exercise, hints, expected, reflection, English summary
lessons = [
('Chạy chương trình đầu tiên', 'Chạy một file Python và thay đổi nội dung được in ra.',
'Cuối bài này, bạn sẽ tự sửa và chạy một chương trình nhỏ. Mình sẽ bắt đầu bằng một lời chào. Sau này, chính những dòng chữ này sẽ hướng dẫn người dùng tủ sách của mình.',
['Cho xem ba dòng kết quả của solution.py, rồi quay lại starter.py. Giải thích file là nơi lưu hướng dẫn, terminal là nơi xem kết quả.', 'Chạy một dòng print. Chỉ rõ dấu ngoặc và dấu nháy bao quanh nội dung.', 'Sửa lời chào, lưu file, chạy lại. Thêm một print cho điều bạn muốn tạo. Máy chạy từ trên xuống dưới.'],
'Trong bản làm thử, bỏ dấu nháy đóng để tạo SyntaxError. Đọc tên lỗi và dòng được chỉ ra; thêm dấu nháy rồi chạy lại. Không cần giải thích toàn bộ thông báo lỗi.',
'In ba dòng: lời chào, một thứ bạn muốn làm bằng Python, và một câu hỏi cho người dùng. Đổi thứ tự hai dòng rồi dự đoán kết quả.',
['Mỗi dòng có thể dùng một print riêng.', 'Văn bản cần nằm giữa hai dấu nháy cùng loại.'],
'Ba dòng xuất hiện đúng thứ tự. Chạy lại sau khi sửa phải hiện nội dung mới.',
'Nếu sửa file mà kết quả không đổi, bạn sẽ kiểm tra hai điều gì?',
'Run a saved Python file, edit a printed message, and rerun it. The terminal shows output in statement order. Check that you saved and ran the correct file.'),
('Biến và câu trả lời của người dùng', 'Lưu hai câu trả lời vào biến và ghép thành thông báo.',
'Lời chào hôm trước luôn giống nhau. Hôm nay mình muốn chương trình hỏi một biệt danh và tên cuốn sách, rồi dùng đúng câu trả lời của bạn.',
['Chạy bản hoàn chỉnh với biệt danh BanA và sách Mat Biec. Không dùng tên hay thông tin liên hệ thật.', 'Gõ input đầu tiên; chỉ vị trí con trỏ chờ trong terminal. Giải thích tên biến là cách mình gọi lại giá trị.', 'Thêm input cho book; dùng print với các đối số ngăn bằng dấu phẩy. Chạy lại với dữ liệu khác.'],
'Đổi book thành Book ở dòng print. Giải thích chữ hoa/thường khác nhau và sửa NameError. Minh họa thêm "book" in ra chữ book, còn book lấy giá trị.',
'Hỏi biệt danh và tên sách rồi in một câu gồm cả hai. Thử tên sách có nhiều từ.',
['Dùng hai lần input và hai tên biến khác nhau.', 'print(nickname, "muon chia se", book) ghép các phần bằng khoảng trắng.'],
'Nhập BanA và Mat Biec phải có cả hai trong kết quả. Đổi dữ liệu, kết quả đổi theo.',
'Sự khác nhau giữa book và "book" là gì?',
'Store input in variables and reuse it in output. input returns text. Variable names are case-sensitive; quoted words are literal text.'),
('Điều kiện: câu đố có phản hồi', 'Dùng if/elif/else để phản hồi ba loại câu trả lời.',
'Một câu đố không nên nói đúng với mọi câu trả lời. Mình sẽ cho chương trình kiểm tra trước khi phản hồi, kể cả khi người dùng chưa nhập gì.',
['Chạy ba trường hợp: print, loop, và Enter trống. Trước mỗi lần chạy hãy đoán nhánh được chọn.', 'Viết if answer == "print" rồi else. Giải thích so sánh bằng ==, thụt dòng và dấu hai chấm.', 'Thêm strip().lower() để bỏ khoảng trắng hai đầu và chuyển chữ thường. Thêm elif cho chuỗi rỗng.'],
'Bỏ dấu hai chấm sau if trong bản thử. Đọc lỗi, sửa rồi chạy lại. Sau đó bỏ lower và thử PRINT để minh họa lỗi hành vi không gây crash.',
'Hoàn thành phản hồi đúng, sai và bỏ trống. Kiểm tra thêm " PRINT " để chắc phần chuẩn hóa hoạt động.',
['So sánh câu trả lời sau khi strip và lower.', 'Nhánh elif answer == "" phải nằm trước else.'],
'print và " PRINT " được chấp nhận; loop nhận gợi ý; Enter trống được nhắc nhập.',
'Chương trình có thể chạy mà vẫn làm sai ý mình không? Cho một ví dụ.',
'Use conditions to distinguish correct, incorrect, and blank answers. Normalize outer spaces and letter case before comparing.'),
('Danh sách và vòng lặp', 'Duyệt một danh sách và đếm số phần tử.',
'Nếu tủ sách có thêm một cuốn, mình không muốn phải viết lại toàn bộ phần in. Một danh sách và vòng lặp sẽ giúp chương trình tự xử lý từng cuốn.',
['Mở starter: print cả list để thấy dữ liệu nhưng chưa dễ đọc.', 'Đổi thành for title in books và print bên trong. Theo dõi title lần lượt nhận giá trị nào.', 'Thêm sách thứ ba rồi in len(books) ngoài vòng lặp. Chạy lại mà không thêm print thủ công.'],
'Đặt dòng in tổng vào trong vòng lặp. Chương trình không crash nhưng in tổng nhiều lần. Sửa thụt dòng và giải thích vì sao.',
'Thêm một cuốn vào danh sách, in mỗi cuốn một dòng với nhãn Sach:, rồi in số cuốn đúng một lần.',
['Các mục trong list được ngăn bằng dấu phẩy.', 'Dòng in tổng không thụt vào cùng phần thân for.'],
'Ba dòng sách và một dòng tổng bằng 3. Thêm cuốn thứ tư thì tổng tự đổi thành 4.',
'Một dòng trong for và một dòng sau for được chạy khác nhau thế nào?',
'A list stores multiple values. A for loop handles each value in turn. Print the total outside the loop to show it only once.'),
('Dictionary: mô tả một cuốn sách', 'Gom mã, tên và trạng thái của mỗi cuốn trong một dictionary.',
'Tên sách thôi chưa đủ: mình còn cần biết sách đang được mượn chưa. Mỗi cuốn sẽ có một nhóm thông tin đi cùng nhau.',
['Chỉ ba trường id, title, borrowed của một book, rồi cho thấy books là list chứa nhiều book.', 'Duyệt books và truy cập book["title"]. Giải thích False chưa mượn, True đang mượn.', 'Viết if để đổi boolean thành chữ dễ đọc. In id, title và status; đổi thứ tự sách và chỉ ra id vẫn giữ nguyên.'],
'Truy cập book["name"] khi dữ liệu chỉ có title. Dùng KeyError để tìm lại tên khóa chính xác.',
'Hiển thị mỗi sách trên một dòng gồm mã, tên và con trong/dang muon. Đổi borrowed của sách 1 rồi chạy lại.',
['Duyệt bằng for book in books.', 'Dùng if book["borrowed"] thay vì so sánh với chuỗi "True".'],
'Sách 1 ban đầu còn trống, sách 2 đang mượn; đổi boolean làm đổi đúng trạng thái tương ứng.',
'Tại sao mã sách không nên phụ thuộc vào vị trí trong danh sách?',
'Represent each book with an ID, title, and boolean loan status. Keep stable IDs when reordering the list. Dictionary keys must match exactly.'),
('Hàm và cách tìm lỗi', 'Viết hàm trả về danh sách tên khớp một từ khóa.',
'Mình sẽ cần tìm sách nhiều lần. Thay vì chép lại đoạn tìm kiếm, mình đặt nó vào một hàm, đưa dữ liệu vào và nhận kết quả ra.',
['Giải thích def, hai tham số titles/keyword, list matches và return. Hàm chỉ chạy khi được gọi.', 'Duyệt từng title; dùng in để kiểm tra chuỗi con, append để thêm kết quả. casefold so sánh không phân biệt hoa/thường, không bỏ dấu.', 'Gọi hàm với " DE MEN ", missing và chuỗi rỗng. In kết quả bên ngoài hàm để phân biệt return với print.'],
'Đặt return matches trong for để chương trình dừng quá sớm. Tìm Mat Biec ở cuối danh sách để phát hiện; đưa return ra ngoài vòng lặp.',
'Hoàn thành find_titles, tìm đúng khi có khoảng trắng ở hai đầu và khác chữ hoa. Trả về list rỗng khi không có kết quả.',
['Chuẩn hóa cả từ khóa và title bằng casefold; strip chỉ cần cho từ khóa.', 'append chạy trong if; return chạy sau vòng lặp.'],
'" DE MEN " trả một tên, missing trả [], từ khóa rỗng trả cả ba tên.',
'Vì sao chỉ thử sách đầu tiên có thể bỏ sót lỗi?',
'Define a reusable search function that returns a list. Test first, last, absent, and blank queries. Returning inside the loop can stop the search too early.'),
('Tủ sách: xây phiên bản nhỏ đầu tiên', 'Tạo danh sách ba sách và một hàm hiển thị rõ trạng thái.',
'Bây giờ mình nối các kiến thức thành một công cụ nhỏ. Phiên bản đầu chỉ cần cho biết có sách gì và cuốn nào đang được mượn.',
['Viết phạm vi trên màn hình: mã, tên, trạng thái; chưa có tài khoản và chưa chạy chung qua mạng.', 'Lấy dữ liệu từ starter, thêm sách mã 3. Chuyển phần hiển thị vào show_books(items) và gọi hàm.', 'Đổi thứ tự sách, chạy lại; đối chiếu mã ổn định. Nhắc rằng ba sách đều là dữ liệu ví dụ.'],
'Cho sách mới dùng lại mã 1 rồi hỏi khi người dùng mượn mã 1 thì muốn cuốn nào. Sửa mã thành 3; lưu vấn đề mã trùng để kiểm tra tự động ở bài cuối.',
'Thêm cuốn sách thứ ba có mã riêng. Đưa phần in thành show_books(items). Thay một tên bằng cuốn bạn chọn.',
['Hàm nhận danh sách qua tham số items.', 'Định nghĩa hàm xong phải gọi show_books(books).'],
'Hiện ba mã khác nhau và đúng trạng thái; đổi thứ tự không đổi mã.',
'Thông tin nào thật sự cần để biết một cuốn có thể được mượn?',
'Scope the project to a local book list with stable IDs and readable loan status. Build a small working version before adding interaction.'),
('Tìm sách, mượn và trả', 'Tìm sách còn trống và thay đổi đúng trạng thái qua menu.',
'Một danh sách chỉ để nhìn chưa đủ. Mình muốn tìm sách còn trống, mượn một cuốn, rồi tìm lại để biết trạng thái đã thay đổi.',
['Viết find_available bằng vòng lặp quen thuộc: tên khớp và chưa mượn mới thêm vào matches. Chạy với từ khóa rỗng.', 'Viết set_loan: tìm đúng id, từ chối trạng thái đã giống yêu cầu, cập nhật rồi return True; không tìm thấy trả False.', 'Đọc menu chuẩn bị sẵn trong solution từng phần: while lặp đến q; int chuyển mã; try/except bắt ValueError; continue quay lại menu. Cho học sinh dự đoán b và r truyền boolean nào.'],
'Trong bản thử, bỏ điều kiện not book["borrowed"] để sách đang mượn vẫn được tìm thấy. Kiểm tra trước/sau khi mượn và khôi phục điều kiện.',
'Xây find_available và set_loan trước. Sau đó nối với menu mẫu. Thử tìm → mượn 1 → tìm lại → trả 1. Thử abc, 99 và mượn hai lần.',
['set_loan nhận True để mượn, False để trả.', 'int("abc") gây ValueError; phần except giúp quay lại menu thay vì dừng chương trình.', 'Menu là khung được cung cấp; không yêu cầu thuộc lòng mọi dòng mới của bài này.'],
'Mượn làm mất sách khỏi kết quả sách trống; trả đưa sách trở lại. Mã lỗi không gây crash. Thoát rồi chạy lại vẫn mất thay đổi: bài sau sẽ giải quyết.',
'Tại sao không được báo thành công nếu người dùng nhập mã không tồn tại?',
'Combine available-book search with borrow/return actions. Read the supplied menu scaffold and handle non-numeric IDs. Data still resets after exit in this version.'),
('Giữ dữ liệu sau khi đóng chương trình', 'Lưu JSON và đọc lại trạng thái ở lần chạy tiếp theo.',
'Hôm trước mình mượn sách rồi đóng chương trình, nhưng mở lại thì sách lại còn trống. Hôm nay mình tách dữ liệu đang nằm trong bộ nhớ và dữ liệu được lưu thành file.',
['Mở starter (bản chưa lưu), mượn 1, thoát và chạy lại để thấy vấn đề. Dùng thư mục thử riêng.', 'Giải thích json.dumps/json.loads và read_text/write_text. Path(__file__).with_name đặt file cạnh script. Đọc trước khi vào menu, lưu sau thay đổi thành công.', 'Dùng khung load_books/save_books trong solution; giải thích trường hợp chưa có file, file hợp lệ, file lỗi. Mượn, thoát, chạy lại và tìm; sau đó trả.'],
'Trong bản sao dữ liệu thử, làm sai cú pháp JSON. Chạy lại và cho thấy lỗi đọc cùng việc file không bị ghi đè. Khôi phục từ bản sao, không xóa dữ liệu để che lỗi.',
'Thêm lưu/đọc vào phiên bản trước bằng khung hỗ trợ. Chứng minh một lượt mượn còn nguyên qua hai lần chạy. Mở books.json và chỉ đúng trường đã đổi.',
['Lưu sau set_loan thành công, không chỉ lúc thoát.', 'Giữ các hàm xử lý file được cung cấp. Phần kiểm tra cấu trúc dài là mã hỗ trợ để đọc, không phải yêu cầu học thuộc.', 'Hãy dùng thư mục khác cho mỗi thí nghiệm để tránh dùng nhầm books.json.'],
'Mượn 1 → thoát → mở lại: mã 1 không còn trong sách trống. Trả 1 → mở lại: xuất hiện. File hỏng được giữ nguyên cùng thông báo lỗi.',
'Một thay đổi trong bộ nhớ có đồng nghĩa với việc đã lưu thành công không?',
'Persist book state in a local JSON file. Save after successful changes and load on startup. Explain missing versus damaged files and do not overwrite unreadable data silently.'),
('Thử với người dùng và cải thiện', 'Ghi kết quả kiểm thử và thêm kiểm tra mã sách trùng.',
'Chạy được một lần chưa đủ. Mình sẽ thử các trường hợp khó, sửa một lỗi cụ thể, rồi nhờ một người dùng thử mà không hướng dẫn từng bước.',
['Mở PROJECT-BRIEF.md và chạy các kiểm tra có đầu vào/kết quả mong đợi. Điền kết quả thật, không giả định đều đạt.', 'Tạo file thử có hai sách cùng id. Phiên bản starter chưa chặn. Giải thích set là nhóm mã đã gặp: nếu gặp lại thì báo lỗi; thêm kiểm tra vào load_books.', 'Đọc lại các ca tìm/mượn/trả/lưu để chắc sửa lỗi không phá chức năng. Chuẩn bị hướng dẫn chạy và giới hạn local-only. Nếu chưa có người thử, nói rõ đây là buổi diễn tập của bạn.'],
'Bản thử có hai sách mã 1 khiến thao tác chỉ chạm cuốn đầu. Đối chiếu starter và solution: bản sửa từ chối dữ liệu trùng thay vì chọn tùy ý.',
'Bổ sung kiểm tra mã trùng từ solution, hoàn thành bảng kiểm và chọn một cải tiến riêng. Nhờ một người thử tìm và mượn sách, ghi lại một điểm khó hiểu rồi sửa.',
['Tạo ids = set() trước vòng lặp kiểm tra dữ liệu.', 'Kiểm tra book["id"] in ids rồi mới ids.add(book["id"]).', 'Chỉ thử với bản sao dữ liệu. Bảng kiểm ở ../../PROJECT-BRIEF.md.'],
'Dữ liệu mã trùng bị từ chối; dữ liệu hợp lệ vẫn chạy. Nộp code, hướng dẫn, kết quả kiểm tra và một ghi chú thay đổi có bằng chứng.',
'Người thử đã làm gì khác với điều bạn dự đoán? Bạn sửa điều gì vì quan sát đó?',
'Test expected behavior, reject duplicate IDs, and improve one interaction based on observed feedback. State the local-only limitation and describe your own contribution.'),
]

for n, row in enumerate(lessons, 1):
    title, outcome, opening, demo, bug, exercise, hints, expected, reflection, english = row
    folder = KIT / 'python-path' / f'{n:02}'
    ident = f'PY{n:02}' if n <= 6 else f'BK{n-6:02}'
    duration = '5–8' if n <= 5 else ('7–10' if n in (6,7,10) else '10–14; có thể tách thành hai video')
    write(folder/'starter.py', starters[n])
    write(folder/'solution.py', solutions[n])
    bullets = '\n'.join(f'{i}. {s}' for i,s in enumerate(demo,1))
    hinttext = '\n'.join(f'{i}. {s}' for i,s in enumerate(hints,1))
    prereq = 'Đọc STUDENT-START.md; chạy được Python 3.' if n == 1 else f'Hoàn thành bài {n-1:02}; giải thích được kết quả của bài trước.'
    write(folder/'TEACHER.md', f'''# {ident} · {title}

Private recording draft · Vietnamese narration · planned, not recorded

**Mục tiêu:** {outcome}

**Chuẩn bị:** {prereq} Mở starter.py và solution.py ở hai tab; chỉ chiếu tab đang dạy. Làm trên bản sao my-work.py. Không sửa bản gốc khi ghi hình.

**Thời lượng dự kiến:** {duration} phút video; dành thêm 15–25 phút cho học sinh thực hành. Đây là ước lượng để diễn tập, không phải thời lượng công bố.

## 1. Mở bài — nói bằng giọng của bạn (khoảng 30 giây)

> {opening}

Cho xem kết quả đích trong solution.py, sau đó quay về starter.py. Không cần đọc lời mở nguyên văn.

## 2. Dạy trên màn hình (phần chính)

{bullets}

Sau mỗi thay đổi: hỏi “Bạn đoán lần chạy này sẽ hiện gì?”, dừng ngắn, chạy thử, giải thích sự khác nhau. Nói lý do trước khi đọc cú pháp.

## 3. Một lỗi để cùng sửa (khoảng 1 phút)

{bug}

## 4. Dừng video và tự làm

> {exercise}

Hiện yêu cầu trên màn hình và nhắc người học tạm dừng. Gợi ý và lời giải nằm trong STUDENT.md và solution.py. Nếu quay lời giải, đặt sau điểm dừng hoặc tách thành đoạn tùy chọn.

## 5. Kiểm tra và kết bài

{expected}

Hỏi: “{reflection}”

Kết bài: “Nếu bạn giải thích được vì sao kết quả thay đổi, hãy thử một đầu vào khác trước khi sang bài tiếp theo.” Không hứa bài tiếp theo đã có video khi chưa xuất bản.

## Ghi chú riêng trước khi quay

- Cách mình sẽ nói lại lời mở: ____
- Điểm mình chưa giải thích tự tin: ____
- Chi tiết thật mình muốn kể, nếu có: ____
- Timestamp cần quay lại: ____

## English lesson summary

{english}

Translate captions from the actual final take. This summary is not a timed subtitle track.
''')
    write(folder/'STUDENT.md', f'''# {ident} · {title}

## Bạn sẽ làm được gì?

{outcome}

Sao chép starter.py thành my-work.py, rồi chạy bằng `python my-work.py` trong thư mục bài học. Xem [hướng dẫn bắt đầu](../../STUDENT-START.md) nếu chưa chạy được Python.

## Tự làm trước khi xem lời giải

{exercise}

## Kiểm tra

{expected}

Ghi một đầu vào, kết quả mong đợi và kết quả thực tế. Nếu khác nhau, ghi thay đổi bạn đã thử.

## Gợi ý từng bước

{hinttext}

## Đối chiếu lời giải

Mở solution.py sau khi đã thử. Chạy cùng đầu vào với bản của bạn. Giải thích một khác biệt thay vì chép lại cả file. Lời giải là một cách làm, không phải cách duy nhất.

## Nghĩ thêm

{reflection}

## English summary

{english}
''')

tracker = ['# Production tracker', '', 'All items start as **script draft / not recorded**. Update after real work; do not treat prepared materials as completed teaching.', '', '| ID | Lesson | Script review | Rehearsal | Recorded | Edited | VI captions | EN captions | Learner pilot | Actual duration |', '|---|---|---|---|---|---|---|---|---|---|']
for n, row in enumerate(lessons, 1):
    ident = f'PY{n:02}' if n <= 6 else f'BK{n-6:02}'
    tracker.append(f'| {ident} | [{row[0]}](python-path/{n:02}/TEACHER.md) | Draft | — | — | — | — | — | — | — |')
tracker += ['', '## Batch completion checks', '', '- [ ] Nam has reviewed explanations and adapted the scripts to his own voice.', '- [ ] Each final code file matches what appears on screen.', '- [ ] Students can find starter, task, hints and solution.', '- [ ] Captions reflect the final edit.', '- [ ] At least one beginner has attempted the path; observed problems have been addressed.', '- [ ] Course description and actual lesson durations match the finished materials.', '- [ ] Website lesson mapping has been reviewed; publishing requires separate authorization.']
write(KIT/'PRODUCTION-TRACKER.md', '\n'.join(tracker))
print('Created 10 lesson packs and production tracker.')
