import os
import sys
from colorama import Fore, Style
sys.path.append(os.getcwd())

# from Model.restraunt_model import RestrauntModel
from Validation.validations import choice, admin_staff_ask, note_validation
from Authentication.signup import SignUp
from Authentication.signin import SignIn

sign_up_obj = SignUp()
sign_in_obj = SignIn()
class auth_main():
    while True:
        print(Fore.RED + Style.BRIGHT +"\n --------------------------------------------")
        print(Fore.YELLOW + Style.BRIGHT + "| (+_+)     Welcome To ELEVEN : 11     (*_*) |")
        print(Fore.RED + Style.BRIGHT +" --------------------------------------------")

        try:
            choice_obj = choice()
            choice_output = choice_obj.menu_choice()

            if choice_output == 1:  # sign up

                sign_up_obj.sign_up_function_staff()

            elif choice_output == 2:  # sign in
                sign_in_obj.SignInFunc()

            elif choice_output == 3:  # exit
                print(Fore.YELLOW + Style.BRIGHT + "Thank you for visiting ELEVEN : 11 Restaurant!\n")
                break
        except Exception:
            note_validation()
