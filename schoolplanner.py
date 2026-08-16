print("==School Planner==")
day = input("Enter the day:").strip().capitalize()
homework = input("Is your homework done? yes/ no:").strip().lower()
weather = input("Is the weather sunny or cloudy:").strip().lower()
if day in ("Saturday","Sunday"):
    print("It is the weekend, have fun")
elif day == "Monday":
    print("It is Monday start of the week. Plan your week")
elif day in ("Tuesday","Wednesday","Thursday"):
    print("Its a regular school day")
elif day == "Friday":
    print("Its end of the weekdays.")
else:
    print("Day not recognised, Check the spelling")
if weather == "sunny" and homework == "yes":
    print("The weather is perfect and your hw is done! Go out and play")
elif weather == "sunny" or homework == "no":
    print("The weather is perfect you may go, But finish your hw first.")
elif weather == "cloudy" or not(homework == "no"):
    print("Great job doing ur hw! But the weather is not good so u can't play")
elif weather == "sunny" and day in ("Saturday","Sunday") and homework == "yes":
    print("Enjoy your careless weekend! Go out play as much you wish to!")
else:
    print("Complete your homwork or go out to play if homework is done and the weather is perfect")