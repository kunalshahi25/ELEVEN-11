from colorama import Fore, Style, init
import time
import json

init(autoreset=True)

path = r"E:\ELEVEN-11\ELEVEN-11_restraunt\Database\Menu.json"


# ==============================
# CLASS: RestrauntMenu
# ==============================
class RestrauntMenu:
    def __init__(self):
        self.NewMenuList = [
            {"itemcode":1,"name":"Paneer Lababdaar","half":90,"full":170},
            {"itemcode":2,"name":"Butter Paneer","half":80,"full":150},
            {"itemcode":3,"name":"Paneer Do Pyaza","half":80,"full":150},
            {"itemcode":4,"name":"Dal Fry","half":70,"full":140},
            {"itemcode":5,"name":"Dal Makhani","half":80,"full":150},
            {"itemcode":6,"name":"Rajma Fry","half":80,"full":150},
            {"itemcode":7,"name":"Kadi","half":70,"full":140},
            {"itemcode":8,"name":"Rajma Chawal","half":80,"full":150},
            {"itemcode":9,"name":"Aloo Paratha","half":50,"full":""},
            {"itemcode":10,"name":"Kadi Chawal","half":80,"full":150},
            {"itemcode":11,"name":"Egg Curry","half":80,"full":150},
            {"itemcode":12,"name":"Mix Veg","half":90,"full":170},
            {"itemcode":13,"name":"Aalo Jeera","half":60,"full":120},
            {"itemcode":14,"name":"White Sauce Pasta","half":100,"full":190},
            {"itemcode":15,"name":"Red Sauce Pasta","half":100,"full":190},
            {"itemcode":16,"name":"Mix Sauce Pasta","half":100,"full":190},
            {"itemcode":17,"name":"Chaap","half":80,"full":150},
            {"itemcode":18,"name":"Paneer Paratha","half":70,"full":""},
            {"itemcode":19,"name":"Plain Paratha","half":40,"full":""},
            {"itemcode":20,"name":"Aloo Pyaz Paratha","half":70,"full":""}
        ]

        # If menu.json is empty, add default items
        try:
            with open(path, "r") as file:
                content = file.read().strip()
                if content:
                    self.MenuList = json.loads(content)
                else:
                    self.MenuList = self.NewMenuList
                    self.save_menu()
        except FileNotFoundError:
            self.MenuList = self.NewMenuList
            self.save_menu()

    def save_menu(self):
        """Save updated menu to JSON file"""
        with open(path, "w") as file:
            json.dump(self.MenuList, file, indent=4)

    def add_item(self):
        """Add a new menu item"""
        add_item_dict = {}
        add_item_dict["itemcode"] = int(input("Enter Item Code: "))
        add_item_dict["name"] = input("Enter Item Name: ")
        add_item_dict["half"] = int(input("Enter Half Plate Price: "))
        full_price = input("Enter Full Plate Price (press Enter if not applicable): ")
        add_item_dict["full"] = int(full_price) if full_price else ""
        self.MenuList.append(add_item_dict)
        self.save_menu()
        print(Fore.GREEN + "Item added successfully!\n")

    def update_item(self):
        """Update an existing menu item"""
        item_code = int(input("Enter the Item Code to update: "))
        for item in self.MenuList:
            if item["itemcode"] == item_code:
                print(Fore.YELLOW + f"Editing {item['name']}...")
                item["name"] = input("Enter New Name: ") or item["name"]
                item["half"] = int(input("Enter New Half Price: ") or item["half"])
                item["full"] = input("Enter New Full Price: ") or item["full"]
                self.save_menu()
                print(Fore.GREEN + "Item updated successfully!\n")
                return
        print(Fore.RED + "1Item not found!\n")

    def delete_item(self):
        """Delete an item by item code"""
        item_code = int(input("Enter the Item Code to delete: "))
        for item in self.MenuList:
            if item["itemcode"] == item_code:
                self.MenuList.remove(item)
                self.save_menu()
                print(Fore.GREEN + "Item deleted successfully!\n")
                return
        print(Fore.RED + " Item not found!\n")

    def show_menu(self):
        """Show all items in a colorful format"""
        if not self.MenuList:
            print(Fore.RED + "No items available in the menu!")
            return

        print(Fore.RED + Style.BRIGHT + "\n|         🍽️  WELCOME TO ELEVEN : 11 RESTAURANT  🍽️         |")
        print(Fore.MAGENTA + "-" * 59)
        print(Fore.YELLOW + Style.BRIGHT + f"| {'Item No.':<10}{'Item Name':<25}{'Half (₹)':<10}{'Full (₹)':<10} |")
        print(Fore.MAGENTA + "-" * 59)

        for item in self.MenuList:
            name = item["name"]
            if "Paneer" in name:
                color = Fore.LIGHTGREEN_EX
            elif any(x in name for x in ["Dal", "Rajma", "Kadi"]):
                color = Fore.LIGHTYELLOW_EX
            elif "Paratha" in name:
                color = Fore.CYAN
            else:
                color = Fore.LIGHTWHITE_EX

            print(
                Fore.LIGHTMAGENTA_EX + f"| {item['itemcode']:<10}" +
                color + f"{item['name']:<25}" +
                Fore.LIGHTGREEN_EX + f"{item['half']:<10}" +
                Fore.LIGHTRED_EX + f"{item['full']:<10} |"
            )
            time.sleep(0.03)

        print(Fore.MAGENTA + "-" * 59)
        print(Fore.CYAN + Style.BRIGHT + "Chef's Special: Try our signature Paneer Lababdaar & Veg Biryani!")
        

    def search_by_price(self):
        """Search items below a given price"""
        try:
            max_price = float(input("Enter maximum half-plate price: ₹"))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
            return

        found = [i for i in self.MenuList if i["half"] <= max_price]
        if found:
            print(Fore.CYAN + f"\nItems priced below ₹{max_price}:")
            for i in found:
                print(f"{i['itemcode']:<10} | {i['name']:<25} | Half ₹{i['half']:<10} | Full ₹{i['full']:<10}")
        else:
            print(Fore.RED + f"\nNo items found below ₹{max_price}.\n")

class AdminDashboard:
    def admin_menu(self):
        menu = RestrauntMenu()

        while True:
            print("\n========= ADMIN DASHBOARD =========")
            print("1. Add Menu Item")
            print("2. Update Menu Item")
            print("3. Delete Menu Item")
            print("4. View All Menu Items")
            print("5. Search Item by Price")
            print("6. Logout")
            print("===================================")

            choice = input("Enter your choice: ")

            if choice == '1':
                try:
                    menu.add_item()
                except Exception:
                    print(Fore.RED + "Some Technical Issue Occurred! Sorry For this Inconvenience.")
                
            elif choice == '2':
                try:
                    menu.update_item()
                except Exception:
                    print(Fore.RED + "Some Technical Issue Occurred! Sorry For this Inconvenience.")
                
            elif choice == '3':
                try:
                    menu.delete_item()
                except Exception:
                    print(Fore.RED + "Some Technical Issue Occurred! Sorry For this Inconvenience.")
                
            elif choice == '4':
                try:
                    menu.show_menu()
                except Exception:
                    print(Fore.RED + "Some Technical Issue Occurred! Sorry For this Inconvenience.")
                
            elif choice == '5':
                try:
                    menu.search_by_price()
                except Exception:
                    print(Fore.RED + "Some Technical Issue Occurred! Sorry For this Inconvenience.")
                
            elif choice == '6':
                print(Fore.YELLOW + "Logging out...")
                break
            else:
                print(Fore.RED + "Invalid choice. Try again.")
class StaffDashboard:

    def staff_menu(self):
        menu = RestrauntMenu()
        while True:
            print("\n========= STAFF DASHBOARD =========")
            print("1. View Menu")
            print("2. Take Order")
            print("3. Generate Bill")
            print("4. Search Item Below Price")
            print("5. Logout")
            print("===================================")

            choice = input("Enter your choice: ")

            if choice == '1':
                try:
                    menu.show_menu()
                except Exception:
                    print(Fore.RED + "Some Technical Issue Occurred! Sorry For this Inconvenience.")
     
            elif choice == '2':
                try:
                    self.order.take_order()
                except Exception:
                    print("Some Technical Issue Occurred! Sorry For this Inconvenience.")
            
            elif choice == '3':
                try:
                    self.order.generate_bill()
                except Exception:
                    print(Fore.RED + "Some Technical Issue Occurred! Sorry For this Inconvenience.")
                
            elif choice == '4':
                try:
                    menu.search_by_price()
                except Exception:
                    print(Fore.RED + "Some Technical Issue Occurred! Sorry For this Inconvenience.")
                
            elif choice == '5':
                print(Fore.YELLOW + "Logging out...")
                break
            else:
                print(Fore.RED + "Invalid choice. Try again.")