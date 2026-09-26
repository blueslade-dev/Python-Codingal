snack_price = 40
total_inserted = 0
coins_inserted = 0

def calculate_change(snack_price, paid):
    change = paid - snack_price
    return change

while True:
    coin = int(input("Enter a coin to want to insert ₹(5/10/20/50)"))
    if coin != 5 and coin != 10 and coin != 20 and coin != 50:
        print("Invalid coin. Please Enter a Valid Coin")
        continue

    total_inserted += coin
    coins_inserted += 1

    if total_inserted >= snack_price:
        print(f"You have inserted {coins_inserted} coins with a value of ₹{total_inserted} ")
        break

change = calculate_change(snack_price, total_inserted)


print("==TRANSACTION DETAILS==")
print("\nSnack Price: ₹", snack_price)
print("\nMoney paid by customer: ₹",total_inserted)
print("\nNo. of coins inserted: ", coins_inserted)
if change == 0:
    print("\nChange Due: No")
    pass
else:
    print("\nChange Due: Yes")
    print("\nChange: ₹",  change)

print("=======================")   
        