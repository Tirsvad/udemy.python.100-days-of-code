import random
from hangman_art import logo, stages
from hangman_words import word_list
import os

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


# define our clear function

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


# Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(logo)

while not end_of_game:
    secret_word = " ".join(display)
    print("\nWord to guess " + secret_word)
    guess = input("\nGuess a letter: ").lower()

    # Check guessed letter if already guess
    if guess in display:
        print(f"You've already guessed {guess}")

    clear()
    print(logo)
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
