import random
from slot_pgk.spin_list import *

def spin():
    # spin
    winnings = 0
    spin_result = []
    for _ in range(3):
        char = random.choice(standart)
        if char == 'special':
            char = random.choice(special)
            if char == 'grant':
                char = grant[0]
        spin_result.append(char)

    print("\n******************")
    print("   | ".join(spin_result))
    print("******************\n")

    # Check for match
    if spin_result.count(spin_result[0]) == 3:
        symbol = spin_result[0]
        winnings += prices.get(symbol, 0)
        print(f"🏆 You won ${winnings}")
    else:
        print("No win this time.")

    return winnings

def start_game():
    choice = (input(f"\nSpin to win!"
                       f"\n1) Spin ($5)"
                       f"\n2) Cash out"
                       f"\n3) Exit"
                       f"\nChoose (1|2|3)> "))
    return choice

