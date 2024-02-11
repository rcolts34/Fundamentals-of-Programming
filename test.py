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

print(f"You chose to go {left_right}, then {swim_wait}, and went through the {door_opt} door. {result} ")

"""

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


