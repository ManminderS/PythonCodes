'''
Program to generate the password
'''

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


#Solution 1

random_letters = "".join(random.sample(letters,nr_letters))
random_numbers = "".join(random.sample(numbers,nr_numbers))
random_symbols = "".join(random.sample(symbols,nr_symbols))
password = ''.join(random_letters + random_numbers + random_symbols)
print(f"Your password is {password}")



#Solution 2

password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
print(f"Your password is: {password}")



#Solution 3
password = []
for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))
for char in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))
for char in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))
length = nr_letters + nr_numbers + nr_symbols
password = "".join(random.sample(password, length))
print(f"Your Password is {password}")
