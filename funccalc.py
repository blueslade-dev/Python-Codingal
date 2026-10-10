def add():
    print("Addition of two numbers:\n")
    try:
       num1 = float(input("Enter a number: "))
       num2 = float(input("Enter another number: "))
       sum = num1 + num2
    except ValueError as w:
        print("Error: ", w)   
    
   
    return sum 


def subtract():
    print("Subtraction of two numbers:\n")
    try:
        num3 = float(input("Enter a number: "))
        num4 = float(input("Enter another number: "))
        sub = num3 - num4
    except ValueError as q:
        print("Error: ", q)
    

    return sub 



def multiply():
    print("Multiplication of two numbers:\n")
    try:
        num5 = float(input("Enter a number:"))
        num6 = float(input("Enter another number: "))
        prod = num5 * num6
    except ValueError as d:
        print("Error: ", d)
    

    return prod



def divide():
    print("Division of two numbers:\n")
    try:
        num7 = float(input("Enter a number:"))
        num8 = float(input("Enter another number:"))
        division = num7/num8
    except ValueError as px:
        print("Error: ", px)
    except ZeroDivisionError as cx:
        print("Error: ",cx)
    
    print(division)



while True:
   choice = input("What do you wish to do? 1 for Addition 2 for Subtraction 3 for Multiplication 4 for Division: ")
   if choice != '1' and choice != '2' and choice != '3' and choice != '4':
        print("Invalid choice Please Try Again")
        continue
   else:
        print("Your choice is okay")
        break

if choice == "1":
    print(add())
elif choice == "2":
    print(subtract())
elif choice == "3":
     print(multiply())
elif choice == "4":
     divide()