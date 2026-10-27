import json
from pathlib import Path


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

DATA = Path(__file__).with_name("books.json")


def load_books(path=DATA):
    if not path.exists():
        return [book.copy() for book in STARTER]
    books = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(books, list):
        raise ValueError("Expected a list of books.")
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
    return books


def save_books(books, path=DATA):
    path.write_text(json.dumps(books, ensure_ascii=False, indent=2), encoding="utf-8")

def main():
    try:
        books = load_books()
    except (OSError, ValueError) as error:
        print("Could not read books.json:", error)
        return
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
                try:
                    save_books(books)
                    print("Saved.")
                except OSError as error:
                    print("Change is in memory but could not be saved:", error)
            else:
                print("Unknown book, or its status already matches.")
        else:
            print("Choose f, b, r or q.")


if __name__ == "__main__":
    main()
