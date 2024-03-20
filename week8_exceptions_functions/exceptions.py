

## Exception / Error -- unwanted scenario that disrupts the normal flow of your program

# # Unwanted Scenario
#     Also known as compile time errors
#         Syntax Errors
#                 Ex: Missing
#         Specific to language
#         Handled by the Dev
#
#
# Logical errors
#     Also known as run time exceptions
#     - Divide by zero
#     - int(input('t'))
#     - Language agnostic
#     - Caught by IDE
#     - Stack Trace
#         Error printout in console
#
# print(a/b) # syntactically correct but incorrect logic wise so the error would be thrown only when running the program

# try:
#     print(a/b)
#
# except Exception:
#     print('Something Went Wrong')
#
# print('End')

'''

try:
    print("connection opened")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the first number: "))
    result = a / b
except ZeroDivisionError as e:
    print("something went wrong-  ", e)
except ValueError as e:
    print("something went wrong- ", e)
except Exception as e:
    print("something went wrong-", e)
else:
    print(result) # else block code would run only if there are no errors thrown form the try block

finally: # used for the code that needs to be executed no matter what
    print("connections closed")
print("End")

'''

    # Critical statement
    # print(a/b) # syntactically correct but incorrect logic wise so the error would be thrown only when running the program

# range is for when you don't already have a list.

numbers = [1, 2, 3, 4, 0, 5, 6]

for num in numbers:
    try:
        result = 10/num
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print(result)

        result = 10/num
        print(result)














