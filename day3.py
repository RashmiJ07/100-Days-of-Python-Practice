# Day 4 | Rock, Paper, and Scissors Game

import art
import random

# printing the opening banner
print(art.logo)
game_over = False

while not game_over:
    # taking user input for the game
    user_choice = input("\nWhat do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor or Press X for quitting the game: \n").lower()

    if user_choice != 'x':
        user_choice = int(user_choice)
        if user_choice < 0 or user_choice > 2:
            print("Invalid Input\nPlease provide the input from the given option.")
        else:
            # generating computer's choice
            computers_choice = random.randint(0, 2)

            print(art.RPS_choices[user_choice])
            print(f"Computer chose:\n{art.RPS_choices[computers_choice]}")

            # 👊 ✋ ✌️

            if user_choice == 0:
                if computers_choice == 1:
                    print('You lose')
                elif computers_choice == 2:
                    print('You Win')
                elif computers_choice == 0:
                    print('Tied')
            elif user_choice == 1:
                if computers_choice == 1:
                    print('Tied')
                elif computers_choice == 2:
                    print('You Lose')
                elif computers_choice == 0:
                    print('You win')
            elif user_choice == 2:
                if computers_choice == 1:
                    print('You win')
                elif computers_choice == 2:
                    print('Tied')
                elif computers_choice == 0:
                    print('You Lose')

    else:
        game_over = True
        print("Good bye!\nGame over!!!!")
