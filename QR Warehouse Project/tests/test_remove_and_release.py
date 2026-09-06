import pytest
from models import Equipment, EstimateItem
from estimate_constructor import Estimate, Inventory

def make_test_item(sku="TEST-001", price=1000.0, days=3):
    return EstimateItem(
        sku=sku,
        name="Test Item",
        category="TEST",
        quantity=1,
        price_per_unit=price,
        days_in_rent=days,
        total_price=0.0,
        from_catalog=True
    )

def test_remove_one_decreases_quantity():
    """Тест 1: Удаление одной штуки из позиции с quantity=3"""
    estimate = Estimate(project_name="Test", days_in_rent=3)
    
    # Добавляем позицию 3 раза (quantity станет 3)
    item1 = make_test_item(sku="A", price=1000.0, days=3)
    estimate.add_item(item1)
    estimate.add_item(make_test_item(sku="A", price=1000.0, days=3))
    estimate.add_item(make_test_item(sku="A", price=1000.0, days=3))
    
    # Удаляем одну штуку
    status, qty_to_return = estimate.remove_one("A")
    
    assert status == "decreased_by_1", "Status should be 'decreased_by_1'"
    assert qty_to_return == 1, "Should be 1"
    assert len(estimate.items) == 1, "Should be 1"
    assert estimate.items[0].quantity == 2, "Should be 2"
    assert estimate.grand_total == 6000.0, "Should be 6000.0"


def test_remove_one_removes_item_completely():
    """Тест 2: Удаление последней штуки полностью убирает позицию"""
    estimate = Estimate(project_name="Test", days_in_rent=3)
    item = make_test_item(sku="A", price=1000.0, days=3)
    estimate.add_item(item)
    
    status, qty_to_return = estimate.remove_one("A")
    
    assert status == "removed_from_estimate", "Should be 'removed_from_estimate"
    assert qty_to_return == 1, "Should be 1"
    assert len(estimate.items) == 0, "Should be 0"
    assert estimate.grand_total == 0.0, "Should be 0.0"

    


def test_remove_one_not_in_estimate():
    """Тест 3: Попытка удалить несуществующую позицию"""
    estimate = Estimate(project_name="Test", days_in_rent=3)
    
    status, qty_to_return = estimate.remove_one("FAKE-999")
    
    assert status == "not_in_estimate", "Should be 'not_in_estimate'"
    assert qty_to_return == 0, "Should be 0"
    assert len(estimate.items) == 0, "Should be 0"


def test_release_equipment_increases_stock():
    """Тест 4: Возврат оборудования на склад увеличивает available"""
    inventory = Inventory()
    eq = Equipment(
        sku="TEST-001",
        name="Test Light",
        price_per_unit=1000.0,
        category="LIGHT",
        available=5,
        total_stored=10
    )
    inventory.register_equipment({"TEST-001": eq})
    
    inventory.release_equipment("TEST-001", 2)
    
    assert inventory._stock["TEST-001"] == 7, "Should be 7"