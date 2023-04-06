import csv

contacts = {}

class Contacts:
    global contacts
    
    def __init__(self):
        self.txt = "This object manipulates contacts."

    def __str__(self):
        return self.txt
    

    def display(self):
        print("Name\t\tContacts")
        for keys in contacts:
            print(f"{keys}\t\t{contacts[keys]}")
    

    def add(self):
        add_num = int(input("How many contacts do you wish to add: "))
        if (add_num == 1):
            add_name = input("Enter the name of the contact: ")
            add_phone = input("Enter the phone number: ")
            # Adding the contacts to the contacts dictionary
            contacts[add_name] = add_phone
            Contacts.display()

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
            Contacts.display()

        else:
            raise ValueError (f"\'{add_num}\' cannot be less than 1!!!")
        

    def save(self, file, mode="w", save_num=1):
        if (save_num > 1):
            save_name = input("Enter the contacts to be saved as comma seperated values: ")
            save_phone = input("Enter their phone numbers: ")
            print("Saving Contacts.\nSaving Contacts..\nSaving Contacts...")
            save_lst = save_name.split(",")
            save_lst2 = save_phone.split(",")

            with open(file, mode=mode) as contacts_file:
                contacts_writer = csv.writer(contacts_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                contacts_writer.writerow(['Name', 'Mobile Phone'])

                for i in range(save_num):
                    each_name = save_lst[i]
                    each_phone = save_lst2[i]
                    contacts_writer.writerow([each_name, each_phone])
                
                return "Contacts saved successfully."
            
        elif (save_num == 1):
            save_name = input("Enter the name of the contact: ")
            save_phone = input("Enter the phone number: ")
            print("Saving Contact.\nSaving Contact..\nSaving Contact...")

            with open(file, mode=mode) as contacts_file:
                contacts_writer = csv.writer(contacts_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

                contacts_writer.writerow(['Name', 'Mobile Phone'])
                contacts_writer.writerow([save_name, save_phone])
                return "Contact saved successfully."

        else:
            raise ValueError (f"\'{save_num}\' cannot be less than 1!!!")
        

    def edit(self):
        edit_contact = input("Enter the name of the contact you wish to edit: ")
        phone = contacts[edit_contact]
        new_name = input("Enter the new name of the contact, enter 'q' to skip: ")
        new_phone = input("Enter the new phone number of the contact, enter 'q' to skip: ")

        if (new_name != 'q') and (new_phone != 'q'):
            contacts.pop(edit_contact)
            contacts[new_name] = new_phone
            Contacts.display()
        elif (new_name == 'q') and (new_phone != 'q'):
            contacts.pop(edit_contact)
            contacts[edit_contact] = new_phone
            contacts[edit_contact] = new_phone
            Contacts.display()
        elif (new_name != 'q') and (new_phone == 'q'):
            contacts.pop(edit_contact)
            contacts[new_name] = phone
            Contacts.display()
        else:
            raise ValueError (f"Invalid input!!!")
        

    def search(self):
        search_name = input("Enter the name of the contact: ")
        # Getting the phone of the searched contact
        print(f"{search_name}\t\t{contacts.get(search_name)}")

        Contacts.display()


    def delete(self):
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

        else:
            raise ValueError (f"\'{del_num}\' cannot be less than 1!!!")