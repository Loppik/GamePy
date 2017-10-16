from logic.Container import *
class SequanceOfMoves:
    @staticmethod
    def sortForInitiative(containerOfCreaturesPlayer1, containerOfCreaturesPlayer2):
        containerOfCreaturesBothPlayers = Container(containerOfCreaturesPlayer1)
        containerOfCreaturesBothPlayers.addElements(containerOfCreaturesPlayer2)

        SequanceOfMoves.sortContainerForValue(containerOfCreaturesBothPlayers)
        return containerOfCreaturesBothPlayers

    @staticmethod
    def sortContainerForValue(container):
        i, j = 0, 0
        while i < len(container.getElements()):
            j = i
            while j < len(container.getElements()):
                if container.getElement(j).initiative > container.getElement(i).initiative:
                    term = container.getElement(j)
                    container.setElement(j, container.getElement(i))
                    container.setElement(i, term)
                j += 1
            i += 1

    @staticmethod
    def findFirstRemaindersForAllCreatures(creatures):
        remainders = []
        index = 0
        while index < len(creatures.getElements()):
            remainders.append(SequanceOfMoves.findRemainderInitiativeElem(creatures.getElement(index)))
            index += 1

        return remainders

    @staticmethod
    def initiativePlusFirstRemainders(creatures, remainders):
        i = 0
        for creature in creatures.getElements():
            SequanceOfMoves.initiativePlusRemainder(creature, remainders[i])
            i += 1

    @staticmethod
    def initiativePlusRemainder(creature, remainder):
        creature.initiative = creature.initiative/10 + remainder

    @staticmethod
    def createStartMoveLine(creatures):
        remainders = SequanceOfMoves.findFirstRemaindersForAllCreatures(creatures)
        SequanceOfMoves.initiativePlusFirstRemainders(creatures, remainders)

    @staticmethod
    def determinateMove(containerCreaturesInMoveLine):
        moveCreature = containerCreaturesInMoveLine.getElement(0)
        remainder = moveCreature.initiative - 1
        #print(remainder)
        if remainder > 1:
            moveCreature.initiative = remainder
            SequanceOfMoves.insertValueForWane(containerCreaturesInMoveLine, moveCreature)
            #print("+ " + containerCreaturesInMoveLine.getElement(0).name)
        else:
            containerCreaturesInMoveLine.getElement(0).initiative = remainder
            SequanceOfMoves.insertValueForWane(containerCreaturesInMoveLine, moveCreature)

        #print(containerCreaturesInMoveLine.getElement(0).initiative)
        containerCreaturesInMoveLine.removeElement(0)
        return moveCreature

    @staticmethod
    def findRemainderInitiativeElem(creature):
        return creature.initiative/10 - 1


    @staticmethod
    def insertValueForWane(container, element):
        index = 0
        check = True
        while index < len(container.getElements()):
            elementIndex = container.getElement(index)
            if element.initiative > elementIndex.initiative:
                container.insertElement(index, element)
                check = False
                break
            index += 1

        if check:
            container.addElement(element)
