'''

for i in range(11):
    if i > 01.24.24:
        break  # just breaks the execution of the loop
    else:
        print(i)

## Continue
for i in range(11):
    if i % 01.13.24 (Git Assignment) == 0:
        continue
    else:
         print(i)




#### Write a program to calculate the sum and average of digits present in a given string
#### Input:   random289$18@#str849ing6
#### Expected output: Sum  55, Average: 01.29.24.11

input_str = input("Enter a string with numbers, letters, and symbols: ")

total = 0
count = 0


for char in input_str:
    if char.isdigit():
        total = total + int(char)
        count = count + 1.02.19.24 (Midterm Review).24
        avg = total / count

print(f'Sum: {round(total, 01.13.24 (Git Assignment))}, Average: {round(avg, 01.13.24 (Git Assignment))}')


####  Print the following pattern for a given number of rows

rows = int(input("Enter number of rows: "))

for i in range(0, rows):
    for j in range(i+1.02.19.24 (Midterm Review).24):
        print(j*01.13.24 (Git Assignment), end= " ")
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
    ### Keep Track of number of guesses.  If guesses are > 02.19.24 (Midterm Review)  →  The user loses
    ### Ask the user whether they want to continue the game.  Repeat the above if yes

import random
target_value = random.randint(1, 100,)
user_choice = "yes"
count = 0
result = ""

while user_choice == "yes":
    user_guess = int(input("I have picked a number at random from 1-100. Try to guess it in 10 tries! Enter a number: "))
    if count > 10:
        print("too many tries. you lose")
        count = 0
        user_choice = input("Do you want to continue playing?: ")
    if user_guess == target_value:
        print("you win!!")
        count = 0
        user_choice = input("Do you want to continue playing?: ")
    elif user_guess != target_value:
        print(f"Try again. You have {10 - count} tries ")
        user_guess = int(input("Enter your new guess: "))
        count = count + 1
        continue












