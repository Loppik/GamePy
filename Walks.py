from Field import *

arCellsPos = [0, 70, 140, 210, 280, 350, 420, 490, 560, 630, 700, 770, 840]

class Walks:
    mapContainerCellsCoordinates = Field.createCellCoordinates(arCellsPos, 10, 12)


    @staticmethod
    def setCellCreaturesLocationOnIt(cell, creature):
        cell.creature = creature

    @staticmethod
    def identifyCoordinatesByCellNumber(cellNum):
        return Walks.mapContainerCellsCoordinates.getValue(cellNum)


    @staticmethod
    def identifyCellByCoordinates(xCoordinate, yCoordinate, cells):
        check = True
        for cell in cells.getElements():
            if cell.xCoordinate == xCoordinate and cell.yCoordinate == yCoordinate:
                check = False
                break

        if check:
            cell = 0
        return cell


    @staticmethod
    def identifyCellNumber(cell):
        xCoordinat = 0
        yCoordinat = 0
        cellNumber = 0
        print(cell.xCoordinate)
        print(cell.xCoordinate)
        for cellNumber in range(120):
            if arCellsPos[xCoordinat] == cell.xCoordinate and arCellsPos[yCoordinat] == cell.yCoordinate:
                break
            if cellNumber % 12 == 0 and cellNumber != 0:
                xCoordinat = 0
                yCoordinat += 1

            xCoordinat += 1
        return cellNumber

    @staticmethod
    def identifyCellsOnWhichCreatureCanMove(creature, cellsOnField):
        cellsOnWhichCreatureCanMove = Container([])
        for correctionCoef in creature.getCorrectionCoefs():
            xCoordinate, yCoordinate = Walks.identifyCoordinatesByCellNumber(creature.position)
            cell = Walks.identifyCellByCoordinates(xCoordinate + correctionCoef.getElement(0), yCoordinate + correctionCoef.getElement(1), cellsOnField)
            if cell != 0:
                cellsOnWhichCreatureCanMove.addElement(cell)

        return cellsOnWhichCreatureCanMove

