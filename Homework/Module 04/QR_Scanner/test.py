from estimate_system.models import Estimate
from estimate_constructor import process_scan
from catalog_loader import load_catalog

path = r"D:\VASILY\Projects\AI-Programming-Mentor-Framework\Homework\Module 04\QR_Scanner\catalog.json"
catalog = load_catalog(path)
estimate = Estimate(project_name="Test", items=[], grand_total=0.0)

estimate, status1 = process_scan(catalog, estimate, "LIGHT-001")
print(f"1-й скан: статус={status1}, позиций={len(estimate.items)}, grand_total={estimate.grand_total}")

estimate, status2 = process_scan(catalog, estimate, "LIGHT-001")
print(f"2-й скан: статус={status2}, позиций={len(estimate.items)}, grand_total={estimate.grand_total}")