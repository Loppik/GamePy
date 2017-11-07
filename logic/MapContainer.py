class MapContainer:
    def __init__(self):
        self.__ar = {}

    def getKeys(self):
        return self.__ar.keys()

    def getValue(self, key):
        return self.__ar.get(key)

    def getValues(self):
        return self.__ar.values()

    def addItem(self, key, value):
        self.__ar[key] = value
