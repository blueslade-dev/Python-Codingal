def greet_customer():
    print("Welcome to my lemonade stand!")
    print("Special lemonade selling for you!")

greet_customer()

price_per_cup = float(input("Enter the price per cup sold: "))
cups_sold = int(input("Enter the number of cups sold: "))

def calculate(price, cups):
    total = price * cups
    return total

total_cost = calculate(price_per_cup,cups_sold)

rounded_cost = round(total_cost, 2)

print("Total cost: ",rounded_cost)

amt_paid = float(input("Enter the amount paid by the customer: "))
def change(amt_paid, total_cost):
    change = amt_paid - total_cost
    return change

change_due = change(amt_paid, rounded_cost)
rounded_change = round(change_due, 2)

print("Change due: ", rounded_change)

def thankyoumessage(cups):
    if cups >= 5:
        return "Big order! Thanks for your support"
    else:
        return "Thanks for standing in our shop"

closing_message = thankyoumessage(cups_sold)

print("\n=== LEMONADE STAND RECEIPT===")
print("Price per cup: ",price_per_cup)
print("Cups sold: ", cups_sold)
print("Total cost: ", rounded_cost)
print("Amount Paid: ", amt_paid)
print("Change due: ", rounded_change)
print(closing_message)
print("==============================")