temp = int(input("Enter temperature in Celcius"))
if temp < 20:
    outfit = "jacket"
    print("It is cold")
    print("Wear a ", outfit)
else:
    outfit = "t-shirt"
    print("It is hot")
    print("Wear a",outfit)

is_raining = input("Is it raining? (Yes/No)")
if is_raining == "Yes":
    print("Carry an umbrella")
else:
    print("Do not carry umbrella")

wind_speed = int(input("Enter wind speed in kmph:"))
if wind_speed > 30:
    print("Wear a windshielder over your", outfit)
else:
    print("No need to wear a windshielder over your", outfit)

has_puddles = input("Does the soil has puddles? (YES/NO)")
if has_puddles == "YES":
    shoe = "Boot"
    print("Wear", shoe)
else:
    shoe = "slinker"
    print("Wear", shoe)
print("Weather")
print("Temperature :", temp, "Degree Celsius")
print("Raining:", is_raining)
print("Wind Speed :",wind_speed, "kmph")
print("Has Puddles:", has_puddles  )

