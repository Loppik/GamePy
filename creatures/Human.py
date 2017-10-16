from creatures.Creature import *

class Human(Creature):
    def __init__(self, name, position, health, attack, defense, initiative, belief):
        Creature.__init__(self, name, position, health, attack, defense, initiative)
        self.belief = belief