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
length_of_randomword = len(random_word)

for i in range(length_of_randomword):
  display.insert(0, "_")

game_end = False

while not game_end:
  guess = input("Please enter your guess: ").lower()
  for position in range(length_of_randomword): #this starts the loop, word length times
    letter = random_word[position] #this 
    if guess == letter:
      display[position] = letter
      
  print(display)
  
  if "_" not in display:
    game_end = True
    print("You Win")
