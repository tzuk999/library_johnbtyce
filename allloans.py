from datetime import datetime, timedelta
from loan import Loan
from customer import Customer
from allcustomers import All_customers
from book import Book
from allbooks import All_books


class All_loans:
    def __init__(self):
        self.all_loans = []

    def new_loan(self,bookslist):
        the_customer_id = int(input("insert your customer id:\n"))
        the_book_id = int(input("insert the book id of the book you want to loan:\n"))
        loandate = datetime.now()
        for book in bookslist:#getting the book to find his type for the return date
            if book.id == the_book_id:
                book_type = book.book_type
                book.loan_book()#changing the book status to unavailable
                break
        if book_type == Book.BookType.TEN_DAYS.value:
            days = 10
        elif book_type == Book.BookType.FIVE_DAYS.value:
            days = 5
        elif book_type == Book.BookType.TWO_DAYS.value:
            days = 2
        returndate = loandate + timedelta(days)
        loandate = loandate.isoformat()
        returndate = returndate.isoformat()
        loan = Loan(the_customer_id, the_book_id, returndate, loandate, "in time")
        self.all_loans.append(loan)
        print("new loan has been added\n")

    def remove_loan(self, booklist):
        bookid = int(input("insert the book id of the book you want to return:\n"))
        for loan in self.all_loans:
            if loan.book_id == bookid:
                self.all_loans.remove(loan)
        for book in booklist:
            if book.id == bookid:
                book.return_book()
                print(f"you return the book: {book.name}\nyour loan has been deleted\n")
                break

    def display_loans(self):
        for loan in self.all_loans:
            print (f"{loan}\n")
        print("those are all the loans\n")


    def display_late_loans(self):
        lateloans = False
        for loan in self.all_loans:
            loan.status_check()
            if loan.status == "late":
                lateloans = True
                print(f"{loan}\n")
        print("those are all the late loans\n") if lateloans else print("there are no late loans\n")

    def display_customer_loans(self):
        customerid = int(input("insert customer id:\n"))
        for loan in self.all_loans:
            if loan.customer_id == customerid:
                print(f"the loans of customer {customerid} are:\n")
                break
            else:
                print(f"customer {customerid} has no loans\n")
        for loan in self.all_loans:
            if loan.customer_id == customerid:
                print(f"the book: {loan.book_id}\nthe returndate: {loan.returndate}\n")

