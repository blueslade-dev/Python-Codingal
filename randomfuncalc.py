import math
import random

lucky_no = random.randint(1,10)
print("Random Lucky number between 1 and 10: ", lucky_no)

fun_choices = ['Coding','Gaming','Watching TV','Watching YouTube','Travelling']
random_choice = random.choice(fun_choices)
print("A Random fun activity you can do is: ", random_choice)

secret = random.randint(1,5)
print("Computer>I have generated a random number from 1 to 5 (both inclusive).")
print("Your job is to guess it.")

attempts = 0
while True:
    try:
       user_input = int(input("Enter a number between 1 and 5 (both inclusive:)"))
       if user_input < 1:
           raise ValueError("Input cannot be less than 1")
           
       elif user_input > 5:
           raise ValueError("Input cannot be more than 1")

       elif user_input == secret:
           attempts += 1
           print(f"Correct Guess!! Attempt #{attempts}")
           if attempts <= 2:
               print("Impressive! You have a high guessing power maybe.")
           else:
               print("Good job on guessing the correct number.")
           break

       else:
           attempts += 1
           print(f"Try again. Attempt #{attempts}")           
           continue
    except ValueError:
        print("Please enter a valid number between 1 and 5 (both inclusive)")
        continue
    except:
        print("Kindly enter a valid integer between 1 and 5 (both inclusive)")
        continue

while True:
    try:
        decnum = float(input("Enter a decimal number:"))
    except:
        print("Invalid number. Try again")
        continue 
    else:
        print("Correct Number.")
        break    

ceilval = math.ceil(decnum)
floorval = math.floor(decnum)
print(f"Ceiling Value of {decnum}: {ceilval} \nFloor Value of {decnum}: {floorval}")

a = +5
b = -8
c = math.copysign(a,b)
print("Copied sign of b to a:", c)
r = random.randint(-100,100)
x = math.fabs(r)
print(f"Absolute value of {r} is {x}")
while True: 
    try:
     num1 = int(input("Enter a number:"))
     num2 = int(input("Enter another number"))
     print(f"Gcd of {num1} and {num2} is:", math.gcd(num1,num2))
    except:
     print("Please kindly enter valid numbers")
     continue
    else:
     break