from creatures.Creature import *

class Elf(Creature):
    def __init__(self, name, position, health, attack, defense, initiative, luck):
        Creature.__init__(self, name, position, health, attack, defense, initiative)
        self.__luck = luck

    @property
    def luck(self):
        return self.__luck

    @luck.setter
    def luck(self, luck):
        self.__luck = luck


