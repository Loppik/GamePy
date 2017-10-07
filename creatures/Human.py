from Creature import *

class Human(Creature):
    def __init__(self, name, health, attack, defense, initiative, belief):
        Creature.__init__(self, name, health, attack, defense, initiative)
        self.belief = belief