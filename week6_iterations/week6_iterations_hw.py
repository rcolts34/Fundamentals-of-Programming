
###  1. Write a program to print a list of all prime numbers till a given target number

"""

target_num = int(input("Enter a number greater than 1: "))

prime_list = []

if target_num <= 1:
    print("Enter a number greater than 1")
elif target_num == 2:
    prime_list.append(target_num)
else:
    for num in range(2, target_num):
        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break
        if isPrime is True:
            prime_list.append(num)



print(prime_list)



### 2. Write a program to print a list of all even numbers till a given target number

target_num = int(input("Enter a number: "))

even_list = []

for num in range(0, target_num+1):
    isEven = True
    for i in range(0, target_num):
        if num % 2 != 0:
            isEven = False
            break
    if isEven is True:
        even_list.append(num)

print(even_list)

[10, 20, 30, 40, 50, 60]



### 3. Use a loop to display elements from a given list present at odd index positions.

list1 = [10, 20, 30, 40, 50, 60]

for i in range(1, len(list1), 2):
    print(list1[i])


range(1, len(list1)):
list1[0:]:
"""
# for i in range(1, len(list1)):
# 4. Find the highest number from a given list of numbers using for loop. Do not use any in-built functions

list1 = [10, 24, 8, 187, 34, 100]
target_number = int(input(list1))

highest_value = []

for i in list1[1::1]:
    for j in range(1, i + 1):
        while highest_value == 0:
            if j > highest_value:
                j = highest_value
        if j < highest_value:
            break

print(highest_value)








