from estimate_system.models import Estimate, EstimateItem, Equipment

def process_scan(catalog: dict, estimate: Estimate, scan: str):
    equipment = _find_scan_in_catalog(catalog, scan)

    if equipment != None:
        from_catalog = True
        item = EstimateItem(
            sku=scan,
            name=equipment.name,
            category=equipment.category,
            quantity=1,
            price_per_unit=equipment.price_per_unit,
            total_price=0,
            from_catalog=from_catalog
            )
        estimate, status = add_position_to_estimate(item, estimate, catalog)
    else:
        status = "not_found"
        return estimate, status

    return estimate, status

def _find_scan_in_catalog(catalog: dict, scan:str) -> Equipment | None:
    position = catalog.get(scan)
    if not position:
        return None
    return position

def add_position_to_estimate(item: EstimateItem, estimate: Estimate, catalog):
    existing_item = None
    
    for position in estimate.items:
        if position.sku == item.sku:
            existing_item = position
            break
    if existing_item is not None:
        existing_item.quantity += 1 
        existing_item.total_price = _calculate_total_position_price(existing_item)
        status = "quantity_updated"
        item_to_check = existing_item
    else:
        item.quantity = 1
        item.total_price = _calculate_total_position_price(item)
        estimate.items.append(item)
        item_to_check = item
        if item.from_catalog:
            status = "added"
        else:
            status = "manually_added"
    estimate.grand_total = _calculate_grand_total_price(estimate)
    stock_status = _check_in_stock(catalog, item_to_check)
    if stock_status == "over_stock":
        status = "over_stock"

    return estimate, status

def _calculate_total_position_price(item: EstimateItem):
    total_price = item.price_per_unit * item.quantity
    return total_price

def _calculate_grand_total_price(estimate: Estimate) -> float:
    grand_total = sum(position.total_price for position in estimate.items)
    return grand_total

def _check_in_stock(catalog: dict, item_to_check: EstimateItem) -> str:
    equipment = catalog.get(item_to_check.sku)
    if equipment is None:
        status = "added"
        return status
    if item_to_check.quantity > equipment.in_stock:
        status = "over_stock"
        return status
    status = "added"
    return status

