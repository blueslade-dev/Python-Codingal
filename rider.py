print("==Ride Chooser==")
print("Enter 1 for Bike")
print("Enter 2 for Car")
choice = input("Enter 1 or 2 for ur vehicle choice").strip()
if choice == "1":
    print("You have two bike choices:")
    print("Enter 1 for Scooter")
    print("Enter 2 for Mountain Bike:")
    bike_choice = input("Enter your vehicle choice: 1 or 2").strip()

    if bike_choice == "1":
        print("Vehicle choosed: Scooter")
        print("Great for : Driving in Urban areas")
    elif bike_choice == "2":
        print("Vehicle choosed: Mountain Bike")
        print("Great for: Driving in irregular terrain/ mountains")
    else:
        print("Invalid bike choice, enter only 1 for Scooter, 2 for Mountain Bike")
elif choice == "2":
    print("You have two car choices:")
    print("Enter 1 for Hyundai car")
    print("Enter 2 for Van")
    car_choice = input("Enter 1 or 2 for your car choice:").strip()

    if car_choice == "1":
        print("Car chosen: Hyundai Car")
        print("Size: Ordinary like seen in urban areas")
        print("Carry capacity: 5 people")
        print("Great for family trips, or small squad trip")
    elif car_choice == "2":
        print("Car chosen: Van")
        print("Size: Big")
        print("Carry Capacity: 8")
        print("Great for trips or off-road adventures")
    else:
        print("Invalid car choice, enter 1 for Ordinary Hyundai Car and 2 for Van")
else:
    print("Invalid Vehicle choice")