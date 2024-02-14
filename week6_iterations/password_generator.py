
'''

Three Lists
Letters → select 4 random
digits → select 5 random
symbols → select ' ' random

'''

import random

letters_u = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letters_l = list("abcdefghijklmnopqrstuvwxyz")
digits = list("0123456789")
symbols = list("!@#$%&*()")

num_letters_u = (int(input("How many letters do you want?: ")))
num_digits_l = (int(input("How many digits do you want?: ")))
num_symbols = (int(input("How many symbols do you want?: ")))


password_chars = []
for letters_u in range(0, num_letters):
    password_chars.append(random.choice(letters_u))

for digit in range(0, num_digits):
    password_chars.append(random.choice(digits))

for symbol in range(0, num_symbols):
    password_chars.append(random.choice(symbols))

print(password_chars)
random.shuffle(password_chars)
print(password_chars)

password = "".join(password_chars)
print(password)

