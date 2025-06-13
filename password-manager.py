# Password Manager CLI

passwords = []

def add_new():
    try:
        data = input("Enter Website name, Username, Password (space-separated): ").strip().split()
        if len(data) != 3:
            print("Invalid input. Please enter exactly 3 values.")
            return
        website, username, passwd = data
        passwords.append({"website": website, "username": username, "password": passwd})
        print("Credential added.")
    except Exception as e:
        print(f"Error: {e}")

def view():
    if not passwords:
        print("No credentials saved yet.")
    else:
        print("Saved websites:")
        for entry in passwords:
            print(f"- {entry['website']}")

def retrieve():
    site = input("Enter website to retrieve password: ").strip()
    for entry in passwords:
        if entry['website'].lower() == site.lower():
            print(f"Username: {entry['username']}, Password: {entry['password']}")
            return
    print("Website not found.")

def update_delete():
    site = input("Enter website to update/delete: ").strip()
    for entry in passwords:
        if entry['website'].lower() == site.lower():
            action = input("Enter 'u' to update, 'd' to delete: ").strip().lower()
            if action == 'u':
                try:
                    new_data = input("Enter new username and password (space-separated): ").split()
                    if len(new_data) != 2:
                        print("Invalid input. Enter exactly 2 values.")
                        return
                    entry['username'], entry['password'] = new_data
                    print("Credential updated.")
                except Exception as e:
                    print(f"Error: {e}")
            elif action == 'd':
                passwords.remove(entry)
                print("Credential deleted.")
            else:
                print("Invalid action.")
            return
    print("Website not found.")

while True:
    print("\n=== Password Manager ===")
    print("1. Add new credentials")
    print("2. View all saved websites")
    print("3. Retrieve a password")
    print("4. Update or delete a credential")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1–5): ").strip())
        if choice == 1:
            add_new()
        elif choice == 2:
            view()
        elif choice == 3:
            retrieve()
        elif choice == 4:
            update_delete()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")
    except ValueError:
        print("Please enter a valid number.")
