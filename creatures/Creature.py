import pygame

from creatures.Characteristics import *
from logic.Container import Container
from Walks import Walks
from creatures.FieldObject import FieldObject

class Creature(FieldObject):
    def __init__(self, name, position, amount, fullHealth, attack, defense, initiative):
        FieldObject.__init__(self, position, None)
        self.__name = name
        self.__characterisitcs = Characteristics(amount, fullHealth, attack, defense, initiative)
        self.__hero = None
        self.__walkArea = Container([])
        self.__cellsOnWhichCanMove = None

    def getCorrectionCoefs(self):
        return self.__walkArea.getElements()


    def renderAmountCreatures(creature, screen):
        font = pygame.font.Font(None, 30)
        scoretext = font.render(str(creature.amount), 1, (255, 0, 0))
        screen.blit(scoretext, (creature.getXcoordinate()+50, creature.getYcoordinate()+50))

    @property
    def name(self):
        return self.__name

    @property
    def amount(self):
        return self.__characterisitcs.amount

    @amount.setter
    def amount(self, amount):
        self.__characterisitcs.amount = amount

    @property
    def health(self):
        return self.__characterisitcs.health

    @health.setter
    def health(self, health):
        self.__characterisitcs.health = health

    @property
    def fullHealth(self):
        return self.__characterisitcs.fullHealth

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

    @property
    def cellsOnWhichCanMove(self):
        return self.__cellsOnWhichCanMove

    @cellsOnWhichCanMove.setter
    def cellsOnWhichCanMove(self, cells):
        self.__cellsOnWhichCanMove = cells
