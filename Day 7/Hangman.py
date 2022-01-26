from random import random
from numpy import choose


import random

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

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
word_list = ['tiger', 'leon', 'gato', 'perro', 'pajaro', 'tiburon', 'ballena', 'delfin', 'lagarto', 'cocodrilo', 'lagartija', 'buitre', 'hormiga', 'araña', 'pollo', 'vaca', 'venado', 'bufeo', 'caballo', 'chancho', 'jirafa', 'elefante', 'lemur', 'mono', 'gorila']
choose_word = random.choice(word_list)
print(f"The answer is {choose_word}")
lives = 6

end_of_game = False

while not end_of_game:
    person = input("Guess a letter: ")

    ans = []
    if person in ans:
        print(f"You've already guessed {person}")

    for i in range(len(choose_word)):
        ans += "_"


    for i in range(len(choose_word)):
        letter = choose_word[i]
        # print(f"Current position: {i}\nCurrent letter: {letter}\nGuessed letter: {person}")
        if person==letter:
            ans[i] = letter
        
    if person not in choose_word:
        print(f"You guessed {person} that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            print("You lose")
            end_of_game = True

    print(f"{' '.join(ans)}")

    if "_" not in ans:
        end_of_game = True
        print("You win")

    print(stages[lives])