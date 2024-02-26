'''

user_input = input("What's you're name:  ")
user_choice = user_input

who = ""
result = ""

if user_choice == "Mary":
    who = "Mary"
    result = "Is Hawt"
elif user_choice == "Marie":
    who = "Marie"
    result = "where's my Newports ??"
else:
    who = user_choice
    result = "who da fukk is that??"
print(f'{who} {result} !!!!!')

'''

import random
random = random.randint(1, 100)
user_guess = "yes"
count = 0
result = ""
tries_left = 10 - count


while user_guess == "yes":
    user_choice = int(input("I have picked a number at random from 1-100. Try to guess it in 10 tries! Enter a number: "))
    count = count + 1
    for user_choice in range(1, 101):
        if user_choice == random and count <= 0:
            result = "You Win!"
            break
            if user_choice != random and count <= 0:
                result = "Guess again"
            if count > 10:
                result = "You lose!"
            if count == 10:
                result = "You lose. Play again? : "

        print(f'You picked {user_choice}. Computer picked {random}. {result}.  {count}.')