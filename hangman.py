#Step 1 
import random
#print welcome message
print("Welcome to word guesser Game")
display = []
print()
word_list = ["aardvark", "baboon", "camel", "ironman", "blackpanther", "spiderman"]

#randomise the word and print the word
random_word = random.choice(word_list)
print(f"random word is {random_word} and has {len(random_word)} characters")
print()
#take input from the player, convert it to lowercase and then split it into
guess = input("Please enter your guess: ").lower()

for i in range(len(random_word)):
  display.insert(0, "_")

print(display)

for position in range(len(random_word)):
  letter = random_word[position]
  if letter == guess:
    display[position] = letter
print(display)
