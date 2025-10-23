import json
import uuid
from datetime import datetime, timedelta
from colorama import Fore

path = r"E:\ELEVEN-11\ELEVEN-11_restraunt\Database\TableBooking.json"

class TableBooking:
    def __init__(self):
        self.tables = {
            "T1": {"capacity": 2, "status": "Available"},
            "T2": {"capacity": 4, "status": "Available"},
            "T3": {"capacity": 4, "status": "Available"},
            "T4": {"capacity": 6, "status": "Available"}
        }
        self.bookings = []

    # ------------------ Load / Save ------------------
    def load_existing_bookings(self):
        try:
            with open(path, 'r') as f:
                self.bookings = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.bookings = []

    def save_bookings(self):
        with open(path, 'w') as f:
            json.dump(self.bookings, f, indent=4)

    # ------------------ Show Available Tables ------------------
    def show_available_tables(self):
        self.load_existing_bookings()
        self.auto_expire_bookings()

        print(Fore.CYAN + "\n==== AVAILABLE TABLES ====")
        booked_tables = {b['table_id'] for b in self.bookings if b['status'] == 'Booked'}
        for table_id, details in self.tables.items():
            status = "Booked" if table_id in booked_tables else "Available"
            print(f"{table_id} | Capacity: {details['capacity']} | Status: {status}")
        print("===========================\n")

    # ------------------ Book Table ------------------
    def book_table(self):
        self.load_existing_bookings()
        self.show_available_tables()

        name = input("Enter Customer Name: ")
        people = int(input("Enter Number of People: "))
        duration = int(input("Enter booking duration (in hours): "))

        # find suitable table
        suitable = None
        for table_id, details in self.tables.items():
            if details["capacity"] >= people:
                overlapping = False
                for b in self.bookings:
                    if b['table_id'] == table_id and b['status'] == 'Booked':
                        end_time = datetime.strptime(b['end_time'], "%Y-%m-%d %H:%M")
                        if datetime.now() < end_time:
                            overlapping = True
                            break
                if not overlapping:
                    suitable = table_id
                    break

        if suitable:
            start_time = datetime.now()
            end_time = start_time + timedelta(hours=duration)

            booking_id = uuid.uuid4().hex[:5].upper()
            booking_data = {
                "booking_id": booking_id,
                "customer_name": name,
                "table_id": suitable,
                "people": people,
                "start_time": start_time.strftime("%Y-%m-%d %H:%M"),
                "end_time": end_time.strftime("%Y-%m-%d %H:%M"),
                "status": "Booked"
            }

            self.bookings.append(booking_data)
            self.save_bookings()

            print(Fore.GREEN + f"\n✅ Table {suitable} booked successfully!")
            print(f"Booking ID: {booking_id}")
            print(f"Customer: {name}")
            print(f"From: {start_time.strftime('%H:%M')} To: {end_time.strftime('%H:%M')}")
            print("==============================")
        else:
            print(Fore.RED + "\n❌ No suitable table available right now.\n")

    # ------------------ View All Bookings ------------------
    def view_bookings(self):
        self.auto_expire_bookings()
        self.load_existing_bookings()

        if not self.bookings:
            print(Fore.YELLOW + "No bookings found.")
        else:
            print(Fore.LIGHTMAGENTA_EX + "\n==== CURRENT BOOKINGS ====")
            for b in self.bookings:
                print(f"{b['booking_id']} | {b['customer_name']} | Table: {b['table_id']} | "
                      f"{b['people']} People | {b['start_time']} - {b['end_time']} | {b['status']}")
            print("==============================")

    # ------------------ Cancel Booking ------------------
    def cancel_booking(self):
        self.load_existing_bookings()
        self.auto_expire_bookings()

        if not self.bookings:
            print(Fore.YELLOW + "No bookings to cancel.")
            return

        self.view_bookings()
        cancel_id = input(Fore.CYAN + "\nEnter Booking ID to cancel: ").strip().upper()
        found = False

        for b in self.bookings:
            if b["booking_id"] == cancel_id:
                if b["status"] == "Booked":
                    b["status"] = "Cancelled"
                    self.save_bookings()
                    found = True
                    print(Fore.RED + f"\n❌ Booking {cancel_id} has been cancelled successfully.")
                    break
                else:
                    print(Fore.YELLOW + f"\n⚠️ Booking {cancel_id} is already {b['status']}.")
                    return

        if not found:
            print(Fore.RED + "Booking ID not found!")

    # ------------------ Auto Expire ------------------
    def auto_expire_bookings(self):
        """Mark bookings as 'Expired' if their end time has passed."""
        self.load_existing_bookings()
        updated = False
        now = datetime.now()

        for booking in self.bookings:
            try:
                end_time = datetime.strptime(booking["end_time"], "%Y-%m-%d %H:%M")
                if booking["status"] == "Booked" and now > end_time:
                    booking["status"] = "Expired"
                    updated = True
            except KeyError:
                continue

        if updated:
            self.save_bookings()
            print(Fore.YELLOW + "Old bookings expired automatically.\n")
