from customer import Customer

class All_customers:
    def __init__(self):
        self.customers_list = []

    def new_customer(self):
        for customer in self.customers_list:
            if customer.id >= Customer.id:
                Customer.id = customer.id + 1
        customer = Customer(id = Customer.id, name = input("insert customer name:\n"),city= input("insert city:\n"), age= (input("insert age (in years):\n")))
        Customer.id += 1
        self.customers_list.append(customer)
        print("new customer has been added\n")

    def display_customers(self):
        print("the customer are:")
        for customer in self.customers_list:
            print(f"{customer}\n")

    def search_customer(self):
        searchword = input("insert your search:\n")
        customer_exist = False
        for customer in self.customers_list:
            if searchword.lower() in customer.name.lower():
                print(f"{customer}\n")
                customer_exist = True
            
        print("does are all the customers that matched the search in the system\n") if customer_exist else print("there are no customer that matched the search\n")

    def remove_customer(self):
        customer_to_remove = input("insert the name of the customer you want to remove:\n")
        for customer in self.customers_list:
            customer_not_removed = True
            if customer_to_remove.lower() in customer.name.lower():
                print(f"{customer}\n")
                remove = int(input(f"is {customer.name} is the cusromer you want to remove?\n1) yes\n2) no\n"))
                if remove == 1:
                    self.customers_list.remove(customer)
                    print("customer removed\n")
                    customer_not_removed = False
                    break
                elif remove == 2:
                    pass
        if customer_not_removed:
            print("the customer you wanted to remove isn't exists or you got the wrong name\n")

