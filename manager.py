import json
import os

FILE_NAME = "contacts.json"
def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return{}
    return {}

def save_contacts(contacts):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)

def add_contact(contacts):
    name = input("Your name: ").strip().title()
    if not name:
        print("Name cannot be empty.")
        return
    
    if name in contacts:
        choice = input(f"{name} already exists. Update number? (y/n): ").lower().strip()
        if choice != 'y':
            print("Cancelled.")
            return
    number = input("Enter number: ").strip()
    if not number:
        print("Number cannot be empty.")
        return

    contacts[name] = number
    save_contacts(contacts)
    print("Contact added!")
    
def find_contact(contacts):
    search_term = input("Enter what to find: ").strip()
    if not search_term:
        print("Search term cannot be empty.")
        return
    
    found = False
    for name, number in contacts.items():
        if search_term.lower() in name.lower() or search_term == number:
            print(f"{name}: {number}")
            found = True       
            
    if not found:
        print("Contact not found.")
def delete_contact(contacts):
    name = input("Enter to delete: ").strip().title()
    if not name:
        print("Name cannot be empty.")
        return
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted!")
    else:
        print("Contact not found")
    
def all_contact(contacts):
    if not contacts:
        print("Contacts list is empty")
    else:
        print(f"Total contacts: {len(contacts)}")
        for name, number in sorted(contacts.items()):
            print(f"{name}: {number}")

if __name__ == "__main__":
    contacts = load_contacts()

    while True:
        command = input("Enter command (add, find, delete, all, exit): ").lower().strip()
    
        if command == 'exit':
            print("Goodbye!")
            break 
        elif command == 'add':
            add_contact(contacts)
        elif command == 'find':
            find_contact(contacts)
        elif command == 'delete':
            delete_contact(contacts)
        elif command == 'all':
            all_contact(contacts)
        else:
            print("Invalid command.")
