from books import show_books, load_books, save_books
import os
from dotenv import load_dotenv

load_dotenv()

name = input("Enter your name: ")
print("Welcome to Personal Book Manager,", name)
admin_mode = input("do you want to enter admin mode (yes/no)? ")
if admin_mode == "yes":
    admin_password = input("enter admin password: ")
    if admin_password == os.getenv("admin_pass"):
        print("admin mode activated")
    else:
        print("wrong password")
books = load_books()

print("Your saved books:")
show_books(books)

number = int(input("How many new books do you want to add? "))

for i in range(number):
    book = input("Enter the name of book: ")
    books.append(book)

save_books(books)

print("All your books:")
show_books(books)
save_books(books)