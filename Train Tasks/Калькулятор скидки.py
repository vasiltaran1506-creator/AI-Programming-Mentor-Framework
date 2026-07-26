price = float(input("Введите цену товара: ").replace(",", "."))
discount = float(input("Введите процент скидки: ").replace(",", "."))

discount_rate = discount / 100
total_price = price - (price * discount_rate)

print(f"Итоговая цена: {total_price}")