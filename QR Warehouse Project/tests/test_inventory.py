import pytest
from models import Equipment
from estimate_constructor import Inventory
from logger import ConsoleLogger

# Вспомогательная функция (фикстура), чтобы не создавать оборудование вручную в каждом тесте
def make_test_equipment(sku="TEST-001", available=5):
    return Equipment(
        sku=sku,
        name="Test Light",
        price_per_unit=1000.0,
        category="LIGHT",
        available=available,
        total_stored=10
    )

def test_inventory_registers_equipment():
    """Тест 1: Склад успешно принимает оборудование и записывает его в _stock"""
    inventory = Inventory(logger=ConsoleLogger())
    eq = make_test_equipment(available=3)
    
    inventory.register_equipment({"TEST-001": eq})

    assert inventory._stock["TEST-001"] == 3, "Result should be 3"


def test_reserve_success():
    """Тест 2: Успешное бронирование уменьшает остаток и возвращает статус 'reserved'"""
    inventory = Inventory(logger=ConsoleLogger())
    eq = make_test_equipment(available=2)
    inventory.register_equipment({"TEST-001": eq})
    
    # Вызываем метод бронирования
    status, returned_eq = inventory.check_and_reserve("TEST-001")

    assert status == "reserved", "Status should be 'reserved'"
    assert inventory._stock["TEST-001"] == 1, "Should be 1 stocked"


def test_reserve_over_stock():
    """Тест 3: Попытка забронировать то, чего нет (available=0), возвращает 'over_stock' и НЕ меняет остаток"""
    inventory = Inventory(logger=ConsoleLogger())
    eq = make_test_equipment(available=0) # На складе пусто!
    inventory.register_equipment({"TEST-001": eq})
    
    status, returned_eq = inventory.check_and_reserve("TEST-001")
    
    assert status == "over_stock", "Status should be 'over_stock'"
    assert inventory._stock["TEST-001"] == 0, "Stock should be 0"


def test_reserve_not_found():
    """Тест 4: Запрос несуществующего SKU возвращает 'not_found' и None"""
    inventory = Inventory(logger=ConsoleLogger())
    # Склад пустой, мы ничего не регистрировали
    
    status, returned_eq = inventory.check_and_reserve("FAKE-999")
    
    assert status == "not_found", "Status should be 'not_found'"
    assert returned_eq == None, "returned_eq should be None"