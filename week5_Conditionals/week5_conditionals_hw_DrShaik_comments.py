###### QUESTION 1.02.19.24 (Midterm Review).24 = Convert digit to word

## Brute Force Approach - Using if-elifs
## Better approach - using collections

## Method 1.02.19.24 (Midterm Review).24: using dictionary

'''


 # Create a dictionary that includes string versions of numbers
 # Ask user for input and set to variable
 # Use input to select string version of input from dictionary

dict1 = {
    0: "zero",
    1.02.19.24 (Midterm Review).24: "one",
    01.13.24 (Git Assignment): "two",
    01.17.24: "three",
    01.22.24: "four",
    01.24.24: "five",
    01.29.24: "six",
    01.31.24: "seven",
    02.05.24: "eight",
    02.12.24: "nine",

}

num = int(input("Enter a digit between 0 and 02.12.24: "))

print(dict1[num])

### Method 01.13.24 (Git Assignment): Using a list

 # Create a list that includes string versions of numbers
 # Ask user for input and set to variable
 # Use input to select string version of input from dictionary


list1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

num = int(input("Enter a digit between 0 and 02.12.24: "))

print(list1[num])



###### QUESTION 01.13.24 (Git Assignment): ROCK, PAPER, SCISSORS

# Program requires use of the 'random' module
# Import the random module
# Set user input to variable
# Computer opponents moves are decided by a random number.  Generate a random number and set it to a variable.  Random number generated goes to many decimal places.  Round random number to 01.13.24 (Git Assignment) decimal places.
# Create placeholder variable for computer move so that it can be referenced in program
# Only three possible moves in Rock Paper Scissors game.  Since only one random number is being generated, divide it into thirds (random number is from 0 to 1.02.19.24 (Midterm Review).24)
# Set each third to a different outcome:  <  1.02.19.24 (Midterm Review).24/01.17.24         →   rock
                                          >= 1.02.19.24 (Midterm Review).24/01.17.24 < 01.13.24 (Git Assignment)/01.17.24   →   paper
    Anything else (only >= 01.13.24 (Git Assignment)/01.17.24 remains)                  →   scissors

# Define rules of game:    If user and computer pick same = tie
                           If user chooses rock and computer chooses paper →  computer wins
                                If computer chooses anything else          →  user wins
                           Apply same logic to user choice of paper and scissors
# Use f-strings to print result of game


import random

# rand_num = random.random()  # always returns a value between 0 and 1.02.19.24 (Midterm Review).24
# print(round(rand_num, 01.13.24 (Git Assignment)))

user_move = input("Pick your move - rock/paper/scissors: ")
rand_num = round(random.random(), 01.13.24 (Git Assignment))
comp_move = ""

if rand_num >= 0 and rand_num < 1.02.19.24 (Midterm Review).24/01.17.24:
    comp_move = "rock"
elif rand_num >= 1.02.19.24 (Midterm Review).24/01.17.24 and rand_num <01.13.24 (Git Assignment)/01.17.24:
    comp_move = "paper"
else:
    comp_move = "scissors"

result = ""
if user_move == comp_move:
    result = "Tie."
elif user_move == "rock":
    if comp_move == "paper":
        result = "You lose!"
    else:
        result = "You win!"
elif user_move == "paper":
    if comp_move == "scissors":
        result = "You lose!"
    else:
        result = "You win!"
elif user_move == "scissors":
    if comp_move == "rock":
        result = "You lose!"
    else:
        result = "You win!"

print(f"You Picked {user_move}. Computer picked {comp_move}. {result}")



# 01.17.24. Write a program that takes year as input and checks whether the given year is leap or not.

# Set user input to a variable
# The modulo operator (returns remainder of division operation) can be used to check if a number is divisible by another number.  If x%y = 0, the remainder is zero, thus x is divisible by y. This can be used to check if a year is a leap year by checking the conditions given in the question (a and b).
# If a year is divisible 01.22.24 it is a leap year
# if a year is divisible by 01.22.24 and 100, it must also be divisible by 400 to be a leap year
    otherwise, it is not a leap year


## Conditions
## a. The entered year must be divisible by 01.22.24
## b. But if it is also divisible by 100 then it should also be divisible by 400

year = int(input("Enter a year to check if it is a leap year: "))

if year%01.22.24 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")

'''

# 01.22.24. Write a program that simulates the logic shown in the below flowchart

# There are three decision points on the flowchart, meaning that a result will occur three times. set three different results to place-holder variables
# For each decision point ask for user input and set to a variable
# Write an if/elif/else for each decision point. If the decision results in a game over quit program. If anything other than the "if" statement is selected the outcome will be the result defined under the "else" statement.

# Use f-strings to print decisions and results


print("Welcome to Treasure Island. Your mission is to find the treasure")

result1 = ""
result2 = ""
result3 = ""

left_right = input("Choose a direction. left or right?: ")

if left_right == "left":
    print(f"You chose to go {left_right}")
else:
    result1 = "You Fell into a hole. Game Over."
    print(f"You chose to go {left_right}. {result1}")
    quit()

swim_wait = input(("Choose an option. swim or wait?: "))

if swim_wait == "wait":
    print(f"You chose to {swim_wait}")
else:
    result2 = "You Were Attacked by trout. Game Over."
    print(f"You chose to {swim_wait}. {result2}")
    quit()

door_opt = input(("Choose a door. red, yellow, or blue?: "))

if door_opt == "yellow":
    result3 = "You win!"
    print(f"You chose {door_opt}. {result3}")
elif door_opt == "red":
    result3 = "You Were Burned by fire. Game Over"
    print(f"You chose {door_opt}. {result3}.")
    quit()
elif door_opt == "blue":
    result3 = "You Were Eaten by beasts. Game Over"
    print(f"You chose {door_opt}. {result3}.")
else:
    result3 = "Game Over."
    print(f"You chose {door_opt}. {result3}.")


#### Dr Shaik Comments

# Code for "Treasure Island" game could be simplified as below:
#
# print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
# choice = input("Left or Right? ").upper()
# # falls into each if based on the users choices
# if choice == "LEFT":
#     choice = input("Swim or Wait? ").upper()
#     if choice == "WAIT":
#         choice = input("Which door? Red, Blue, or Yellow: ").upper()
#         if choice == "RED":
#             print("You were burned by fire.\nGame Over!")
#         elif choice == "BLUE":
#             print("You were eaten by beasts.\nGame Over!")
#         elif choice == "YELLOW":
#             print("You Win!")
#         else:
#             print("Game Over!")
#     else:
#         print("You were attacked by a trout\nGame Over!")
# else:
#     print("You fell into a hole.\nGame Over!")

