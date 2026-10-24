from dotenv import load_dotenv
import os
from books import show_books, load_books, save_books

load_dotenv()

name = input("Enter your name: ")
print("Welcome", name)

admin = input("Enter Admin Mode? (yes/no): ")

if admin == "yes":
    password = input("Enter password: ")

    if password == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("Admin login successful")
    else:
        print("Wrong password")

books = load_books()

count = int(input("How many new books? "))

for i in range(count):
    book = input("Enter book name: ")
    books.append(book)

save_books(books)
show_books(books)