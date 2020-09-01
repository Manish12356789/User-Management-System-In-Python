class View:
    def __init__(self):
        pass

    def admin_login(self):
        admin_name = input("Enter Your Email: ")
        admin_password = input("Enter the Password: ")
        return admin_name, admin_password

    def user_login(self):
        user_name = input("Enter your Email: ")
        user_password = input("Enter your Password: ")
        return user_name, user_password

    def user_input(self):     # this is used to input data for normal user or admin
        inputs = list()
        user_name = str(input("Enter User Name: "))
        email = str(input("Enter User Email: "))
        password = str(input("Enter the Password: "))
        address = str(input("Enter User Address: "))
        phone_num = str(input("Enter Phone Number: "))

        inputs.append(user_name)   # all data into the list
        inputs.append(email)
        inputs.append(password)
        inputs.append(address)
        inputs.append(phone_num)
        print(inputs)
        return inputs

    def user_output(self, data):
        print("Your Information:")
        print("User Id: ", data[0])
        print("User Name: ", data[1])
        print("Email Address: ", data[2])
        print("Password: ", data[3])
        print("Address: ", data[4])
        print("Phone Number: ", data[5])

    def user_edit(self, data):
        print(" ")
        print("If you want to edit data fill the field otherwise leave without fill.")

        un = input("Enter new User Name: ")
        if un == '':
            un = data[1]

        em = input("Enter new Email Address: ")
        if em == '':
            em = data[2]

        pw = input("Enter new Password: ")
        if pw == '':
            pw = data[3]

        add = input("Enter new Address: ")
        if add == '':
            add = data[4]

        pn = input("Enter new Phone Number: ")
        if pn == '':
            pn = data[5]

        return un, em, pw, add, pn

    def delete_user_data(self):
        print("Enter User Name Which you want to remove or block.")
        un = input("Enter User Name: ")
        return un

    def admin_output_of_user(self, rows):   # show the information which admin inputs

        print("-------------------------")
        print("All User's Information: ")
        print("-------------------------")
        for row in rows:
            print()
            print("Information about", row[1])
            print("---------------------------------------")
            print("User Id: ", row[0])
            print("User Name: ", row[1])
            print("Email Address: ", row[2])
            print("Password: ", row[3])
            print("Address: ", row[4])
            print("Phone Number: ", row[5])

    def admin_output(self, row):
        print("-------------------------")
        print("Information of", row[1])
        print("-------------------------")
        print("User Id: ", row[0])
        print("User Name: ", row[1])
        print("Email Address: ", row[2])
        print("Password: ", row[3])
        print("Address: ", row[4])
        print("Phone Number: ", row[5])
