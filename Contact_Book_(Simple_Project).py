# Simple Contact Book Application
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter Contact Name:")
    phone = input("Enter Contact Number:")
    email = input("Enter Contact Email:")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\nContacts List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']},\n Phone: {contact['phone']},\n Email: {contact['email']}")
        print()

def search_contact():
    search_name = input("Enter the name to search:")
    found = False
    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print(f"Found Contact - Name: {contact['name']},\n Phone: {contact['phone']},\n Email: {contact['email']}")
            found = True
            break
    if not found:
        print("Contact not found.") 

def delete_contact():
    del_name = input("Enter the name of the contact to delete:")
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == del_name.lower():
            del contacts[i]
            print("Contact deleted successfully!")
            return
    print("Contact not found.")


# Main loop
while True:
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")