from creatures.FieldObject import FieldObject
import pygame

class Cell(FieldObject):
    passiveCell = pygame.image.load("images/passiveCell.png")
    activeCell = pygame.image.load("images/activeCell.png")
    moveCell = pygame.image.load("images/attackCell.png")

    def __init__(self, cellBackground, position, status):
        FieldObject.__init__(self, position, cellBackground)
        self.__status = status
        self.__creature = None

    def renderCell(self, screen):
        screen.blit(self.background, self.position.getElements())

    def updateBackground(self):
        if self.status == 1:
            self.background = Cell.activeCell
        elif self.status == 2:
            self.background = Cell.passiveCell
        elif self.status == 3:
            self.background = Cell.moveCell


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def creature(self):
        return self.__creature

    @creature.setter
    def creature(self, creature):
        self.__creature = creature