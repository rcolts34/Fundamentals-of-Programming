

### Checking all numbers for divisible by 0, 3 or both
## Have to use loops and conditions


target_num = int(input("Input a number: "))

for num in range(1, target_num+1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

