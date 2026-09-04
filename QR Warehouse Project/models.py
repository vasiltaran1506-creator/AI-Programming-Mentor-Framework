from dataclasses import dataclass

@dataclass
class Equipment:
    sku: str
    name: str
    price_per_unit: float
    category: str
    available: int
    total_stored: int


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