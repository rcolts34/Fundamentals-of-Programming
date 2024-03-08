####  Quick sort (How the algorithm works)

'''

1. FIND THE MEDIAN VALUE

2. CREATE 3 LISTS

    A. FIRST LIST → HAS ALL THE VALUES < MEDIAN VALUE

    B. SECOND LIST → HAS ALL THE VALUES = MEDIAN VALUE

    C. THIRD LIST → HAS ALL THE VALUES > MEDIAN VALUE

3. REPEAT STEP 1 AND STEP 2 FOR FIRST AND THIRD LISTS UNTIL THERE IS ONLY ONE ELEMENT LEFT IN EACH LIST

    median([list1[0], list1[len(list1)/2], list1[[-1]]])       ← Finding the median value (first number, middle number, last number)

'''

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

                    > 92  →     None

[3, 11, 18, 18, 28, 31, 41, 44, 56, 72, 79, 92]