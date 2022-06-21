#IMPORT FUNCTIONS
import contact_list_functions as clf

#VARIABLE DECLARATION
contact_list = []


print("Welcome to your Contact List!")

#GETTING INPUT
while True:

    #OPTIONS FOR THE USER
    print("-------------------")
    print("1 - Add a Contact")
    print("2 - Edit a Contact")
    print("3 - View Contacts")
    print("4 - Delete a Contact")
    print("0 - Quit")
    print("-------------------")

    user_input = input("Please choose an option above[type the number]: ")

    #INPUT VALIDATION
    if user_input not in ["1","2","3","4","0"]:
        print("Please type only the number corresponding to your choice.\n")
        continue

    #USER CHOOSES TO ADD A CONTACT
    if user_input == "1":
        print("Please enter the contact information.")
        contact_info = clf.get_contact_info()
        print("\nGreat! You've added a contact succesfully.\n")
        contact = clf.create_contact(contact_info)
        contact_list = clf.add_contact_to_list(contact_list, contact)

    #USER CHOOSES TO EDIT A CONTACT
    elif user_input == "2":
        if len(contact_list) == 0:
            print("\nYou have no contacts.")
        else: 
            clf.show_list(contact_list)
            to_edit = input("Which contact would you want to edit?[type the number corresponding to the contact]: ")
            clf.edit_contact(contact_list, int(to_edit) - 1)

    #USER CHOOSES TO VIEW THE CONTACTS
    elif user_input == "3":
        if len(contact_list) == 0:
            print("\nYou have no contacts.")
        else: 
            clf.show_list(contact_list)

    #USER CHOOSES TO DELETE A CONTACT
    elif user_input == "4":
        if len(contact_list) == 0:
            print("\nYou have no contacts.")
        else:
            clf.show_list(contact_list)
            to_delete = input("Which contact do you want to delete?[type the number corresponding to the contact]: ")
            clf.delete_contact(contact_list, int(to_delete) - 1)
            print("\nYou deleted Contact " + to_delete)

    #USER QUITS
    else:
        quit()