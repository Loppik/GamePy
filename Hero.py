from logic.Container import *

class Hero:
    def __init__(self, name, creatures):
        self.__creatures = Container(creatures)

    def getAllCreatures(self):
        return self.__creatures.getElements()

    def addCreature(self, creature):
        self.__creatures.addElement(creature)

    @property
    def creatures(self):
        return self.__creatures
