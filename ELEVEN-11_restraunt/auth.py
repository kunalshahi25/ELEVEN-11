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

while True:
    print("\n --------------------------------------------")
    print("| (+_+)     Welcome To ELEVEN : 11     (*_*) |")
    print(" --------------------------------------------")

    ch = choice()
    ch_output = ch.menu_choice()

    if ch_output == 1:  # Sign Up
        
        ob.sign_up_function_staff()

    elif ch_output == 2:  # Sign In
        SI.SignInFunc()

    elif ch_output == 3:  # Exit
        print(Fore.YELLOW + Style.BRIGHT + "Thank you for visiting ELEVEN : 11 Restaurant!\n")
        break

    else:
        note_validation()
