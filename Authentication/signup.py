import uuid
import getpass
from colorama import Fore
import os
import sys
import json
sys.path.append(os.getcwd())
path = r"E:\ELEVEN-11\Database\UserAuth.json"

# from Validation.validations import password_validation
class SignUp():
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
        
        admin_staff_dict={}
        admin_staff_list=[]
        admin_dict={}
        admin_dict["id"]=uuid.uuid4().hex[:5]
        admin_dict["fname"] = self.get_required_input("Please Enter Your First Name: ")
        admin_dict["lname"] = input("Please Enter Your Last Name: ")
        admin_dict["address"] = self.get_required_input("Please Enter Your Current Address: ")
        admin_dict["contact"] = self.get_required_input("Please Enter Your Contact Number: ")
        email = self.get_required_input("Please Enter Your Email: ")
        
        if "@" not in email or ".com" not in email:
            print(Fore.RED + "Invalid email format.")
            for i in range(3):
                print(Fore.RED + f"You Have {3-i} Attempts left..")
                email = self.get_required_input("Please Enter Your Email: ")
                if "@" not in email or ".com" not in email:
                    print(Fore.RED + "Invalid email format.")
                else:
                    break
            
        admin_dict["email"] = email
        
        qualification_list=[]
        qualification_dict={}
        admin_dict["qualification"]=qualification_list
        
        qualification_dict["highest_qualification"]=self.get_required_input("Enter Your Highest Qualification: ")
        qualification_dict["passing_year"]=int(self.get_required_input("Enter Passing year: "))
        for i in range(10):
            more_qualification=input("Do You Want to Add More Qualifications? \'Yes' or \'No\'\n").title()
            if more_qualification=="Yes":
                qualification_dict[f"qualification_name{i+1}"]=self.get_required_input("Enter Qualification Name: ")
                qualification_dict[f"passing_year{i+1}"]=self.get_required_input("Enter Qualification Passing Year: ")
            elif more_qualification == "No":
                break
            else:
                print("Enter Only \'Yes\' or \'No\'")  
          
        qualification_list.append(qualification_dict)
        admin_dict["experience"]=self.get_required_input("Please Enter Your Work Experince: ")
        
        #username function
        username = self.username_validation()
        admin_dict["username"]=username

        password = self.password_validation()
        admin_dict["password"]=password

        admin_staff_list.append(admin_dict)
        admin_staff_dict["staff"] =admin_staff_list
        with open(path, "r") as file:
            content = file.read().strip()  
            if content:
                signup_data_list = json.loads(content)
            else:
                signup_data_list = []
        signup_data_list.append(admin_staff_dict)
        with open(path, 'w') as file:
            json.dump(signup_data_list, file, indent=4)

            
    def username_validation(self):
        username=self.get_required_input("Please Enter Username: ")
        
        for attempt in range(3):

            if username.startswith("0"):
                print(Fore.RED + "Username should NOT start with '0'.")
                print(Fore.RED + f"You have {3 - attempt} attempts left.")
                username = self.get_required_input("Please Enter Username: ")
                continue

            if username.count("0") > 2:
                print(Fore.RED + "Username can contain a maximum of 2 zeros.")
                print(Fore.RED + f"You have {3 - attempt} attempts left.")
                username = self.get_required_input("Please Enter Username: ")
                continue
            break #if all validation are correct than break
        
        else:
            print(Fore.RED + "Too many invalid attempts! Exiting...")
            exit()
        return username
    
    def password_validation(self):
        special_chars = ['!', '@', '#', '&', '*', '(', ')', '-', '_', '=', '+', '?', '[', ']']

        for attempt in range(3):
            password = self.get_required_password("Please Enter Password: ")
            confirm_password = self.get_required_password("Confirm Password: ")

            has_zero = '0' in password
            has_special = any(ch in special_chars for ch in password)

            if has_zero:
                print(Fore.RED + "Invalid password: should NOT contain '0'.")
                print(Fore.RED + f"You have {2 - attempt} attempts left.\n")
                continue
            
            if len(password) < 8:
                print(Fore.RED + "Invalid password: must be at least 8 characters long.")
                print(Fore.RED + f"You have {2 - attempt} attempts left.\n")
                continue
            
            if not has_special:
                print(Fore.RED + "Invalid password: must include at least one special character.")
                print(Fore.RED + f"You have {2 - attempt} attempts left.\n")
                continue
            
            if password != confirm_password:
                print(Fore.RED + "Passwords do not match!")
                print(Fore.RED + f"You have {2 - attempt} attempts left.\n")
                continue

            print(Fore.GREEN + "Sign up Successful..")
            break
            
        else:
            print("Too many invalid attempts. Exiting...")
            exit()
        return password
    