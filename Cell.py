from creatures.FieldObject import FieldObject

class Cell(FieldObject):
    def __init__(self, cellBackground, position):
        FieldObject.__init__(self, position, cellBackground.get_rect(topleft=position.getElements()))
        self.__cellBackground = cellBackground
        self.__creature = None

    def renderCell(self, screen):
        screen.blit(self.__cellBackground, self.model)

    @property
    def cellBackground(self):
        return self.__cellBackground

    @cellBackground.setter
    def cellBackground(self, background):
        self.__cellBackground = background

    @property
    def creature(self):
        return self.__creature

    @creature.setter
    def creature(self, creature):
        self.__creature = creature