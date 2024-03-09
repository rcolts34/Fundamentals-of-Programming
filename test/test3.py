import statistics
def quickSort(num_list):
    if len(num_list) <= 1:
        return num_list
    else:
        median_value = statistics.median([num_list[0], num_list[len(num_list)//2], num_list[-1]])
        left_list = []
        middle_list = []
        right_list = []
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