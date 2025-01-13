from random import randint

# Input the password from the user
user_password = input("Enter your password: ")

# Define the characters that can be used in the password
password_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Validate the user's password
if any(char not in password_characters for char in user_password):
    print("Error: Your password contains unsupported characters. Please try again.")
else:
    # Initialize the guess
    guess = ""

    # Initialize an attempt counter
    attempts = 0

    # Loop until the guessed password matches the user's password
    while guess != user_password:
        guess = ""  # Reset the guess for each attempt
        for _ in range(len(user_password)):
            # Randomly select a character from the password characters
            guess_letter = password_characters[randint(0, len(password_characters) - 1)]
            guess += guess_letter  # Add the character to the guess
        
        # Increment the attempt counter
        attempts += 1

        # Debugging: Print the current guess
        print(f"Attempt {attempts}: {guess}")

        # Break the loop if too many attempts (optional safeguard)
        if attempts > 10**6:  # Stop after 1 million attempts
            print("Too many attempts! Exiting for safety.")
            break

    # Output the result
    if guess == user_password:
        print(f"Your password is: {guess}")
    else:
        print("Failed to guess the password within the attempt limit.")
