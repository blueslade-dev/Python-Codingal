import random

actions = ['rock','paper','scissors']
computer_choice = random.choice(actions)

while True:
    user_choice = input("Enter a choice(rock/paper/scissors)").lower().strip()
    if user_choice not in actions:
        print("Invalid choice. Try again")
        continue
    else:
        print("Correct Choice")
        
        if user_choice == computer_choice:
            print("Our choices are same. We have Tied!")
        elif computer_choice == "rock":
            if user_choice == "scissors":
                print("My rock has smashed your scissors! You Lost!")
            else:
                print("Your paper turned out to be invincible, You Won!")
        elif computer_choice == "paper":
            if user_choice == "scissors":
                print("Your scissors tore my paper apart! You Won!")
            else:
                print("Your rock cannot smash my paper! You Lost!")
        elif computer_choice ==  "scissors":
            if user_choice == "rock":
                print("Your rock has absoluted smashed my scissors. You Won!")
            else:
                print("Your paper can never beat my scissors! You Lost!")
        play_again = input("Wanna play again(yes/no)").strip().lower()
        if play_again != "yes":
            print("Fine. We can play later")
            break
        else:
            print("Lets play again!")
        


