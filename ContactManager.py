class Contact():     
    def set_name(self):
        self.name = str(input("Enter name: \n"))

    def get_name(self):
        return self.name

    def set_phone(self):
        self.phone_number = str(input("Enter phone number: \n"))
        
    def get_phone(self):
        return self.phone_number

    def set_email(self):
        self.email = str(input("Enter email: \n"))

    def get_email(self):
        return self.email

    def set_gender(self):
        self.gender = str(input("Enter gender: \n"))

    def get_gender(self):
        return self.gender

    def set_post(self):
        self.post_address = str(input("Enter Postal Address: \n"))

    def get_post(self):
        return self.post_address

    def get_contact(self):
        print("CONTACT DETAILS\nName: {0}\nPhone: {1}\nEmail: {2}\nGender: {3}\nPostal address: {4}\n".format(self.get_name(), self.get_phone(), self.get_email(), self.get_gender(), self.get_post()))




class ContactManager:
    def __init__(self):
        self.contact_holder = list()
        

    def add_contact(self):
        print("Adding a New Contact:")
        tempContact = Contact()

        tempContact.set_name()
        tempContact.set_post()
        tempContact.set_gender()
        tempContact.set_email()
        tempContact.set_phone()
        self.contact_holder.append(tempContact)
        print("Contact added\n")

    def delete_contact(self):
        parameter = input("Enter name to delete:")
        index = 0
        for present_contact in self.contact_holder:
            if present_contact.name == parameter:
                self.contact_holder.remove(present_contact)
                index += 1
                print("Contact Deleted!\n")
            else:
                print("Contact not Found.\n")

    def search_contact(self):
        search_name = input("Enter name to search:")
        index = 0
        found_contact = list()
        for present_contact in self.contact_holder:
            if present_contact.name == search_name:
                found_contact.append(present_contact)
            index += 1
        
        if len(found_contact) == 0:
            print("Contact not found")
        else:
            for one in found_contact:
                one.get_contact()


            


newContact = ContactManager()
newContact.add_contact()
newContact.delete_contact()
newContact.search_contact()

            