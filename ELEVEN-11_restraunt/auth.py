import os
import sys
from colorama import Fore, Style
sys.path.append(os.getcwd())

# from Model.restraunt_model import RestrauntModel
from Validation.validations import choice, admin_staff_ask, note_validation
from Authentication.signup import SignUp
from Authentication.signin import SignIn

ob = SignUp()
SI = SignIn()
class auth_main():
    while True:
        print(Fore.RED + Style.BRIGHT +"\n --------------------------------------------")
        print(Fore.YELLOW + Style.BRIGHT + "| (+_+)     Welcome To ELEVEN : 11     (*_*) |")
        print(Fore.RED + Style.BRIGHT +" --------------------------------------------")

        try:
            ch = choice()
            ch_output = ch.menu_choice()

            if ch_output == 1:  # sign up

                ob.sign_up_function_staff()

            elif ch_output == 2:  # sign in
                SI.SignInFunc()

            elif ch_output == 3:  # exit
                print(Fore.YELLOW + Style.BRIGHT + "Thank you for visiting ELEVEN : 11 Restaurant!\n")
                break
        except Exception:
            note_validation()
auth_main()