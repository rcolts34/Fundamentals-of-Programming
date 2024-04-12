
    ## Lambda functions are one-time functions (not call-able like "def" functions) that are useful when a function is only needed for a short time.  They should only be used for one or two operations, otherwise it makes more sense to define a function that can be called at will.

###  1. Write a lambda function that takes 2 arguments and returns the product of those 2 arguments

    ## lambda function is set to variable multiply, takes two arguments, and returns their product.

multiply = lambda a, b: a*b
print(multiply(4, 5))


###  2. Write a lambda IIFE that takes 2 numbers as parameters and returns the difference between them.

    ## IIFEs (Immediately Invoked Function Expression, aka Anonymous Functions) are lambda functions that are defined and immediately called.  They are not stored anywhere, thus are used only when you want to use it immediately and only once.
    ## IIFE lambda function takes two arguments, calculates the difference, and prints it.

print((lambda a, b: a-b)(10,5))


###  3. Using filter and lambda write a function that returns all the numbers greater than 5 from a given list

    ## Filter is a Higher Order Function that expects two parameters: function and data.  It iterates on a collection and filters it based on defined conditions.
    ## Lambda function is used to keep only numbers greater than 5.  "List" is applied to the function to convert the output to a list so that it can be calculated.


    # Sample List: nums = [3, 2, 6, 8, 4, 6, 2, 9]

nums = [3, 2, 6, 8, 4, 6, 2, 9]
greater_5 = list(filter(lambda x: x > 5, nums))
print(greater_5)


###  4. Write a lambda function that returns num/5 if a given number is greater than 10. Otherwise, returns num + 5

    ## Lambda function uses conditional logic to divide a given number by 5 if it is less than 10, otherwise it adds 5 to the number.


divide_or_add = lambda num: num/5 if num > 10 else num+5
print(divide_or_add(20))
print(divide_or_add(5))


##  5. Using map and lambda, write a function to multiply every number in a list by 2.

    ## Map is a Higher Order Function that expects two paramters: function and data.  It iterates on a collection and applies the function to each element.
    ## Lambda function multiplies every number in a list by 2 and prints the result. "List" is applied to the function to convert the output to a list so that it can be calculated.

nums = [3, 2, 6, 8, 4, 6, 2, 9]
doubles = list(map(lambda x: x*2, nums))
print(doubles)


##  6. Using map, filter and reduce

    # i) Find the odd numbers from a given list

    ## Filter function is used to keep numbers that are not divisible by 2 (odd numbers) and result is converted to a list. Result is printed.

nums = [3, 2, 6, 8, 4, 6, 2, 9]
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)

        # Result  →  [3, 9]

    # ii) Square each odd number

    ## Map function is used on list from previous problem (odd_nums) to square each number and result is converted to a list  Result is printed.

square_odd = list(map(lambda x: x*x, odd_nums))
print(square_odd)

        # Result  →  [9, 81]

    # iii) Sum of squared odd numbers

    ## Reduce function is imported from functools (Standard Python module).  Reduce is a Higher Order Function that iterates on a collection and applies a function to each element, ultimately obtaining a single value from the given collection.
    ## Reduce funciton is used to sum all squared odd numbers.


from functools import reduce
add_square_odd = reduce(lambda a, b: a+b, square_odd)
print(add_square_odd)

        # Result  →  90