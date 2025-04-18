# Battle Game

def play_game():
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    dwarf = "Dwarf"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    dwarf_hp = 250

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    dwarf_damage = 75

    dragon_hp = 300
    dragon_damage = 50

    # Chosing your character
    while True:

        print("****************Kill the Dragon****************")
        print("\n1) Wizard\n2) Elf\n3) Human\n4) Dwarf\n5) q to quit")
        character = input("Choose your character: ")

        if character.lower() == 'wizard' or character == '1':
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character.lower() == 'elf' or character == '2':
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character.lower() == 'human' or character == '3':
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif character.lower() == 'dwarf' or character == '4':
            character = dwarf
            my_hp = dwarf_hp
            my_damage = dwarf_damage
            break
        elif character.lower() == 'q' or character == '5':
            print("Exiting the game")
            exit()
        else:
            print(f"{character} is unknown.")


    print(f"\nYou have chosen the character: {character}")
    print(f"Health: {my_hp}")
    print(f"Damage: {my_damage}")
    print("**************** Fight! ****************")

    # Fighting the Dragon
    while True:
        
        dragon_hp -= my_damage
        print(f"\nThe {character} damaged the Dragon!")
        print(f"The Dragon's hitpoints are now: {dragon_hp}")
        
        my_hp -= dragon_damage
        print(f"\nThe Dragon strikes back at {character}")
        print(f"The {character}'s hitpoints are now: {my_hp}")

        if dragon_hp <= 0:
            print(f"The Dragon lost the battle.")
            break

        if my_hp <= 0:
            print(f"The {character} has lost the battle")
            break

play_game()

while True:
    replay = input("Would you like to play again? (Y/N): ")

    if replay.lower() == 'y':
        play_game()
    else:
        exit()

