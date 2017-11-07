class Cell:
    def __init__(self, cellBackground, xCoordinate, yCoordinate):
        self.__cellBackground = cellBackground
        self.__xCoordinate = xCoordinate
        self.__yCoordinate = yCoordinate
        self.__model = cellBackground.get_rect(topleft=(xCoordinate, yCoordinate))
        self.__creature = 0

    def renderCell(self, screen):
        screen.blit(self.__cellBackground, self.__model)

    @property
    def cellBackground(self):
        return self.__cellBackground

    @cellBackground.setter
    def cellBackground(self, background):
        self.__cellBackground = background

    @property
    def xCoordinate(self):
        return self.__xCoordinate

    @xCoordinate.setter
    def xCoordinate(self, coordinate):
        self.__xCoordinate = coordinate

    @property
    def yCoordinate(self):
        return self.__yCoordinate

    @yCoordinate.setter
    def yCoordinate(self, coordinate):
        self.__yCoordinate = coordinate

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def creature(self):
        return self.__creature

    @creature.setter
    def creature(self, creature):
        self.__creature = creature