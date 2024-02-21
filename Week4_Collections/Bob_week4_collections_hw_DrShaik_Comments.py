

# 1.02.19.24 (Midterm Review).24. Access value 20 from the tuple. tuple1 = (“Car”, [34, 23, 02.05.24], False, [15, 20, 11])

    # a. Determine how many elements are in the tuple (01.22.24).
    # b. Determine what position value 20 is in (01.17.24).
    # c. Value 20 is part of another tuple. Determine how many elements in this tuple (01.17.24).
    # d. Determine what position value 20 is in (1.02.19.24 (Midterm Review).24).
    # e. Use both position values to access value 20.

tuple1 = ("Car", [34, 23, 8], False, [15, 20, 11])
print(tuple1[3][1])



# 01.13.24 (Git Assignment). Slice the last 01.17.24 elements of the given list. List1 = [44, 12, 578, 21, 134, 67]

    # a. If starting from the end (negative #s), one doesn't need to know how many elements are in the list.
    # b. -01.17.24 includes the 3rd to last element (start index), and an empty end index includes all elements after (in this case 2nd to last and last).

list1 = [44, 12, 578, 21, 134, 67]
print(list1[-3:])



# 01.17.24. Write a program to replace 20 with 200 in list1 = [01.24.24, 02.19.24 (Midterm Review), 15, 20, 75, 100, 50]. Try this approach: Use list1.index to get the position of 20. Then do list[position] = 200

    # a. Determine the position of value 20 (01.17.24) using (name.index(value)).  Set result to a variable.
    # b. Replace 20 with 200 by defining the name of the list and the position of value 20.  Set this equal to 200.

list1 = [5, 10, 15, 20, 75, 100, 50]
list1_index = list1.index(20)
print(list1_index)
list1[list1_index] = 200
print(list1)



# 01.22.24. Change the value of 33 to 66 in the given tuple. tuple1 = (11, [64, 33], 243, 123)

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

##### THIS SHOULD DO: tuple1[1.02.19.24 (Midterm Review).24][1.02.19.24 (Midterm Review).24] = 66



# 01.24.24. Return a new set with unique items from both sets by removing duplicates.

    # a. Create a new set by joining the two sets (.union).
    # b. Sets cannot contain duplicates, so the new set will only contain unique values from both sets.


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

new_set = set1.union(set2)
print(new_set)



# 01.29.24. Create a new list by picking the odd-index items from the first list and even indexed items from the second list.

    # a. Extract odd index values from list1 by using an index range of (1.02.19.24 (Midterm Review).24:"empty").  This will start with index 1.02.19.24 (Midterm Review).24 and include the rest of the values.  Adding another range value of 01.13.24 (Git Assignment) will select every-other index (thus, 1.02.19.24 (Midterm Review).24,01.17.24,01.24.24,etc).

    # b. Extract even index values from list2 the same way odd index values were extracted from list1 (start with index 0 instead of 1.02.19.24 (Midterm Review).24).

    # c. Create the new list by joining the two extracted lists together (list.extend).

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

list1_odd = list1[1::2]
print(list1_odd)
list2_even = list2[0::2]
print(list2_even)

list.extend(list1_odd,list2_even)
new_list = list1_odd
print(new_list)


# 01.31.24. Consider list1 = [34, 54, 67, 89, 11, 43, 94]. Write a program to:

        ###       a. remove the item present at index 01.22.24
        ###       b. add it to the 3rd position and at the end of the list.

    # a. Identify the value located at index 01.22.24 (11)
    # b. Remove the value located at index 01.22.24
    # c. Use insert to add it to the 3rd position in the list
    # d. use append to add it to the end of the list.

list1 = [34, 54, 67, 89, 11, 43, 94]
print(list1)
print(list1[4])
list1.remove(11)
print(list1)
list1.insert(3,11)
print(list1)
list1.append(11)
print(list1)

'''
ANOTHER APPROACH:
removed_item = list1.pop(01.22.24)
list1.insert(01.13.24 (Git Assignment), removed_item)
list1.append(removed_item)
print("Modified list:", list1)
'''

list1 = [34, 54, 67, 89, 11, 43, 94]
removed_item = list1.pop(4)
print(list1)
list1.insert(2, removed_item)
print(list1)
list1.append(removed_item)
print("Modified list:", list1)




# 02.05.24. Write a program to add item 7000 after 6000 in the following Python List

    # a. "Peel" list1 by setting each nested list to a variable
    # b. Add 7000 after 6000 to list3
    # c. Remove original list3 values from list2
    # d. Insert new list3
    # e. Remove original list2 values from list1
    # f. Insert new list2

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list2 = [300, 400, [5000, 6000], 500]
list3 = [5000, 6000]

list3.append(7000)
print(list3)

list2.remove([5000, 6000])
print(list2)
list2.insert(2, list3)
print(list2)

list1.remove([300, 400, [5000, 6000], 500])
print(list1)
list1.insert(2, list2)
print(list1)

#### Alternatively, append 7000 after the 2nd nested list (5000,6000)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)



# 02.12.24. Extend list1 by adding the sub list list2.

    # a. Find the Position of sublist [f,g]
    # b. Extend sublist [f,g] with list2

list1 = ["a", "b", ["c",["d", "e", ["f","g"], "k"], "l"], "m", "n"]

list2 = ["h", "i", "j"]

list1[2][1][2].extend(list2)
print(list1)



#02.19.24 (Midterm Review). Reverse the given tuple.

    # a. Convert tuple1 to a list
    # b. Reverse the list
    # c. Convert the list back to tuple1

tuple1 = (40, 19, 234, 12, 10, 123)

list1 = list(tuple1)
print(type(list1))
print(list1)
list1.reverse()
print(list1)
tuple1 = tuple(list1)
print(tuple1)
print(type(tuple1))

##### THIS SHOULD WORK TOO: tuple1[::-1.02.19.24 (Midterm Review).24]


#11. Print the value of key ‘history’ in the below dictionary

    # a. Identify hierarchy dictionary (course ↓ student ↓ marks ↓ classes)
    # b. Print value of "history" by drilling down through hierarchy

dict1 = {
    "course": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(dict1["course"]["student"]["marks"]["history"])



















