import csv


add_num = int(input("How many contacts do you wish to add: "))
if (add_num == 1):
    add_name = input("Enter the name of the contact: ")
    add_phone = input("Enter the phone number: ")
    print("Adding Contact...")

    with open("contacts_saver.csv", mode="w") as contacts_file:
        contacts_writer = csv.writer(contacts_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

        contacts_writer.writerow(['Name', 'Mobile Phone'])
        contacts_writer.writerow([add_name, add_phone])
        print("Contact successfully added.")


elif (add_num > 1):
    add_name = input("Enter the contacts to be added as comma seperated values: ")
    add_phone = input("Enter their phone numbers: ")
    add_lst = add_name.split(",")
    add_lst2 = add_phone.split(",")
    print("Adding Contacts...")

    with open("contacts_saver.csv", mode="w") as contacts_file:
        contacts_writer = csv.writer(contacts_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        contacts_writer.writerow(['Name', 'Mobile Phone'])

        for i in range(add_num):
            each_name = add_lst[i]
            each_phone = add_lst2[i]
            contacts_writer.writerow([each_name, each_phone])
        
        print("Contacts successfully added.")