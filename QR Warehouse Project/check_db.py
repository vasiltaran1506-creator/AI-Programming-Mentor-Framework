import sqlite3

conn = sqlite3.connect(r"D:\VASILY\Projects\AI-Programming-Mentor-Framework\QR Warehouse Project\warehouse db\warehouse.db")
cursor = conn.cursor()

# Спрашиваем: "Сколько товаров в таблице equipment?"
cursor.execute("SELECT COUNT(*) FROM equipment")
count = cursor.fetchone()[0]
print(f"Товаров в базе данных: {count}")

# Выводим первые 3 товара, чтобы убедиться, что данные корректные
cursor.execute("SELECT sku, name, price_per_unit, available FROM equipment LIMIT 3")
rows = cursor.fetchall()

print("\nПервые 3 товара:")
for row in rows:
    print(f"  SKU: {row[0]}, Name: {row[1]}, Price: {row[2]}, Available: {row[3]}")

conn.close()