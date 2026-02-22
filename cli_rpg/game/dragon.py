import random
from game.battle import battle

dragons = [
    {"name": "Vorthakar the Ashen Maw", "hp": 5320, "damage": 1095, "xp": 300, "loot": "Dragon Heart"},
    {"name": "Zeranyx the Frostbrand", "hp": 5360, "damage": 1090, "xp": 280, "loot": "Dragon Heart"},
    {"name": "Kael’Drath the Dreadfire", "hp": 5340, "damage": 10100, "xp": 320, "loot": "Dragon Heart"},
]


def dragon(player):
    print("\n🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🐉🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    print("The trees bend under a searing wind, ash and embers swirling in the air.")
    print("The sky darkens as smoke rolls down the mountainside like a living thing.")
    print("A massive shadow unfurls its wings — the DRAGON has arrived.")
    print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🐉🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥\n")

    while True:
        monster = random.choice(dragons).copy()
        print("Then, with a voice like an earthquake, the dragon speaks")
        print(f"I am {monster['name']}!")
        print(f"Who dares to steal the book of old!")

        battle(player, monster, 'mountain')
    