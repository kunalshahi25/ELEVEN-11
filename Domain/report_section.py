import json
import os

class ReportSection:
    def __init__(self):
        self.order_path = r"E:\ELEVEN-11\Database\orders.json"

    def show_report(self):
        if not os.path.exists(self.order_path):
            print("No orders found yet.")
            return

        with open(self.order_path, "r") as file:
            content = file.read().strip()

        if not content:
            print("No orders to show in report.")
            return

        orders = json.loads(content)

        total_orders = len(orders)
        total_sales = 0
        category_sales = {}


        for order in orders:
            total_sales += order.get("total_amount", 0)

            category = order.get("category", "Uncategorized")
            category_sales[category] = category_sales.get(category, 0) + order.get("total_amount", 0)

        
        print("\n===== DAILY SALES REPORT =====")
        print(f"Total Orders      : {total_orders}")
        print(f"Total Sales (₹)   : {total_sales}")
        print("\nSales by Category:")
        for cat, amt in category_sales.items():
            print(f"  {cat} : ₹{amt}")
        print("==============================\n")
