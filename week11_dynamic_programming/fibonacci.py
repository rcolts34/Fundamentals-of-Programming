
'''

#### Recursive Solution

    ## def fib_num_rec(req_fib_num)

    # This is a recursive solution for calculating the fibonacci sequence as well as how many function calls are made.
    # rec_call_count variable is initialized and the function is defined.
    # In order for rec_call_count variable to be used inside the function, the global keyword must be used
    # rec_call_count is incremented by 1 to keep track of each time the function is called
    # If the req_fib_num is <= 1, req_fib_num is returned.  This is because the 0th and 1st numbers in the sequence are 0 and 1, respectively.
    # Else, the fibonacci number is calculated. req_fib_num is called twice: req_fib_num - 2 and req_fib_num - 1.  The sum of these values gives the fibonacci number, which by definition is the sum of the two preceding values.

    ## for loop

    # the number of function calls is reset for each iteration
    # iterates over the given list, passing the values to the fib_num_rec(req_fib_num) function to calculate the fibonacci number.
    # the total number of function calls required to calculate the fibonacci number is printed
    # This solution is not very efficient
        # Calls (40th value): 331,160,281

rec_call_count = 0

def fib_num_rec(req_fib_num):
    global rec_call_count
    rec_call_count = rec_call_count + 1
    if req_fib_num <= 1:  # fib(0), fib(1)
        return req_fib_num
    else:
        return fib_num_rec(req_fib_num - 2) + fib_num_rec(req_fib_num - 1)

for num in [5, 10, 15, 20, 25, 30, 35, 40]:
    rec_call_count = 0
    print(f"{num}th value is {fib_num_rec(num)}")
    print(f"Total recursive calls: {rec_call_count:,}")
    print('*'*500)
    print()



#### Memoization Solution

    # Memoization is used to improve efficiency.  Results of function calls are stored and used later so that the same calculations do not have to be repeated.
    # fib_val_memo and memo_call_count variables are initialized
    # Function is defined and global keyword is used to access variables
    # memo_call_count increments by 1 each time the function is called
    # if logic →  function checks if the result is already in the fib_val_memo dictionary.  If it is, the result is returned.
        # This reduces function calls significantly
    # elif logic → if req_fib_num is <=1, it is stored in the dictionary
    # else logic → the fibonacci number is calculated. req_fib_num is called twice: req_fib_num - 2 and req_fib_num - 1.  The sum of these values gives the fibonacci number, which by definition is the sum of the two preceding values.  The result is stored in the dictionary.  The dictionary is size limited to the last two stored values.
        # Calculating the fibonacci number only requires the preceding two vales.  This cuts down on memory usage and increases efficiency.
    # The calculated Fibonacci number is returned.  It is then printed, along with the amount of function calls
    # The solution is far more efficient than using Recursion.
        # Calls (40th value): 79


fib_val_memo = {}
memo_call_count = 0

def fib_num_memo(req_fib_num):
    global fib_val_memo, memo_call_count
    memo_call_count = memo_call_count + 1
    if req_fib_num in fib_val_memo:
        return fib_val_memo[req_fib_num]

    elif req_fib_num <= 1:
        fib_val_memo[req_fib_num] = req_fib_num

    else:
        fib_val_memo[req_fib_num] = fib_num_memo(req_fib_num - 2) + fib_num_memo(req_fib_num - 1)
        fib_val_memo = dict(list(fib_val_memo.items())[-2:])

    return fib_val_memo[req_fib_num]

print(fib_num_memo(40))
print(f"Memoization Call Count: {memo_call_count}")

'''


#### Tabulation Solution


    # Bottom-Up solution to for calculating Fibonacci numbers.  Sub-problems are solved first and solutions are stored in an array. Those solutions are used to solve larger sub-problems, and so on.
    # ite_call_count is initialzed and global keyword is used to access it inside the function
    # ite_call_count increments by 1 each time the function is called
    # if logic → If the req_fib_num is <= 1, 1 is returned.  This is because the 0th and 1st numbers in the sequence are 0 and 1, respectively.
    # else logic → fib_list is defined with the first two fibonacci numbers.  The function then iterates from 2 up to req_fib_num-1. Because the value passed to the function is calculated using the previous two fib numbers, we do not need to include the req_fib_num.
    # Fibonacci number is calculated and appended to the list of fibonacci numbers
    # The last number of fib_list is returned
    # the function is called, and the fibonacci number and number of calls are printed
        # This is the most efficient solution, only requiring one function call.
        # Calls (40th value): 1

ite_call_count = 0

def fib_val_ite(req_fib_num):
    global fib_list
    global ite_call_count
    ite_call_count += 1
    if req_fib_num <= 1:
        return 1
    else:
        fib_list = [1, 1]
        for i in range(2, req_fib_num):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[-1]

print(fib_val_ite(40))
print(f"Tabulation Call Count: {ite_call_count}")
