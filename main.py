me = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

choice = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''' , '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
import random
computer_choice = random.randint(0, 2)