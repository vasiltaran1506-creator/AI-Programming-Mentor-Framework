from abc import ABC, abstractmethod
from models import Equipment
import json

class EquipmentRepository(ABC):

    @abstractmethod
    def find_by_sku(self, sku: str,) -> Equipment | None:
        pass

    @abstractmethod
    def update_available(self, sku: str, quantity_change: int):
        pass


class JsonEquipmentRepository(EquipmentRepository):

    def __init__(self, catalog_path) -> None:
        self.catalog_path = catalog_path

    def find_by_sku(self, sku: str) -> Equipment | None:

        with open(self.catalog_path, "r", encoding="utf-8") as file:
            catalog = json.load(file)

        if sku not in catalog:
            return None

        data = catalog[sku]
        self._validate_equipment_data(data)

        return Equipment(
            sku=sku,
            name=data["name"],
            price_per_unit=data["price_per_unit"],
            category=data["category"],
            available=data["available"],
            total_stored=data["total_stored"]
        )

    def update_available(self, sku: str, quantity_change: int):

        with open(self.catalog_path, "r", encoding="utf-8") as file:
            catalog = json.load(file)

        if sku not in catalog:
            raise ValueError(f"SKU {sku} not found in catalog")

        catalog[sku]["available"] += quantity_change

        with open(self.catalog_path, "w", encoding="utf-8") as file:
            json.dump(catalog, file, indent=4, ensure_ascii=False)

    def _validate_equipment_data(self, data):

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
   