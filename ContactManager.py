import csv

class Contact():     

    def __init__(self, name, post_address, gender, email, phone_number):
        self.name=name
        self.post_address=post_address
        self.gender=gender
        self.email=email

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def set_phone(self, phone_number):
        self.phone_number = phone_number
        
    def get_phone(self):
        return self.phone_number

    def set_email(self,email):
        self.email = email

    def get_email(self):
        return self.email

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_post(self, post_address):
        self.post_address = post_address

    def get_post(self):
        return self.post_address

    def get_contact(self):
        print("CONTACT DETAILS\nName: {0}\nPhone: {1}\nEmail: {2}\nGender: {3}\nPostal address: {4}\n".format(self.get_name(), self.get_phone(), self.get_email(), self.get_gender(), self.get_post()))




class ContactManager:
    def __init__(self):
        self.contact_holder = list()
        

    def add_contact(self, name, post_address, gender, email, phone_number):
        print("Adding a New Contact:")
        tempContact = Contact(name,post_address,gender,email,phone_number)

        tempContact.set_name(name)
        tempContact.set_post(post_address)
        tempContact.set_gender(gender)
        tempContact.set_email(email)
        tempContact.set_phone(phone_number)
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
        found_contact = list()
        
        for present_contact in self.contact_holder:
            if present_contact.name == search_name:
                found_contact.append(present_contact)
        
        if len(found_contact) == 0:
            print("Contact not found")
        else:
            for one in found_contact:
                one.get_contact()

    def read_csv(self, csv):
        with open( csv, 'r') as contact_file:
           contact_file.readline()

           for line in contact_file.readlines():
                text = line.strip().split(",")





newContact = ContactManager()
newContact.add_contact("asd","asd","asd","asd","asd")
newContact.delete_contact()
newContact.search_contact()

            