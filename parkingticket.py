def calculatechange(paid,price):
    change = paid - price
    return change

ticket_price = 45
total_inserted = 0
coins_inserted = 0


while True:
    coin = int(input("Enter a coin you want to register ₹(5/10/20/50)"))
    if coin != 5 and coin != 10 and coin != 20 and coin != 50:
        print("Invalid coin please give a valid coin")
        continue
    
    total_inserted += coin
    coins_inserted += 1

    if total_inserted >= ticket_price:
        print("You have paid all the money")
        break

change = calculatechange(total_inserted, ticket_price)

print("\n==TRANACTION DETAILS==")
print("\nTicket Price: ",ticket_price)
print("\nMoney paid by the customer: ",total_inserted)
print("\nNo. of Coins inserted by the customer: ",coins_inserted)
if change == 0:
    print("\nNo change is due")
    pass
else:
    print(f"\nChange of ₹{change} has been given to the customer.")

print("\n======================")
