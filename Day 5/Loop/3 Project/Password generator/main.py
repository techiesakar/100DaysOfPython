# Python Password Generator

import random
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'y', 'z']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                   'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['~', '`', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '-', '_', '=', '+', '.', ',', '<', '>', ':', ';', '"', '|', '{', '}', '[', ']']

print("Max 5 Characters allowed for each type")
nr_small_letters = int(input("Enter total small letters you want : "))
nr_capital_letters = int(input("Input total capital letters you want : "))
nr_numbers = int(input("Input total numbers you want : "))
nr_symbols = int(input("Input total symbols you want : "))

password_list = []
for char in range(1, nr_small_letters+1):
    password_list.append(random.choice(small_letters))


for char in range(1, nr_capital_letters+1):
    password_list.append(random.choice(capital_letters))

for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is : {password}")
