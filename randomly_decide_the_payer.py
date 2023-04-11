import random
peoples_name = input("provide names of all the people separated by commas")
people = peoples_name.split(",")
print(people)

payer = random.choice(people)
print(f"{payer} is going to pay for everyone")
