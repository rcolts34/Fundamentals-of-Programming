
'''

#### Lambda Functions

    ## Lamda Functions good for one or two operations, otherwise use regular function

def square_num(a):
    return a * a

print(f'a^2: {square_num(5)}')

square_num1 = lambda a: a * a
print(square_num1(5))

add_nums = lambda a, b: a + b
print(add_nums(4,5))

hello_user = lambda name: f"Hello {name}!"
print(hello_user("Carl"))

    ## Write a lambda function that checks whether a number is even or odd
        ## Print "Even Number" if it is even otherwise print "Odd Number"

check_even = lambda num: "Even Number" if num % 2 == 0 else "Odd Number"
print(check_even(16))
print(check_even(21541))
print(check_even(89))
print(check_even(1))
print(check_even(0))


#### Immediately Invoked Function Expressions IIFEs
    ## AKA Annoynymous Functions
        ## Function is not stored anywhere.
        ## Used only when you want to use it immediately and use it one time.

print((lambda name: f"Hello {name}!")('Jane'))
print((lambda x: x + 5)(10))


#### Higher Order Functions
    ## Filter
        ## Expects two parameters: function, data
        ## Picking out items from a list based on certain conditions
        ## filter(function, data)

nums = [3, 2, 6, 8, 4, 6, 2, 9]
def is_even(n):
    return n % 2 == 0
even_nums = list(filter(is_even, nums))
print(list(even_nums))

even_nums1 = list(filter(lambda x:x % 2 == 0, nums))
print(list(even_nums1))

    ## Map
        ## Used to perform some operation on every element in a list

def double_num(n):
    return n * 2
doubles = map(double_num, nums)
print(list(doubles))

doubles1 = map(lambda x:x * 2, nums)
print(list(doubles1))



    ## Using map and lambda, return a list with the lengths of all the cities

cities = ["New York", "Miami", "Phoenix", "Columbus", "Pittsburgh"]
lengths = map(lambda x: len(x), cities)
print(list(lengths))


'''

    ## Reduce
        ## Used to obtain a single value from a given list
            ## Calculating one value from a given list
            ## Example → Find the sum of all numbers in a list

nums = [3, 2, 6, 8, 4, 6, 2, 9]

from functools import reduce
    # a → accumulator
    # b → current value
def add_all(a, b):
    return a + b
total_sum = reduce(add_all, nums)
print(total_sum)

total_sum1 = reduce(lambda a,b: a+b, nums)
print(total_sum1)




