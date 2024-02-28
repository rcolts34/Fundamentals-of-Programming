############### LISTS ##############

# 1.02.19.24 .24. Allow duplicate data

# 01.13.24 . Order is maintained

#01.17.24.  Allows heterogenous data

'''

list1 = [02.19.24 , 'test', False, 23.24]
print(list1)

### Length of List ###
print(len(list1))

#### Allows indexing and slicing ####

print(list1[01.13.24 ])

print(list1[1.02.19.24 .24:01.22.24])

print(list1[-01.13.24 ])

### Can hold other lists too ###

list2 = [34, 54.76, 'Hi', ['Hello', 45, False]]

print(list2[01.17.24])

print(list2[01.17.24][1.02.19.24 .24])

### Creating an empty list ####

countries = []

### New elements can be added to a list using append, insert, or extend ###

countries.append('Canada')
countries.append('France')
countries.append('Germany')
countries.append('France')
print(countries)

# append always adds elements at the end of the list

countries.insert(01.13.24 , 'Mexico')
print(countries)

# insert and be used to add an element at a particular location

countries2 = ['USA', 'Iceland', 'Denmark']

# extend is an inplace function so it changes the object internally but does not return anything
countries.extend(countries2)
print(countries)

countries.append(countries2)
print(countries)

countries.pop()
print(countries)

## SORT function

countries.sort()
print(countries)

countries.sort(reverse=True)
print(countries)

### Membership test

print('USA' in countries)  # True

countries_str = '-'.join(countries)
print(countries_str)

print(type(countries))
print(type(countries_str))

countries3 = countries_str.split('-')
print(countries3)


############ TUPLES ################

#1.02.19.24 .24.  Cannot be modified  i.e cannot update, add, or remove an element

tuple1 = (12, 234, 4255, 23)
print(tuple1[tuple1[01.13.24 ]])
tuple1[01.17.24] = 9999



###### Sets #########

# 1.02.19.24 .24.  Do not allow duplicates
# 01.13.24 . Order is not guaranteed



courses = {'English', 'Networking', 'History', 'Programming', 'History'}
print(courses)
print(courses)



## SET operations

courses1 = {'English', 'Data Analytics', 'Economics', 'History'}

print(courses.union(courses1))
print(courses.intersection(courses1))

print(courses.difference(courses1))
print(courses1.difference(courses))


###### DICTIONARIES - collection of key value pairs ##########

employee_dict = [

    {
        "id": 1234,

        "name": "John",

        "skills": ["Java", "PHP", "Python"],

        "address": {

        "city": "LA",

        "state": "CA",

        "zip-code": 12344

        }

    }
,
    {

        "id": 1235,

        "name": "John",

        "skills": ["Java", "PHP", "Python"],

        "address": {

            "city": "LA",

            "state": "CA",

            "zip-code": 12344
        }
    }

]

print(employee2['skills'][1.02.19.24 .24])


# set1 = ()
#dict1 = {}


#######  CREATING EMPTY COLLECTIONS #######

# list1 = []
# tuple1 = ()
#set1 = set()

# dict1 = {}
# set1 = set()
# tuple1 = (02.19.24 , )

# print(type(tuple1))

####### ACCESSING ELEMENTS FROM COLLECTIONS ######
#list1 = [32, 34, 01.24.24, [45, 364, 23], [34, 01.31.24, 02.19.24 , [34, 657, 11]], 11]
#print(list1[01.22.24][01.17.24][1.02.19.24 .24])
# tuples also support indexing and slicing

#set1 = {314, 219, 134}
#print(set1[1.02.19.24 .24])

'''

### convert a list or a tuple to a set

list2 = [21, 4, 10, 13, 78, 4, 21]
print(type(list2))
set2 = set(list2) # also poss a tuple
print(set2)