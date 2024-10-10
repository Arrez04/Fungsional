# Global dictionaries to store user accounts, profiles, and friend lists
accounts = {}  # Stores {NIM: password}
profiles = {}  # Stores {NIM: {"name": "", "age": 0, "address": ""}}
friend_lists = {}  # Stores {NIM: ["friend_NIM1", "friend_NIM2"]}

def register():
    nim = input("Enter NIM: ")
    if nim in accounts:
        print("NIM already registered.")
        return
    password = input("Enter password: ")
    accounts[nim] = password
    profiles[nim] = {"name": "", "age": 0, "address": ""}
    friend_lists[nim] = []
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
    print(f"Friends: {friend_lists[nim]}")

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

def add_friend(nim):
    friend_nim = input("Enter friend's NIM to add: ")
    if friend_nim in friend_lists[nim]:
        print(f"{friend_nim} is already in your friend list.")
    elif friend_nim not in accounts:
        print(f"Friend with NIM {friend_nim} not found.")
    else:
        friend_lists[nim].append(friend_nim)
        print(f"Friend {friend_nim} added successfully.")

def remove_friend(nim):
    friend_nim = input("Enter friend's NIM to remove: ")
    if friend_nim in friend_lists[nim]:
        friend_lists[nim].remove(friend_nim)
        print(f"Friend {friend_nim} removed successfully.")
    else:
        print(f"Friend {friend_nim} not found in your friend list.")

def delete_profile(nim):
    confirm = input(f"Are you sure you want to delete your profile and all data for NIM {nim}? (yes/no): ")
    if confirm == "yes":
        del accounts[nim]
        del profiles[nim]
        del friend_lists[nim]
        print(f"Profile and data for NIM {nim} deleted successfully.")
        return True
    return False

def user_menu(nim):
    while True:
        print("\nUser Menu:")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Add Friend")
        print("4. Remove Friend")
        print("5. Delete Profile")
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_profile(nim)
        elif choice == "2":
            edit_profile(nim)
        elif choice == "3":
            add_friend(nim)
        elif choice == "4":
            remove_friend(nim)
        elif choice == "5":
            if delete_profile(nim):
                break
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
