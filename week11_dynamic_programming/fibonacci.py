
'''

#### Recursive Solution
    ## Calls (40th value): 331,160,281

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
    ## Calls (40th value): 79

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
        # fib_val_memo[req_fib_num] = fib_num_memo(req_fib_num - 2) + fib_num_memo(req_fib_num - 1)


        # to store only the last 2 values at any time
        fib_val_memo[req_fib_num] = fib_num_memo(req_fib_num - 2) + fib_num_memo(req_fib_num - 1)

        fib_val_memo = dict(list(fib_val_memo.items())[-2:])
    return fib_val_memo[req_fib_num]

print(fib_num_memo(40))
print(f"Memoization Call Count: {memo_call_count}")

'''


#### Tabulation Solution
    ## Calls (40th value): 1

ite_call_count = 0

def fib_val_ite(req_fib_num):
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
