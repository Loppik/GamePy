from creatures.Characteristics import *
from logic.Container import Container

class Creature:
    def __init__(self, name, position, health, attack, defense, initiative):
        self.__name = name
        self.__characterisitcs = Characteristics(health, attack, defense, initiative)
        self.__position = position
        self.__model = 0
        self.__hero = 0
        self.__walkArea = Container([])

    def getCorrectionCoefs(self):
        return self.__walkArea.getElements()

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__characterisitcs.health

    @property
    def attack(self):
        return self.__characterisitcs.attack

    @property
    def defense(self):
        return self.__characterisitcs.defense

    @property
    def initiative(self):
        return self.__characterisitcs.initiative

    @initiative.setter
    def initiative(self, initiative):
        self.__characterisitcs.initiative = initiative

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def hero(self):
        return self.__hero

    @hero.setter
    def hero(self, hero):
        self.__hero = hero

    @property
    def walkArea(self):
        return self.__walkArea

    @walkArea.setter
    def walkArea(self, walkArea):
        self.__walkArea = walkArea
