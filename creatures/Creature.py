from creatures.Characteristics import *

class Creature:
    def __init__(self, name, health, attack, defense, initiative):
        self.name = name
        self.characterisitcs = Characteristics(health, attack, defense, initiative)

