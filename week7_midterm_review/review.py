'''

for i in range(11):
    if i > 5:
        break  # just breaks the execution of the loop
    else:
        print(i)

## Continue
for i in range(11):
    if i % 2 == 0:
        continue
    else:
         print(i)




#### Write a program to calculate the sum and average of digits present in a given string
#### Input:   random289$18@#str849ing6
#### Expected output: Sum  55, Average: 6.11

input_str = input("Enter a string with numbers, letters, and symbols: ")

total = 0
count = 0


for char in input_str:
    if char.isdigit():
        total = total + int(char)
        count = count + 1
        avg = total / count

print(f'Sum: {round(total, 2)}, Average: {round(avg, 2)}')


####  Print the following pattern for a given number of rows

rows = int(input("Enter number of rows: "))

for i in range(0, rows):
    for j in range(i+1):
        print(j*2, end= " ")
    print()





### Write a program to print the number of digits, letters and special symbols in a given string
    ##  Input:   random289$18@str849ing6

input_str = input("Enter a string with numbers, letters, and symbols: ")

digits_list = []
letters_list = []
symbols_list = []

for char in input_str:
    if char.isdigit():
        digits_list.append(char)
    elif char.isalpha():
        letters_list.append(char)
    else:
        symbols_list.append(char)

print(f'Number of digits: {len(digits_list)}, Number of letters {len(letters_list)}, Number of symbols: {len(symbols_list)}')

'''

#### Number Guessing Game ####
    ### Choose a target value , ask the user to guess the value
    ### Display whether the number is greater than or less than the target value and ask user to guess again
    ###  Ex:  Too low!
    ###         Too High!
    ### Keep Track of number of guesses.  If guesses are > 10  →  The user loses
    ### Ask the user whether they want to continue the game.  Repeat the above if yes

import random

user_choice = "yes"
count = 0
result = ""
tries_left = 10 - count


while user_choice.lower() == "yes":
    user_guess = int(input("I have picked a number at random from 1-100. Try to guess it in 10 tries! Enter a number: "))
    count = count + 1
    target_value = random.randint(1, 100)
    for user_guess in range(1, 101):
        if user_guess == target_value and count <= 0:
            result = "You Win!"
            break
        elif user_guess != target_value and count <= 0:
            result = "Guess again"
        elif count > 10:
            result = "You lose!"
    if count == 10:
        result = "You lose. Play again? : "


    print(f'You picked {user_guess}. Computer picked {target_value}. {result}.  {count}.')











