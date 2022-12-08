import random


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

game_img = [rock, paper, scissors]
user = int(input('What do you choose? Rock - 0, Paper - 1, Scissors - 2. '))
if user >= 3 or user < 0:
    print('Invalid number')
else:
    print(game_img[user])

    computer = random.randint(0, 2)
    print('Computer Chose:')
    print(game_img[computer])


    if user == 0 and computer == 2:
    	print('You Win!')
    elif computer == 0 and user == 2:
    	print('You Lose!')
    elif computer > user:
    	print('You Lose!')
    elif computer < user:
    	print('You Win!')
    elif computer == user:
    	print("It`s a draw")
