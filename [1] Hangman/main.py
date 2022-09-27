# TASKS:
# 1. Update the word list to use the 'word_list' from hangman_words.py
# 2. Import the logo from hangman_art.py and print it at the start of the game.
# 3. If the user has entered a letter they've already guessed, print the letter and let them know.
# 4. If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

import os
def clear_console(): return os.system('clear')
    
import random
from countries import countries_list
from hangman_art import logo, stages

print(logo)

end_of_game=False
lives = len(stages)-1

chosen_word = random.choice(countries_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Please guess a letter.\n").lower()
    clear_console()
    
    if guess in display:
        print(f"You've already guessed {guess}!\n")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter    
    print(f"{' '.join(display)}\n")

    if guess not in chosen_word:
        print(f"You guessed {guess}. This is not in the word, you've lost a life!\n")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"Womp, womp. You lose!\n The word was {chosen_word}")
            
    if "_" not in display:
        end_of_game=True
        print("You win!")
        
    print(stages[lives])
