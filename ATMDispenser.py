print("==ATM Dispenser==")
total_100 = total_50 = total_20 = total_10 = total_5 = 0
amount = int(input("Enter the amount you want:"))

if amount <= 0 :
    print("Invalid amount")
else:
    print("Valid amount")
    remainder = amount
    idx = 1
    while idx <= 6:
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx  == 4: value = 10
        elif idx == 5: value = 5
        else: value = 1

        count = remainder//value
        if count > 0:
            print(f"{count} * {value} unit note")
            remainder -= count * value
            if value == 100:
                total_100 += count
            elif value == 50: total_50 += count
            elif value == 20: total_20 += count
            elif value == 10: total_10 += count
            elif value == 5: total_5 += count

        idx += 1
print("Daily Denomination Report:")
for i in range (1,7):

    if i == 1:
        value = 100 
        total = total_100
    elif i == 2:
        value = 50 
        total = total_50
    elif i == 3:
        value = 20
        total = total_20
    elif i == 4:
        value = 10
        total = total_10
    elif i == 5:
        value = 5
        total = total_5

    if total > 0:
       print("Dispened value = ", total)