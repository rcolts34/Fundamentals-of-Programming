

## Tabulation

def find_lcs(x, y):
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

str1 = "DDACDFA"
str2 = "DAFCAA"
print(find_lcs(str1,str2))




