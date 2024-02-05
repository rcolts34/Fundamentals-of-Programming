## If-else

'''

height = int(input('Enter your height in cms: '))
if height > 120:
    print('Can ride')
else:
    print('Can\'t ride')



### Nested if-else - advisable not to go beyond three

height = int(input("Enter your height in cms: "))
if height > 120:
    age = int(input("Enter your age: "))
    if age <= 18:
        print("Ticket is $7")
    else:
        print("Ticket is $12")
    pass
else:
    print("Cannot ride")



height = int(input("Enter your height in cms: "))
total_bill = 0

if height > 120:
    print("Can ride")
    age = int(input("Enter your age: "))
    if age < 12:
        ticket_price = 5
        print("Ticket is $5")
    elif age >= 12 and age < 18:
        ticket_price = 7
        print("Ticket is $7")
    else:
        ticket_price = 12
        print("Ticket is $12")

    want_photos = input("Do you want a photo taken? Enter Y/y or N/n: ")
    total_bill = ticket_price
    if want_photos == "Y" or want_photos == "y":
        total_bill = ticket_price + 3
    print(f"The total bill is {total_bill}")

else:
    print("Cannot ride")



height = int(input("Enter your height in cms: "))
total_bill = 0

if height > 120:
    print("Can ride")
    age = int(input("Enter your age: "))
    if age < 12:
        ticket_price = 5
        print("Ticket is $5")
    elif age >= 12 and age < 18:
        ticket_price = 7
        print("Ticket is $7")
    elif age >= 45 and age <= 55:
        ticket_price = 0
    else:
        ticket_price = 12
        print("Ticket is $12")

    want_photos = input("Do you want a photo taken? Enter Y/y or N/n: ")
    total_bill = ticket_price
    if want_photos == "Y" or want_photos == "y":
        total_bill = ticket_price + 3
    print(f"The total bill is {total_bill}")

else:
    print("Cannot ride")

'''

grade = int(input("Enter your grade: "))

if grade < 60:
    print("F")

if grade < 70:
    print
    elif grade <= 89 and grade >= 87:
    print("B+")













