
###  1. Write a program to print a list of all prime numbers till a given target number

"""

target_num = int(input("Enter a number greater than 1: "))  (Input is 10)

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

target_num = int(input("Enter a number: "))   (Input is 10)

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



### 3. Use a loop to display elements from a given list present at odd index positions.

(Input is [10, 20, 30, 40, 50, 60])


list1 = [10, 20, 30, 40, 50, 60]

for num in range(1, len(list1), 2):
    print(list1[num])



"""

# 4. Find the highest number from a given list of numbers using for loop. Do not use any in-built functions

list1 = [10, 24, 8, 187, 34, 100]

highest_value = 0

for num in list1:
    if num > highest_value:
        highest_value = num

print(f'Highest Value: {highest_value}')








