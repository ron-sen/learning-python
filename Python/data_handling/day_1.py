import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])
def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    # Check for duplicate name using csv.reader (index-based)
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        
        # Skip the header row so we only check actual contacts
        next(reader, None) 
        
        for row in reader:
            # row[0] is the 'Name' column index
            if row and row[0].lower() == name.lower():
                print("Contact name already exists.")
                return

    # Append the new contact
    with open(FILENAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact added.")


def view_contacts():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) <= 1:
            print("No contacts found.")
            return

        print("\nYour Contacts:\n")
        
        for row in rows[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

def search_contact():
    term = input("Enter the name to search: ").strip().lower()
    found = False

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row['Name']} | {row['Phone']} | {row['Email']}")
                found = True

    if not found:
        print("No matching contact found.")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1 - 4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Thanks for using our software! 👋")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()