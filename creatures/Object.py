class Object:
    def __init__(self, position, background):
        self.__position = position
        self.__background = background

    def render(self, screen):
        pass

    def getXcoordinate(self):
        return self.__position.getElement(0)

    def getYcoordinate(self):
        return self.__position.getElement(1)

    def setXcoordinate(self, coordinate):
        return self.__position.setElement(0, coordinate)

    def setYcoordinate(self, coordinate):
        return self.__position.setElement(1, coordinate)

    def getModel(self):
        return self.background.get_rect(topleft=self.position.getElements())

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, background):
        self.__background = background

