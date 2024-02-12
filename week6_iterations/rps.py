import random

# rand_num = random.random()  # always returns a value between 0 and 1
# print(round(rand_num, 2))

user_choice = "yes"

while user_choice.lower() == "yes":
    user_move = input("Pick your move - rock/paper/scissors: ")
    rand_num = round(random.random(), 2)
    comp_move = ""

    if rand_num >= 0 and rand_num < 1/3:
        comp_move = "rock"
    elif rand_num >= 1/3 and rand_num <2/3:
        comp_move = "paper"
    else:
        comp_move = "scissors"

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
    user_choice = input("Do you want to play again? Enter yes or no: ")

print("Thank you!")



