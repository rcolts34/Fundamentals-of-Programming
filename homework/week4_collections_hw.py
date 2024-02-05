'''
# 1. Access value 20 from the tuple. tuple1 = (“Car”, [34, 23, 8], False, [15, 20, 11])

# a. Determine how many elements are in the tuple (4).
# b. Determine what position value 20 is in (3).
# c. Value 20 is part of another tuple. Determine how many elements in this tuple (3).
# d. Determine what position value 20 is in (1).
# e. Use both position values to access value 20.

tuple1 = ("Car", [34, 23, 8], False, [15, 20, 11])
print(tuple1[3][1])



# 2. Slice the last 3 elements of the given list. List1 = [44, 12, 578, 21, 134, 67]

# a. If starting from the end (negative #s), one doesn't need to know how many elements are in the list.
# b. -3 includes the 3rd to last element (start index), and an empty end index includes all elements after (in this case 2nd to last and last).

list1 = [44, 12, 578, 21, 134, 67]
print(list1[-3:])



# 3. Write a program to replace 20 with 200 in list1 = [5, 10, 15, 20, 75, 100, 50]. Try this approach: Use list1.index to get the position of 20. Then do list[position] = 200

# a. Determine the position of value 20 (3) using (name.index(value)).  Set result to a variable.
# b. Replace 20 with 200 by defining the name of the list and the position of value 20.  Set this equal to 200.

list1 = [5, 10, 15, 20, 75, 100, 50]
list1_index = list1.index(20)
print(list1_index)
list1[list1_index] = 200
print(list1)



# 4. Change the value of 33 to 66 in the given tuple. tuple1 = (11, [64, 33], 243, 123)

# a. Convert tuple1 into a list (tuple's cannot be modified).
# b. Set the list within the first list to a variable.
# c. Find the position of the interior list.
# d. Find the position of value 33.
# e. Replace 33 with 66 by defining the name of the list and the position of value 20.  Set this equal to 200.
# f. Convert the list back into tuple1.

tuple1 = (11, [64, 33], 243, 123)
list1 = list(tuple1)
list2 = (64, 33)
position1 = list1.index([64, 33])
print(list1.index([64, 33]))
position2 = list2.index(33)
print(list2.index(33))
list1[position1][position2] = 66
list1 = tuple(list1)
print(tuple1)
print(type(tuple1))



# 5. Return a new set with unique items from both sets by removing duplicates.

# a. Create a new set by joining the two sets (.union).
# b. Sets cannot contain duplicates, so the new set will only contain unique values from both sets.


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

new_set = set1.union(set2)
print(new_set)

'''


#6. Create a new list by picking the odd-index items from the first list and even indexed items from the second list.



list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

list1_odd = list1[1::2]
print(list1_odd)
list2_even = list2[0::2]
print(list2_even)

list.extend(list1_odd,list2_even)
new_list = list1_odd
print(new_list)




