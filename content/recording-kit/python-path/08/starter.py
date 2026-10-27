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

# TODO: them tim kiem, muon/tra va menu. Xem STUDENT.md.
