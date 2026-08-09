field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

total = field1 + field2 + field3 + field4 + field5
average = total/5

print("Total harvest:", total,"kg")
print("Average:",average,"kg")

price_per_kg = 15
earnings = total * price_per_kg
print("Total earnings: ₹", earnings)

bags = total // 25
leftover = total % 25
print("Bags packed:",bags)
print("Leftover grains:",leftover,"kg")

last_year = 500
print("Better than last year?: ",total > last_year)
print("Same as last year?:  ",total == last_year)
print("Atleast good? :", total >= last_year)

total += 30
print("Bonus crop :",total)
total -= 15
print("Seed reserve:",total)

bags = total // 25
print("Final Bags Packed:",bags)