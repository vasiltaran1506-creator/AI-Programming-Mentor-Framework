from pathlib import Path
from models import Equipment
import json

def load_catalog(catalog_path):
    try:
        with open(catalog_path, "r", encoding="utf-8") as file:
            catalog = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError
    equipment_dict = _parse_catalog(catalog)
    return equipment_dict

def _parse_catalog(raw_data):
    catalog = {}
    for sku, data in raw_data.items():
        _validate_equipment_data(data)
        equipment = Equipment(
        sku= sku,
        name= data["name"],
        price_per_unit= data["price_per_unit"],
        category= data["category"],
        available=data["available"],
        total_stored= data["total_stored"],
        )
        catalog[sku] = equipment
    return catalog

def _validate_equipment_data(data):

    if "name" not in data:
        raise ValueError("'name' is missing from the catalog")
    if "price_per_unit" not in data:
        raise ValueError("'price_per_unit' is missing from the catalog")
    if not isinstance(data["price_per_unit"], (int, float)):
        raise ValueError("price_per_unit is not float")
    if "category" not in data:
        raise ValueError("'category' is missing from the catalog")
    if "available" not in data:
        raise ValueError("'available' is missing from the catalog")
    if not isinstance(data["available"], int):
        raise ValueError("in_stock is not int")
    if "total_stored" not in data:
        raise ValueError("'total_stored' is missing from the catalog")
    if not isinstance(data["total_stored"], int):
        raise ValueError("'total_stored' is not int")


def main():
    path = Path(input("Enter catalog path:\n"))
    load_catalog(path)
    

if __name__ == "__main__":
    main()