items = ['Pen','Pencil','Eraser','Sharpener','Whitener']
stock_count = [2,4,1,2,0]
inventory = {item: count for item,count in zip(items,stock_count)}
print("Items in stock: ",inventory)

chosen_item = input("What Item would you like to buy?")
if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(f"{chosen_item} not found in stock")
    exit()   
   
price = [10,5,3,4,15]
item_bought = list(map(lambda p:p-2,price))

print("Thank you for the purchase!")
inventory[chosen_item] -= 1

print("Updated stock: ",inventory)