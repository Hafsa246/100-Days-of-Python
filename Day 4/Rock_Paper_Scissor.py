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
game_images= [rock, paper, scissors]

person = int(input("What do you choose? Select 0 for Rock, 1 for Paper or 2 for Scissors: "))
print("You chose\n" + game_images[person])

computer = random.randint(0,2)
print("Computer chose\n" + game_images[computer])

if person == computer:
    print("It's a Draw!")
elif(person == 0 and computer == 1):
    print("Computer wins!")
elif(person == 0 and computer == 2):
    print("You win!")
elif(person == 1 and computer == 0):
    print("You win!")
elif(person == 1 and computer == 2):
    print("Computer wins!")
elif(person == 2 and computer == 1):
    print("You win!")
elif(person == 2 and computer == 0):
    print("Computer wins!")
else:
    print("InValid input")