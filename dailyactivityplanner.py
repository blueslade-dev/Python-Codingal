temp = int(input("Enter the temperature outside: (in Celsius)"))
print(f"Temperature : {temp}°C")
if temp > 20:
    print("Stay indoors and read books or magazines or comics!")
elif temp <= 20:
    print("Play outdoors with your friends!")
elif -50 < temp < 60:
    print("Stop joking around")
else:
    print("You have done something wrong. Please try to fill the info again")

is_raining = input("Is it raining? (Yes/No)").capitalize().strip()
print(f"Raining: {is_raining}") 
if is_raining == "Yes":
    print("Don't go outside, stay indoors and play indoor games with ur family or read books")
elif is_raining == "No":
    print("Go and play outside with your friends")
else:
    print("U have done smth wrong")

homework_time = int(input("How many hours have you been doing your homework"))
print(f"My homework time: {homework_time} hrs")
if homework_time > 2:
    print("Go out and play, you have done enough work!")
else:
    print("Do more work then go out and play")

has_freetime = input("Do you have free time now?(Yes/No)").capitalize().strip()
print(f"Has Free Time: {has_freetime}")
if has_freetime == "Yes":
    print("It's your hobby time!")
elif has_freetime == "No":
    print("Its your planning time.")

print(f"Temperature : {temp}°C")
print(f"Raining: {is_raining}") 
print(f"Homework time: {homework_time} hrs")
print(f"Has Free Time: {has_freetime}")