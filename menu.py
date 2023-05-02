from book import *
from allbooks import *
from customer import *
from loan import *
from allloans import *
from utils import *
def menu():
    books = All_books()
    customers = All_customers()
    loans = All_loans()
# load all data
    load_all(books.books_list, "books.json", Book)
    load_all(customers.customers_list, "customers.json", Customer)
    #load_loans(loans.all_loans, "loans.json")
    load_all(loans.all_loans, "loans.json", Loan)

    ADD_NEW_CUSTOMER = 1
    DISPLAY_CUSTOMERS = 2
    FIND_CUSTOMER = 3
    REMOVE_CUSTOMER = 4
    ADD_NEW_BOOK = 5
    DISPLAY_BOOKS = 6
    FIND_BOOK = 7
    REMOVE_BOOK = 8
    LOAN_BOOK = 9
    RETURN_BOOK = 10
    DISPLAY_LOANS = 11
    DISPLAY_LOANS_OF_CUSTOMER = 12
    DISPLAY_LATE_LOANS = 13
    EXIT = 20
    while True:
        while True:
            try:
                command = int(input("insert the number of the action you want to preform:\n1) Add new customer\n2) Display all customers\n3) Find customer by name\n4) Remove customer\n5) Add a new book\n6) Display all books\n7) Find book by name\n8) Remove book\n9) Loan a book\n10) Return a book\n11) Display all loans\n12) Display all loans of specific customer\n13) Display late loans\n20) exit\n"))
                break
            except:
                print("type error, plaese enter a valid number\n")

        if command == ADD_NEW_CUSTOMER:
            print("you choose to add a new customer\n")
            customers.new_customer()

        if command == DISPLAY_CUSTOMERS:
            print("you choose to display all customers\n")
            customers.display_customers()

        if command == FIND_CUSTOMER:
            print("you choose to find a customer by name\n")
            customers.search_customer()

        if command == REMOVE_CUSTOMER:
            print("you choose to remove a customer\n")
            customers.remove_customer()

        if command == ADD_NEW_BOOK:
            print("you choose to add a new book\n")
            books.new_book()

        if command == DISPLAY_BOOKS:
            print("you choose to display all books\n")
            books.display_books()

        if command == FIND_BOOK:
            print("you choose to find a book by name\n")
            books.search_book()

        if command == REMOVE_BOOK:
            print("you choose to remove a book\n")
            books.remove_book()

        if command == LOAN_BOOK:
            print("you choose to loan a book\n")
            loans.new_loan(books.books_list)
            #save_loans(loans.all_loans, "loans.json")

        if command == RETURN_BOOK:
            print("you choose to return a book\n")
            loans.remove_loan(books.books_list)
            #save_loans(loans.all_loans, "loans.json")

        if command == DISPLAY_LOANS:
            print("you choose to display all loans\n")
            loans.display_loans()
        

        if command == DISPLAY_LOANS_OF_CUSTOMER:
            print("you choose to display all loans of specific customer\n")
            loans.display_customer_loans()

        if command == DISPLAY_LATE_LOANS:
            print("you choose to display all late loans\n")
            loans.display_late_loans()
    
        if command == EXIT:
            print("you are exiting the program\n")
            break
# save all data        
        save_all(books.books_list, "books.json")
        save_all(customers.customers_list, "customers.json")
        save_all(loans.all_loans, "loans.json")
        

menu()