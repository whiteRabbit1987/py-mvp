# Python Slot Machine
import sys
from slot_pgk.slot_mods import *
    
def main():
    print(f"*********SLOT MANIA*********"
        f"\n3*🐟 = $10"
        f"\n3*🍌 | 🍒 | 🍊 = $100"
        f"\n3*🪙 = $1000"
        f"\n3*🌟 = $10,000")
    total = int(input("Deposit to play: "))
    first_spin = True
    on_house = 0
    while True:
        choice = start_game()
        if choice == '1':
            if first_spin:
                    for x in range(3):
                        print('🍒', end=' ')
                    first_spin = False
                    total += 10
                    print()
                    continue
            else:
                if total <= 4:
                    print("No more spins")
                    sys.exit()
                else:
                    total += spin()
                    total -= 5
                    if total <= 5:
                        if on_house < 1:
                            on_house += 1
                            pitty = 0
                            pitty += random.randint(1, 50)
                            total += pitty
                            print(f"You get ${pitty} on the house!")
                    print(f"Total: ${total}")

        elif choice == '2':
            print(f"Congratulations, you won ${total}" if total else "No wins today..")
            sys.exit()
        elif choice == '3':
            sys.exit()
        else:
            print("Invalild")
            continue


if __name__ == '__main__':
     main()