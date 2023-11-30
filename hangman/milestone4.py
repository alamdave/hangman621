import random

class Hangman:
    #constuctor
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.list_of_guesses = []
        #word to be guessed
        self.word = random.choice(self.word_list)
        print(self.word)
        #word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        self.word_guessed = ["_" for num in range(len(self.word))]
        print(self.word_guessed)
        #num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
        self.num_letters = len(list(set(self.word)))

    def ask_for_input(self):
        while True:    
            print("Enter a Letter:")
            guess = input().lower()
            if not(len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif (guess in self.list_of_guesses):
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
    def check_guess(self, guess):
        if(guess in self.word):
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")



newgame = Hangman(["Apple", "Banana", "Cherry", "Guava", "Strawberry","Pear"])
newgame.ask_for_input()
