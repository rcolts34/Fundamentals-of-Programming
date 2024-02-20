'''

for i in range(11):
    if i > 5:
        break  # just breaks the execution of the loop
    else:
        print(i)

## Continue
for i in range(11):
    if i % 2 == 0:
        continue
    else:
         print(i)




#### Write a program to calculate the sum and average of digits present in a given string
#### Input:   random289$18@#str849ing6
#### Expected output: Sum  55, Average: 6.11

input_str = input("Enter a string with numbers, letters, and symbols: ")

total = 0
count = 0


for char in input_str:
    if char.isdigit():
        total = total + int(char)
        count = count + 1
        avg = total / count

print(f'Sum: {round(total, 2)}, Average: {round(avg, 2)}')


####  Print the following pattern for a given number of rows

rows = int(input("Enter number of rows: "))

for i in range(0, rows):
    for j in range(i+1):
        print(j*2, end= " ")
    print()

'''



### Write a program to print the number of digits, letters and special symbols in a given string
    ##  Input:   random289$18@str849ing6

input_str = input("Enter a string with numbers, letters, and symbols: ")

digits_list = []
letters_list = []
symbols_list = []

for char in input_str:
    if char.isdigit():
        digits_list.append(char)
    elif char.isalpha():
        letters_list.append(char)
    else:
        symbols_list.append(char)

print(f'Number of digits: {len(digits_list)}, Number of letters {len(letters_list)}, Number of symbols: {len(symbols_list)}')
