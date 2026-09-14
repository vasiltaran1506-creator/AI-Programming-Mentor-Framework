import json
import sqlite3


conn = sqlite3.connect(r"D:\VASILY\Projects\AI-Programming-Mentor-Framework\QR Warehouse Project\warehouse db\warehouse.db")
cursor = conn.cursor()

with open("catalog.json", "r", encoding="utf-8") as file:
    catalog = json.load(file)

for item, data in catalog.items():
    equipment = {
        "sku": item,
        "name": data["name"],
        "price_per_unit": data["price_per_unit"],
        "category": data["category"],
        "available": data["available"],
        "total_stored": data["total_stored"]
    }

    sql_query = """
    INSERT OR IGNORE INTO equipment (sku, name, price_per_unit, category, available, total_stored)
    VALUES (?,?,?,?,?,?)
    """
    cursor.execute(sql_query, (equipment["sku"], equipment["name"], equipment["price_per_unit"], equipment["category"], equipment["available"], equipment["total_stored"]))
conn.commit()
conn.close()