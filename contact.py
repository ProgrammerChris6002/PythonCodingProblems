# creating a dictionary to store contacts
contacts = {}


# function to display/view saved contacts
def display_contact():
    print("Name\t\tContacts")
    for keys in contacts:
        print(f"{keys}\t\t{contacts[keys]}")



# Running an infinite loop
while True:
    # Getting user input
    choice = int(input("1. Add new contact\n2. Search contact\n3. Display contact\n4. Edit contact\n5. Delete contact\n6. Exit\nEnter your choice==> "))

    if (choice == 1):
        add_num = int(input("How many contacts do you wish to add: "))
        if (add_num == 1):
            add_name = input("Enter the name of the contact: ")
            add_phone = input("Enter the phone number: ")
            # Adding the contacts to the contacts dictionary
            contacts[add_name] = add_phone

        elif (add_num > 1):
            add_name = input("Enter the contacts to be added as comma seperated values: ")
            add_phone = input("Enter their phone numbers: ")
            add_lst = add_name.split(",")
            add_lst2 = add_phone.split(",")

            # Running a for loop based on the number of contacts to be added
            for i in range(add_num):
                each = add_lst[i]
                each2 = add_lst2[i]
                # Adding the contacts to the contacts dictionary
                contacts[each] = each2


    elif (choice == 2):
        search_name = input("Enter the name of the contact: ")
        # Getting the phone of the searched contact
        print(f"{search_name}\t\t{contacts.get(search_name)}")


    elif (choice == 3):
        display_contact()


    elif (choice == 4):
        edit_contact = input("Enter the name of the contact you wish to edit: ")
        phone = contacts[edit_contact]
        new_name = input("Enter the new name of the contact, enter 'q' to skip: ")
        new_phone = input("Enter the new phone number of the contact, enter 'q' to skip: ")

        if (new_name != 'q') and (new_phone != 'q'):
            contacts.pop(edit_contact)
            contacts[new_name] = new_phone
        elif (new_name == 'q') and (new_phone != 'q'):
            contacts.pop(edit_contact)
            contacts[edit_contact] = new_phone
            contacts[edit_contact] = new_phone
        elif (new_name != 'q') and (new_phone == 'q'):
            contacts.pop(edit_contact)
            contacts[new_name] = phone


    elif (choice == 5):
        del_num = int(input("How many contacts do you wish to delete: "))
        if (del_num == 1):
            del_contact = input("Enter the contact to be deleted: ")
            # Deleting the contact
            contacts.pop(del_contact)

        elif (del_num > 1):
            del_contacts = input("Enter the contacts to be deleted as comma seperated values: ")
            del_lst = del_contacts.split(",")
            # Running a for loop on our list of contacts to be deleted
            for i in del_lst:
                # Deleting the contacts
                contacts.pop(i)


    elif (choice == 6):
        print("Bye...")
        break

    else:
        print("Invalid input!")
        break