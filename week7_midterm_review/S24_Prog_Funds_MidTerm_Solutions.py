
# 1. Print odd numbers until a given target

target_num = int(input('Enter a target number: '))

num = 1

while num <= target_num:
    if num % 2 != 0:
        print(num)
    num = num + 1





"""
1.	Coin-Toss Game
•	Ask the user to pick either heads or tails
•	Assign a random move to the computer by using random module and defining ranges for heads and tails
•	Heads win, Tails lose, Tie when both selections are the same
Example Output:  You picked heads, Computer picked tails – You Win!
Use a while loop to continue the game as long as user says “yes” in any case.
"""

"""
import random

comp_move = ''
result = ''

keep_playing = 'yes'  # taking this variable to keep track of whether user wants to play or not

while keep_playing == 'yes':  # keep repeating the game as long as the user wants to play
    user_move = input('Pick a move - Heads or Tails: ').lower()  # user could enter any case so converting to 
    # lowercase to make it easier for checking
    rand_num = round(random.random(),
                     2)  # taking a random value  between 0 and 1 and rounding it off to 2 decimal points

    if rand_num < 1 / 2:  # If the randomly chosen value is between 0 (including) ad 0.5, assign 'heads' to 
        # computer
        comp_move = "heads"
    else:
        comp_move = "tails"  # else i.e. if the randomly chosen value is greater than or equal to 0.5, assign 'tails' 
        # to computer

    # comparing user move to comp move and then assigning the result accordingly
    if user_move == 'heads' and comp_move == 'tails':
        result = 'You win'
    elif user_move == 'tails' and comp_move == 'heads':
        result = 'You lose'
    else:  # # In neither of the above cases, the only possible scenario is that both have chosen the same sides so 
        # result will be a tie
        result = 'Tie'

    # Printing the result using f-strings that dynamically grabs the corresponding user and comp moves along with the
    # result
    print(f'You picked {user_move}, computer picked {comp_move}. {result}')

    # Asking the users whether they want to continue playing. Could enter Yes or No in any  case so converting to lower
    keep_playing = input('Do you want to continue? Type yes or no: ').lower()
"""


"""
2.	Write a program that prints the multiples of 5 from the given list with the following conditions.
    a.	Continue with the next iteration of the loop if value is greater than 150
    b.	Break the loop if the value is greater than 500
    c.	Otherwise, print the item if it is divisible by 5.
"""
"""
list1 = [12, 75, 150, 180, 145, 525, 50]
for i in list1:  ## Just need to access each element from the already given list
    if i > 500:  ## if the value > 500, then just break the loop. No need to execute anything else
        break
    elif i > 150:  ## if value > 150 then skip the current iteration and continue with the next one
        continue
    else:  ## if n one of the above conditions are satisfied, then print the value only if it is divisible by 5
        if i % 5 == 0:
            print(i)
"""


"""
3. Odd Number Pattern
"""

"""
print()
rows = int(input('Enter the number of rows: '))
for i in range(1, rows + 1):  # Starting the range from 1 since we need odd numbers and first odd number is one
    for j in range(1, i + 1):  # Taking j's range from 1 to row number + 1. Ex: If we are on 2nd row, we need 2 odd 
        # numbers to be printed. So range( 1, 2+1) ==> range(1, 3) ==> 2 possible values for j ==> 1 and 2
        # Multiplying j with 2 which makes it even and then subtracting 1 to get the odd number 
        print((j * 2) - 1,
              end=" ")  # Using a space separator so that each value in a row stays in the same line with a 
        # space in between
    print() # Moving  next row to new line
"""

"""
# ALTERNATE APPROACH
rows = int(input('Enter the number of rows: '))
count = 0
for i in range(1, rows + 1):  # Starting the range from 1 since we need odd numbers and first odd number is one
    count = count + 1  # keeping track of how many odd numbers to print in the ith row
    for j in range(1, i + count):  # taking range to count+1 since we are starting from 1. Ex: if we want 2 odd 
        # numbers then since we are starting from 1 with count + 1, we will get range values 1, 2, 3 which will 
        # execute the below code 3 times with j = 1, j = 2, j = 3.
        # if j is divisible by 2, then j is not an odd number so will continue the loop with next value of j
        if j % 2 == 0:
            continue
        # if j i s not divisible by 2, then it is an odd number so it is printed
        else:
            print(j, end=' ')  # Using a space separator so that each value in a row stays in the same line with a 
            # space in between
    print()  # Moving next row to new line
"""


