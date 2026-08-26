"""
def process_scan() # catalog: dict, estimate: dict, scan: str -> updated_estimate: dict, status: str

def _find_scan_in_catalog() # catalog: dict, scan: str -> position: dict/None

def _add_position_to_estimate() # position: dict, estimate: dict -> updated_estimate: dict

def _manual_add_position_to_estimate() # position: dict -> estimate: dict

def _check_in_stock() # catalog: dict # position dict, -> bool

def _calculate_total_position_price() # position: dict -> total_position_price: float

def _calculate_grand_total() # items: list[dict] -> grand_total: float



# Contracts

## _find_scan_in_catalog():
Input: catalog: dict, scan: str
Output: position: dict/None
Normal absence: 
Possible errors:
Side effects:
Responsibility:

"added"            → позиция добавлена из каталога
"quantity_updated" → количество увеличено
"not_found"        → sku не найден в каталоге
"over_stock"       → отсканировано больше, чем на складе    

"""