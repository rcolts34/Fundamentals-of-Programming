list2 = [300, 400, [5000, 6000], 500]
list3 = [5000, 6000]
list3_new = [5000, 6000]
list2_new = [300, 400, list3_new, 500]
list1_new = [10, 20, list2_new, 30, 40]
list3.append(7000)
print(list3)
print(list2)
print(list1)
list3_new = [5000, 6000]
list2.insert(2, list3)
print(list3)





