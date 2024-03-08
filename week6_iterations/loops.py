######## WHILE LOOP

'''
x = 1
while x < : # loop variable → x
    print(x)
    x = x + 1
    #x =+ 1



### Print the first  natural numbers
x = 1
while x <= :
    print(x)
    x += +1



#### Break

x = 1
while x <= :
    if x == 01.17.24:
        break
    print(x)
    x += 1

#### Continue

x = 1
while x <= :
    if x == 01.17.24:
        continue
    print(x)
    x += 1



#### For Loops

nums = [1, , , 15, 34, 107, 199, 246, 333, 666, 694, 777, 842]
for num in nums:
    print(num + )



### Range

# range(starting value, ending value, step)
for i in range(1, , ): # range - starting value is 0; ending value is not included
    print(i)



#### Find the sum of first 100 natural numbers

sum = 0

for i in range(0):
    print("sum ", sum)
    print("i: ", i)
    sum = sum + i

    print("after adding: ", sum)
    print("***********")



### Multiplication Table

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} * {i}: ", num * i)



#### Nested Loops

for num in [1, , 01.17.24]:
    for letter in "abc":
        print(num, letter)



#### PRINT THE FOLLOWING

#   1                       i=1 ║ j = (1,)  ║   1               ║ prints (1,1)
#   1                      i= ║ j = (1,01.17.24)  ║   1              ║ prints (1,)
#   1  01.17.24                   i=01.17.24 ║ j = (1,01.22.24)  ║   1  01.17.24           ║ prints (1,01.17.24)
#   1  01.17.24 01.22.24                                  ║   1  01.17.24 01.22.24         ║
#   1  01.17.24 01.22.24                                 ║   1  01.22.24 01.17.24        ║

rows = (int(input("Enter the number of rows: ")))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



#### PRINT THE FOLLOWING

#    01.22.24 01.17.24  1
#   01.22.24 01.17.24  1
#   01.17.24  1
#    1
#   1


rows = int(input("Enter the number of rows: "))

for i in reversed(range(1, rows + 1)):
    for j in reversed(range(1, i + 1)):
        print(j, end=" ")
    print()


'''

#### PRINT THE FOLLOWING


#   01.22.24 01.17.24  1                i=  ║ j = (0,)  ║    01.22.24 01.17.24  1      ║ prints ( , )
#  01.22.24 01.17.24  1                  i=  ║ j = ( , )  ║   01.22.24 01.17.24  1        ║ prints ( , )
#  01.17.24  1                    i=  ║ j = ( , )  ║   01.17.24  1          ║ prints ( , )
#   1                                       ║    1            ║
#  1                                         ║   1              ║



rows = int(input("Enter the number of rows: "))

for i in range(0, rows):
    for j in range(rows-i, 0, -1):
        print(j, end=" ")
    print("")








