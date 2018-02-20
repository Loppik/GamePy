from creatures.Object import Object

class FieldObject(Object):
    def __init__(self, position, background):
        Object.__init__(self, position, background)
        self.__cellNumber = None

    @property
    def cellNumber(self):
        return self.__cellNumber

    @cellNumber.setter
    def cellNumber(self, number):
        self.__cellNumber = number
