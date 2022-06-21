#FUNCTION THAT GETS THE CONTACT INFO
def get_contact_info():
    name = input("Contact name: ")
    number = input("Mobile number:")
    email = input("Email address: ")
    return [name, number, email]

#FUNCTION THAT CREATES THE CONTACT
def create_contact(contact_info):
    contact = {
        "Name" : contact_info[0],
        "Number" : contact_info[1],
        "Email" : contact_info[2]
    }
    return contact

#FUNCTION THAT ADDS THE CONTACT TO THE LIST
def add_contact_to_list(contact_list, contact):
    contact_list.append(contact)
    return contact_list

#FUNCTION THAT SHOWS THE CONTACT LIST
def show_list(contact_list):
    for contact in contact_list:
        print("\n---- Contact " + str(contact_list.index(contact) + 1) + " ----")
        print("Name: " + contact["Name"])
        print("Mobile Number: " + contact["Number"])
        print("Email Address: " + contact["Email"])
        print("-------------------\n")

#FUNCTION THAT DELETES THE CONTACT
def delete_contact(contact_list, to_delete):
    del contact_list[to_delete]

#FUNCTION THAT EDITS THE CONTACT
def edit_contact(contact_list, to_edit):
    print("1 - Name: " + contact_list[to_edit]["Name"])
    print("2 - Mobile Number: " + contact_list[to_edit]["Number"])
    print("3 - Email Address: " + contact_list[to_edit]["Email"])
    info_to_edit = input("What do you want to edit in this contact?[type the number corresponding to your choice]:")
    if info_to_edit == "1":
        contact_list[to_edit]["Name"] = input("Enter new name: ")
        print("\nYou successfully edited the Name for Contact " + str(to_edit + 1))
    if info_to_edit == "2":
        contact_list[to_edit]["Number"] = input("Enter new mobile number: ")
        print("\nYou successfully edited the Mobile number for Contact " + str(to_edit + 1))
    if info_to_edit == "3":
        contact_list[to_edit]["Email"] = input("Enter new email address: ")
        print("\nYou successfully edited the Email Address for Contact " + str(to_edit + 1))