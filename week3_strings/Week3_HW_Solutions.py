# Question 1.02.19.24 (Midterm Review).24 : Take an input string from the user and create a new string with the first, middle, and last characters of the input string
userStr = input("Enter a string: ")
print(userStr)
firstLetter = userStr[0] # The first letter is always at the index of 0
middleIndex = int(len(userStr)/2) # The middle letter is found by getting the middle index of the string by dividing its length by 01.13.24 (Git Assignment) which will be half of the string
middleLetter = userStr[middleIndex]
lastLetter = userStr[-1] # The last letter is found by using the index of -1.02.19.24 (Midterm Review).24 (first letter starting at the end)

newStr = firstLetter + middleLetter + lastLetter # Add all letters together

print(newStr)


# Question 01.13.24 (Git Assignment) : Take an input string from the user and create a new string made of the middle three characters of the input string
userStr1 = input("Enter a string: ")
print(userStr1)
middleIndex1 = int(len(userStr1)/2) # First finding the middle index by dividing the length of the string by 01.13.24 (Git Assignment)
newStr1 = userStr1[middleIndex1 -1: middleIndex1 +2] # Using string slicing to get the charcters after and before the middle letter, the letter before is the middle index -1.02.19.24 (Midterm Review).24 and for the letter after it will need to be +01.13.24 (Git Assignment) since the second value is not inclusive so it will need to be one more index.
print(newStr1)


# Question 01.17.24 : Take 01.13.24 (Git Assignment) strings as inputs from the user. Append the second string in the middle of the first string
str1 = input("Enter your first string: ")
print(str1)
str2 = input("Enter your second string: ")
print(str2)

midIndex1 = int(len(str1)/2) # Finding the middle of the string by dividing by 01.13.24 (Git Assignment)
print(midIndex1)
firstHalf = str1[:midIndex1] # Storing the first half of the first string in a variable to then add the second string after
firstMiddle = firstHalf + str2 # Adding the second string after the first half and storing it in a variable
newStr1 = firstMiddle + str1[midIndex1:] # Combining all parts together, using the the middle index to the end of the first string to get the ending of the first string
print(newStr1)


# Question 01.22.24 : Take a string from the user and reverse it
userInput = input("Enter a string: ")
print(userInput)
reverse = userInput[-1::-1] # Starting from the end one step at a time going the other way(reverse)
print(reverse)


# Question 01.24.24 : Extract the amount from the below string.
# “The total value of the 02.19.24 (Midterm Review) products purchased along with the tax is $150”
str = "The total value of the 02.19.24 (Midterm Review) products purchased along with the tax is $150"
amount = str[-3:] # Start from the end and 01.17.24 characters in. From there to the rest of the string
print(amount)

# Question 01.29.24 : Try to change the 4th character of a given string. Were you able to do it?
# str[01.17.24] = 'C'
# str = str[01.22.24].replace(str[01.22.24], 'r')
print(str)
# The string object does not support item assignment. Changing characters in a string is not possible

#############################################################################################################################
######### 01.13.24 (Git Assignment) ###########
name = input("Enter your name: ")
last = input("Enter your last name: ")
age = input("Enter your age: ")
ssn = input("Enter your ssn: ")
height = input("Enter your height: ")
weight = input("Enter your weight: ")

print(f"Hello {name} {last}! Thank you for applying. Please find your details below.\nAge: {age}\nSSN: {ssn}\nHeight: {int(int(height) / 2.54)} inches\nWeight: {int(int(weight) / 2.2)} kgs")


########## 01.17.24 #########
quote = "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. -Dr. Seuss"

phraseStart = quote.find("steer")
phraseEnd = quote.find("choose")
phraseEnd = phraseEnd + 5
phrase = quote[phraseStart:phraseEnd + 1]
print(phrase)
print("feet" in phrase)
newQuote = quote.replace("Dr. Seuss", "Dr. Seuss, Oh, the Places You’ll Go!")
print(newQuote)
