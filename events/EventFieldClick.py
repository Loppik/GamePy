from Walks import Walks

class EventFieldClick:

    # Click on cell
    @staticmethod
    def cellOnWhichClick(cells, mousePosition):
        check = True
        for cell in cells.getElements():
            if cell.getModel().collidepoint(mousePosition):
                check = False
                break

        if check:
            cell = 0

        return cell

    @staticmethod
    def moveCreatureInOtherPos(field, walkNow, cellOnWhichMove):
        field.setCreatureInCell(cellOnWhichMove, walkNow)
        walkNow.position = cellOnWhichMove.position
        walkNow.cellNumber = cellOnWhichMove.cellNumber
        cellOnWhichMove.creature = walkNow

    # Click on creature
    @staticmethod
    def creatureOnWhichMouseCursor(creatures, mousePosition):
        creature = 0
        check = True
        for creature in creatures.getElements():
            if creature.getModel().collidepoint(mousePosition):
                check = False
                break
        if check:
            creature = 0

        return creature



    @staticmethod
    def objectInDownMenuWhichClick(objects, mousePosition):
        check = True
        for object in objects.getElements():
            if object.getModel().collidepoint(mousePosition):
                check = False
                break
        if check:
            object = 0
        return object

