class Container:
    def __init__(self, ar):
        self.__array = ar

    def getWithoutRelations(self):
        return self.__array[:]

    def getElement(self, index):
        return self.__array[index]

    def getElements(self):
        return self.__array

    def setElement(self, index, element):
        self.__array[index] = element

    def addElement(self, element):
        self.__array.append(element)

    def addElements(self, container):
        for element in container:
            self.addElement(element)

    def insertElement(self, index, element):
        self.__array.insert(index, element)

    def setElement(self, index, element):
        self.__array[index] = element

    def removeElement(self, index):
        self.__array.pop(index)

    def remove(self, element):
        self.__array.remove(element)

    def getSize(self):
        return len(self.__array)

