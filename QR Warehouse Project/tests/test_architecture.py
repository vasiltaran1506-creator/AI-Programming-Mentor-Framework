import pytest
from models import Equipment
from repository import EquipmentRepository
from estimate_constructor import Inventory

# ==========================================
# ТЕСТОВЫЙ ДВОЙНИК (Каскадёр / Fake)
# ==========================================
class InMemoryEquipmentRepository(EquipmentRepository):
    """
    Fake-репозиторий для тестов. 
    Он не читает JSON и не ходит в базу данных. 
    Он просто хранит объекты Equipment в обычном словаре.
    """
    def __init__(self, initial_data: dict[str, Equipment]):
        self._data = initial_data

    def find_by_sku(self, sku: str) -> Equipment | None:
        return self._data.get(sku)

    def update_available(self, sku: str, quantity_change: int) -> None:
        if sku in self._data:
            self._data[sku].available += quantity_change


# ==========================================
# ТЕСТЫ АРХИТЕКТУРЫ (Твоя очередь)
# ==========================================

def test_inventory_successfully_reserves_via_repository():
    """Тест 1: Успешное бронирование. Inventory должен приказать репозиторию уменьшить available."""
    # ARRANGE (Подготовка)
    eq = Equipment(
        sku="CAM-001", name="Test Camera", price_per_unit=1000.0, 
        category="CAMERA", available=5, total_stored=10
    )
    fake_repo = InMemoryEquipmentRepository({"CAM-001": eq})
    inventory = Inventory(repository=fake_repo)

    # ACT (Действие)
    status, equipment = inventory.reserve_equipment("CAM-001")

    assert status == "reserved"
    assert equipment is not None
    assert fake_repo._data["CAM-001"].available == 4

def test_inventory_rejects_over_stock_via_repository():
    """Тест 2: Товара нет в наличии. Inventory должен проверить репозиторий и отказать."""
    # ARRANGE (Подготовка)
    eq = Equipment(
        sku="LIGHT-999", name="Broken Light", price_per_unit=500.0, 
        category="LIGHT", available=0, total_stored=5 # Доступно 0!
    )
    fake_repo = InMemoryEquipmentRepository({"LIGHT-999": eq})
    inventory = Inventory(repository=fake_repo)

    # ACT (Действие)
    status, equipment = inventory.reserve_equipment("LIGHT-999")
    
    assert status == "over_stock"
    assert fake_repo._data["LIGHT-999"].available == 0

def test_inventory_releases_equipment_back_to_repository():
    """Тест 3: Возврат на склад. Inventory должен приказать репозиторию увеличить available."""
    # ARRANGE (Подготовка)
    eq = Equipment(
        sku="CABLE-001", name="Test Cable", price_per_unit=50.0, 
        category="CABLE", available=10, total_stored=20
    )
    fake_repo = InMemoryEquipmentRepository({"CABLE-001": eq})
    inventory = Inventory(repository=fake_repo)

    # ACT (Действие)
    inventory.release_equipment("CABLE-001", 3) # Возвращаем 3 штуки

    assert fake_repo._data["CABLE-001"].available == 13