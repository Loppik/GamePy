from Consts import Consts

class EventMouseMotion:
    @staticmethod
    def identifyAttackSide(xCoordinate, yCoordinate, mousePosition):
        attackSide = 0
        i = 0
        while(i < 8):
            if mousePosition[0] > Consts.ATTACK_CONTAINER.getElement(i).getElement(0).getElement(0) + xCoordinate and mousePosition[0] < Consts.ATTACK_CONTAINER.getElement(i).getElement(1).getElement(0) + xCoordinate and mousePosition[1] > Consts.ATTACK_CONTAINER.getElement(i).getElement(0).getElement(1) + yCoordinate and mousePosition[1] < Consts.ATTACK_CONTAINER.getElement(i).getElement(1).getElement(1) + yCoordinate:
                attackSide = i + 1
                break
            i += 1

        return attackSide

    @staticmethod
    def identifyShiftToNewCell(attackSide):
        result = 0
        if attackSide == 1:
            result = -12
        elif attackSide == 2:
            result = -11
        elif attackSide == 3:
            result = 1
        elif attackSide == 4:
            result = 13
        elif attackSide == 5:
            result = 12
        elif attackSide == 6:
            result = 11
        elif attackSide == 7:
            result = -1
        elif attackSide == 8:
            result = -13
        return result





