from catalog_loader import load_catalog
from estimate_constructor import Estimate, Inventory
import exporter
import json
import os

#TODO
"""
"""




def main():
    config_path = r"D:\VASILY\Projects\AI-Programming-Mentor-Framework\QR Warehouse Project\config.json"
    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)
    catalog_path = config["catalog_path"]
    save_path = config["save_path"]

    catalog = load_catalog(catalog_path)
    inventory = Inventory()
    inventory.register_equipment(catalog)

    project_name = input("Enter project name: ")
    days = int(input("Enter days of rent: "))
    estimate = Estimate(
        project_name=project_name,
        days_in_rent=days
    )

    while True:
        scan = input("Enter SKU ('done' for save): ")
        clear_console()

        parts = scan.split()
        if not parts:
            continue 
        if parts[0] == "delete" and len(parts) >= 2:
            sku = parts[1]
            status, quantity = estimate.remove_one(sku)

            if status == "decreased_by_1":
                inventory.release_equipment(sku, quantity)
                print("Equipment quantity decreased by 1")

            elif status == "removed_from_estimate":
                inventory.release_equipment(sku, quantity)
                print("Equipment deleted from the estimate")

            elif status == "not_in_estimate":
                print(f"No such scan '{sku}' in current estimate")
            display_estimate(estimate)
            continue
            
        elif scan == "done": 
            text = exporter.format_estimate(estimate)
            exporter.save_estimate(save_path, text, project_name)
            break

        elif scan == "stop":
            break

        status, equipment = inventory.check_and_reserve(scan)
        if status == "reserved" and equipment is not None:
            status = estimate.process_scan(scan, equipment)
            if status == "added":
                print(f"{equipment.name} added successfully.")
            elif status == "quantity_updated":
                print(f"Quantity of {equipment.name} updated successfully")
        elif status == "over_stock" and equipment is not None:
            print(f"Equipment {equipment.name} is out of stock")
        elif status == "not_found":
            print(f"No scan {scan} in catalog")

        display_estimate(estimate)


#       =========================================
#       =           Service functions           =
#       =========================================

def display_estimate(estimate: Estimate):
    text = exporter.format_estimate(estimate)
    print(text)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()

