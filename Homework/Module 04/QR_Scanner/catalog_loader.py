from pathlib import Path
from estimate_system.models import Equipment
import json

def load_catalog(path):
    try:
        with open(path, "r", encoding="utf-8") as text:
            catalog = json.load(text)
    except FileNotFoundError:
        raise FileNotFoundError
    equipment_dict = _parse_catalog(catalog)
    return equipment_dict

def _parse_catalog(raw_data):
    catalog = {}
    for sku, data in raw_data.items():
        _validate_equipment_data(sku, data)
        equipment = Equipment(
        sku= sku,
        name= data["name"],
        price_per_unit= data["price_per_unit"],
        category= data["category"],
        in_stock= data["in_stock"]
        )
        catalog[sku] = equipment
    return catalog

def _validate_equipment_data(sku, data):

    if "name" not in data:
        raise ValueError("'name' is missing from the catalog")
    if "price_per_unit" not in data:
        raise ValueError("'price_per_unit' is missing from the catalog")
    if not isinstance(data["price_per_unit"], (int, float)):
        raise ValueError("price_per_unit is not float")
    if "category" not in data:
        raise ValueError("'category' is missing from the catalog")
    if "in_stock" not in data:
        raise ValueError("'in_stock' is missing from the catalog")
    if not isinstance(data["in_stock"], int):
        raise ValueError("in_stock is not int")
    return

def main():
    path = Path(input("Enter catalog path:\n"))
    load_catalog(path)
    pass

if __name__ == "__main__":
    main()