from creatures.Characteristics import *

class Creature:
    def __init__(self, name, position, health, attack, defense, initiative):
        self.name = name
        self.characterisitcs = Characteristics(health, attack, defense, initiative)
        self.position = position

    @property
    def health(self):
        return self.characterisitcs.health

    @property
    def attack(self):
        return self.characterisitcs.attack

    @property
    def defense(self):
        return self.characterisitcs.defense

    @property
    def initiative(self):
        return self.characterisitcs.initiative

    @initiative.setter
    def initiative(self, initiative):
        self.characterisitcs.initiative = initiative
