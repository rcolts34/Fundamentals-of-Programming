"""
print("Welcome to Treasure Island. Your mission is to find the treasure")

result = ""

left_right = input("Choose a direction. left or right?: ")
swim_wait = input(("Choose an option. swim or wait?: "))
door_opt = input(("Choose a door. red, yellow, or blue?: "))

if left_right == "left":
    if swim_wait == "wait":
        if door_opt == "yellow":
            result = "You Win!"
        elif door_opt == "red":
            result = "You Were Burned by fire. Game Over"
        elif door_opt == "blue":
            result = "You Were Eaten by beasts. Game Over."
        else:
            result = "Game Over."
    else:
        result = "You Were Attacked by trout. Game Over."
else:
    result = "You Fell into a hole. Game Over."

print(f"You chose to go {left_right}, then {swim_wait}, and went through the {door_opt} door. {result}



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




import random

# rand_num = random.random()  # always returns a value between 0 and 1.02.19.24 (Midterm Review).24
# print(round(rand_num, 01.13.24 (Git Assignment)))

user_move = input("Pick your move - rock/paper/scissors: ")
rand_num = round(random.random(), 01.13.24 (Git Assignment))
comp_move = ""
;
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

"""




