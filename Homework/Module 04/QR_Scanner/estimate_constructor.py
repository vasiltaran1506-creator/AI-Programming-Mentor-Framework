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
    _find_scan_in_catalog(catalog, scan)
    quantity = 0
    if _find_scan_in_catalog is not None:
        quantity += 1
        EstimateItem(
            sku=scan,
            name=Equipment.name,
            category=Equipment.category,
            quantity= 1,
            price_per_unit=Equipment.price_per_unit,
            total_price=quantity,
            from_catalog=True
        )

        _add_position_to_estimate(EstimateItem, estimate)

    elif _find_scan_in_catalog is None:
        _manual_add_position_to_estimate()
    
def _find_scan_in_catalog(catalog: dict, scan:str) -> Equipment | None:
    position = catalog.get(scan)
    if position == None:
        return None
    Equipment(
        sku=scan,
        name=position["name"],
        price_per_unit=position["price_per_unit"],
        category=position["category"],
        in_stock=position["in_stock"]
    )
    return Equipment

def _add_position_to_estimate(EstimateItem, Estimate):
    pass

def _manual_add_position_to_estimate():
    pass

def _calculate_total_position_price(position):

    return 

def _calculate_grand_total_price():
    pass