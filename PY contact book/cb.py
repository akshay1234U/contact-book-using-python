import json

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ").strip().capitalize()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} added successfully.")
        save_contacts(contacts)

def view_contacts(contacts):
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("No contacts found.")

def search_contact(contacts):
    name = input("Enter the name to search: ").strip().capitalize()
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print("Contact not found!")


def update_contact(contacts):
    name = input("Enter the name to update: ").strip().capitalize()
    if name in contacts:
        print(f"Current details - Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email address: ").strip()
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} updated successfully.")
        save_contacts(contacts)
    else:
        print("Contact not found!")


def delete_contact(contacts):
    name = input("Enter the name to delete: ").strip().capitalize()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
        save_contacts(contacts)
    else:
        print("Contact not found!")


def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
