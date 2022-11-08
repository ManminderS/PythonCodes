'''
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.
'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_1 = name1.lower()
name_2 = name2.lower()
t = name_1.count("t")
t2 = name_2.count("t")
r = name_1.count("r")
r2 = name_2.count("r")
u = name_1.count("u")
u2 = name_2.count("u")
e = name_1.count("e")
e2 = name_2.count("e")
true = t + t2 + r + r2 + u + u2 + e + e2
l = name_1.count("l")
l2 = name_2.count("l")
o = name_1.count("o")
o2 = name_2.count("o")
v = name_1.count("v")
v2 = name_2.count("v")
e = name_1.count("e")
e2 = name_2.count("e")
love = l + l2 + o + o2 + v + v2 + e +e2
value = (str(true) + str(love))
score = int(value)


if score > 90 or score < 10:
    print(f"your score is {score}, you go like coke and mentos")
elif score >= 40 or score <= 50:
    print("your score is {score}, you are alright together")
else:
    print("your score is", score)





