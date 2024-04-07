
import random
from hangman_ascii import stages, logo
from words import words
# words = ["forest", "mountain", "ocean", "surprise"]
chosen_word = random.choice(words).lower()
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
try_again = "no"
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

    else:
        for idx, val in enumerate(chosen_word):
            if val == guessed_letter:
                word_display[idx] = guessed_letter
    print(word_display)
    if '_' not in word_display:
        game_over = True
        print("Game over. You win!")
    print(stages[lives_left])









