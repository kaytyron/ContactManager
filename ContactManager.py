class Contact():
    def __init__(self, name, phone_number, email, gender, post_address ):
        self.name = name
        self.phone_number = phone_number
        self.gender = gender
        self.email = email
        self.post_address = post_address
        
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

if __name__ == "__main__":

    contact_holder = list()

    code = -1

    while( code != 0):
        code = int(input("Enter 1 to add contact, 2 to delete, 3 to search, 0 to exit :\n"))

        if code == 0:
            #exit loop
            break

        elif code == 1:
            #add contact
            print("Adding a New Contact:")
            newContact.set_name()
            newContact.set_post()
            newContact.set_gender()
            newContact.set_email()
            newContact.set_phone()
            contact_holder.append(newContact)
            print("Contact added\n")

        elif code == 2:
            #delete contact
            parameter = input("Enter name to delete:")
            index = 0
            for present_contact in contact_holder:
                if present_contact.name == parameter:
                    contact_holder.remove(present_contact)
                    index += 1
                    print("Contact Deleted!\n")
                else:
                    print("Contact not Found.\n")
            
        elif code == 3:
            #search contact
            parameter = input("Enter name to search:")
            index = 0
            for present_contact in contact_holder:
                if present_contact.name == parameter:
                    present_contact.get_contact()
                    index += 1
                else:
                    print("Name not found\n")

        else:
            print("Not a valid option. Kindly Re-enter a number.")        


            