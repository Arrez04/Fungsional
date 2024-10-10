# Global dictionaries to store user accounts, profiles, and borrowing records
accounts = {}  # Stores {NIM: password}
profiles = {}  # Stores {NIM: {"name": "", "age": 0, "address": ""}}
borrow_records = {}  # Stores {NIM: [("book_id", "title", "author", "year")]}

# List of available books (tuple format: (id, title, author, year))
books = [
    (1, "Python Programming", "John Zelle", 2010),
    (2, "Clean Code", "Robert C. Martin", 2008),
    (3, "Artificial Intelligence", "Stuart Russell", 2009)
]

def register():
    nim = input("Enter NIM: ")
    if nim in accounts:
        print("NIM already registered.")
        return
    password = input("Enter password: ")
    accounts[nim] = password
    profiles[nim] = {"name": "", "age": 0, "address": ""}
    borrow_records[nim] = []
    print(f"User with NIM {nim} registered successfully.")

def login():
    nim = input("Enter NIM: ")
    if nim not in accounts:
        print("NIM not found.")
        return None
    password = input("Enter password: ")
    if accounts[nim] == password:
        print(f"Login successful for NIM {nim}.")
        return nim
    else:
        print("Incorrect password.")
        return None

def view_profile(nim):
    profile = profiles[nim]
    print(f"Profile of NIM {nim}:")
    print(f"Name: {profile['name']}")
    print(f"Age: {profile['age']}")
    print(f"Address: {profile['address']}")

def edit_profile(nim):
    profile = profiles[nim]
    print("Edit your profile:")
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    address = input("Enter new address: ")
    profile['name'] = name
    profile['age'] = age
    profile['address'] = address
    print("Profile updated successfully.")

def view_books():
    print("Available books:")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")

def borrow_book(nim):
    view_books()
    book_id = int(input("Enter the ID of the book to borrow: "))
    for book in books:
        if book[0] == book_id:
            borrow_records[nim].append(book)
            print(f"Book '{book[1]}' borrowed successfully.")
            return
    print("Invalid book ID.")

def return_book(nim):
    if not borrow_records[nim]:
        print("You have no borrowed books.")
        return
    print("Your borrowed books:")
    for i, book in enumerate(borrow_records[nim], 1):
        print(f"{i}. {book[1]} by {book[2]} ({book[3]})")
    choice = int(input("Enter the number of the book to return: "))
    if 1 <= choice <= len(borrow_records[nim]):
        returned_book = borrow_records[nim].pop(choice - 1)
        print(f"Book '{returned_book[1]}' returned successfully.")
    else:
        print("Invalid choice.")

def user_menu(nim):
    while True:
        print("\nUser Menu:")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. View Available Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_profile(nim)
        elif choice == "2":
            edit_profile(nim)
        elif choice == "3":
            view_books()
        elif choice == "4":
            borrow_book(nim)
        elif choice == "5":
            return_book(nim)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice, please try again.")

def main():
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            nim = login()
            if nim:
                user_menu(nim)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main program
main()
