from Model.model import Model
from View.view import View


class Controller:
    def __init__(self):
        self.aid = None
        self.um_obj = Model()
        self.uv_obj = View()

    def admin_validate_control(self):
        admin_login = self.uv_obj.admin_login()
        email = admin_login[0]
        password = admin_login[1]
        #print(email)
        #print(password)

        # calling admin_validate method of Model class for admin
        data = self.um_obj.admin_validate(email, password)
        self.aid = data[0]
        em = data[1]
        pw = data[2]
        #print(aid, em, pw)

        if email == em and password == pw:  # admin validation
            admin_session = em
            print("---------------------------")
            print("Welcome To Admin Panel!")
            print("---------------------------")

            self.admin_control()         # if admin user name and password is correct,
                                        # it calls user_input() method to input data
        else:
            print("Incorrect UserName and Password!")

    def user_validate_control(self):
        user_login = self.uv_obj.user_login()
        email = user_login[0]
        password = user_login[1]
        # print(email, password)

        # calling admin_validate method of Model class for admin
        data = self.um_obj.user_validate(email, password)
        uid = data[0]
        ema = data[1]
        pwa = data[2]
        # print(ema, pwa)

        if email == ema and password == pwa:    # if true call user_input() method
            user_session = ema
            print("---------------------------")
            print("Welcome To User Panel!")
            print("---------------------------")
            user_data = self.um_obj.user_data_show(uid)
            self.uv_obj.user_output(user_data)
            edit = input("Do you want to edit (yes/no)?")
            if edit == "yes":
                edit_data = self.uv_obj.user_edit(user_data)
                update_user = self.um_obj.update_user(edit_data, uid)
                print(update_user)
            else:
                pass

        else:
            print("Incorrect UserName and Password! ")

    def admin_control(self):  # to control which action admin's can perform edit, delete or show
        print("""Hint:
        To View all Users Data: enter "show users"
        To View Your Own Data: enter "show"
        To Edit: enter "edit"
        To Delete User: enter "delete"
        """)
        mode = input("Which action you want to perform (Retrieve/Edit/Delete )? ")
        if mode == "edit":
            admin_data = self.um_obj.admin_data_show(self.aid)
            edit_data = self.uv_obj.user_edit(admin_data)
            update_admin = self.um_obj.update_admin(edit_data, self.aid)
            print(update_admin)
        elif mode == "delete":
            delete_name = self.uv_obj.delete_user_data()
            delete = self.um_obj.delete_user_by_admin(delete_name)
            print(delete)
        elif mode == "show users":
            user_rows = self.um_obj.all_user_data_for_admin()
            self.uv_obj.admin_output_of_user(user_rows)
        elif mode == "show":
            admin_row = self.um_obj.admin_data_show(self.aid)
            self.uv_obj.admin_output(admin_row)
        else:
            print("Wrong Instruction!")

    def user_control(self):
        print("""Hint: To Sign Up: enter "sign up" 
        To Login: enter "login"
        """)
        mode = input("Which action you want to perform (Sign Up/Login)? ")
        if mode == "sign up":
            user_input = self.uv_obj.user_input()
            add_db = self.um_obj.add_to_user_db(user_input)
            print(add_db)
        elif mode == "login":
            self.user_validate_control()
        else:
            print("Enter sign up to Sign Up for  new user and enter login to LogIn for exist user.")
