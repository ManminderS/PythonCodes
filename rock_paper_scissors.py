# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#1. line to take input from player and display their choice
#2. logic for displaying what computer chose
#3. logic to declare result on the basis of selection between you and computer
#Write your code below this line 👇
import random
selection = input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.: ")
if selection == "0":
    print(rock)
elif selection == "1":
    print(paper)
else:
    print(scissors)

options = [rock, paper, scissors]
computer_chose = random.choice(options)
print("Computer chose:" , computer_chose)

if selection == "0" and computer_chose == scissors:
    print("You win")
elif selection == "1" and computer_chose == rock:
    print("You win")
elif selection == "2" and computer_chose == paper:
    print("You win")
else:
    print("You lose")

