import json

def show_books(books):
    print("\n===== MY BOOKS =====")

    for book in books:
        print("Book Name:", book["name"])
        print("Book Priority:", book["priority"].upper())
        print("====================")


def load_books():
    try:
        file = open("books.json", "r")
        books = json.load(file)
        file.close()
        return books

    except FileNotFoundError:
        return []


def save_books(books):
    file = open("books.json", "w")
    json.dump(books, file, ensure_ascii=False, indent=4)
    file.close()