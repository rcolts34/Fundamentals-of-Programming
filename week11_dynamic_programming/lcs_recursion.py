

## Recursion

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
# str1 = "bd"
# str2 = "abcd"
str1 = "CGATAATTGAGA"
str2 = "GTTCCTAATA"

str1 = str1 + "\0"
str2 = str2 + "\0"

# seq_len = lcs_rec(A=str1, B=str2, i=0, j=0)
# print(seq_len)

lcs_char = lcs_rec(A=str1, B=str2, i=0, j=0)
print(lcs_char)
print(F"Recursion calls: {calls}")