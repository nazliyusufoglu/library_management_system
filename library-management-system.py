class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_book(self):
        self.file.seek(0)  # Move the file pointer to the beginning
        books = self.file.readlines()
        for book in books:
            title, author, release_year, pages = book.strip().split(",")
            print(
                f"Title: {title}, Author: {author}, Release Year: {release_year}, Pages: {pages}"
            )
        self.file.seek(0)  # Reset file pointer to the beginning

    def add_book(self):
        books = input(
            "Please enter the book title, book author, first release year and number of pages"
        )
        self.file.write(books + "\n")

    def remove_book(self):
        self.file.seek(0)
        title = input("Please enter the book title you want to remove")
        new_books = self.file.read().splitlines()
        
        book_index = -1
        for index, book in enumerate(new_books):
            book_title = book.strip().split(",")[0]
            if book_title == title:
                book_index = index
            
                break
        if book_index != -1:
            self.file.truncate(0)
            new_books.remove(new_books[book_index])
            for i in new_books:
                self.file.write(i+'\n')
            print('The book has successfully removed.')
        else:
              print(f"The book '{title}' was not found.")
        
library = Library()

while True:
    print("""
      *** MENU***
    1- List Books
    2- Add Book
    3- Remove Book
    ***IF YOU WANT TO EXIT PRESS (4)***
""")
    selection = int(input("Enter the number of operation you want to do: "))


    if selection == 1:
        library.list_book()
    elif selection == 2:
        library.add_book()
    elif selection == 3:
        library.remove_book()
    elif selection == 4:
        print("You exit the menu")
        break
    else:
        print("You entered an invalid value! Try again. ")




 

