## Recursion
# A process in which a function repeatedly calls itself as long a condition is satisfied.
# an extension of loops
# Recursion calls are not recommended if there are an excessive amount of recursion calls to be made
# Whenever you call a function (b) within a function (a), the initial function will pause (a) until (b) has finished executing.

'''

def sayHello(name):
    print(f"Hello {name}!")

def userDetails():
    user_name = input("Enter a name: ")
    sayHello(user_name)
    user_city = input("Enter a city: ")
    print(f"You are from {user_city}")
userDetails()

#### RECURSION FUNCTION

# test1
# printing the value
# "3"
# calling the function
# printing the value
# "2"
# calling the function

def test1(n):
    if(n > 0):
        print("Printing the value. ")
        print(n)
        print("Calling the function")
        test1(n - 1)
test1(3)


### test2
# Print "n" is paused until the function has stopped running
# Once the function has stopped running, control is given back to the parent function (Parent → Child , test2(3) → test2(2), etc
# Temporary values are stored in "stack memory" with time stamps

def test2(n):
    if(n > 0):
        print("Calling the function")
        test2(n - 1)
        print("Printing the value. ")
        print(n)
test2(3)


### Find the factorial of a number

#             - n!              = n x (n-1)!
# factorial   - 5! - 5x4x3x2x1  = 5 x 4!
#             - 4! - 4x3x2x1    = 4 x 3!
#             - 3! - 3x2x1      = 3 x 2!
#             - 2! - 2x1        = 2 x 1!
#             - 1!              = 1 x 0!
#             - 0!              = 1

# Write a function to find the factorial of a number

# 5 x 4 !

def findFactorial(num):
    if (num < 0):
        print("Please provide a positive number: ")
        return
    elif (num <= 1):
        return 1
    else:
        return num * findFactorial(num-1)
factorial_value = findFactorial(4)
print(factorial_value)

'''

### Fibonacci Series
# Every number is the sum of the previous two numbers (starting from third number)
# Try to write recursive program that prints Fibonacci Series

# Fibonacciseries(5)
# Prints → 11235
# Fibonacciseries(6)
# Prints → 112358
# Fibonacci →

def fibSeries(num):
    if (num <= 0):
        print("Please provide a positive number: ")
        return
    else:
        return num - fibSeries(num)
 = fibSeries(2)
print(result)
