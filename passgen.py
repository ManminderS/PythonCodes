import random
import string
letters = string.ascii_letters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("...Welcome to password generator...")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

random_letters = "".join(random.sample(letters,nr_letters))
random_numbers = "".join(random.sample(numbers,nr_numbers))
random_symbols = "".join(random.sample(symbols,nr_symbols))
password = "".join(random_letters + random_numbers + random_symbols)
print(password)
