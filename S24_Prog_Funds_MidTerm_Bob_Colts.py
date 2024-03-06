
'''

# 1 Using a while loop, print odd numbers until a given target number

x = 0
while x < 10:
    if x % 2 != 0:
        print(x)
    x += 1

# 2 Using a for loop, remove all "apple elements from the below list and print the final list



fruits_list = ["banana", "orange", "apple", "kiwi", "apple", "apple", "grapes"]

set1 = set(fruits_list)
print(new_list)

new_list = list(set1)
print(new_list)
print(type(new_list))

# 3 Coin Toss Game

import random

user_move = input("Choose heads or tails: ")
rand_num = round(random.random(), 2)
comp_move = ""

if rand_num >= 0 and rand_num <= 1/2:
    comp_move = "heads"
else:
    comp_move = "tails"

if user_move == comp_move:
    result = "Tie."
elif user_move == "heads":
    if comp_move == "tails":
        result = "You win!"
else:
    result = "You lose!"

print(f'You picked {user_move}, Computer picked {comp_move} - {result}.')

'''

# 4 Write a program that prints the multiples of 5 from the given list with the following conditions

    # a.	Continue with the next iteration of the loop if value is greater than 150
    # b.	Break the loop if the value is greater than 500
    # c.	Otherwise, print the item if it is divisible by 5.


list1 = [12, 75, 150, 180, 145, 525, 50]

for num in list1:
    if num >= 150 and num % 5 == 0:
        print(num)
    elif num >= 500:
        break

for i in list1:
    if i > 500:
        break
    elif i > 150:
        continue
    else:
        if i % 5 == 0:
            print(i)


# 5 Create the Below Pattern

# rows = int(input("Enter the number of rows: "))
# count = 0
#
# for i in range(0, rows+1):
#     count = count + 1
#     for j in range(1, i + count):
#         if j % 2 != 0:
#         print(j, end=" ")
#     print("")

rows = int(input("Enter the number of rows: "))

for i in range(0, rows):
    for j in range(0, i + 1):
        print(j*2, end=" ")
    print("")




