import uuid
import getpass
import os
import sys
import json
sys.path.append(os.getcwd())
path = r"E:\ELEVEN-11\ELEVEN-11_restraunt\Database\UserAuth.json"

# from Validation.validations import password_validation
class SignUp():
    def sign_up_function_staff(self):
        admin_staff_dict={}
        admin_staff_list=[]
        admin_dict={}
        admin_dict["id"]=uuid.uuid4().hex[:5]
        admin_dict["fname"]=input("Please Enter Your First Name: ")
        admin_dict["lname"]=input("Please Enter Your Last Name: ")
        admin_dict["address"]=input("Please Enter Your Current Address: ")
        admin_dict["contact"]=input("Please Enter Your Contact Number: ")
        
        qualification_list=[]
        qualification_dict={}
        admin_dict["qualification"]=qualification_list
        
        qualification_dict["highest_qualification"]=input("Enter Your Highest Qualification: ")
        qualification_dict["passing_year"]=int(input("Enter Passing year: "))
        for i in range(10):
            more_qualification=input("Do You Want to Add More Qualifications? \'Yes' or \'No\'\n")
            if more_qualification=="Yes":
                qualification_dict[f"qualification_name{i+1}"]=input("Enter Qualification Name: ")
                qualification_dict[f"passing_year{i+1}"]=input("Enter Qualification Passing Year: ")
            elif more_qualification == "No":
                break
            else:
                print("Enter Only \'Yes\' or \'No\'")  
          
        qualification_list.append(qualification_dict)
        admin_dict["experience"]=input("Please Enter Your Work Experince: ")
        
        username=input("Please Enter Username: ")
        for i in username:
            if i == '0':
                print("Username should Not contain Zero.")
                exit()
        admin_dict["username"]=username

        password = getpass.getpass("Please Enter Password: ")
        confirm_password = getpass.getpass("Confirm Password: ")

        special_chars = ['!', '@', '#', '&', '*', '(',')', '-', '_', '=', '+', '?', '[', ']']

        has_special = False
        has_zero = False

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


