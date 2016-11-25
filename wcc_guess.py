# Guess Again v1
# Kelly Faber 11/21

import random
min = 1
max = 100

def get_guess():

    # Get initial guess
    guess = raw_input('Enter your guess: ')

    # Assume it's not valid, until it's proven otherwise
    valid = False

    while valid != True:
        try:
            guess = int(guess)
        except Exception:
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()
        valid = True
    return guess

def compare(numA, numB):
    if numA > numB:
        hilo = 'high'
    if numA < numB:
        hilo = 'low'
    return(hilo)

def play():
    # Pick a secret number
    secret_number = random.randint(min, max)

    print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    # Print message at the start the game
    print("I'm thinking of a number between " + str(min) + " and " + str(max) +"; what do you think it is?")

    for guess_count in range(0,5):
        guess = get_guess()
        if guess_count == 4:
            print("Sorry, you ran out of guesses. The correct answer was " + str(secret_number) + ".")
            break
        elif guess == secret_number:
            print('You got it! The number was ' + str(secret_number))
            break
        else:
            left = 4 - guess_count
            comparison = compare(guess, secret_number)
            print("Too " + comparison + "; you have " + str(left) + " guesses left.")

# Run the game
play()
