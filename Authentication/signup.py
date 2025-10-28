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
        special_chars = ['!', '@', '#', '&', '*', '(',')', '-', '_', '=', '+', '?', '[', ']']

        has_special = False
        has_zero = False
        
        admin_staff_dict={}
        admin_staff_list=[]
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
        
        username=input("Please Enter Username: ")
        for i in username:
            if i == '0':
                print("Username should Not contain Zero.")
                exit()
        admin_dict["username"]=username

        password = self.get_required_password("Please Enter Password: ")
        confirm_password = self.get_required_password("Confirm Password: ")

        for ch in password:
            if ch == '0':
                has_zero = True
            if ch in special_chars:
                has_special = True

        if has_zero or len(password) < 8:
            print("Invalid password: should not contain '0' and should not be less than 8 characters.")
            exit()
        elif not has_special:
            print("Invalid password: must include at least one special character")
            exit()
            

        elif password != confirm_password:
            print("Passwords do not match! Please try again.")
            return
        else: 
            admin_dict["password"]=password
            print(Fore.GREEN + "Sign up Successfull... ")
        admin_staff_list.append(admin_dict)
        admin_staff_dict["staff"] =admin_staff_list
        with open(path, "r") as file:
            content = file.read().strip()  
            if content:
                signup_data_list = json.loads(content)
            else:
                signup_data_list = []
        signup_data_list.append(admin_staff_dict)
        with open(path,'w') as file:
            file.write(json.dumps(signup_data_list))