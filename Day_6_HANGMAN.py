import random
import os

# Import internal modules
import word_lists
import art

# Constants
WELCOME_MESSAGE = "Welcome to HANGMAN!"
INSTRUCTIONS = (
    "Guess the word by typing one letter at a time.\n"
    "Each incorrect guess reduces your lives. Good luck!\n"
)
LEVELS = ['easy', 'medium', 'hard']
RETRY_PROMPT = "Would you like to play again? (y/n): "
REPEATED_GUESS_MESSAGE = "You already guessed this letter. Try another one."
CORRECT_GUESS_MESSAGE = "Correct guess!"
INCORRECT_GUESS_MESSAGE = "Incorrect guess!"


def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For MacOS and Linux
        os.system('clear')


def set_difficulty(level):
    if level == 'easy':
        return word_lists.easy_words, 8, art.stages
    elif level == 'medium':
        return word_lists.medium_words, 6, art.stages[0:6]
    elif level == 'hard':
        return word_lists.hard_words, 4, art.stages[0:8:2]


def display_hangman_stage(lives_remaining):
    print(art.stages[lives_remaining - 1])


def start_hangman_game():
    clear_screen()
    print(art.banner)
    print(WELCOME_MESSAGE)
    print(INSTRUCTIONS)

    total_score = 0
    restart_game = True

    while restart_game:
        game_lost = False

        for level in LEVELS:
            words, lives, stages = set_difficulty(level)
            print(f"\nStarting {level.upper()} level with {lives} lives.")

            # Play each word in the level
            while words:
                current_word = random.choice(words)
                # Uncomment for debugging: print(f"FOR DEBUG PURPOSE: {current_word}")
                print(f"FOR DEBUG PURPOSE {current_word}")
                words.remove(current_word)
                guessed_letters = set()
                display_word = ["_" for _ in current_word]

                while lives > 0:
                    print(f"\nWord: {' '.join(display_word)}")
                    print(f"Lives remaining: {lives}")
                    display_hangman_stage(lives)

                    player_guess = input("Guess a letter: ").lower()
                    clear_screen()

                    if player_guess in guessed_letters:
                        print(REPEATED_GUESS_MESSAGE)
                        continue

                    guessed_letters.add(player_guess)
                    if player_guess in current_word:
                        # Reveal guessed letters in display_word
                        display_word = [
                            letter if letter == player_guess else display_word[idx]
                            for idx, letter in enumerate(current_word)
                        ]
                        print(CORRECT_GUESS_MESSAGE)

                        if "_" not in display_word:
                            print(f"\nGreat job! You guessed the word: {current_word}")
                            total_score += 10
                            print(f"Current score: {total_score}")  # Show current score
                            break
                    else:
                        lives -= 1
                        print(INCORRECT_GUESS_MESSAGE)

                if lives == 0:
                    print(f"\nOut of lives! The word was: {current_word}")
                    game_lost = True
                    break

            if game_lost:
                print("Game Over!")
                break

            print(f"\nYou've completed {level.upper()} level! Your score: {total_score}")

        print(f"\nYour final score is: {total_score}")
        player_again = input(RETRY_PROMPT).lower()
        restart_game = player_again == 'y'
        if restart_game:
            # Reset total score only when the game restarts
            total_score = 0


start_hangman_game()
