from dataclasses import dataclass
from models import Equipment, EstimateItem


class Inventory:

    def __init__(self) -> None:
        self._catalog = {}
        self._stock = {}

    def register_equipment(self, equipment: Equipment):
        self._catalog[equipment.sku] = equipment
        self._stock[equipment.sku] = equipment.available

class Estimate:

    def __init__(self, project_name) -> None:
        self.project_name = project_name
        self.items = []
        self.grand_total = 0.0

    def __str__(self) -> str:
        return f"Project name: {self.project_name}, Items in estimate: {self.items}, Grand total: {self.grand_total}"

    def process_scan(self, position, days):
            from_catalog = True
            item = EstimateItem(
                sku=position.sku,
                name=position.name,
                category=position.category,
                quantity=1,
                price_per_unit=position.price_per_unit,
                days_in_rent= days,
                total_price=0,
                from_catalog=from_catalog
            )
            
            self.add_item(item)


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
            existing_item.update_total_price()

        #Если позиция новая, добавляем ее в self.items
        if existing_item is None:
            item.update_total_price()
            self.items.append(item)

        self.grand_total = self._recalculate_total()

    def _recalculate_total(self):
        return sum(pos.price_per_unit * pos.quantity * pos.days_in_rent for pos in self.items)


def main():
    inventory = Inventory()

    pos1 = Equipment(
        sku="LIGHT-0001",
        name="Auture LS600D", 
        price_per_unit=3500.0,
        category="LIGHT",
        available=1,
        total_stored=1
    )

    inventory.register_equipment(pos1)

    print(inventory._catalog)
    print(inventory._stock)


if __name__ == "__main__":
    main()