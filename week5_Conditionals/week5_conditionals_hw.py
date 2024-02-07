###### QUESTION 1 = Convert digit to word
## Brute Force Approach - Using if-elifs
## Better approach - using collections

## Method 1: using dictionary

'''

dict1 = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",

}

num = int(input("Enter a digit between 0 and 9: "))

print(dict1[num])



###### QUESTION 2: ROCK, PAPER, SCISSORS

import random

# rand_num = random.random()  # always returns a value between 0 and 1
# print(round(rand_num, 2))

user_move = input("Pick your move - rock/paper/scissors: ")
rand_num = round(random.random(), 2)
comp_move = ""

if rand_num >= 0 and rand_num < 1/3:
    comp_move = "rock"
elif rand_num >= 1/3 and rand_num <2/3:
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



# 3. Write a program that takes year as input and checks whether the given year is leap or not.

## Conditions
## a. The entered year must be divisible by 4
## b. But if it is also divisible by 100 then it should also be divisible by 400

year = int(input("Enter a year to check if it is a leap year: "))

if year%4 == 0:
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

# 4. Write a program that simulates the logic shown in the below flowchart

print("Welcome to Treasure Island. Your mission is to find the treasure")

left_right = input("Choose a direction. left or right?: ")

if left_right = "left"
    print(


