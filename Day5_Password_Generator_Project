import random


def main():
    print("Welcome to the pyPassword Generator!")

    # Get user input for password characteristics
    password_length = int(input("How many letters would you like in your password? "))
    nr_symbols = int(input("How many symbols would you like? "))
    nr_numbers = int(input("How many numbers would you like? "))

    # Calculate the number of letters based on total length
    nr_letters = password_length - (nr_symbols + nr_numbers)

    # Define possible characters
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    symbols = [
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
        '-', '_', '=', '+', '{', '}', '[', ']', '|',
        ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'
    ]

    # Create final password list
    finalPassword = []

    # Add random letters
    for _ in range(nr_letters):
        finalPassword.append(random.choice(letters))

    # Add random numbers
    for _ in range(nr_numbers):
        finalPassword.append(random.choice(numbers))

    # Add random symbols
    for _ in range(nr_symbols):
        finalPassword.append(random.choice(symbols))

    # Shuffle the final password
    random.shuffle(finalPassword)

    # Display the generated password
    print(f"Your password is: {''.join(finalPassword)}")


if __name__ == "__main__":
    main()
