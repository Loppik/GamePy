from logic.Container import *

class Hero:
    def __init__(self, name, creatures):
        self.creatures = Container(creatures)

    def getAllCreatures(self):
        return self.creatures.getElements()