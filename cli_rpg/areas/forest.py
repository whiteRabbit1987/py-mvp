import random
from game.battle import battle

forest_monsters = [
    {"name": "Wild Boar", "hp": 30, "damage": 20, "xp": 5, "loot": "Pelt"}, 
    {"name": "Wolf", "hp": 40, "damage": 30, "xp": 15, "loot": "Pelt"},
    {"name": "Huge Spider", "hp": 40, "damage": 30, "xp": 15, "loot": "Pouch"}, 
    {"name": "Goblin", "hp": 75, "damage": 50, "xp": 35, "loot": "Pouch"}, 
    {"name": "Bandit", "hp": 75, "damage": 50, "xp": 35, "loot": "Diamond"},
    {"name": "Warlock", "hp": 100, "damage": 70, "xp": 50, "loot": "Stone of Light"}
]


def forest(player):
    print("\n    🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲")
    print("You enter the forest....danger lurks all around you.")
    print("    🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲\n")
    while True:
        monster = random.choice(forest_monsters).copy()
        print(f"A {monster['name']} appears!")

        if "Demon Staff" in player.items:
            monster['hp'] = monster['hp'] // 2
            monster['damage'] = monster['damage'] // 2

        battle(player, monster, 'forest')

        