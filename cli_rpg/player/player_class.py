from items.items import weapons, armour

class Player:
    def __init__(self, character, skill):
        self.character = character
        self.skill = skill
        self.emoji = ''
        self.hp = 0
        self.damage = 0
        self.xp = 0
        self.gold = 0
        self.weapons = []
        self.armour = ""
        self.loot = []
        self.items = []
        self.is_king = False
        self.set_character()
        self.set_skill()

    def set_character(self):
        pass  # Implemented in subclass

    def set_skill(self):
        if self.skill == "Mage":
            self.emoji = "🧙‍♂️"
            self.hp += 10
            self.armour = "Magic Robes"
            self.weapons.append("Magic Staff")
        elif self.skill == "Hunter":
            self.emoji = "🏹"
            self.hp += 5
            self.armour = "Leather Armour"
            self.weapons.append("Bow")
        elif self.skill == "Warrior":
            self.emoji = "🤺"
            self.hp += 15
            self.damage += 5
            self.armour = "Chain Mail"
            self.weapons.append("Warhammer")
        elif self.skill == "Druid":
            self.emoji = "🧌"
            self.hp += 10
            self.armour = "Dark Robes"
            self.weapons.append("Wooden Stick")

        # Apply weapon bonus
        if self.weapons:
            weapon_damage = max([weapons.get(w, 0) for w in self.weapons])
            self.damage += weapon_damage

        # Apply armor bonus
        if self.armour in armour:
            self.hp += armour[self.armour]


# Subclasses
class Human(Player):
    def set_character(self):
        self.hp = 40
        self.damage = 25
        


class Dwarf(Player):
    def set_character(self):
        self.hp = 45
        self.damage = 30


class Halfling(Player):
    def set_character(self):
        self.hp = 30
        self.damage = 20


class Elf(Player):
    def set_character(self):
        self.hp = 35
        self.damage = 30
