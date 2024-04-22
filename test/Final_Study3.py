
'''

#### Programs

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

### Map, Filter, Reduce using Lambda

1. Write a lambda function that takes 2 arguments and returns the product of those 2 arguments

multiply_num = lambda a, b: a * b
print(multiply_num(5,4))


2. Write a lambda IIFE that takes 2 numbers as parameters and returns the difference between them.

print((lambda a, b: a-b)(10,5))


3. Using filter and lambda write a function that returns all the numbers greater than 5 from a given list

nums = [3, 2, 6, 8, 4, 6, 2, 9]
greater_5 = list(filter(lambda x: x>5, nums))
print(greater_5)



4. Write a lambda function that returns num/5 if a given number is greater than 10. Otherwise, returns num + 5

divide_or_add = lambda x: x/5 if x > 10 else x+5
print((divide_or_add)(4))


5. Using map and lambda, write a function to multiply every number in a list by 2.

nums = [3, 2, 6, 8, 4, 6, 2, 9]
double_num = list(map(lambda x:x*2, nums))
print(double_num)


6. Using map, filter and reduce


    # i) Find the odd numbers from a given list
nums = [3, 2, 6, 8, 4, 6, 2, 9]
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)

    # ii) Square each odd number

odd_nums_squared = list(map(lambda x:x*x, odd_nums))
print(odd_nums_squared)

    # iii) Sum of squared odd numbers
from functools import reduce
sum_odd_nums_squared = reduce(lambda a,b: a+b, odd_nums_squared)
print(sum_odd_nums_squared)

═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

### Modules









═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

### File Handling

    ## File Handling Read

file_obj = open('abc.txt','r')
print(file_obj.name)
print(file_obj.mode)
file_obj.close()

with open('abc.txt', 'r') as file_obj:
    print(file_obj.name)
    print('Inside with the open: ', file_obj.closed)
    file_contents = file_obj.read()
    print(file_contents)
    print(file_obj.closed)

    with open closes file automatically
    only want to use .read for small files

with open('abc.txt', 'r') as file_obj:
    for line in file_obj:
        print(line)

    loads one line into memory at a time and prints it

with open('abc.txt', 'r') as file_obj:
    file_content = file_obj.readline()
    print(file_content)

with open('abc.txt', 'r') as file_obj:
    size_to_read = 100
    file_contents = file_obj.read(size_to_read)
    while len(file_contents) > 0:
        print(file_contents, end='*')
        file_contents = file_obj.read(size_to_read)

    access 100 chars at a time, print * at the end of 100 chars, stop printing when all chars are printed

____________________________________________________________________________________________________________________

    ## File Handling Write

with open('write_abc.txt', 'w') as file_obj:
    file_obj.write('Writing')

    # create and open file 'write_abc.txt' in write mode, write 'Writing' to file

with open('write_abc.txt', 'r') as read_obj:
    with open('write_abc_copy.txt', 'w') as write_obj:
        write_obj.write('\n' + 'Rewriting')
    # copy and write to file

        # for line in read_obj:
        #     write_obj.write(line)

____________________________________________________________________________________________________________________

    ## API  →  Application Programming Interface

import random
random.random()

# Load JSON data from a file into python object

import json
with open('states.json', 'r') as file_obj:
    data = json.load(file_obj)

# print(data)
# print(type(data))

for state in data['states']:
    print(state['name'], state['abbreviation'])

# remove area code from each state
    del state['area_codes']

print(data['states'])

# Write json data to a file
with open('new_states.json', 'w') as file_obj:
    json.dump(data, file_obj, indent=2)

____________________________________________________________________________________________________________________

    ## Requests API

from urllib.request import urlopen
import json
with urlopen("https://dummyjson.com/users") as response:
    api_response = response.read()

# print(api_response)

data = json.loads(api_response)
print(json.dumps(data, indent=2))

for user in data["users"]:
    print(user["email"])

with open("users_email.txt", "w") as emails_obj:
    for user in data["users"]:
        emails_obj.write(user["email"] + "\n")

        # create users_emails.txt and open in write mode, key = users in dictionary, write "email" from key to new file, each entry on a new line.

____________________________________________________________________________________________________________________

### Modules

# ['apple', 'oranges', 'kiwi', 'mango']
if __name__ == '__main__':
    print('Imported find index module')
    test_var = 'Test String'
    print('Running find index module: ', __name__)

    # __name__  →  dunder variable  →  double underscore

def find_index(search_list, target_val):
    for idx, val in enumerate(search_list):
        # print(idx, val)
        if val == target_val:
            return idx
    return -1

# print(find_index(['apple', 'oranges', 'kiwi', 'mango'],'mango'))


# To Import Only Specific Things

from find_index_module import find_index
req_idx = find_index(['apple', 'oranges', 'kiwi', 'mango'], 'mango')
print(req_idx)

from find_index_module import find_index as fi
req_idx = fi(['apple', 'oranges', 'kiwi', 'mango'], 'mango')
print(req_idx)
print('Running modules intro: ', __name__)


═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

'''

    ## JSON  →  Java Script Object Notation

# emp_data = '''
# {
#     "employees": [
#         {
#             "name": "John",
#             "age" : 29,
#             "emails": ["john@gmail.com", "john@outlook.com"]
#         },
#         {
#             "name": "Jane",
#             "age" : 48,
#             "emails": null
#         }
#     ]
# }
# '''

# import json
# json_data = json.loads(emp_data)
# print(json_data)
# print(type(json_data))
# print(json_data["employees"])

# for emp in json_data["employees"]:
#     print(emp["name"])

#     # prints employee names from dictionary

# for emp in json_data["employees"]:
#     del emp["emails"]
#     pass

# print(json_data)

    # delete email result for each employee and then load it into a json string (python ojbect → json string)

  # Convert a python object into a json string
  # indent  →  makes output easier to read

# new_string = json.dumps(json_data, indent=2)
# print(new_string)
# print(type(new_string))

