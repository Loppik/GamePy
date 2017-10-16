from creatures.Creature import *

class Elf(Creature):
    def __init__(self, name, position, health, attack, defense, initiative, luck):
        Creature.__init__(self, name, position, health, attack, defense, initiative)
        self.luck = luck


