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

# Write your code below this line 👇

import random

games_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ? "))
computer_choice = random.randint(0, 2)

if user_choice < 0 or user_choice >= 3:
    print("you type an invalid number, you lose!")
    exit()

print(games_images[user_choice])
print("\nComputer choice:")

print(games_images[computer_choice])

if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_choice == 2:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif user_choice < computer_choice:
    print("you lose!")
