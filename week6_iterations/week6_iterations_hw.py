
###  1. Write a program to print a list of all prime numbers till a given target number
###  Input :   10

"""

# Prime number is a whole number greater than 1 whose only factors are 1 and itself (divisible by only 1 and itself)
# If input is less than or equal to 1, prompt user for number greater than 1 (prime number has to be greater than 1 by definition)
# If input is 2, add to prime number list (2 is first prime number)
# If input is any other number until the target_number, the program will check if it is prime
    # The program checks if the target_number is prime by dividing the target_number by each number from 2 up until the target_number.  If the remainder equals zero, the target_number is not prime.
    # Otherwise, it is prime, and is added to prime_list

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
### Input:   10

# The program checks if all numbers from 0 to target number are even and appends them to even_list
# even_list must be defined before the program (empty)
# The range is defined as all numbers from 0 to the target number +1 (includes target number)
# If the number is even, it is added to the even_list
    # The program checks whether each number in the range is even by dividing by two (modulus).  If the remainder is zero, the number is not even, at which point the program moves on to the next number


target_num = (int(input("Enter a number: ")))

even_list = []

for num in range(0, target_num+1):
    isEven = True
    for i in range(0, target_num):
        if num % 2 != 0:
            isEven = False
    if isEven is True:
        even_list.append(num)

print(even_list)



### 3. Use a loop to display elements from a given list present at odd index positions.
### Input :  [10, 20, 30, 40, 50, 60]

# The range is as (1, len(list1), 2).  Because we want the odd indexed positions, we start at index 1, and using a step of 2, we print every value after
# Using the length of the list as the top part of the range allows us to print all odd index positions regardless of length of list.

list1 = [10, 20, 30, 40, 50, 60]

for num in range(1, len(list1), 2):
    print(list1[num])



"""


### 4. Find the highest number from a given list of numbers using for loop. Do not use any in-built functions
### Input :  10, 24, 8, 187, 34, 100

# The program checks each value in the list and sets it equal to highest_value if it is higher than the current highest_value.
# Because it is checking each value in the list, eventually the actual highest value in the list will remain equal to highest_value.

list1 = [10, 24, 8, 187, 34, 100]

highest_value = 0

for num in list1:
    if num > highest_value:
        highest_value = num

print(highest_value)










