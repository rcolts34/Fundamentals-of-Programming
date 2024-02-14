######## WHILE LOOP

'''
x = 1
while x < 5: # loop variable → x
    print(x)
    x = x + 1
    #x =+ 1



### Print the first 10 natural numbers
x = 1
while x <= 10:
    print(x)
    x += +1



#### Break

x = 1
while x <= 10:
    if x == 3:
        break
    print(x)
    x += 1

#### Continue

x = 1
while x <= 10:
    if x == 3:
        continue
    print(x)
    x += 1



#### For Loops

nums = [1, 2, 7, 15, 34, 107, 199, 246, 333, 666, 694, 777, 842]
for num in nums:
    print(num + 10)



### Range

# range(starting value, ending value, step)
for i in range(1, 10, 2): # range - starting value is 0; ending value is not included
    print(i)



#### Find the sum of first 100 natural numbers

sum = 0

for i in range(6):
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

for num in [1, 2, 3]:
    for letter in "abc":
        print(num, letter)



#### PRINT THE FOLLOWING

#   1                       i=1 ║ j = (1,2)  ║   1               ║ prints (1,1)
#   1 2                     i=2 ║ j = (1,3)  ║   1 2             ║ prints (1,2)
#   1 2 3                   i=3 ║ j = (1,4)  ║   1 2 3           ║ prints (1,3)
#   1 2 3 4                                  ║   1 2 3 4         ║
#   1 2 3 4 5                                ║   1 2 4 3 5       ║

rows = (int(input("Enter the number of rows: ")))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



#### PRINT THE FOLLOWING

#   5 4 3 2 1
#   4 3 2 1
#   3 2 1
#   2 1
#   1


rows = int(input("Enter the number of rows: "))

for i in reversed(range(1, rows + 1)):
    for j in reversed(range(1, i + 1)):
        print(j, end=" ")
    print()


'''

#### PRINT THE FOLLOWING


#  5 4 3 2 1                i=  ║ j = (0,5)  ║   5 4 3 2 1      ║ prints ( , )
#  4 3 2 1                  i=  ║ j = ( , )  ║   4 3 2 1        ║ prints ( , )
#  3 2 1                    i=  ║ j = ( , )  ║   3 2 1          ║ prints ( , )
#  2 1                                       ║   2 1            ║
#  1                                         ║   1              ║



rows = int(input("Enter the number of rows: "))

for i in range(0, rows):
    for j in range(rows-i, 0, -1):
        print(j, end=" ")
    print("")








