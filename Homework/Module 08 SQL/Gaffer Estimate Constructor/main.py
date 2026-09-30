import sqlite3
import sys
import os


def main():
    create_tables()
    while True:
        print("\nActions:\n1. Add new equipment.\n2. Show all equipment.\n0. Exit")
        action = input()
        if action == "1":
            clear_console()
            add_new_equipment()
        elif action == "2":
            clear_console()
            show_all_equipment()
        elif action == "0":
            sys.exit()

def create_tables():
    with sqlite3.connect("rentals.db") as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipment (
        id INTEGER PRIMARY KEY,
        vendor_id INTEGER NOT NULL,
        sku TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL,
        price_per_unit REAL NOT NULL CHECK (price_per_unit >= 0),
        category TEXT NOT NULL,
        available INTEGER NOT NULL,
        total_stored INTEGER NOT NULL CHECK (total_stored >= 0),
        FOREIGN KEY (vendor_id) REFERENCES vendors(id)
        )""")

        conn.commit()

def add_new_equipment():
    with sqlite3.connect("rentals.db") as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, name 
        FROM vendors
        """)
        rows = cursor.fetchall()

        while True:
            vendor_map = {}
            print("\nAvailable Vendors:")
            for index, (vendor_id, vendor_name) in enumerate(rows, start=1):
                vendor_map[index] = (vendor_id, vendor_name)
                print(f"{index}. {vendor_name}")

            user_input = input("\nEnter Vendor number (or 'stop'): ")
            if user_input.lower() == "stop":
                return
            
            try:
                choice = int(user_input)
                if choice in vendor_map:
                    vendor_id, vendor_name = vendor_map[choice]
                    print(f"Selected: {vendor_name} (ID: {vendor_id})")
                    break
                else:
                    print("Invalid number. Please choose from the list.")
            except ValueError:
                print("Please enter a valid number.")
            clear_console()
            
            sku = input("Enter sku: ")
            if sku == "stop":
                return
            cursor.execute("SELECT 1 FROM equipment WHERE sku = ?", (sku,))
            check_unique = cursor.fetchall()
            if check_unique:
                print(f"Entered sku '{sku}' already exists")
                continue

            name = input("Enter equipment name: ")
            if name == "stop":
                return

            price_per_unit = input("Enter price per unit: ")
            if price_per_unit == "stop":
                return

            category = input("Enter category: ")
            if category == "stop":
                return

            available = input("Enter available: ")
            if available == "stop":
                return

            total_stored = input("Enter total stored: ")
            if total_stored == "stop":
                return

            cursor.execute("""
            INSERT INTO equipment (vendor_id, sku, name, price_per_unit, category, available, total_stored)
            VALUES (?,?,?,?,?,?,?)
            """, (vendor_id, sku, name, float(price_per_unit), category, int(available), int(total_stored)))
            conn.commit()

def show_all_equipment():
    with sqlite3.connect("rentals.db") as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()

        cursor.execute("""
        SELECT equipment.name, vendors.name, equipment.price_per_unit, equipment.category, equipment.available
        FROM equipment 
        JOIN vendors ON equipment.vendor_id = vendors.id
        ORDER BY CASE category
            WHEN 'LED_LIGHT' THEN 1
            WHEN 'HMI_LIGHT' THEN 2
            WHEN 'TNG_LIGHT' THEN 3
            WHEN 'STAND' THEN 4
            WHEN 'CABLE' THEN 5
            ELSE 6
        END, equipment.name ASC
        """)

        print(f"\n{'Equipment name':<30} {'Vendor':<20} {'Price per unit':<10} {'Available':<8}")

        rows = cursor.fetchall()
        current_category = None
        for row in rows:
            equipment_name, vendor_name, price, category, available = row
            if category != current_category:
                current_category = category

                print(f"\n========КАТЕГОРИЯ: {current_category}========")
            print(f"{equipment_name:<30} {vendor_name:<20} {price:<10} {available:<8}")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
    


