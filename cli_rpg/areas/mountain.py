import random
from game.battle import battle

mountain_pass_monsters = [
    {"name": "Ancient Stone Golem", "hp": 300, "damage": 75, "xp": 250, "loot": "Diamond"},
    {"name": "Frost Wyrm", "hp": 260, "damage": 90, "xp": 300, "loot": "Diamond"},
    {"name": "Cursed Warlock", "hp": 220, "damage": 100, "xp": 350, "loot": "Grimoire"}
]

def mountain_pass(player):
    if player.xp < 2000:
        print("\nYou can't climb the mountain yet!\n")
        from areas.town import town_square as town
        town(player)
    elif 'Grimoire' in player.items:
        from game.dragon import dragon
        dragon(player)

    print("\n🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨")
    print("You climb the mountian....you see a shadow up above")
    print("🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨\n")
        

    climb_mountain = True
    while climb_mountain:
        monster = random.choice(mountain_pass_monsters).copy()
        print(f"A {monster['name']} appears!")

        if "Demon Staff" in player.items:
            monster.hp = monster.hp // 2
            monster.damage = monster.damage // 2

        battle(player, monster, 'mountain')