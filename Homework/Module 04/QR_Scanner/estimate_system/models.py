from dataclasses import dataclass

@dataclass
class Equipment:
    sku: str
    name: str
    price_per_unit: float
    category: str
    in_stock: int

@dataclass
class EstimateItem:
    sku: str
    name: str
    category: str
    quantity: int
    price_per_unit: float
    total_price: float
    from_catalog: bool

@dataclass
class Estimate:
    project_name: str
    items: list[EstimateItem]
    grand_total: float