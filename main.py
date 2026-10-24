from books import show_books

name = input("Enter your name: ")
print("Welcome", name)
books = []
count = int(input("How many books do you have? "))
for i in range(count):
    book = input("Enter book name: ")
    books.append(book)

show_books(books)