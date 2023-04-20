import random

#Declare Variables
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
game = ["johnwick", "gta5", "witcher", "fifa23"]
random_game = random.choice(game)
word_length = len(random_game)
lives = 6



print(f"The solution is {random_game}.")
print()


#create a list "display" and add _ for every word selected randomly
display = []
for i in range(word_length):
  display += "_"
print(display)


#Ask Player to Guess and enter the correct guessed alphabet to exact position as in the word
while not end_of_game:
  guess = input("Guess the alphabet: ").lower()
  for position in range(word_length):
    letter = random_game[position]
    if guess == letter:
      display[position] = guess

  if guess not in random_game:
    lives -= 1
    if lives == 0:
      print("You Lose")
    
  print(f"{''.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You Win")
  print(stages[lives])
  print(f"you have {lives} lives left")
