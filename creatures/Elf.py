from creatures.Creature import *

class Elf(Creature):
    def __init__(self, name, position, amount, health, attack, defense, initiative, direction, luck):
        Creature.__init__(self, name, position, amount, health, attack, defense, initiative, direction)
        self.__luck = luck

    @property
    def luck(self):
        return self.__luck

    @luck.setter
    def luck(self, luck):
        self.__luck = luck


