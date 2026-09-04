from dataclasses import dataclass


@dataclass
class Equipment:
    sku: str
    name: str
    price_per_unit: float
    category: str


@dataclass
class EstimateItem:
    sku: str
    name: str
    category: str
    quantity: int
    price_per_unit: float
    days_in_rent: int
    total_price: float
    from_catalog: bool

    def update_total_price(self):
        self.total_price = (self.price_per_unit * self.quantity * self.days_in_rent)


class Estimate:

    def __init__(self, project_name) -> None:
        self.project_name = project_name

        self.items = []
        self.grand_total = 0.0

    def __str__(self) -> str:
        return f"Project name: {self.project_name}, Items in estimate: {self.items}, Grand total: {self.grand_total}"

    def process_scan(self, position):
            from_catalog = True
            item = EstimateItem(
                sku=position.sku,
                name=position.name,
                category=position.category,
                quantity=1,
                price_per_unit=position.price_per_unit,
                days_in_rent= 1,
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


estimate = Estimate("Captain's daughter")
pos1 = Equipment("C001", "Sony FX3", 3500.0, "Cameras")

estimate.process_scan(pos1)
print(estimate)
estimate.process_scan(pos1)
print(estimate)