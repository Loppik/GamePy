from math import ceil

from Field import *

arCellsPos = [0, 70, 140, 210, 280, 350, 420, 490, 560, 630, 700, 770, 840]

class Walks:
    mapContainerCellsCoordinates = Field.createCellCoordinates(arCellsPos, 8, 12)

    @staticmethod
    def checkCellOnExistenceInContainer(cell, cellsCon):
        res = False
        for c in cellsCon.getElements():
            if c == cell:
                res = True
                break
        return res

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
            #print(str(cell.getXcoordinate()) + '-' + str(cell.getYcoordinate()))
            if cell.getXcoordinate() == xCoordinate and cell.getYcoordinate() == yCoordinate:
                check = False
                break

        if check:
            cell = 0
        return cell



    @staticmethod
    def identifyCellsOnWhichCreatureCanMove(creature, coefs, cellsOnField):
        cellsOnWhichCreatureCanMove = Container([])
        for correctionCoef in coefs:
            cell = Walks.identifyCellByCoordinates(creature.getXcoordinate() + correctionCoef.getElement(0), creature.getYcoordinate() + correctionCoef.getElement(1), cellsOnField)
            if cell != 0:
                cellsOnWhichCreatureCanMove.addElement(cell)

        return cellsOnWhichCreatureCanMove

    @staticmethod
    def checkOnOpportunityToMove(attaker, prey, shiftCellNumber):
        for cell in attaker.cellsOnWhichCanMove.getElements():
            if shiftCellNumber + prey.cellNumber == cell.cellNumber and not Walks.endLine(prey, shiftCellNumber):
                return True
        return False

    @staticmethod
    def endLine(prey, shift):
        if prey.cellNumber % 11 == 0 and (shift == 1 or shift == 13):
            return True
        return False


