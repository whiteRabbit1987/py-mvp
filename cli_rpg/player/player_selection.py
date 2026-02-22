import random
import sys
from player.player_class import Human, Dwarf, Halfling, Elf

def character_choice():
    character = int(input("Please select a character (select #): "
                          "\n#1 Human"
                          "\n#2 Dwarf"
                          "\n#3 Halfling"
                          "\n#4 Elf"
                          "\n#5 Random Character\n: "))
    if character == 5:
        character = random.randint(1, 4)
    character_map = {1: "Human", 2: "Dwarf", 3: "Halfling", 4: "Elf"}
    return character_map.get(character, None)

def skill_choice():
    skill = int(input("Please select a trait (select #): "
                      "\n#1 Mage"
                      "\n#2 Hunter"
                      "\n#3 Warrior"
                      "\n#4 Druid"
                      "\n#5 Random Skill\n: "))
    if skill == 5:
        skill = random.randint(1, 4)
    skill_map = {1: "Mage", 2: "Hunter", 3: "Warrior", 4: "Druid"}
    return skill_map.get(skill, None)

def create_player(character, skill):
    char_classes = {
        "Human": Human,
        "Dwarf": Dwarf,
        "Halfling": Halfling,
        "Elf": Elf
    }
    player_class = char_classes.get(character)
    if not player_class:
        print("❌ Invalid character selected.")
        sys.exit()
    return player_class(character, skill)

def main():
    character = character_choice()
    if not character:
        print("❌ Invalid character selection.")
        sys.exit()

    skill = skill_choice()
    if not skill:
        print("❌ Invalid skill selection.")

    player = create_player(character, skill)
    return player