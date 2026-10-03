import random
number = random.randint(1,10)
playing = True
print("I have guessed a number between 1 to 10 (both inclusive).\n ")
while playing:
    guess = int(input("Guess a number between 1 and 10(both inclusive): "))
    if guess == number:
        print("Correct guess!")
        print("The number is: ",number)   
        break 
    else:
        print("Incorrect guess")

