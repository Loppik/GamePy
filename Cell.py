from creatures.FieldObject import FieldObject
import pygame

class Cell(FieldObject):
    passiveCell = pygame.image.load("cell2.png")
    activeCell = pygame.image.load("activeCell.jpg")
    moveCell = pygame.image.load("attackCell.jpg")

    def __init__(self, cellBackground, position, status):
        FieldObject.__init__(self, position, cellBackground.get_rect(topleft=position.getElements()))
        self.__cellBackground = cellBackground
        self.__status = status
        self.__creature = None

    def renderCell(self, screen):
        screen.blit(self.__cellBackground, self.model)

    def updateBackground(self):
        if self.status == 1:
            self.cellBackground = Cell.activeCell
        elif self.status == 2:
            self.cellBackground = Cell.passiveCell
        elif self.status == 3:
            self.cellBackground = Cell.moveCell

    @property
    def cellBackground(self):
        return self.__cellBackground

    @cellBackground.setter
    def cellBackground(self, background):
        self.__cellBackground = background

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