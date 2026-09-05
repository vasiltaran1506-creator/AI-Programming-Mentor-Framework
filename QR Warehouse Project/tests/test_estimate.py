import pytest
from models import Equipment, EstimateItem
from estimate_constructor import Estimate

# Вспомогательная функция (фикстура) для создания тестовой позиции
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


def test_estimate_initial_state():
    """Тест 1: Новая смета пуста, grand_total равен 0"""
    estimate = Estimate(project_name="Test Project", days_in_rent=3)
    
    assert len(estimate.items) == 0, "List 'estimate.items' should be 0"
    assert estimate.grand_total == 0.0, "'estimate.grand_total' should be 0.0"

def test_add_new_item():
    """Тест 2: Добавление новой позиции увеличивает количество позиций и grand_total"""
    estimate = Estimate(project_name="Test Project", days_in_rent=3)
    item = make_test_item(sku="A", price=1000.0, days=3)
    
    status = estimate.add_item(item)
    
    assert status == "added", "Status should be 'added'"
    assert len(estimate.items) == 1, "'estimate.items' should consist of 1 item"
    assert estimate.grand_total == 3000.0, "'estimate.grand_total' should be 3000.0"
    assert item.total_price == 3000.0, "'item.total_price' should be 3000.0"


def test_add_duplicate_item():
    """Тест 3: Добавление того же SKU увеличивает quantity, а не создает новую позицию"""
    estimate = Estimate(project_name="Test Project", days_in_rent=3)
    
    # Добавляем первый раз
    item1 = make_test_item(sku="A", price=1000.0, days=3)
    estimate.add_item(item1)
    
    # Добавляем тот же SKU второй раз
    item2 = make_test_item(sku="A", price=1000.0, days=3)
    status = estimate.add_item(item2)
    
    assert status == "quantity_updated", "Status should be 'quantity_updated'"
    assert len(estimate.items) == 1, "Should be 1"
    assert item1.quantity == 2, "Should be 2"
    assert estimate.grand_total == 6000.0, "Should be 6000.0"