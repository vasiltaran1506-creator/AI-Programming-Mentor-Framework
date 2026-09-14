from estimate_constructor import Inventory, Estimate
from models import Equipment


class AddItemToEstimate:
    def __init__(self, inventory: Inventory, estimate: Estimate) -> None:
        self.inventory = inventory
        self.estimate = estimate

    def execute(self, sku: str) -> tuple[str, Equipment | None]:
        status, equipment = self.inventory.reserve_equipment(sku)

        if status == "reserved" and equipment is not None:
            status = self.estimate.process_scan(sku, equipment)
            return status, equipment
        elif status == "over_stock" and equipment is not None:
            return status, equipment
        elif status == "not_found" and equipment is None:
            return status, None

        return status, equipment