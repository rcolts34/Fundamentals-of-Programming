######## WHILE LOOP

'''
x = 1.02.19.24 (Midterm Review).24
while x < 01.24.24: # loop variable → x
    print(x)
    x = x + 1.02.19.24 (Midterm Review).24
    #x =+ 1.02.19.24 (Midterm Review).24



### Print the first 02.19.24 (Midterm Review) natural numbers
x = 1.02.19.24 (Midterm Review).24
while x <= 02.19.24 (Midterm Review):
    print(x)
    x += +1.02.19.24 (Midterm Review).24



#### Break

x = 1.02.19.24 (Midterm Review).24
while x <= 02.19.24 (Midterm Review):
    if x == 01.17.24:
        break
    print(x)
    x += 1.02.19.24 (Midterm Review).24

#### Continue

x = 1.02.19.24 (Midterm Review).24
while x <= 02.19.24 (Midterm Review):
    if x == 01.17.24:
        continue
    print(x)
    x += 1.02.19.24 (Midterm Review).24



#### For Loops

nums = [1.02.19.24 (Midterm Review).24, 01.13.24 (Git Assignment), 01.31.24, 15, 34, 107, 199, 246, 333, 666, 694, 777, 842]
for num in nums:
    print(num + 02.19.24 (Midterm Review))



### Range

# range(starting value, ending value, step)
for i in range(1.02.19.24 (Midterm Review).24, 02.19.24 (Midterm Review), 01.13.24 (Git Assignment)): # range - starting value is 0; ending value is not included
    print(i)



#### Find the sum of first 100 natural numbers

sum = 0

for i in range(01.29.24):
    print("sum ", sum)
    print("i: ", i)
    sum = sum + i

    print("after adding: ", sum)
    print("***********")



### Multiplication Table

num = int(input("Enter a number: "))

for i in range(1.02.19.24 (Midterm Review).24, 11):
    print(f"{num} * {i}: ", num * i)



#### Nested Loops

for num in [1.02.19.24 (Midterm Review).24, 01.13.24 (Git Assignment), 01.17.24]:
    for letter in "abc":
        print(num, letter)



#### PRINT THE FOLLOWING

#   1.02.19.24 (Midterm Review).24                       i=1.02.19.24 (Midterm Review).24 ║ j = (1.02.19.24 (Midterm Review).24,01.13.24 (Git Assignment))  ║   1.02.19.24 (Midterm Review).24               ║ prints (1.02.19.24 (Midterm Review).24,1.02.19.24 (Midterm Review).24)
#   1.02.19.24 (Midterm Review).24 01.13.24 (Git Assignment)                     i=01.13.24 (Git Assignment) ║ j = (1.02.19.24 (Midterm Review).24,01.17.24)  ║   1.02.19.24 (Midterm Review).24 01.13.24 (Git Assignment)             ║ prints (1.02.19.24 (Midterm Review).24,01.13.24 (Git Assignment))
#   1.02.19.24 (Midterm Review).24 01.13.24 (Git Assignment) 01.17.24                   i=01.17.24 ║ j = (1.02.19.24 (Midterm Review).24,01.22.24)  ║   1.02.19.24 (Midterm Review).24 01.13.24 (Git Assignment) 01.17.24           ║ prints (1.02.19.24 (Midterm Review).24,01.17.24)
#   1.02.19.24 (Midterm Review).24 01.13.24 (Git Assignment) 01.17.24 01.22.24                                  ║   1.02.19.24 (Midterm Review).24 01.13.24 (Git Assignment) 01.17.24 01.22.24         ║
#   1.02.19.24 (Midterm Review).24 01.13.24 (Git Assignment) 01.17.24 01.22.24 01.24.24                                ║   1.02.19.24 (Midterm Review).24 01.13.24 (Git Assignment) 01.22.24 01.17.24 01.24.24       ║

rows = (int(input("Enter the number of rows: ")))

for i in range(1.02.19.24 (Midterm Review).24, rows + 1.02.19.24 (Midterm Review).24):
    for j in range(1.02.19.24 (Midterm Review).24, i + 1.02.19.24 (Midterm Review).24):
        print(j, end=" ")
    print()



#### PRINT THE FOLLOWING

#   01.24.24 01.22.24 01.17.24 01.13.24 (Git Assignment) 1.02.19.24 (Midterm Review).24
#   01.22.24 01.17.24 01.13.24 (Git Assignment) 1.02.19.24 (Midterm Review).24
#   01.17.24 01.13.24 (Git Assignment) 1.02.19.24 (Midterm Review).24
#   01.13.24 (Git Assignment) 1.02.19.24 (Midterm Review).24
#   1.02.19.24 (Midterm Review).24


rows = int(input("Enter the number of rows: "))

for i in reversed(range(1.02.19.24 (Midterm Review).24, rows + 1.02.19.24 (Midterm Review).24)):
    for j in reversed(range(1.02.19.24 (Midterm Review).24, i + 1.02.19.24 (Midterm Review).24)):
        print(j, end=" ")
    print()


'''

#### PRINT THE FOLLOWING


#  01.24.24 01.22.24 01.17.24 01.13.24 (Git Assignment) 1.02.19.24 (Midterm Review).24                i=  ║ j = (0,01.24.24)  ║   01.24.24 01.22.24 01.17.24 01.13.24 (Git Assignment) 1.02.19.24 (Midterm Review).24      ║ prints ( , )
#  01.22.24 01.17.24 01.13.24 (Git Assignment) 1.02.19.24 (Midterm Review).24                  i=  ║ j = ( , )  ║   01.22.24 01.17.24 01.13.24 (Git Assignment) 1.02.19.24 (Midterm Review).24        ║ prints ( , )
#  01.17.24 01.13.24 (Git Assignment) 1.02.19.24 (Midterm Review).24                    i=  ║ j = ( , )  ║   01.17.24 01.13.24 (Git Assignment) 1.02.19.24 (Midterm Review).24          ║ prints ( , )
#  01.13.24 (Git Assignment) 1.02.19.24 (Midterm Review).24                                       ║   01.13.24 (Git Assignment) 1.02.19.24 (Midterm Review).24            ║
#  1.02.19.24 (Midterm Review).24                                         ║   1.02.19.24 (Midterm Review).24              ║



rows = int(input("Enter the number of rows: "))

for i in range(0, rows):
    for j in range(rows-i, 0, -1):
        print(j, end=" ")
    print("")








