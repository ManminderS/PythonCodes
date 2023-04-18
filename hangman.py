#Step 1 
import random
#print welcome message
print("Welcome to word guesser Game")
word_list = ["aardvark", "baboon", "camel", "ironman", "blackpanther", "spiderman"]

#randomise the word and print the word
random_word = random.choice(word_list)
print(f"the randomly guessed word is {random_word}")

#take input from the player, convert it to lowercase and then split it into
guess = input("Please enter your guess: ").lower()

for letter in random_word:
  if letter == guess:
    print("Input matches an element of the string.")
  else:
    print("Input does not match any element of the word.")
