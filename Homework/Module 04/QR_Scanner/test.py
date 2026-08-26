from catalog_loader import load_catalog


def main():
    catalog = load_catalog(r"D:\VASILY\Projects\AI-Programming-Mentor-Framework\Homework\Module 04\QR_Scanner\catalog.json")

    print("Тип каталога:", type(catalog))
    print("Количество позиций:", len(catalog))
    print()

    for sku, equipment in catalog.items():
        print(f"sku: {sku}")
        print(f"  Тип: {type(equipment)}")
        print(f"  name: {equipment.name}")
        print(f"  category: {equipment.category}")
        print(f"  price_per_unit: {equipment.price_per_unit}")
        print(f"  in_stock: {equipment.in_stock}")
        print()


if __name__ == "__main__":
    main()