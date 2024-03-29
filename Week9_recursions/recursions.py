
'''

#### RECURSION

# A process in which a function repeatedly calls itself as long a condition is satisfied.
# an extension of loops
# Recursion calls are not recommended if there are an excessive amount of recursion calls to be made
# Whenever you call a function (b) within a function (a), the initial function will pause (a) until (b) has finished executing.

def sayHello(name):
    print(f"Hello {name}!")

def userDetails():
    user_name = input("Enter a name: ")
    sayHello(user_name)
    user_city = input("Enter a city: ")
    print(f"You are from {user_city}")
userDetails()

#### RECURSION FUNCTION

### TEST1

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


### TEST2

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


from tabulate import tabulate
all_data = [["n!","     ","n x (n-1)!"],
            ["5!","5x4x3x2x1","5x4!"],
            ["4!","4x3x2x1","4x3!"],
            ["3!","3x2x1","3x2!"],
            ["2!","2x1","2x1!"],
            ["1!","  ","1x0!"],
            ["0!","  ","1"]]
table1 = tabulate(all_data,tablefmt="fancy_grid")
print(table1)


╒════╤═══════════╤════════════╕
│ n! │           │ n x (n-1)! │
├────┼───────────┼────────────┤
│ 5! │ 5x4x3x2x1 │ 5x4!       │
├────┼───────────┼────────────┤
│ 4! │ 4x3x2x1   │ 4x3!       │
├────┼───────────┼────────────┤
│ 3! │ 3x2x1     │ 3x2!       │
├────┼───────────┼────────────┤
│ 2! │ 2x1       │ 2x1!       │
├────┼───────────┼────────────┤
│ 1! │           │ 1x0!       │
├────┼───────────┼────────────┤
│ 0! │           │ 1          │
╘════╧═══════════╧════════════╛

### WRITE A FUNCTION TO FIND THE FACTORIAL OF A NUMBER

    # 5 x 4 !
    # 1000! → 1000 x 999! →  999! x 998! → .......!0
    # if you are making that many recursive calls, it is not the place to use recursion

def findFactorial(num):
    if (num < 0):
        print("Please provide a positive number: ")
        return
    elif (num <= 1):
        return 1
    else:
        return num * findFactorial(num-1)

factorial_value = findFactorial(1000)
print(factorial_value)



### FIBONACCI SERIES

    # Every number is the sum of the previous two numbers (starting from third number)
    # Try to write recursive program that prints Fibonacci Series

# Fibonacciseries(5)
# Prints → 11235
# Fibonacciseries(6)
# Prints → 112358
# Fibonacci →

# Reuse the code provided, add explanation
# Create quicksort.py file
# Add quicksort.py and recursion.py to archive and upload for Homework
# Due on Friday
# Classes may be online, watch email



#### USING RECURSION

    ## recurFibo

    # If logic →  If n is less than or equal to one, one will be returned.  The first two numbers of the fibonacci sequence are 1.
    # else logic → Each subsequent number in the sequence is found by adding the two numbers preceding it (or the n-1 and n-2 numbers).  These two numbers are added and returned.

def recurFibo(n):
    if n <= 1:
        return n
    else:
        return(recurFibo(n-1) + recurFibo(n-2))

    ## fibSeries

    # If / else → if nterms is less than or equal to 0, print the Please enter a positive integer, else, print Fibonacci sequence.  The function will be printed up to nterms numbers, thus a negative  number does not work.
    # for logic → iterates from 1 to nterms, at each iteration recurFibo(i) function is called, which will compute and print the fibonacci number.
        #

def fibSeries(nterms):
    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci sequence")
    for i in range(1, nterms+1):
        print(recurFibo(i))

fibSeries(30)
print()

'''

#### USING LOOPS

    #  If logic →  If n is less than or equal to one, one will be returned.  The first two numbers of the fibonacci sequence are 1.
    #  elif / else logic → the first two numbers are 1 in the sequence, so 1 is returned if num is one.  If num is 2, two ones are returned.  The function is using lists and slicing to create the sequence, so starting out this way gurantees that the list being appended to will start off the same every time.
    #  for logic → the function iterates from 3 up to num, the next term is calculated as the sum of the two preceding terms, and is appended to fib_list.

def fibonacciSeries(num):
    if num <= 0:
        print("Enter a value greater than zero. ")
        return
    elif num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    else:
        fib_list = [1, 1]
        for i in range(2, num):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list
print(fibonacciSeries(30))












