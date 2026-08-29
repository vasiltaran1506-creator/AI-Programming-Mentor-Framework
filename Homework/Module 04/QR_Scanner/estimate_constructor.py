from estimate_system.models import Estimate, EstimateItem, Equipment

def process_scan(catalog: dict, estimate: Estimate, scan: str):
    equipment = _find_scan_in_catalog(catalog, scan)

    if equipment != None:
        from_catalog = True
        item = EstimateItem(
            sku=scan,
            name=equipment.name,
            category=equipment.category,
            quantity=0,
            price_per_unit=equipment.price_per_unit,
            total_price=0,
            from_catalog=from_catalog
            )
        status = _add_position_to_estimate(item, estimate, catalog)
    else:
        status = "not_found"
        return estimate, status

    return estimate, status

def _find_scan_in_catalog(catalog: dict, scan:str) -> Equipment | None:
    position = catalog.get(scan)
    if not position:
        return None
    return position

def _add_position_to_estimate(item: EstimateItem, estimate: Estimate, catalog):
    existing_item = None
    for position in estimate.items:
        if position.sku == item.sku:
            existing_item = position
            break
    if existing_item is not None:
        position.quantity = position.quantity + 1
    else:
        position.quantity = 1
    item.total_price = _calculate_total_position_price(item)
    status = _check_in_stock(catalog, item)
    if status == "added":
        estimate.items.append(item)
        estimate.grand_total = _calculate_grand_total_price(estimate)
        return estimate, status
    else:
        return estimate, status


def _calculate_total_position_price(item: EstimateItem):
    total_price = item.price_per_unit * item.quantity
    return total_price

def _calculate_grand_total_price(estimate: Estimate) -> float:
    grand_total = sum(position.total_price for position in estimate.items)
    return grand_total

def _check_in_stock(catalog: Equipment, item: EstimateItem) -> str:
    if item.quantity > Equipment.in_stock:
        status = "over_stock"
        return status
    else:
        status = "added"
        return status

