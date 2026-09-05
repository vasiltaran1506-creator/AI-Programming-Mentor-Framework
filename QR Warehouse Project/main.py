from catalog_loader import load_catalog
from estimate_constructor import Estimate, Inventory
import exporter
import json


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
        scan = input("Enter SKU ('done' for exit): ")
        if scan == "done": 
            text = exporter.format_estimate(estimate)
            exporter.save_estimate(save_path, text, project_name)
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


if __name__ == "__main__":
    main()

