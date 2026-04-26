phone_book = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    phone_book[name] = number
    print("Contact saved!")

def search_contact():
    name = input("Enter name: ")
    print(phone_book.get(name, "Contact not found"))

def view_contacts():
    for name, number in phone_book.items():
        print(f"{name}: {number}")

while True:
    print("\n1.Add 2.Search 3.View 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_contact()
    elif ch == "2":
        search_contact()
    elif ch == "3":
        view_contacts()
    elif ch == "4":
        break