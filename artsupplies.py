def greet_customer():
    print("Welcome! to my Art Supplies Shop!")
    print("Best-quality Art supplies for you!")

greet_customer()

price_per_art_item = round(float(input("Enter the price per art item in ₹:")), 2)
no_of_items_bought = int(input("Enter the Number of items bought:"))

def calculate_total(price,no_of_items):
    return no_of_items * price

total = round(calculate_total(price_per_art_item, no_of_items_bought), 2)

def calculate_change(paid,price):
    return paid - price

while True:
    paid_per_item = float(input("Amount Customer paid (in ₹):"))
    total_paid = paid_per_item * no_of_items_bought
    if total_paid < total:
        print(f"₹{total - total_paid} left to be paid")
        print("Returning money back and asking customer for the money again....")
        continue
    elif total_paid > total:
        print("Change: ₹", total_paid - total)
        break 
    else:
        print("No change is due")
        break 

change = calculate_change(total_paid, total)
def thank_you_message():
    if no_of_items_bought > 5:
        print("Big Purchase! Thanks for ur support")
    else:
        print("Thanks for coming to our shop!")

thank_you_message()

print("\n==ART SUPPLIES PURCHASE BILL==")
print("\nPrice per Art Supply: ₹", price_per_art_item)
print("\nNumber of Items brought: ", no_of_items_bought)
print("\nTotal Cost: ₹",total)
print("\nAmount paid by customer: ₹",total_paid)
print("\nChange Due: ₹",change)
print("\n==============================")

