import sqlite3
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


class SQLRepository(EquipmentRepository):
    def __init__(self, db_path) -> None:
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        sql_query = """
        CREATE TABLE IF NOT EXISTS equipment (
            sku TEXT PRIMARY KEY,
            name TEXT,
            price_per_unit REAL,
            category TEXT,
            available INTEGER,
            total_stored INTEGER
        )
        """
        cursor.execute(sql_query)
        conn.commit()
        conn.close()

    def find_by_sku(self, scan: str) -> Equipment | None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        sql_query = """
        SELECT * FROM equipment WHERE sku = ?
        """
        cursor.execute(sql_query, (scan,))

        line = cursor.fetchone()
        conn.close()

        if line is None: 
            return None
        else:
           sku, name, price_per_unit, category, available, total_stored = line
           return Equipment(
               sku=sku, name=name, price_per_unit=price_per_unit, category=category, available=available, total_stored=total_stored
           )

    def update_available(self, scan: str, quantity_change: int) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        sql_query = """
        UPDATE equipment SET available = available + ? WHERE sku = ?
        """
        cursor.execute(sql_query, (quantity_change, scan))

        conn.commit()
        conn.close()
