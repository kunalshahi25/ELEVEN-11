from colorama import Fore

class choice:
    def menu_choice(self):
        print(Fore.MAGENTA + "1. \'Sign Up\' \n2. \'Sign In\' \n3. \'Exit\'")
        choice = int(input(Fore.CYAN + "Enter your choice: "))
        return choice
class admin_staff_ask:
    def admin_staff_position_choice(self):
        print(Fore.MAGENTA + "1. \'Admin\'\n2. \'Staff\' \n3. \'Exit\'")
        position_choice = int(input(Fore.CYAN + "Give Your Position?\n"))
        return position_choice

def note_validation():
    print("Number not Matched ! Please Enter Correct Option!")
