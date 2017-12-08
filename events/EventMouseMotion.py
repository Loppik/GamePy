from consts import Consts

class EventMouseMotion:
    @staticmethod
    def identifyAttackSide(xCoordinate, yCoordinate, mousePosition):

        # print("-" + str(Consts.ATTACK_CONTAINER.getElement(0).getElement(1).getElement(0)))
        # print(Consts.ATTACK_CONTAINER.getElement(0).getElement(0).getElement(1))
        # print(str(Consts.ATTACK_CONTAINER.getElement(0).getElement(1).getElement(1)) + "+++")
        #print(str(mousePosition[0]) + " - " + str(mousePosition[1]))
        attackSide = 0
        i = 0
        while(i < 8):
            if mousePosition[0] > Consts.ATTACK_CONTAINER.getElement(i).getElement(0).getElement(0) + xCoordinate and mousePosition[0] < Consts.ATTACK_CONTAINER.getElement(i).getElement(1).getElement(0) + xCoordinate and mousePosition[1] > Consts.ATTACK_CONTAINER.getElement(i).getElement(0).getElement(1) + yCoordinate and mousePosition[1] < Consts.ATTACK_CONTAINER.getElement(i).getElement(1).getElement(1) + yCoordinate:
                attackSide = i + 1
                break
            i += 1
        # i = 1
        # for attackSide in Consts.ATTACK_CONTAINER.getElements():
        #     k = 0
        #     check = False
        #     for side in attackSide.getElements():
        #         # print(side.getElement(0))
        #         # print(side.getElement(1))
        #         if k == 0:
        #             if mousePosition[0] > xCoordinate + side.getElement(0) and mousePosition[0] < xCoordinate + side.getElement(1):
        #                 check = True
        #         elif mousePosition[1] > yCoordinate + side.getElement(0) and mousePosition[1] < yCoordinate + side.getElement(1) and check:
        #             print(i)
        #             break
        #         k += 1
        #     i += 1

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





