import uuid
import getpass
from colorama import Fore
import os
import json

path = r"E:\ELEVEN-11\Database\UserAuth.json"

class SignUp:
    def get_required_input(self,prompt_text):
        while True:
            value = input(prompt_text).strip()
            if value:
                return value
            else:
                print(Fore.RED + "This field is mandatory. Please enter a value.")

    def get_required_password(self,prompt_text):
        while True:
            password = getpass.getpass(prompt_text).strip()
            if password:
                return password
            else:
                print(Fore.RED + "Password cannot be blank. Please enter a value.")

    def sign_up_function_staff(self):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.exists(path):
            with open(path, 'w') as f:
                json.dump([], f)

        admin_dict={}
        admin_dict["id"]=uuid.uuid4().hex[:5]
        admin_dict["fname"] = self.get_required_input(Fore.LIGHTCYAN_EX + "Please Enter Your First Name: ")
        admin_dict["lname"] = self.get_required_input(Fore.LIGHTCYAN_EX + "Please Enter Your Last Name: ")
        admin_dict["address"] = self.get_required_input(Fore.LIGHTCYAN_EX + "Please Enter Your Current Address: ")
        admin_dict["contact"] = self.get_required_input(Fore.LIGHTCYAN_EX + "Please Enter Your Contact Number: ")
        email = self.get_required_input(Fore.LIGHTCYAN_EX + "Please Enter Your Email: ")

        if "@" not in email or ".com" not in email:
            print(Fore.RED + "Invalid email format.")
            exit()
        admin_dict["email"] = email

        qualification_list = []
        highest = input("Enter Your Highest Qualification: ")
        year = input("Enter Passing year: ")
        qualification_list.append({"qualification": highest, "year": year})

        while True:
            more = input("Do you want to add more qualifications? (Yes/No): ").lower()
            if more == "yes":
                qname = input("Enter Qualification Name: ")
                qyear = input("Enter Qualification Passing Year: ")
                qualification_list.append({"qualification": qname, "year": qyear})
            elif more == "no":
                break
            else:
                print(Fore.RED + "Enter only 'Yes' or 'No'.")

        admin_dict["qualification"] = qualification_list
        admin_dict["experience"] = input("Please Enter Your Work Experience: ")

        username = self.get_required_input("Please Enter Username: ")
        if '0' in username:
            print(Fore.RED + "Username should not contain '0'.")
            exit()
        admin_dict["username"] = username

        special_chars = ['!', '@', '#', '&', '*', '(', ')', '-', '_', '=', '+', '?', '[', ']']
        password = self.get_required_password("Please Enter Password: ")
        confirm_password = self.get_required_password("Confirm Password: ")

        if '0' in password or len(password) < 8:
            print(Fore.RED + "Invalid password: should not contain '0' and should not be less than 8 characters.")
            exit()

        if not any(ch in special_chars for ch in password):
            print(Fore.RED + "Invalid password: must include at least one special character.")
            exit()

        if password != confirm_password:
            print(Fore.RED + "Passwords do not match!")
            exit()

        admin_dict["password"] = password
        print(Fore.GREEN + "Sign Up Successful!")

        with open(path, 'r+') as f:
            data = json.load(f)
            data.append(admin_dict)
            f.seek(0)
            json.dump(data, f, indent=4)
            