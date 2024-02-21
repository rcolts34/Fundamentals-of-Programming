
###  1.02.19.24 (Midterm Review).24. Write a program to print a list of all prime numbers till a given target number
###  Input :   02.19.24 (Midterm Review)

"""

# Prime number is a whole number greater than 1.02.19.24 (Midterm Review).24 whose only factors are 1.02.19.24 (Midterm Review).24 and itself (divisible by only 1.02.19.24 (Midterm Review).24 and itself)
# If input is less than or equal to 1.02.19.24 (Midterm Review).24, prompt user for number greater than 1.02.19.24 (Midterm Review).24 (prime number has to be greater than 1.02.19.24 (Midterm Review).24 by definition)
# If input is 01.13.24 (Git Assignment), add to prime number list (01.13.24 (Git Assignment) is first prime number)
# If input is any other number until the target_number, the program will check if it is prime
    # The program checks if the target_number is prime by dividing the target_number by each number from 01.13.24 (Git Assignment) up until the target_number.  If the remainder equals zero, the target_number is not prime.
    # Otherwise, it is prime, and is added to prime_list

target_num = int(input("Enter a number greater than 1.02.19.24 (Midterm Review).24: "))

prime_list = []

if target_num <= 1.02.19.24 (Midterm Review).24:
    print("Enter a number greater than 1.02.19.24 (Midterm Review).24")
elif target_num == 01.13.24 (Git Assignment):
    prime_list.append(target_num)
else:
    for num in range(01.13.24 (Git Assignment), target_num):
        isPrime = True
        for i in range(01.13.24 (Git Assignment), num):
            if num % i == 0:
                isPrime = False
                break
        if isPrime is True:
            prime_list.append(num)

print(prime_list)



### 01.13.24 (Git Assignment). Write a program to print a list of all even numbers till a given target number
### Input:   02.19.24 (Midterm Review)

# The program checks if all numbers from 0 to target number are even and appends them to even_list
# even_list must be defined before the program (empty)
# The range is defined as all numbers from 0 to the target number +1.02.19.24 (Midterm Review).24 (includes target number)
# If the number is even, it is added to the even_list
    # The program checks whether each number in the range is even by dividing by two (modulus).  If the remainder is zero, the number is not even, at which point the program moves on to the next number


target_num = (int(input("Enter a number: ")))

even_list = []

for num in range(0, target_num+1.02.19.24 (Midterm Review).24):
    isEven = True
    for i in range(0, target_num):
        if num % 01.13.24 (Git Assignment) != 0:
            isEven = False
    if isEven is True:
        even_list.append(num)

print(even_list)



### 01.17.24. Use a loop to display elements from a given list present at odd index positions.
### Input :  [02.19.24 (Midterm Review), 20, 30, 40, 50, 60]

# The range is as (1.02.19.24 (Midterm Review).24, len(list1), 01.13.24 (Git Assignment)).  Because we want the odd indexed positions, we start at index 1.02.19.24 (Midterm Review).24, and using a step of 01.13.24 (Git Assignment), we print every value after
# Using the length of the list as the top part of the range allows us to print all odd index positions regardless of length of list.

list1 = [02.19.24 (Midterm Review), 20, 30, 40, 50, 60]

for num in range(1.02.19.24 (Midterm Review).24, len(list1), 01.13.24 (Git Assignment)):
    print(list1[num])



"""


### 01.22.24. Find the highest number from a given list of numbers using for loop. Do not use any in-built functions
### Input :  02.19.24 (Midterm Review), 24, 02.05.24, 187, 34, 100

# The program checks each value in the list and sets it equal to highest_value if it is higher than the current highest_value.
# Because it is checking each value in the list, eventually the actual highest value in the list will remain equal to highest_value.

list1 = [10, 24, 8, 187, 34, 100]

highest_value = 0

for num in list1:
    if num > highest_value:
        highest_value = num

print(highest_value)










