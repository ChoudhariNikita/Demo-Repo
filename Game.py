import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    # Initialize the number of attempts
    attempts = 0
    
    # Loop until the player guesses the correct number
    while True:
        try:
            # Ask the player to input their guess
            guess = int(input("Enter your guess: "))
            
            # Increment the number of attempts
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} correctly! Hurray :))")
                print(f"It took you {attempts} attempts to guess the number.")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Call the function to start the game
guess_number()
