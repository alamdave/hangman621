word = "apple"
def ask_for_input():
    while True:    
        print("Enter a Letter:")
        guess = input().lower()
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Oops! That is not a valid input.")
    check_guess(guess)

def check_guess(guess):
    if(guess in word):
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


ask_for_input()
