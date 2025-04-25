# Python number guessing game
import random

def guess_game(name):
    lowest = 1
    highest = 100
    num = random.randint(lowest, highest)  # Random number between 1 and 100
    attempts = 0
    is_running = True

    print(f"\nWelcome {name} to:\n"
           "********INTEGER MANIA********"
           "\n****Guess a random number****")

    while is_running:
        guess = input(f"\nGuess a number between {lowest} and {highest}"
                       "\nEnter your guess (q to quit): ")

        if guess.lower() == 'q':
            break
            
        if guess.isdigit():
            guess = int(guess)
            attempts += 1

            if guess < lowest or guess > highest:
                print("\n**********************")
                print("Your guess is out of range!")
                print("**********************\n")
                continue
            elif guess > num:
                print("\n**********************")
                print("Your guess is to high!")
                print("**********************\n")
            elif guess < num:
                print("\n**********************")
                print("Your guess is to low!")
                print("**********************\n")
            else:
                print("\n**********************")
                print(f"Correct guess! Your guess: {guess} = Random number: {num}"
                    f"\n It took you {attempts} tries.")
                print("**********************\n")
                choose = input("Do you want to play again? (Y/N) ")
                if choose.lower() == 'y':
                    guess_game(user_name)
                else:
                    is_running = False
        else:
            print("\n**********************")
            print("Invalid guess. You must enter a number.")
            print("**********************\n")
            continue
    
    
user_name = input("Hello, what is your name?"
                  "\n>")
guess_game(user_name)
