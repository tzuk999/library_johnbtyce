from book import Book
from allbooks import All_books
import json
from allcustomers import All_customers
from customer import Customer
import datetime
from loan import Loan


def load_all(list, json_name, class_name):
    with open(json_name) as f:
        all_file_json = json.load(f)

    for single_json in all_file_json:
        object = class_name(**single_json)
        list.append(object)
    return list

def save_all(list, json_name):
    new_list = []
    for object in list:
        new_list.append(object.__dict__)
    with open(json_name,"w") as f:
        json.dump(new_list, f)