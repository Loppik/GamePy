from creatures.Creature import *

class Human(Creature):
    def __init__(self, name, position, amount, health, attack, defense, initiative, direction, belief):
        Creature.__init__(self, name, position, amount, health, attack, defense, initiative, direction)
        self.__belief = belief

    @property
    def belief(self):
        return self.__belief

    @belief.setter
    def belief(self, belief):
        self.__belief = belief