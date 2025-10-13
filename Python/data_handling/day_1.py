import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME , "w" , newline="" , encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name ","Phone","Email"])

def add_contact():
    name = input("Name:").strip()        
    phone = input("Phone:").strip()        
    email = input("Email:").strip()        

    with open(FILENAME , 'r' , encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader :
            if row["name"].lower() == name.lower():
                print("Contact name alreadt exists")
                return
            
    with open(FILENAME , 'a' , encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name , phone , email]) 
        print("Contact added")

def veiw_contacts():
    with open(FILENAME , 'r' , encoding="utf-8") as f:
        reader = csv.reader()
        rows = list(reader)

        if len(rows) < 1:
            print("No contact founds")
            return
        
        print("\n Your contacts : \n")

        for row in rows[1:] :
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

def serch_contact():
    term = input("Enter the name to search: ").strip().lower() 
    found = False

    with open(FILENAME , 'r' , encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row["Name"]} | {row["Phone"]}")
                found = True 

    if not found :
        print("NO matching contact found")


def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. view All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an aption (1 - 4)").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            veiw_contacts()
        elif choice == "3" :
            serch_contact()
        elif choice == "4":
            print("Thanks for using our software")
            break 
        else:
            print("Invalid choice of number")


if __name__ == "__main__":
    main()
    

        
