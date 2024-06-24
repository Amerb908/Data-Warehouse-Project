#this is experimental where I would get user info and store it in a csv 
# and maybe soon store it in a database

import csv
import os

class User:
    def __init__(self, name, country):
        self.name = name
        self.country = country

class LinkedList:
    def __init__(self):
        self.head = None
        self.current_id = 0  # Initialize ID counter

    class Node:
        def __init__(self, user, user_id):
            self.user = user
            self.user_id = user_id
            self.next = None

    def insert(self, user):
        self.current_id += 1
        new_node = self.Node(user, self.current_id)
        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append({'id': current.user_id, 'name': current.user.name, 'country': current.user.country})
            current = current.next
        return result

def collect_user_data():
    name = input("Enter user's name: ")
    country = input("Enter user's country: ")
    return User(name, country)

def write_to_csv(users):
    fieldnames = ['id', 'name', 'country']
    file_exists = os.path.isfile('Data/users.csv')
    with open('Data/users.csv', 'a', newline='') as file:  # Change to 'a' for append mode
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:  # Check if file does not exist to write header
            writer.writeheader()
        for user in users:
            writer.writerow(user)

def main():
    linked_list = LinkedList()
    while True:
        user_input = input("Do you want to add a user? (yes/no): ")
        if user_input.lower() == 'no':
            break
        user = collect_user_data()
        linked_list.insert(user)

    # Write to CSV
    user_data = linked_list.to_list()
    write_to_csv(user_data)
    print("Data has been written to CSV.")

if __name__ == "__main__":
    main()
