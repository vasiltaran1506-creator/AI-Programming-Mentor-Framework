from pathlib import Path
from estimate_system import models
import json

def load_catalog(path):
    try:
        with open(path, "r", encoding="utf-8") as text:
            catalog = json.load(text)
    except FileNotFoundError:
        return []
    Equipment = _parce_catalog(catalog)
    return Equipment

def _parce_catalog(catalog):
    Equipment = models.Equipment
    for item in catalog:
        _validate_equipment_data(item)
        Equipment.name = item["name"]
        Equipment.price_per_unit = item["price_per_unit"]
        Equipment.category = item["category"]
        Equipment.in_stock = item["in_stock"]
    return Equipment

def _validate_equipment_data(item):
    if "name" not in item:
        return False
    if "price_per_unit" not in item:
        return False
    if not isinstance("price_per_unit", float):
        raise ValueError("price_per_unit is not float")
    if "category" not in item:
        return False
    if "in_stock" not in item:
        return False    
    if not isinstance("in_stock", int):
        raise ValueError("in_stock is not int")
    pass

def main():
    path = Path(r"D:\Github\AI Programming Mentor Framework\Homework\Module 04\QR_Scanner\catalog.json")
    load_catalog(path)
    pass

if __name__ == "__main__":
    main()