import random
rock = '''
      __________
_____(   _______}
           (______)
          (________)
          (_______)
------.___(_____)
'''
paper = '''
      __________
_____(   _______}_____
            __________)
          ______________)
          ___________)
-----._______)
'''

scissors = '''
      __________
_____(   _______}_____
            __________)
          ______________)
          (_______)
-----.___(_____)
'''
game_images = [rock, paper, scissors]
user_choosed = int(input(
    "\nWhat is your choose ? Type '0' for Rock '1' for paper and '2' for scissor  \nType Here ... :"))

if user_choosed >= 3 or user_choosed < 0:
    print("You entered invalid number, you lose !")
else:
    print("You choosed")
    print(game_images[user_choosed])

    computer_choosed = random.randint(0, 2)

    print("Computer choosed")
    print(game_images[computer_choosed])

    if user_choosed == computer_choosed:
        print("Draw")
    elif user_choosed == 0 and computer_choosed == 1:
        print("You lose")
    elif user_choosed == 0 and computer_choosed == 2:
        print("You win")
    elif user_choosed == 1 and computer_choosed == 0:
        print("You win")
    elif user_choosed == 1 and computer_choosed == 2:
        print("You lose")
    elif user_choosed == 2 and computer_choosed == 0:
        print("You lose")
    elif user_choosed == 2 and computer_choosed == 1:
        print("You win")
