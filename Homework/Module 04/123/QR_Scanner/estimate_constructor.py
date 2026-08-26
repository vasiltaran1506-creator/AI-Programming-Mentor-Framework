"""
def process_scan() # catalog: dict, estimate: dict, scan: str -> updated_estimate: dict, status: str

def _find_scan_in_catalog() # catalog: dict, scan: str -> position: dict/None

def _add_position_to_estimate() # position: dict, estimate: dict -> updated_estimate: dict

def _manual_add_position_to_estimate() # position: dict -> estimate: dict

def _check_in_stock() # catalog: dict # position dict, -> bool

def _calculate_total_position_price() # position: dict -> total_position_price: float

def _calculate_grand_total() # items: list[dict] -> grand_total: float




"""