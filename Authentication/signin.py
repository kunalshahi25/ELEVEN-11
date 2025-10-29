import json
from colorama import Fore
import getpass
from Validation.validations import admin_staff_ask, note_validation
from Authentication.signup import SignUp
from Model.restraunt_model import AdminDashboard
from Model.restraunt_model import StaffDashboard

path = r"E:\ELEVEN-11\Database\UserAuth.json"
sign_up = SignUp()

class SignIn:
    def SignInFunc(self):
        while(True):
            ob = admin_staff_ask()
            output = ob.admin_staff_position_choice()

            if output in [1, 2]:
                role = "admin" if output == 1 else "staff"

                with open(path, 'r') as file:
                    data = json.load(file)

                if not data:
                    print(Fore.RED +"No users found! Please Sign Up first.")
                    return

                user_name = input(f"Enter {role.capitalize()} Username: ")
                Pass_word = getpass.getpass(f"Enter {role.capitalize()} Password: ")

                found = False
                for record in data:
                    if role in record:
                        for person in record[role]:
                            if (person["username"] == user_name and 
                                person["password"] == Pass_word):
                                print(Fore.GREEN + f"\n {role.capitalize()} Sign In Successful!\n")
                                found = True
                                # this will redirect to the dashboard
                                if role == "admin":
                                    AdminDashboard().admin_menu()
                                else:
                                    StaffDashboard().staff_menu()
                                break
                    if found:
                        break

                if not found:
                    print(Fore.RED +"Invalid Username or Password.")
                    return

            elif output == 3:
                print(Fore.YELLOW + "Want To Add New Staff Member *_* .....")
                break
            else:
                note_validation()
