import csv


class ContactSaver(object):

    def __init__(self):
        self.txt = "This ContactSaver Object makes it easier to save contacts."


    def __str__(self):
        return self.txt


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