def calculate_discount(price, discount):
    total_price = price - (price * discount / 100)
    return total_price

prices = []
discounts = []

# collecting data
while True:
    user_input_price = input("Enter price (or press enter to calculate): ").replace(",",".").strip()
    if user_input_price == "":  
        print("Price collection ended")
        break
    else:
        price = float(user_input_price)
        prices.append(price)
        user_input_discount = input("Enter discount: ").replace(",",".").strip()
        discount = float(user_input_discount)
        discounts.append(discount)

print(f"Collected {len(prices)} goods, price calculataion:")

# calculating

grand_total = 0

for N in range(len(prices)):
    price = prices[N]
    discount = discounts[N] 

    #Printing result
    total_price = calculate_discount(price, discount)
    grand_total += total_price

    print(f"Good {N+1}: price {price}, discount {discount}%, total price: {total_price}")
print(f"Grand total price: {grand_total}")