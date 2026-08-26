from models import Equipment, EstimateItem, Estimate


def main():
    equipment = Equipment(
        sku="LIGHT-001",
        name="LED-панель Aputure 600d",
        price_per_unit=3500,
        category="lighting",
        in_stock=10
    )

    print("Тип объекта:", type(equipment))
    print("sku:", equipment.sku)
    print("name:", equipment.name)
    print("price_per_unit:", equipment.price_per_unit)
    print("category:", equipment.category)
    print("in_stock:", equipment.in_stock)


if __name__ == "__main__":
    main()