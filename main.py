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

if me == 0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    print("Computer Choice ")
    print(choice[computer_choice])
    if computer_choice == 0:
        print("It's a draw")
    elif computer_choice == 1:
        print("You Lose")
    elif computer_choice == 2:
        print("You Win")
