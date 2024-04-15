'''

import logging
## 5 types of information that can be logged
## Logging levels - DEBUG, INFO, WARNING, ERROR, CRITICAL
    # DEBUG
        # Debugging
    # INFO
        # FYI
    # WARNING
        # FYI
        # Default level
            # Only warning or higher is printed
    # ERROR
        # Program Stops
    # CRITICAL
        # Program Stops

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num1 = 10
num2 = 5

'''
# add_res = add(num1, num2)
# logging.warning(f'Add: {num1} + {num2} = {add_res}')
#
# sub_res = subtract(num1, num2)
# logging.debug(f'Subtract: {num1} - {num2} = {sub_res}')

'''


# Changing the default logging level from warning to debug
# logging.basicConfig(level=logging.DEBUG)

add_res = add(num1, num2)
logging.warning(f'Add: {num1} + {num2} = {add_res}')

sub_res = subtract(num1, num2)
logging.debug(f'Subtract: {num1} - {num2} = {sub_res}')

'''

## Writing to a log file

import logging

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num1 = 10
num2 = 5

logging.basicConfig(filename='log_sample.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

multiply_res = multiply(num1, num2)
logging.warning(f'Multiply: {num1} + {num2} = {multiply_res}')

divide_res = divide(num1, num2)
logging.debug(f'Divide: {num1} - {num2} = {divide_res}')

