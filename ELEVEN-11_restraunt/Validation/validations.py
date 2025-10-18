
class choice:
    def menu_choice(self):
        print("1. \'Sign Up\' \n2. \'Sign In\' \n3. \'Exit\'")
        choice = int(input("Enter your choice: "))
        return choice
class admin_staff_ask:
    def admin_staff_position_choice(self):
        print("1. \'Admin\'\n2. \'Staff\' \n3. \'Exit\'")
        position_choice = int(input("Give Your Position?\n"))
        return position_choice

def note_validation():
    print("Number not Matched ! Please Enter Correct Option!")

def menu_choice():
    print("1. \'View Menu\' \n2. \'Search Menu\' \n3. \'Search By Price\'\n2. \'Exit\'") 