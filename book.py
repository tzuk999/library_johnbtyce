from enum import Enum
class Book:
    class BookType(Enum):
        TEN_DAYS = 1
        FIVE_DAYS = 2
        TWO_DAYS = 3
    id = 2
    def __init__(self, id, name, author, year_published, book_type, status):
        self.id = id
        Book.id +=1
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type
        self.status = status

    def loan_book(self):
        self.status = "unavailable"

    def return_book(self):
        self.status = "available"

    def __str__(self):
        return f"book id- {self.id} \nbook name- {self.name} \nauthor- {self.author} \nyear published- {self.year_published} \ntype- {self.book_type} \nstatus- {self.status}\n"
    

    def booktest():
        b = Book(1 ,"The Test", "Tzuk", 2023, Book.BookType.TEN_DAYS.value, "blabla")
        print(b)


    