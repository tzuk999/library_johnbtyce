from datetime import datetime, date, timedelta
from book import Book
from allbooks import All_books
class Loan:
    
    def __init__(self, customer_id, book_id, returndate, loandate, status):
        self.customer_id = customer_id
        self.book_id = book_id
        self.loandate = loandate 
        self.returndate = returndate
        self.status = status

    def status_check(self):
        if datetime.fromisoformat(self.returndate) < datetime.now():
            self.status = "late"


    def __str__(self):
        return f"the customer that loaned the book: {self.customer_id}\nthe book that been loaned: {self.book_id}\nthe return date: {self.returndate}"