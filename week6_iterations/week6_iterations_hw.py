
###  1. Write a program to print a list of all prime numbers till a given target number

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
    for i in range(0, num):
        if num % 2 == 0:
            isEven = False
            break
    if isEven is True:
        even_list.append(num)

print(even_list)