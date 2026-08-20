day = input("Enter today's day: ").capitalize().strip() 


weather = input("What's the wheather? (sunny/ cloudy / rainy)").lower().strip()
book_due = input("Do you have a book that needs to be returned? (Yes/ No)").capitalize().strip()
print(f"==Library Visit Planner for {day}==")
if day in ("Saturday","Sunday"):
    print("It's a weekend, the library is closed.")
elif day == "Monday":
    print("Today is Mornday the beginning of school! Library is open. ")
elif day in ("Tuesday","Wednesday","Thursday"):
    print("Today is a Regular School Day, Library is open.")
elif day == "Friday":
    print("It's the end of the week, Library is open.")
else:
    print("Invalid day. Check spelling , The advice would continue but you wont get good advice")
    
if day in ("Saturday","Sunday") and book_due == "Yes":
    print("It is a weekend, Return your book when you come back on Monday.")
elif day not in ("Saturday", "Sunday") and weather == "sunny" and book_due == "Yes":
    print("Go to school library and return the book")
elif day not in ("Saturday", "Sunday") and weather == "cloudy" and book_due == "Yes":
    print("Go to school but take an umbrella with you and return the book.")
elif day not in ("Saturday", "Sunday") and weather == "rainy" and book_due == "Yes":
    print("If you can come , come with an umbrella and return your book. If raining is heavy no need to come")
elif day not in ("Saturday","Sunday") and (weather == "rainy" or weather == "cloudy") and book_due == "No":
    print("If you think you can come to school without getting sick, then only come.")
elif day not in ("Saturday", "Sunday") and weather == "sunny" and book_due == "No":
    print("Come to school without thinking about dued books. Issue any book you wish to!")
else:
    print("If weather is bad its not recommended to come to school. If its good come, and return any dued books or issue a new book if u don't have a book to return.")