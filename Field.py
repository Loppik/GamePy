from logic.MapContainer import *
from logic.Container import *
from Cell import *

class Field:
    def __init__(self, screen, cellImage, activeCellImage):
        self.__screen = screen
        self.__cellImage = cellImage
        self.__activeCellImage = activeCellImage
        self.__cells = Container([])
        self.__creatures = Container([])

    # Methods for self.__cells
    def getCellInCells(self, cellNumber):
        return self.cells.getElement(cellNumber)

    def getCreatureInCell(self, cellNumber):
        return Field.getCellInCells(self, cellNumber).creature

    def setCreatureInCell(self, cell, creature):
        cell.creature = creature

    def getModelInCell(self, cellNumber):
        return Field.getCellInCells(self, cellNumber).model

    # End

    @staticmethod
    def createCellCoordinates(arCellsPos, lineNumber, columnNumber):
        mapContainerCellsCoordinates = MapContainer()
        cellNumber = 0
        for yCoordinate in range(lineNumber):
            for xCoordinate in range(columnNumber):
                mapContainerCellsCoordinates.addItem(cellNumber, [arCellsPos[xCoordinate], arCellsPos[yCoordinate]])
                cellNumber += 1
        return mapContainerCellsCoordinates


    def renderCells(self, mapContainerCellsCoordinates):
        for cellNumber in mapContainerCellsCoordinates.getKeys():
            cell = Cell(self.__cellImage, mapContainerCellsCoordinates.getValue(cellNumber)[0], mapContainerCellsCoordinates.getValue(cellNumber)[1])
            cell.renderCell(self.__screen)
            self.__cells.addElement(cell)

    def renderActiveCells(self, activeCells):
        for cell in activeCells.getElements():
            cell = Cell(self.__activeCellImage, cell.xCoordinate, cell.yCoordinate)
            cell.renderCell(self.__screen)


    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, screen):
        self.__screen = screen

    @property
    def cellImage(self):
        return self.__cellImage

    @cellImage.setter
    def cellImage(self, image):
        self.__cellImage = image

    @property
    def activeCellImage(self):
        return self.__activeCellImage

    activeCellImage.setter
    def activeCellImage(self, image):
        self.__activeCellImage = image

    @property
    def cells(self):
        return self.__cells

    @property
    def creatures(self):
        return self.__creatures




