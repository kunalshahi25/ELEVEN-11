special_chars = ['!', '@', '#', '&', '*', '(', ')', '-', '_', '=', '+', '?', '[', ']']
password = input("Please Enter Password: ")
confirm_password = input("Confirm Password: ")
    
for attempt in range(3):
    

    has_zero = '0' in password
    has_special = any(ch in special_chars for ch in password)

    # --- Validation checks ---
    if has_zero:
        print("Invalid password: should NOT contain '0'.")
        print(f"You have {3 - attempt} attempts left.\n")
        password = input("Please Enter Password: ")
        confirm_password = input("Confirm Password: ")
        continue

    if len(password) < 8:
        print("Invalid password: must be at least 8 characters long.")
        print(f"You have {3 - attempt} attempts left.\n")
        password = input("Please Enter Password: ")
        confirm_password = input("Confirm Password: ")
        continue

    if not has_special:
        print("Invalid password: must include at least one special character.")
        print(f"You have {3 - attempt} attempts left.\n")
        continue

    if password != confirm_password:
        print("Passwords do not match!")
        print(f"You have {3 - attempt} attempts left.\n")
        password = input("Please Enter Password: ")
        confirm_password = input("Confirm Password: ")
        continue

    # --- If all checks passed ---
    print("Sign up Successful ✅")
    break

else:
    print("Too many invalid attempts. Exiting...")
