import json


# Contact Book
class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.file_path = "contact_book.json"
        self.load_contacts()

    # load contact book from file
    def load_contacts(self):
        try:
            with open(self.file_path, "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("Error decoding JSON. Contact data might be corrupted.")

    # save contact book to file
    def save_contacts(self):
        with open(self.file_path, "w") as file:
            json.dump(self.contacts, file, indent=2)

    # add contact info to contact book
    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {
            "phone_number": phone_number,
            "email": email,
            "address": address,
        }
        print(f"Contact {name} added successfully!")
        self.save_contacts()

    # view contact list
    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for name, contact_info in self.contacts.items():
                print(f"{name}: {contact_info['phone_number']}")

    # search_key with name or phone number
    def search_contact(self, search_key):
        for name, contact_info in self.contacts.items():
            if (
                search_key.lower() in name.lower()
                or search_key in contact_info["phone_number"]
            ):
                print(f"Name: {name}")
                print(f"Phone Number: {contact_info['phone_number']}")
                print(f"Email: {contact_info['email']}")
                print(f"Address: {contact_info['address']}")
                return
        print(f"No contact found with '{search_key}'.")

    # update contact info
    def update_contact(self, name, phone_number, email, address):
        if name in self.contacts:
            self.contacts[name] = {
                "phone_number": phone_number,
                "email": email,
                "address": address,
            }
            print(f"Contact {name} updated successfully!")
            self.save_contacts()
        else:
            print(f"No contact found with the name {name}.")

    # delete contact info
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
            self.save_contacts()
        else:
            print(f"No contact found with the name {name}.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)

        elif choice == "2":
            contact_book.view_contact_list()

        elif choice == "3":
            search_key = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_key)

        elif choice == "4":
            name = input("Enter name of the contact to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_book.update_contact(name, phone_number, email, address)

        elif choice == "5":
            name = input("Enter name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
