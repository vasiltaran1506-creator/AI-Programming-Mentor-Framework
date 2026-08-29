# Estimate_constructor

## Dataclasses

Equipment
├── sku: str              — уникальный номер позиции
├── name: str             — название оборудования
├── price_per_unit: float — цена за одну единицу
├── category: str         — категория (light, camera, cable...)
└── in_stock: int         — количество единиц на складе

EstimateItem
├── sku: str              — код позиции
├── name: str             — название
├── category: str         — категория
├── quantity: int         — количество в смете
├── price_per_unit: float — цена за единицу
├── total_price: float    — итог по позиции (quantity × price_per_unit)
└── from_catalog: bool    — True если из каталога, False если вручную

Estimate
├── project_name: str             — название проекта
├── items: list[EstimateItem]     — список позиций сметы
└── grand_total: float            — общая сумма

## List of estimate_constructor functions:

process_scan(catalog, estimate, scan)
    ↓
обновлённая смета + статус

_find_scan_in_catalog(catalog, scan)
    ↓
позиция или None

_add_position_to_estimate(position, estimate)
    ↓
обновлённая смета

_check_in_stock(catalog, position)
    ↓
True или False

_calculate_total_position_price(position)
    ↓
итог по позиции

_calculate_grand_total(items)
    ↓
общая сумма

## List of statuses

"added"            → позиция добавлена из каталога впервые
"quantity_updated" → позиция уже была, количество увеличено
"not_found"        → sku не найден, нужен ручной ввод
"over_stock"       → отсканировано больше, чем на складе

## Function contracts:

- process_scan(catalog, estimate, scan)

Input: catalog: dict, estimate: Estimate, scan: str
Output: updated_estimate: Estimate, status: str
Normal absence: - 
Possible errors: - 
Side effects: - 
Responsibility:
    обработать один отсканированный sku:
    найти позицию в каталоге,
    добавить позицию в смету или сообщить, что позиция не найдена,
    проверить количество на складе,
    вернуть обновлённую смету и статус.

- find_scan_in_catalog(catalog, scan)

Input: catalog: dict, scan: str
Output: Equipment или None
Normal absence: Если scan не найден в каталоге, возвращает None
Possible errors: - 
Side effects: - 
Responsibility: Отвечает за поиск конкретной единицы оборудования в каталоге по скану кода. 

- add_position_to_estimate(EstimateItem, Estimate)

Input: EstimateItem (sku, name, category, quantity, price_per_unit, total_price, from_catalog), Estimate (items: list[EstimateItem])
Output: Estimate (items:list[EstimateItem])
Normal absence: Поведение при дубликате:
    если позиция с таким sku уже есть в смете,
    увеличить quantity существующей позиции.
Possible errors: -
Side effects: - 
Responsibility:
    добавить EstimateItem в Estimate.
    Если позиция с таким sku уже есть в Estimate — увеличить quantity.
    Если позиции ещё нет — добавить новую строку.

- check_in_stock(catalog, position)

Input: catalog: dict, position: EstimateItem
Output: bool
Normal absence: -
Possible errors: -
Side effects: - 
Responsibility:
    проверить, достаточно ли единиц оборудования на складе
    для запрашиваемого количества в смете.

