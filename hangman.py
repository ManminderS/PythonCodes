#Step 1 
import random
import string
print("Welcome to word guesser Game")
word_list = ["aardvark", "baboon", "camel", "ironman", "blackpanther", "spiderman"]
random_word = random.choice(word_list)
print(f"the randomly guessed word is {random_word}")
user_input = input("Please enter your guess: ")
print(user_input)
