from View.view import View                     # import user view to access methods of View class
from Controller.controller import Controller
from Model.model import Model


# This is main class to control all the other classes and login as admin or user
class Main:
    def __init__(self):
        pass

    def user_or_admin(self):
        user_login = input("Login As (admin/user): ")
        if user_login == "admin":  # if user input admin, it opens as admin panel and input user, it opens as user panel
            control_obj.admin_validate_control()

        elif user_login == "user":  # for normal user
            control_obj.user_control()

        else:
            print('Enter "admin" for Admin and "user" for Normal User')


main_obj = Main()
view_obj = View()
control_obj = Controller()
model_obj = Model()
main_obj.user_or_admin()
