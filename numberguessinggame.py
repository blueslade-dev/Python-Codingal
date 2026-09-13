secret = 18

total_guesses = 5
i = 0
while i <= 5:
    guess = int(input("Guess a number between 1 and 50: "))
    while 0 >= guess or guess >= 50:
        print("\nInvalid Guess the number must be between 1 and 50")
        guess = int(input("\nGuess a number between 1 and 50: "))

    i += 1
    guesses_left = total_guesses - i
    if guess == secret:
        print("\nYou have made the correct guess!")
        print("\nYOU WON!")
        break
    elif guess != secret:
        print(f"\nYou have {guesses_left} guesses left")
        print("❤️ "*guesses_left, " remaining")
        if guesses_left == 0:
            print("\nYou have lost the game. The secret number is", secret)

