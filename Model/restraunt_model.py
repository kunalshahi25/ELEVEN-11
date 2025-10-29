from colorama import Fore, Style, init
import time
import json
import os
import uuid
import datetime
from Validation.table_booking import TableBooking
from Model.report_section import ReportSection

init(autoreset=True)

path = r"E:\ELEVEN-11\Database\Menu.json"


class RestrauntMenu:
    def __init__(self):
        # Default categorized menu
        self.NewMenuList = [
            # Breakfast
            {"itemcode": 1, "name": "Aloo Paratha", "half": 50, "full": "", "category": "Breakfast"},
            {"itemcode": 2, "name": "Paneer Paratha", "half": 70, "full": "", "category": "Breakfast"},
            {"itemcode": 3, "name": "Plain Paratha", "half": 40, "full": "", "category": "Breakfast"},
            {"itemcode": 4, "name": "Aloo Pyaz Paratha", "half": 70, "full": "", "category": "Breakfast"},

            # Lunch
            {"itemcode": 5, "name": "Dal Fry", "half": 70, "full": 140, "category": "Lunch"},
            {"itemcode": 6, "name": "Dal Makhani", "half": 80, "full": 150, "category": "Lunch"},
            {"itemcode": 7, "name": "Rajma Chawal", "half": 80, "full": 150, "category": "Lunch"},
            {"itemcode": 8, "name": "Kadi Chawal", "half": 80, "full": 150, "category": "Lunch"},
            {"itemcode": 9, "name": "Mix Veg", "half": 90, "full": 170, "category": "Lunch"},
            {"itemcode": 10, "name": "Aalo Jeera", "half": 60, "full": 120, "category": "Lunch"},

            # Dinner
            {"itemcode": 11, "name": "Paneer Lababdaar", "half": 90, "full": 170, "category": "Dinner"},
            {"itemcode": 12, "name": "Butter Paneer", "half": 80, "full": 150, "category": "Dinner"},
            {"itemcode": 13, "name": "Paneer Do Pyaza", "half": 80, "full": 150, "category": "Dinner"},
            {"itemcode": 14, "name": "Egg Curry", "half": 80, "full": 150, "category": "Dinner"},
            {"itemcode": 15, "name": "Chaap", "half": 80, "full": 150, "category": "Dinner"},
            {"itemcode": 16, "name": "Kadhai Chicken", "half": 200, "full": 400, "category": "Dinner"},
            {"itemcode": 17, "name": "Butter Chicken", "half": 210, "full": 420, "category": "Dinner"},

            # Starters
            {"itemcode": 18, "name": "White Sauce Pasta", "half": 100, "full": 190, "category": "Starters"},
            {"itemcode": 19, "name": "Red Sauce Pasta", "half": 100, "full": 190, "category": "Starters"},
            {"itemcode": 20, "name": "Mix Sauce Pasta", "half": 100, "full": 190, "category": "Starters"},
            {"itemcode": 21, "name": "11:11 Special Chicken", "half": 150, "full": 300, "category": "Starters"},
            
            #thali
            {"itemcode": 22, "name": "Veg Thali", "half": 100, "full": "", "category": "Thali"},
            {"itemcode": 23, "name": "Paneer Thali", "half": 120, "full": "", "category": "Thali"},
            {"itemcode": 24, "name": "Paneer Thali + Coke", "half": 140, "full": "", "category": "Thali"},
            {"itemcode": 25, "name": "Chicken Thali", "half": 150, "full": "", "category": "Thali"},
            {"itemcode": 26, "name": "Chicken Thali + Coke", "half": 170, "full": "", "category": "Thali"},
            {"itemcode": 27, "name": "Mutton Thali", "half": 200, "full": "", "category": "Thali"},
            {"itemcode": 28, "name": "Mutton Thali + Coke", "half": 220, "full": "", "category": "Thali"},
        ]

        
        
        try:
            with open(path, "r") as file:
                content = file.read().strip()
                if content:
                    self.MenuList = json.loads(content)

                else:
                    self.MenuList = self.NewMenuList
                    self.save_menu()
                    
        except (FileNotFoundError, json.JSONDecodeError):
            self.MenuList = self.NewMenuList
            self.save_menu()


    def save_menu(self):
        """Save updated menu to JSON file"""
        with open(self.path, "w") as file:
            json.dump(self.MenuList, file, indent=4)


    def add_item(self):
        add_item_dict = {}
        add_item_dict["itemcode"] = int(input("Enter Item Code: "))
        add_item_dict["name"] = input("Enter Item Name: ")
        add_item_dict["half"] = int(input("Enter Half Plate Price: "))
        full_price = input("Enter Full Plate Price (press Enter if not applicable): ")
        add_item_dict["full"] = int(full_price) if full_price else ""

        print("\nSelect Category:")
        print("1. Breakfast\n2. Lunch\n3. Dinner\n4. Starters\n5. Thali")
        cat_choice = input("Enter choice: ")
        categories = {"1": "Breakfast", "2": "Lunch", "3": "Dinner", "4": "Starters", "5": "Thali"}
        add_item_dict["category"] = categories.get(cat_choice, "Lunch")

        self.MenuList.append(add_item_dict)
        self.save_menu()
        print(Fore.GREEN + "Item added successfully!\n")


    def update_item(self):
        item_code = int(input("Enter the Item Code to update: "))
        for item in self.MenuList:
            if item["itemcode"] == item_code:
                print(Fore.YELLOW + f"Editing {item['name']}...")
                item["name"] = input("Enter New Name: ") or item["name"]
                item["half"] = int(input("Enter New Half Price: ") or item["half"])
                full_val = input("Enter New Full Price: ") or item["full"]
                item["full"] = int(full_val) if full_val else item["full"]

                print("\nSelect New Category (press Enter to skip):")
                print("1. Breakfast\n2. Lunch\n3. Dinner\n4. Starters\n5. Thali")
                cat_choice = input("Enter choice: ")
                if cat_choice in ["1", "2", "3", "4", "5"]:
                    categories = {"1": "Breakfast", "2": "Lunch", "3": "Dinner", "4": "Starters", "5": "Thali"}
                    item["category"] = categories[cat_choice]

                self.save_menu()
                print(Fore.GREEN + "Item updated successfully!\n")
                return
        print(Fore.RED + "Item not found!\n")


    def delete_item(self):
        item_code = int(input("Enter the Item Code to delete: "))
        for item in self.MenuList:
            if item["itemcode"] == item_code:
                self.MenuList.remove(item)
                self.save_menu()
                print(Fore.GREEN + "Item deleted successfully!\n")
                return
        print(Fore.RED + "Item not found!\n")


    def show_menu(self):
        if not self.MenuList:
            print(Fore.RED + "No items available in the menu!")
            self.save_menu()
            return

        print(Fore.MAGENTA + " " +"-" * 60)
        print(Fore.RED + Style.BRIGHT + "|           🍽️  WELCOME TO ELEVEN : 11 RESTAURANT  🍽️          |")
        print(Fore.MAGENTA +" " + "-" * 60)

        categories = ["Breakfast", "Lunch", "Dinner", "Starters", "Thali"]
        for cat in categories:
            print(Fore.CYAN + f"\n                   --- {cat.upper()} ---")
            print(Fore.YELLOW + f"{'Item No.':<10}{'Name':<35}{'Half(₹)':<10}{'Full(₹)':<10}")
            print(Fore.MAGENTA + "-" * 62)
            for item in self.MenuList:
                if item["category"].lower() == cat.lower():
                    print(Fore.LIGHTWHITE_EX + f"{item['itemcode']:<10}{item['name']:<35}{item['half']:<10}{item['full']:<10}")
            time.sleep(0.1)
        
        print(Fore.MAGENTA + "-" * 62)
        print(Fore.CYAN + Style.BRIGHT + "Chef's Special: Try our signature Paneer Lababdaar & 11:11 Special Chicken !")    


    def search_by_price(self):
        try:
            max_price = float(input("Enter maximum half-plate price: ₹"))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
            return

        found = [i for i in self.MenuList if i["half"] <= max_price]
        if found:
            print(Fore.CYAN + f"\nItems priced below ₹{max_price}:")
            for i in found:
                print(Fore.LIGHTYELLOW_EX + f"{i['itemcode']:<10} | {i['name']:<35} | Half ₹{i['half']:<10} | Full ₹{i['full']:<10} | {i['category']}")
        else:
            print(Fore.RED + f"\nNo items found below ₹{max_price}.\n")


class OrderSystem:
    def __init__(self):
        with open(path, "r") as f:
            self.menu = json.load(f)
        self.order_items = []
        self.total_amount = 0

    def take_order(self):
        """Allow staff to take an order from the menu"""
        print(Fore.CYAN + "\n------ TAKE ORDER ------")
        while True:
            try:
                item_code = int(input("Enter Item Code to order (0 to finish): "))
            except ValueError:
                print(Fore.RED + "Please enter a valid item code.")
                continue

            if item_code == 0:
                break

            # find item
            item = next((i for i in self.menu if i["itemcode"] == item_code), None)
            if not item:
                print(Fore.RED + "Item not found! Please try again.")
                continue

            print(Fore.YELLOW + f"Selected: {item['name']}")
            size_choice = input("Half (H) or Full (F): ").strip().upper()
            if size_choice == "H" and item["half"] != "":
                price = float(item["half"])
            elif size_choice == "F" and item["full"] != "":
                price = float(item["full"])
            else:
                print(Fore.RED + "Invalid choice or size not available.")
                continue

            try:
                quantity = int(input("Enter Quantity: "))
            except ValueError:
                print(Fore.RED + "Please enter a valid quantity.")
                continue

            total_price = price * quantity
            self.order_items.append({
                "name": item["name"],
                "size": "Half" if size_choice == "H" else "Full",
                "price": price,
                "qty": quantity,
                "total": total_price
            })
            self.total_amount += total_price

            print(Fore.GREEN + f"Added {quantity} x {item['name']} ({size_choice}) = ₹{total_price}\n")

        if not self.order_items:
            print(Fore.YELLOW + "No items ordered.\n")
        else:
            print(Fore.GREEN + "Order Taken Successfully!")

    

class Order(OrderSystem):
    

    def add_item(self, name, size, qty, price):
        total = qty * price
        self.order_items.append({
            "name": name,
            "size": size,
            "qty": qty,
            "price": price,
            "total": total
        })
        self.total_amount += total

    def generate_bill(self):
        bill_path = r"E:\ELEVEN-11\Database\Bills.json"
        os.makedirs(os.path.dirname(bill_path), exist_ok=True)

        subtotal = self.total_amount
        gst = round(subtotal * 0.05, 2)
        net_total = round(subtotal + gst, 2)

        bill_data = {
            "bill_id": uuid.uuid4().hex[:6].upper(),
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": self.order_items,
            "subtotal": subtotal,
            "gst": gst,
            "net_total": net_total
        }

        # load existing bills 
        if os.path.exists(bill_path):
            with open(bill_path, "r") as f:
                try:
                    bills = json.load(f)
                except json.JSONDecodeError:
                    bills = []
        else:
            bills = []

        # adding new bill 
        bills.append(bill_data)

        with open(bill_path, "w") as f:
            json.dump(bills, f, indent=4)

        print(Fore.YELLOW + f"-"*42)
        print(Fore.RED + "============== Eleven:11 BILL =============")
        print(Fore.YELLOW + f"-"*42)
        print(Fore.GREEN + f"Bill ID: {bill_data['bill_id']}")
        print(Fore.GREEN + f"Date: {bill_data['date']}")
        print(Fore.YELLOW + f"-"*42)
        for item in bill_data["items"]:
            print(Fore.GREEN + f"{item['name']} ({item['size']}) x{item['qty']} = ₹{item['total']}")
        print(Fore.YELLOW + f"-"*42)
        print(Fore.GREEN + f"Subtotal: ₹{subtotal}")
        print(Fore.GREEN + f"GST (5%): ₹{gst}")
        print(Fore.GREEN + f"Net Total: ₹{net_total}")
        print(Fore.YELLOW + f"-"*42)
        print(Fore.YELLOW + "Thank You For Visiting Eleven:11  (*_*)  Visit Again..")
        print(Fore.YELLOW + f"-"*42)
        

class AdminDashboard:
    def admin_menu(self):
        report=ReportSection()
        menu = RestrauntMenu()
        generatebill=Order()
        booking = TableBooking()
        while True:
            print(Fore.LIGHTCYAN_EX + "\n========= ADMIN DASHBOARD =========")
            print(Fore.MAGENTA + "1.  Add Menu Item")
            print(Fore.MAGENTA + "2.  Update Menu Item")
            print(Fore.MAGENTA + "3.  Delete Menu Item")
            print(Fore.MAGENTA + "4.  View All Menu Items")
            print(Fore.MAGENTA + "5.  Search Item by Price")
            print(Fore.MAGENTA + "6.  Take Order")
            print(Fore.MAGENTA + "7.  Generate Bill")
            print(Fore.MAGENTA + "8.  Table Booking")
            print(Fore.MAGENTA + "9.  Report")
            print(Fore.MAGENTA + "10. Logout")
            print(Fore.LIGHTCYAN_EX + "===================================")

            choice = input("Enter your choice: ")

            if choice == '1':
                try:
                    menu.add_item()
                except Exception:
                    print(Fore.RED +"Some Technical Issue Occurred! Sorry For this Inconvenience.")
            elif choice == '2':
                try:
                    menu.update_item()
                except Exception:
                    print(Fore.RED +"Some Technical Issue Occurred! Sorry For this Inconvenience.")
            elif choice == '3':
                try:
                    menu.delete_item()
                except Exception:
                    print(Fore.RED +"Some Technical Issue Occurred! Sorry For this Inconvenience.")
            elif choice == '4':
                try:
                    menu.show_menu()
                except Exception:
                    print(Fore.RED +"Some Technical Issue Occurred! Sorry For this Inconvenience.")
            elif choice == '5':
                try:
                    menu.search_by_price()    
                except Exception:
                    print(Fore.RED +"Some Technical Issue Occurred! Sorry For this Inconvenience.")
            elif choice == '6':
                try:
                    generatebill.take_order()
                except Exception:
                    print(Fore.RED +"Some Technical Issue Occurred! Sorry For this Inconvenience.")
            elif choice == '7':
                try:
                    generatebill.generate_bill()
                except Exception:
                    print(Fore.RED +"Some Technical Issue Occurred! Sorry For this Inconvenience.")
            elif choice == '8':
                while(True):
                    print(Fore.CYAN + "\n--- TABLE BOOKING ---")
                    print(Fore.BLUE + "1. View Available Tables")
                    print(Fore.BLUE + "2. Book a Table")
                    print(Fore.BLUE + "3. Cancel Bookings")
                    print(Fore.BLUE + "4. View Bookings")
                    print(Fore.BLUE + "5. Exit")
                    sub = input(Fore.CYAN + "Enter choice: ")
                    try:
                        if sub == '1':
                            booking.show_available_tables()
                        elif sub == '2':
                            booking.book_table()
                        elif sub == '3':
                            booking.cancel_booking()
                        elif sub == '4':
                            booking.view_bookings()
                        elif sub == '5':
                            break
                        else:
                            print("Invalid choice.")
                    except Exception:
                        print(Fore.RED +"Some Technical Issue Occurred! Sorry For this Inconvenience.")
            
            elif choice == '9':
                try:
                    report.show_report()
                    
                except Exception:
                    print(Fore.RED +"Some Technical Issue Occurred! Sorry For this Inconvenience.")
                
            elif choice == '10':
                print(Fore.YELLOW + "Logging out...")
                break
            else:
                print(Fore.RED + "Invalid choice. Try again.")


class StaffDashboard:
    def staff_menu(self):
        menu = RestrauntMenu()
        # takeorder=OrderSystem()
        generatebill=Order()
        booking = TableBooking()
        while True:
            print(Fore.LIGHTCYAN_EX +"\n========= STAFF DASHBOARD =========")
            print(Fore.MAGENTA + "1. View Menu")
            print(Fore.MAGENTA + "2. Take Order")
            print(Fore.MAGENTA + "3. Generate Bill")
            print(Fore.MAGENTA + "4. Search Item Below Price")
            print(Fore.MAGENTA + "5. Table Booking")
            print(Fore.MAGENTA + "6. Logout")
            print(Fore.LIGHTCYAN_EX + "===================================") 

            choice = input(Fore.LIGHTCYAN_EX +"Enter your choice: ")

            if choice == '1':
                try:
                    menu.show_menu()
                except Exception:
                    print(Fore.RED + "Some Technical Issue Occurred! Sorry For this Inconvenience.")
     
            elif choice == '2':
                try:
                    generatebill.take_order()
                except Exception:
                    print(Fore.RED +"Some Technical Issue Occurred! Sorry For this Inconvenience.")
            
            elif choice == '3':
                try:
                    generatebill.generate_bill()
                except Exception:
                    print(Fore.RED + "Some Technical Issue Occurred! Sorry For this Inconvenience.")
                
            elif choice == '4':
                try:
                    menu.search_by_price()
                except Exception:
                    print(Fore.RED + "Some Technical Issue Occurred! Sorry For this Inconvenience.")
            elif choice == '5':
                print(Fore.CYAN + "\n--- TABLE BOOKING ---")
                print(Fore.BLUE + "1. View Available Tables")
                print(Fore.BLUE + "2. Book a Table")
                print(Fore.BLUE + "3. View Bookings")
                sub = input(Fore.CYAN + "Enter choice: ")
                try:
                    if sub == '1':
                        booking.show_available_tables()
                    elif sub == '2':
                        booking.book_table()
                    elif sub == '3':
                        booking.view_bookings()
                    else:
                        print("Invalid choice.")
                except Exception:
                    print(Fore.RED +"Some Technical Issue Occurred! Sorry For this Inconvenience.")
                
            elif choice == '6':
                print(Fore.YELLOW + "Logging out...")
                break
            else:
                print(Fore.RED + "Invalid choice. Try again.")
