class Customer:
    id = 2
    def __init__(self, id, name, city, age):
        self.id = id
        self.name = name
        self.city = city
        self.age = age
        
    def __str__(self):
        return f"customer {self.id} is {self.name} from {self.city}"