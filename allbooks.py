from book import Book

class All_books:
    def __init__(self):
        self.books_list = []

    def new_book(self):
        id = Book.id
        Book.id += 1
        name = input("insert book name:\n")
        author= input("insethert the author name:\n")
        year_published= input("insert the year when the book published:\n")
        book_type = input("choose the type of the book:\n1) ten days loan\n2) five days loan\n3) two days loan\n")
        status = "available"
        if book_type == "1":
            book_type = Book.BookType.TEN_DAYS.value
        elif book_type == "2":
            book_type = Book.BookType.FIVE_DAYS.value
        elif book_type =="3":
            book_type = Book.BookType.TWO_DAYS.value
        book = Book(id, name, author, year_published, book_type, status)
        self.books_list.append(book)
        print("new book has been added\n")

    def display_books(self):
        print("the books are:")
        for book in self.books_list:
            print(book.name)
        print("\nthose are all the book\n")

    def search_book(self):
        searchword = input("insert book name:\n")
        for book in self.books_list:
            if searchword.lower() in book.name.lower():
                print(f"{book}\n")
            else:
                pass
        print("this is all the books that matched your search, if you dont find the book you wanted\nthe book not exists in the system or you got the wrong name\n")

    def remove_book(self):
        book_to_remove = input("insert the name of the book you want to remove:\n")
        book_not_removed = True
        for book in self.books_list:
            if book_to_remove.lower() in book.name.lower():
                print(f"{book}\n")
                remove = int(input(f"is {book.name} is the book you want to remove?\n1) yes\n2) no\n"))
                if remove == 1:
                    self.books_list.remove(book)
                    print("book removed\n")
                    book_not_removed = False
                    break
                elif remove == 2:
                    book_not_removed = True
        if book_not_removed:
            print("the book you wanted to remove isn't exists or you got the wrong name\n")