"""
def process_scan() # catalog: dict, estimate: dict, scan: str -> updated_estimate: dict, status: str

def _find_scan_in_catalog() # catalog: dict, scan: str -> position: dict/None

def _add_position_to_estimate() # position: dict, estimate: dict -> updated_estimate: dict

def _manual_add_position_to_estimate() # position: dict -> estimate: dict

def _check_in_stock() # catalog: dict # position dict, -> bool

def _calculate_total_position_price() # position: dict -> total_position_price: float

def _calculate_grand_total() # items: list[dict] -> grand_total: float




"""
from estimate_system.models import Estimate, EstimateItem, Equipment




def process_scan(catalog: dict, estimate: Estimate, scan: str):
    equipment = _find_scan_in_catalog(catalog, scan)
    quantity = 1

    if equipment != None:
        from_catalog = True
        total_price = Equipment.price_per_unit * quantity
        item = EstimateItem(
                sku=scan,
                name=Equipment.name,
                category=Equipment.category,
                quantity=quantity,
                price_per_unit=Equipment.price_per_unit,
                total_price=total_price,
                from_catalog=from_catalog
            )
        _add_position_to_estimate(item, estimate)

    else:
        _manual_add_position_to_estimate()

def _find_scan_in_catalog(catalog: dict, scan:str) -> Equipment | None:
    position = catalog.get(scan)
    if not position:
        return None
    return Equipment(
        sku=scan,
        name=position["name"],
        price_per_unit=position["price_per_unit"],
        category=position["category"],
        in_stock=position["in_stock"]
    )

def _check_in_stock():
    
    pass

def _add_position_to_estimate(item, estimate):
    pass

def _manual_add_position_to_estimate():
    pass

def _calculate_total_position_price(position):

    return 

def _calculate_grand_total_price():
    pass