import pytest
from models import Equipment, EstimateItem
from estimate_constructor import Estimate, Inventory
from price_policy import VGIK_Policy
from logger import ConsoleLogger

def make_test_item(sku, price, days):
    return EstimateItem(
        sku=sku,
        name="Test item",
        category="HMI_LIGHT",
        price_per_unit=price,
        quantity=1,
        days_in_rent=days,
        total_price=0.0,
        from_catalog=True
    )

def test_VGIK_Price_Policy():
    price_policy = VGIK_Policy()

    estimate = Estimate(
        project_name="TEST",
        days_in_rent=3,
        price_policy=price_policy,
        logger=ConsoleLogger()
    )

    item1 = make_test_item(sku="A", price=1000.0, days=1)
    estimate.add_item(item1)

    assert estimate.items[0].total_price == 400.0, "Should be 400.0"