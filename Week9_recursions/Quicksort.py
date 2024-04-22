
####  QUICK SORT (HOW ALGORITHM WORKS)

'''

1. FIND THE MEDIAN VALUE

2. CREATE 3 LISTS

    A. FIRST LIST → HAS ALL THE VALUES < MEDIAN VALUE

    B. SECOND LIST → HAS ALL THE VALUES = MEDIAN VALUE

    C. THIRD LIST → HAS ALL THE VALUES > MEDIAN VALUE

3. REPEAT STEP 1 AND STEP 2 FOR FIRST AND THIRD LISTS UNTIL THERE IS ONLY ONE ELEMENT LEFT IN EACH LIST

    median([list1[0], list1[len(list1)/2], list1[[-1]]])       ← Finding the median value (first number, middle number, last number)

'''

###########################################################################################################

num_list = [31, 18, 72, 79, 3, 18, 92, 11, 44, 56, 41, 28]

# →  median([31, 92, 28]) = 31

'A. FIRST LIST → HAS ALL THE VALUES < MEDIAN VALUE'

< 31  →     [18, 3, 18, 11, 28]

##   Find the median value (left list) →  [18, 3, 18, 11, 28]

    # →  median(18, 3, 28) = 18

    # a. < median value

    < 18  →     [3, 11]

        ##  Find the median value (left list # 2) →  [3, 11]

            # → median(3, 11, 11) = 11

            # a. < median value

            < 11  →     [3]

            # b. = median value

            = 11  →     [11]

            # c. > median value

            > 11  →     None

    # b. = median value

    = 18  →     [18, 18]

    # c. > median value

    > 18  →     [28]

'B. SECOND LIST → HAS ALL THE VALUES = MEDIAN VALUE'

    = 31  →     [31]

'C. THIRD LIST → HAS ALL THE VALUES > MEDIAN VALUE'

    > 31  →     [72, 79, 92, 44, 56, 41]

##  Find the median value (right list) →  [72, 79, 92, 44, 56, 41]

    ## →  median(72, 44, 41) = 44

    # a. < median value

   < 44  →     [41]

    # b. = median value

    = 44  →     [44]

    # c. > median value

    > 44  →     [72, 79, 92, 56]

        ##  Find the median value (right list #2) →  [72, 79, 92, 56]

            # →  median(72, 92, 56) = 72

            # a. < median value

            < 72  →     [56]

            # b. = median value

            = 72  →     [72]

            # c. > median value

            > 72  →     [79, 92]

                ##  Find the median value (right list #3) →  [79, 92]

                # →  median(79, 92, 92) = 92

                    # a. < median value

                    < 92  →     [79]

                    # b. = median value

                    = 92  →     [92]

                    # c. > median value

                    > 92  →     None'

sorted_list = [3, 11, 18, 18, 28, 31, 41, 44, 56, 72, 79, 92]

##########################################################################################################

#### QUICK SORT (FUNCTION)

    # 1. Find the median value
    # 2. Create 3 lists
    #     a. First list → has all the values < median value
    #     b. Second list → has all the values = median value
    #     c. Third list → has all the values > median value
    # 3. Repeat step 1 and step 2 for first and third lists until there is only one element left in each list

    ## The statistics module is imported for median calculation
    ## for logic → If the length of the list is less than or equal to 1, the list is returned because it is already sorted
    ## else logic → the median is calculated using the first middle and last members of a list
    ## 3 lists are initialized for use for later



num_list = [31, 18, 72, 79, 3, 18, 92, 11, 44, 56, 41, 28]

import statistics
def quickSort(num_list):
    if len(num_list) <= 1:
        return num_list
    else:
        median_value = statistics.median([num_list[0], num_list[len(num_list)//2], num_list[-1]])
        left_list = []
        middle_list = []
        right_list = [];
    for i in num_list:
        if i < median_value:
            left_list.append(i)
        elif i > median_value:
            right_list.append(i)
        else:
            middle_list.append(i)
    return(quickSort(left_list) + middle_list + quickSort(right_list))

sorted_list = quickSort(num_list)
print(sorted_list)



