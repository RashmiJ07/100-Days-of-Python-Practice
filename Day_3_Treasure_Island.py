import logo

def play_game():
    """
    Function to play the Treasure Island game.
    """
    print(logo.banner)
    print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

    direction = input("Do you want to go left or right? ").lower()

    if direction == 'right':
        action = input("Do you want to swim or wait? ").lower()
        if action == 'wait':
            door = input("Which door will you choose? (yellow/blue/red) ").lower()
            if door == 'yellow':
                print("Congratulations! You found the treasure. You win!")
            elif door == 'blue':
                print("You were eaten by beasts. Game Over.")
            elif door == 'red':
                print("You were burned by fire. Game Over.")
            else:
                print("Invalid choice. Game Over.")
        else:
            print("You were attacked by a trout. Game Over.")
    elif direction == 'left':
        print("You fell into a hole. Game Over.")
    else:
        print("Invalid direction. Game Over.")

def main():
    """
    Main function to control the game loop.
    """
    keep_playing = True

    while keep_playing:
        play_game()
        replay = input("Do you want to play again? Type 'Y' to continue or 'N' to quit: ").lower()

        if replay != 'y':
            keep_playing = False
            print("Thanks for playing! Have a great day!")

if __name__ == "__main__":
    main()
