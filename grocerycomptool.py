rice_price = 50
milk_price = 20
fruit_price = 40
basket_no = 3
family_members = 5

basket_cost_per_person = (rice_price + milk_price + fruit_price) * basket_no / family_members 

print("Grocery cost per person:",basket_cost_per_person)

total_items = int(input("\nEnter total no of grocery items:"))
people = int(input("\nEnter the no of family members:"))
if total_items % people == 0:
    print(f"\n{total_items} grocery items \ncan be divided among \n{people}people")
else:
    print(f"\n{total_items} grocery items \ncannot be divided among \n{people} people. Remainder:{total_items % people} grocery items")
recorded_average = 750
incorrect_weekly_cost = 850
correct_weekly_cost = 800
no_of_weeks = 3

total = recorded_average * no_of_weeks
corrected_total = ((total - incorrect_weekly_cost) + correct_weekly_cost)
corrected_mean = corrected_total/no_of_weeks
print("\n Corrected Total:", corrected_total)
print("\n Corrected Mean:",corrected_mean)

storeA = 500
storeB = 400
storeC = 550
avg = storeA + storeB + storeC/ 3
if avg >= storeA and storeB and storeC:
    print("Cheap stuff in all stores!")
elif avg >= storeA:
    print("Cheap stuff in Store A")
elif avg >= storeB:
    print("Cheap goods in Store B") 
elif avg <= storeA and storeB:
    print("Goods are expensive in Stores A and B")
elif avg == storeC and storeB and storeA:
    print("Ordinary costs in all stores")
else:
    print("Some other sort of combination present")