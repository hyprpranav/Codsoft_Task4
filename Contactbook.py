import sqlite3
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    name TEXT PRIMARY KEY,
    phone TEXT,
    email TEXT,
    address TEXT
)
''')
conn.commit()

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    try:
        cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                       (name, phone, email, address))
        conn.commit()
        print(f"Contact '{name}' added successfully!\n")
    except sqlite3.IntegrityError:
        print(f"Contact '{name}' already exists.\n")

def view_contacts():
    cursor.execute("SELECT name, phone FROM contacts")
    rows = cursor.fetchall()
    if not rows:
        print("No contacts found.\n")
    else:
        print("Contact List:")
        for name, phone in rows:
            print(f"{name} - {phone}")
        print()

def search_contact():
    query = input("Enter name or phone number to search: ").strip().lower()
    cursor.execute("SELECT name, phone, email, address FROM contacts")
    rows = cursor.fetchall()
    found = False
    for name, phone, email, address in rows:
        if query in name.lower() or query in phone:
            print("\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {phone}")
            print(f"Email: {email}")
            print(f"Address: {address}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    cursor.execute("SELECT name, phone, email, address FROM contacts WHERE name = ?", (name,))
    row = cursor.fetchone()
    if row:
        print("Leave blank to keep current value.")
        current_name, current_phone, current_email, current_address = row
        new_name = input(f"New name [{current_name}]: ").strip() or current_name
        new_phone = input(f"New phone number [{current_phone}]: ").strip() or current_phone
        new_email = input(f"New email [{current_email}]: ").strip() or current_email
        new_address = input(f"New address [{current_address}]: ").strip() or current_address

        cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ?, address = ? WHERE name = ?",
                       (new_name, new_phone, new_email, new_address, current_name))
        conn.commit()
        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
    if cursor.rowcount:
        conn.commit()
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")

def menu():
    while True:
        print("CONTACT BOOK MENU")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Bye!")
            conn.close()
            break
        else:
            print("Invalid choice. Please select from 1 to 6.\n")
            
menu()