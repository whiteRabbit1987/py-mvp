import random
from game.battle import battle

cave_monsters = [
    {"name": "Goblin", "hp": 30, "damage": 5, "xp": 20, "loot": "Pouch"},
    {"name": "Skeleton", "hp": 40, "damage": 10, "xp": 30, "loot": "Sword"},
    {"name": "Orc", "hp": 60, "damage": 15, "xp": 50, "loot": "Pouch"},
    {"name": "Troll", "hp": 80, "damage": 20, "xp": 70, "loot": "Chest"},
    {"name": "Mimic", "hp": 50, "damage": 12, "xp": 40, "loot": "Treasure"},
    {"name": "Demon", "hp": 100, "damage": 75, "xp": 100, "loot": "Demon Staff"}
]


def cave(player):
    print("\n🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻")
    print("You enter a dark mountain cave...you can't hear or see anything!")
    print("🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻🗻\n")
    if "Stone of Light" in player.items:
        print("You notice a bright light from you backpack and take out the stone of light.")
    else:
        from areas.town import town_square as town
        print("***************************************")
        print("\tYou decide to return to town.")
        print("***************************************\n")
        town(player)

    in_cave = True
    while in_cave:
        monster = random.choice(cave_monsters).copy()
        print(f"A {monster['name']} appears!")

        if "Demon Staff" in player.items:
            monster['hp'] = monster['hp'] // 2
            monster['damage'] = monster['damage'] // 2

        battle(player, monster, "cave")
