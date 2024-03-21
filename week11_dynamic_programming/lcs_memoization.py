

## Memoization

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
# str1 = "bd"
# str2 = "abcd"
str1 = "CGATAATTGAGA"
str2 = "GTTCCTAATA"

str1 = str1 + "\0"
str2 = str2 + "\0"

lcs_memo = []

for _ in range(len(str1)):
    # print([" "] * len(str2))
    lcs_memo.append([" "] * len(str2))

# print(lcs_memo)
seq_len = lcs_memoization(A=str1, B=str2, i=0, j=0)
print(seq_len)
print(f"Memoization calls: {calls}")

