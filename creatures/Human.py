from creatures.Creature import *

class Human(Creature):
    def __init__(self, name, position, health, attack, defense, initiative, belief):
        Creature.__init__(self, name, position, health, attack, defense, initiative)
        self.__belief = belief

    @property
    def belief(self):
        return self.__belief

    @belief.setter
    def belief(self, belief):
        self.__belief = belief