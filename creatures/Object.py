class Object:
    def __init__(self, position, model):
        self.__position = position
        self.__model = model



    def getXcoordinate(self):
        return self.__position.getElement(0)

    def getYcoordinate(self):
        return self.__position.getElement(1)

    def setXcoordinate(self, coordinate):
        return self.__position.setElement(0, coordinate)

    def setYcoordinate(self, coordinate):
        return self.__position.setElement(1, coordinate)

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
