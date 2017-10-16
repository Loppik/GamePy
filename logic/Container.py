class Container:
    def __init__(self, ar):
        self.array = ar

    def getElement(self, index):
        return self.array[index]

    def getElements(self):
        return self.array

    def addElement(self, element):
        self.array.append(element)

    def addElements(self, container):
        for element in container:
            self.addElement(element)

    def insertElement(self, index, element):
        self.array.insert(index, element)

    def setElement(self, index, element):
        self.array[index] = element

    def removeElement(self, index):
        self.array.pop(index)

