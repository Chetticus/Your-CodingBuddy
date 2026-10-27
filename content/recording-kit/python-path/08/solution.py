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
