
#### Code Explanation

    # Files "hangman_ascii.py" and "words.py" are custom modules necessary for "main.py" to function
    # Random module is imported
    # "hangman_ascii" is called, "stages" and "logo" are imported.  These are used to create the ascii "hangman" art.
    # "words" is called, and "words_alpha" function is imported.  words_alpha contains the words list used by "main.py", selecting alpha characters only.  This ensures that the words list used only contains words that use alpha characters (some words had hyphens in them, making them impossible to guess).
    # A loop is started where if play_again equals "yes", the loop continues (game starts over).  When the game ends, the player is asked if they would like to play again. If they answer "yes" or "y", the game starts over.  If they answer anything else, the game ends.
    # A word is chosen randomly (using random  from words_alpha and set to variable chosen_word.
    # The length of the chosen word is set to variable len_chosen_word
    # The hangman logo is printed
    # word_display variable is initialized. Underscores are appended to word_display, using the length of the chosen word
        # Amount of underscores appended to word_display equals the amount of letters in the chosen word.
        # word_display is printed.
    # game_over variable is intially set to "False" and lives_left variable initially set to "7".
    # incorrect_guesses variable is initialzed.
    # While not game_over logic:
        # Player is asked to guess a letter:
            # if logic:
                # if the guessed letter is found in word_display list or incorrect_guesses list, player is informed that they have already guessed the letter as well as how many lives they have left.
            # elif logic:
                # if the guessed leter is not found in chosen_word list:
                    # Player is informed that their guessed later is not present in the chosen word and that they lose a life.
                    # live_left has 1 subtracted from it, player is informed how many lives they have left.
                    # The guessed letter is appended to the guessed_letter list
                # if lives left is equal to zero:
                    # game_over equals true
                    # Player is informed that the game is over and that they lose.
                    # The chosen word is printed.
                    # Player is given the option to play again.
            # else logic:
                # else logic applies when the guessed letter has not been guessed before and it is in the chosen word.
                # for logic:
                    # enumerate is used to loop through chosen_word.  Enumerate returns two values: index and value.  Index is the position of the current character and value is the charatcer at the position.
                    # if the character at a certain position matches the later guessed, the matching index in word_display is updated to change the underscore with the correctly guessed letter.
            # After each guess, word_display is printed
            # if '_' not in word_display logic:
                # if there are no longer any underscores left in word_display, the player wins.  This is because all letters in the chosen word have been guessed and all underscore have been updated with the correct letter.
                # game_over is updated to True.
                # Player is informed that the game is over and that they have won.
                # Player is given the option to play again
            # After each guess, the stage of the hangman ascii art is printed that corresponds with the amount of lives the player has left.

import random
from hangman_ascii import stages, logo
from words import words_alpha

# Debugging

play_again = "yes"

while play_again in ["yes", "y"]:
    chosen_word = random.choice(words_alpha).lower()
    len_chosen_word = len(chosen_word)
    # print(chosen_word)
    print(logo)
    word_display = []
    for _ in range(len_chosen_word):
        word_display.append('_')
    print(word_display)
    game_over = False
    incorrect_guesses = []
    lives_left = 7
    while not game_over:
        guessed_letter = input("Guess a letter: ".lower())
        if guessed_letter in word_display or guessed_letter in incorrect_guesses:
            print(f"You have already guessed this {guessed_letter}. Try again!")
            print(f"You have {lives_left} lives left.")
        elif guessed_letter not in chosen_word:
            print(f"Your guess '{guessed_letter}' is not present in the chosen word. You lose a life.")
            lives_left -= 1     # same as lives_left = lives_left -1
            print(f"You have {lives_left} lives left.")
            incorrect_guesses.append(guessed_letter)
            if lives_left == 0:
                game_over = True
                print("Game over. You lose!")
                print(f"The chosen word was '{chosen_word}'")
                play_again = input("Play again? y/n: ")
        else:
            for idx, val in enumerate(chosen_word):
                if val == guessed_letter:
                    word_display[idx] = guessed_letter
        print(word_display)
        if '_' not in word_display:
            game_over = True
            print("Game over. You win!")
            play_again = input("Play again? y/n: ")
        print(stages[lives_left])