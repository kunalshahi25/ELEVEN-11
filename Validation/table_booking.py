import json
import uuid
from datetime import datetime, timedelta
from colorama import Fore

path = r"E:\ELEVEN-11\Database\TableBooking.json"

class TableBooking:
    def __init__(self):
        # 10 tables max
        self.tables = {
            f"T{i}": {"capacity": (2 if i <= 3 else 4 if i <= 6 else 6), "status": "Available"}
            for i in range(1, 11)
        }
        self.bookings = []

    def load_existing_bookings(self):
        try:
            with open(path, 'r') as f:
                self.bookings = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.bookings = []

    def save_bookings(self):
        with open(path, 'w') as f:
            json.dump(self.bookings, f, indent=4)

    def show_available_tables(self, booking_date=None):
        self.load_existing_bookings()
        self.auto_expire_bookings()

        print(Fore.CYAN + "\n==== AVAILABLE TABLES ====")
        booked_tables = set()

        if booking_date:
            # filter for the given date
            for b in self.bookings:
                if b['status'] == 'Booked' and b['date'] == booking_date:
                    booked_tables.add(b['table_id'])

        for table_id, details in self.tables.items():
            status = "Booked" if table_id in booked_tables else "Available"
            print(f"{table_id} | Capacity: {details['capacity']} | Status: {status}")
        print("===========================\n")

    def book_table(self):
        self.load_existing_bookings()
        self.auto_expire_bookings()

        name = input("Enter Customer Name: ")
        people = int(input("Enter Number of People: "))
        duration = int(input("Enter booking duration (in hours): "))

        date_str = input("Enter booking date (YYYY-MM-DD): ")
        time_str = input("Enter start time (HH:MM in 24-hr format): ")

        try:
            start_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        except ValueError:
            print(Fore.RED + "Invalid date/time format! Please try again.")
            return

        end_time = start_time + timedelta(hours=duration)
        booking_date = date_str

        # show available tables for that date
        self.show_available_tables(booking_date)

        # find suitable table
        suitable = None
        for table_id, details in self.tables.items():
            if details["capacity"] >= people:
                overlapping = False
                for b in self.bookings:
                    if (
                        b['table_id'] == table_id and 
                        b['status'] == 'Booked' and
                        b['date'] == booking_date
                    ):
                        existing_start = datetime.strptime(b['start_time'], "%Y-%m-%d %H:%M")
                        existing_end = datetime.strptime(b['end_time'], "%Y-%m-%d %H:%M")
                        if not (end_time <= existing_start or start_time >= existing_end):
                            overlapping = True
                            break
                if not overlapping:
                    suitable = table_id
                    break

        if suitable:
            booking_id = uuid.uuid4().hex[:5].upper()
            booking_data = {
                "booking_id": booking_id,
                "customer_name": name,
                "table_id": suitable,
                "people": people,
                "date": booking_date,
                "start_time": start_time.strftime("%Y-%m-%d %H:%M"),
                "end_time": end_time.strftime("%Y-%m-%d %H:%M"),
                "status": "Booked"
            }

            self.bookings.append(booking_data)
            self.save_bookings()

            print(Fore.GREEN + f"\nTable {suitable} booked successfully!")
            print(f"Booking ID: {booking_id}")
            print(f"Customer: {name}")
            print(f"Date: {booking_date}")
            print(f"From: {start_time.strftime('%H:%M')} To: {end_time.strftime('%H:%M')}")
            print("==============================")
        else:
            print(Fore.RED + "\nNo suitable table available at the chosen time.\n")

    def view_bookings(self):
        self.auto_expire_bookings()
        self.load_existing_bookings()

        if not self.bookings:
            print(Fore.YELLOW + "No bookings found.")
        else:
            print(Fore.LIGHTMAGENTA_EX + "\n==== CURRENT BOOKINGS ====")
            for b in self.bookings:
                print(f"{b['booking_id']} | {b['customer_name']} | Table: {b['table_id']} | "
                      f"{b['people']} People | {b['date']} | "
                      f"{b['start_time'].split()[1]} - {b['end_time'].split()[1]} | {b['status']}")
            print("==============================")


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
                    print(Fore.RED + f"\nBooking {cancel_id} has been cancelled successfully.")
                    break
                else:
                    print(Fore.YELLOW + f"\nBooking {cancel_id} is already {b['status']}.")
                    return

        if not found:
            print(Fore.RED + "Booking ID not found!")


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
            # print(Fore.YELLOW + "Old bookings expired automatically.\n")
