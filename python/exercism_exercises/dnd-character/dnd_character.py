import math
import random


class Character:

    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = self.get_max_hit_points()

    def get_max_hit_points(self):
        return 10 + modifier(self.constitution)

    def ability(self):
        rolls = [random.randint(1, 6),
                 random.randint(1, 6),
                 random.randint(1, 6),
                 random.randint(1, 6)]

        rolls.remove(min(rolls))
        return sum(rolls)

def modifier(ability):
    return math.floor((ability - 10)/2)


if __name__ == '__main__':
    message = 'Welcome to the DnD character creator'

    vlad = Character()
    print(vlad.hitpoints)

