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
