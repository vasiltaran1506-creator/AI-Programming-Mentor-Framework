from dataclasses import dataclass
from models import Equipment, EstimateItem
from price_policy import PricePolicy
from logger import Logger, FileLogger, ConsoleLogger

class Inventory:
    def __init__(self, logger: Logger) -> None:
        self._catalog = {}
        self._stock = {}
        self.log = logger

    def register_equipment(self, catalog):
        for sku, equipment_data in catalog.items():
            self._catalog[sku] = equipment_data
            self._stock[sku] = equipment_data.available

    def check_and_reserve(self, sku: str) -> tuple[str, Equipment | None]:
        if sku in self._catalog:
            if self._stock[sku] >= 1:
                self._stock[sku] -= 1
                return "reserved", self._catalog.get(sku)
            else:
                return "over_stock", self._catalog.get(sku)
        return "not_found", None

    def release_equipment(self, sku: str, quantity: int):
        self._stock[sku] += quantity


class Estimate:
    def __init__(self, project_name, days_in_rent, price_policy: PricePolicy, logger: Logger) -> None:
        self.project_name = project_name
        self.days_in_rent = days_in_rent
        self.price_policy = price_policy

        self.log = logger
        
        self.items = []
        self.grand_total = 0.0

    def __str__(self):
        return f"Project name: {self.project_name}, Items in estimate: {self.items}, Grand total: {self.grand_total}"

    def process_scan(self, scan: str, equipment: Equipment):

        item = EstimateItem(
            sku=scan,
            name=equipment.name,
            category=equipment.category,
            price_per_unit=equipment.price_per_unit,
            quantity=1,
            days_in_rent= self.days_in_rent,
            total_price=0,
            from_catalog=True
        )
        status = self.add_item(item)

        return status

    def add_item(self, item: EstimateItem):

        existing_item = None
        #Проверка, есть ли уже позиция в смете
        for position in self.items:
            if position.sku == item.sku:
                existing_item = position
                break
        
        #Если позиция уже существует, увеличиваем ее количество в смете
        if existing_item is not None:
            existing_item.quantity += 1
            existing_item.update_total_price(self.price_policy.calculate_discount(existing_item.category))
            status = "quantity_updated"

        #Если позиция новая, добавляем ее в self.items
        if existing_item is None:
            item.update_total_price(self.price_policy.calculate_discount(item.category))
            self.items.append(item)
            status = "added"

        self.grand_total = self._recalculate_total()

        return status

    def remove_one(self, scan: str) -> tuple[str, int]:
        existing_item = None

        for position in self.items:
            if position.sku == scan:
                existing_item = position
                break

        if existing_item is not None:
            existing_item.quantity -= 1
            if existing_item.quantity >= 1:
                status = "decreased_by_1"
                existing_item.update_total_price(self.price_policy.calculate_discount(existing_item.category))
                self.grand_total = self._recalculate_total()
            else:
                self.items.remove(existing_item)
                status = "removed_from_estimate"
                self.grand_total = self._recalculate_total()

        if existing_item is None:
            status = "not_in_estimate"
            return status, 0
        return status, 1

    def _recalculate_total(self):
        return sum(pos.total_price for pos in self.items)

    