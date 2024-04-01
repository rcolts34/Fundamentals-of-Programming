


###  1. Write a lambda function that takes 2 arguments and returns the product of those 2 arguments

multiply = lambda a, b: a*b
print(multiply(4, 5))


###  2. Write a lambda IIFE that takes 2 numbers as parameters and returns the difference between them.

print((lambda a, b: a-b)(10,5))


###  3. Using filter and lambda write a function that returns all the numbers greater than 5 from a given list

    ## Sample List: nums = [3, 2, 6, 8, 4, 6, 2, 9]

nums = [3, 2, 6, 8, 4, 6, 2, 9]
greater_5 = list(filter(lambda x: x > 5, nums))
print(greater_5)


###  4. Write a lambda function that returns num/5 if a given number is greater than 10. Otherwise, returns num + 5

divide_or_add = lambda num: round((num/5) if num > 10 else (num+5))
print(divide_or_add(20))
print(divide_or_add(5))


##  5. Using map and lambda, write a function to multiply every number in a list by 2.

nums = [3, 2, 6, 8, 4, 6, 2, 9]
doubles = list(map(lambda x: x*2, nums))
print(doubles)


##  6. Using map, filter and reduce

    ##  i) Find the odd numbers from a given list

nums = [3, 2, 6, 8, 4, 6, 2, 9]
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)

        # Result  →  [3, 9]

    ##  ii) Square each odd number

square_odd = list(map(lambda x: x*x, odd_nums))
print(square_odd)

        # Result  →  [9, 81]

    ##  iii) Sum of squared odd numbers
from functools import reduce
add_square_odd = (reduce(lambda a, b: a+b, square_odd))
print(add_square_odd)

        # Result  →  90