# Python Rock Paper Scissors
import random

def rock_paper_scissors(name):
    print(f"\nWelcome {name} to:\n"
          "******* RPS BATTLE MODE *******"
          "\n**** Rock 🪨 - Paper 📃 - Scissors ✂️ ****")

    guns = ["🪨", "📃", "✂️"]
    is_running = True

    while is_running:
        pc_gun = random.choice(guns)
        user = input("\nPlease enter your choice (r/p/s or q to quit): ").lower()

        if user == 'q':
            print("Thanks for playing!")
            break

        user_gun = '🪨' if user == 'r' else '📃' if user == 'p' else '✂️' if user == 's' else '⁉️'

        if user_gun == '⁉️':
            print("Invalid input! Please enter r, p, or s.")
            continue

        print(f"\nPC: {pc_gun} vs Player: {user_gun}")

        if pc_gun == user_gun:
            print("It's a tie!")
        elif (pc_gun == '🪨' and user_gun == '📃') or \
             (pc_gun == '📃' and user_gun == '✂️') or \
             (pc_gun == '✂️' and user_gun == '🪨'):
            print("You win!")
        else:
            print("You lose!")

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            is_running = False
            print("Thanks for playing!")

# Ask for player name and start the game
user_name = input("Hello, what is your name?\n> ")
rock_paper_scissors(user_name)