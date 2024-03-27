
'''

#### Recursion

    # Recursion is used to find the Longest Common Subsequence
    # This is the least efficient method
        # Calls: 30582


def lcs_rec(A, B, i, j):
    global calls
    calls = calls + 1
    if len(A) == 0 or len(B) == 0 or A[i] == "\0" or B[j] == "\0":
        # return 0
        return " "
    elif A[i] == B[j]:
        # return 1 + lcs_rec(A, B, i + 1, j + 1)
        return A[i] + lcs_rec(A, B, i+1, j+1)
    else:
        # return max(lcs_rec(A, B, i + 1, j), lcs_rec(A, B, i, j + 1))
        return max(lcs_rec(A, B, i + 1, j), lcs_rec(A, B, i, j + 1), key=len)

calls = 0

str1 = "CGATAATTGAGA"
str2 = "GTTCCTAATA"

str1 = str1 + "\0"
str2 = str2 + "\0"

lcs_char = lcs_rec(A=str1, B=str2, i=0, j=0)
print(lcs_char)
print(F"Recursion calls: {calls}")


#### Memoization

    # Memoization is used to find the Longest Common Subsequence
    # This is far more efficient than the Recursion method
        # Calls: 147


def lcs_memoization(A, B, i, j):
    global lcs_memo, calls
    calls = calls + 1
    if len(A) == 0 or len(B) == 0 or A[i] == "\0" or B[j] == "\0":
        return 0
    if lcs_memo [i][j] == ' ':
        if A[i] == B[j]:
            lcs_memo[i][j] = 1 + lcs_memoization(A, B, i+1, j+1)

        else:
            lcs_memo[i][j] = max(lcs_memoization(A, B, i + 1, j), lcs_memoization(A, B, i, j + 1))
    return lcs_memo[i][j]

calls = 0

str1 = "CGATAATTGAGA"
str2 = "GTTCCTAATA"

str1 = str1 + "\0"
str2 = str2 + "\0"

lcs_memo = []

for _ in range(len(str1)):
    lcs_memo.append([" "] * len(str2))

seq_len = lcs_memoization(A=str1, B=str2, i=0, j=0)
print(seq_len)
print(f"Memoization calls: {calls}")

'''


#### Tabulation

    # Tabulation is used to find the Longest Common Subsequence
    # This is by far the most efficient method
        # Calls: 1

def find_lcs(x, y):
    global calls
    calls = calls + 1
    len_x = len(x)
    len_y = len(y)
    lcs_array = []
    for i in range(len_x + 1):
        zero_row = [0] * (len_y + 1)
        lcs_array.append(zero_row)

    for row in range(1, len_x + 1):
        for col in range(1, len_y + 1):
            if x[row - 1] == y[col - 1]:
                lcs_array[row][col] = 1 + lcs_array[row - 1][col - 1]
            else:
                lcs_array[row][col] = max(lcs_array[row-1][col], lcs_array[row][col - 1])

    for row1 in lcs_array:
        print(row1)
    return lcs_array[row][col]

calls = 0

str1 = "CGATAATTGAGA"
str2 = "GTTCCTAATA"
print(f'LCS Length: {find_lcs(str1,str2)}')
print(f"Tabulation calls: {calls}")



