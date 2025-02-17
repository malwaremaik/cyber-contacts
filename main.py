contact_list = []

def show_contact_list():
    print("Contact List:")

    for i, contact in enumerate(contact_list):
        print(f"{i + 1}.")
        print(f"Name: {contact["name"]}")
        print(f"Email: {contact["email"]}")
        print(f"Phone Number: {contact["phone number"]}")

    return

def add_contact():
    name = input("Enter a name: ")
    email = input("Enter an email: ")
    phone_number = input("Enter a phone number: ")
    contact_list.append({ "name": name, "email": email, "phone number": phone_number })    

    return

print()
print("Welcome to CYBERCONTACTS!")

while True:
    print("""
    1. ADD contact (a)
    2. DELETE contact (d)
    3. SHOW all contacts (s)
    4. QUIT the program (q)
    """)
    option = input("Type a, d, s or q: ")
    print()

    if option == "a":
        add_contact()
    elif option == "d":
        pass
    elif option == "s":
        show_contact_list()
    elif option == "q":
        break
    else: 
        print("Invalid option. Please choose again!")