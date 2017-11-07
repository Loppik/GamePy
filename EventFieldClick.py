from Walks import Walks

class EventFieldClick:

    # Click on cell
    @staticmethod
    def cellOnWhichClick(cells, mousePosition):
        cell = 0
        for cell in cells.getElements():
            if cell.model.collidepoint(mousePosition):
                break

        return cell

    @staticmethod
    def moveCreatureInOtherPos(field, walkNow, cellOnWhichMove):
        print(cellOnWhichMove.yCoordinate)
        field.setCreatureInCell(cellOnWhichMove, walkNow)
        walkNow.position = Walks.identifyCellNumber(cellOnWhichMove)
        print(walkNow.position)
        cellOnWhichMove.creature = walkNow

    # Click on creature
    @staticmethod
    def creatureOnWhichClick(creatures, mousePosition):
        creature = 0
        check = True
        for creature in creatures.getElements():
            if creature.model.collidepoint(mousePosition):
                check = False
                break
        if check:
            creature = 0

        return creature

    @staticmethod
    def checkClickOnCreatureWhichWalksNow(creatureOnWhichClick, walkNow):
        res = False
        if creatureOnWhichClick == walkNow:
            res = True
        return res
