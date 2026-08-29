from estimate_system.models import Estimate, EstimateItem
from catalog_loader import load_catalog
from estimate_constructor import process_scan, add_position_to_estimate
import exporter


def main():
    project_name = input("Enter project name:\n")
    config_path = r"D:\VASILY\Projects\AI-Programming-Mentor-Framework\Homework\Module 04\QR_Scanner\catalog.json"
    save_path = r"D:\VASILY\Projects\AI-Programming-Mentor-Framework\Homework\Module 04\QR_Scanner\estimates"
    catalog = load_catalog(config_path)
    estimate = Estimate(
        project_name=project_name,
        items=[],
        grand_total=0.0
    )
    while True:
        scan = input("Enter sku: ")
        if scan == "done":
            break
        estimate, status = process_scan(catalog, estimate, scan)
        if status == "not_found":
            already_in_estimate = any(item.sku == scan for item in estimate.items)
            if already_in_estimate:
                for item in estimate.items:
                    if item.sku == scan:
                        item.quantity += 1
                        item.total_price = item.price_per_unit * item.quantity
                        break
                estimate.grand_total = sum(position.total_price for position in estimate.items)
                print(f"Quantity updated (manually). Grand total: {estimate.grand_total}")
            else:
                manual_item = EstimateItem(
                    sku=scan,
                    name=input("Enter equipment name: "),
                    category="misc",
                    quantity=1,
                    price_per_unit=float(input("Enter equipment price per unit: ")),
                    total_price=0,
                    from_catalog=False
                )
                estimate, status = add_position_to_estimate(manual_item, estimate, catalog)
                print(f"Grand total: {estimate.grand_total}, Status: manually_added")
            continue
        print(f"Grand total: {estimate.grand_total}, Status: {status}")
    
    print(f"Total positions: {len(estimate.items)}, Grand total: {estimate.grand_total}")

    formated_estimate = exporter.format_estimate(estimate)
    exporter.save_estimate(save_path, formated_estimate, estimate.project_name)






if __name__ == "__main__":
    main()