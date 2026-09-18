print("=== Grocery Billing Queue ===\n")

low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0

billing = True

while billing:
    customer_name = input("Enter customer name: ")
    item_count = int(input("How many items are you buying? "))

    if item_count <= 0:
        print("Invalid item count. Please try again.")
        continue

    customer_total = 0
    item_number = 1

    while item_number <= item_count:
        item_name = input("Enter item name: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        if price <= 0 or quantity <= 0:
            print("Invalid price or quantity. Please try again.")
            continue

        item_total = price * quantity
        print(f"{item_name}: {quantity} x {price} = {item_total}")

        customer_total += item_total

        if price < 50:
            low_price_items += quantity
        elif price <= 100:
            medium_price_items += quantity
        else:
            high_price_items += quantity

        item_number += 1

    customers_served += 1
    total_sales += customer_total

    print(f"{customer_name}'s total: {customer_total}")

    next_customer = input("Next customer? (yes/no): ")

    if next_customer != "yes":
        billing = False

for band in range(1, 4):
    if band == 1:
        print("Low price items: ", end="")
        count = low_price_items
    elif band == 2:
        print("Medium price items: ", end="")
        count = medium_price_items
    else:
        print("High price items: ", end="")
        count = high_price_items

    for item in range(count):
        print("*", end="")

    print()

print("Customers served:", customers_served)
print("Total sales:", total_sales)
