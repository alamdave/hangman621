while True:
    print("Enter a Letter:")
    guess = input()
    if len(guess) == 1 and guess.isalpha():
        print("Good Guess!")
        break
    else:
        print("Oops! That is not a valid input.")