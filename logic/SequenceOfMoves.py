from logic.Container import *
from creatures.Object import Object
import pygame

class SequenceOfMoves(Object):
    def __init__(self, position):
        Object.__init__(self, position, pygame.image.load("images/waitButton.png"))
        self.sequence = None
        self.__lastCreature = None

    def render(self, screen, walkNow):
        font = pygame.font.Font(None, 30)
        coef = 0
        self.sequence.insertElement(0, walkNow)
        for creature in self.sequence.getElements():
            scoretext = font.render(creature.name, 1, (0, 0, 0))
            screen.blit(scoretext, (self.position.getElement(0) + coef, self.position.getElement(1)))
            coef += 120
        self.sequence.removeElement(0)

    @staticmethod
    def sortForInitiative(containerOfCreaturesPlayer1, containerOfCreaturesPlayer2):
        containerOfCreaturesBothPlayers = Container(containerOfCreaturesPlayer1)
        containerOfCreaturesBothPlayers.addElements(containerOfCreaturesPlayer2)

        SequenceOfMoves.sortContainerForValue(containerOfCreaturesBothPlayers)
        return containerOfCreaturesBothPlayers

    @staticmethod
    def sortContainerForValue(container):
        i, j = 0, 0
        while i < len(container.getElements()):
            j = i
            while j < len(container.getElements()):
                if container.getElement(j).chanInitiat > container.getElement(i).chanInitiat:
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
            remainders.append(SequenceOfMoves.findRemainderInitiativeElem(creatures.getElement(index)))
            index += 1

        return remainders

    @staticmethod
    def initiativePlusFirstRemainders(creatures, remainders):
        i = 0
        for creature in creatures.getElements():
            SequenceOfMoves.initiativePlusRemainder(creature, remainders[i])
            i += 1

    @staticmethod
    def initiativePlusRemainder(creature, remainder):
        creature.chanInitiat = creature.chanInitiat/10 + remainder

    @staticmethod
    def createStartMoveLine(creatures):
        remainders = SequenceOfMoves.findFirstRemaindersForAllCreatures(creatures)
        SequenceOfMoves.initiativePlusFirstRemainders(creatures, remainders)


    def determinateMove(self):
        moveCreature = self.sequence.getElement(0)
        remainder = moveCreature.chanInitiat - 1
        if remainder > 1:
            moveCreature.chanInitiat = remainder
            SequenceOfMoves.insertValueForWane(self.sequence, moveCreature)
        else:
            self.sequence.getElement(0).chanInitiat = remainder
            SequenceOfMoves.insertValueForWane(self.sequence, moveCreature)

        self.sequence.removeElement(0)
        return moveCreature

    @staticmethod
    def findRemainderInitiativeElem(creature):
        return creature.chanInitiat/10 - 1


    @staticmethod
    def insertValueForWane(container, element):
        index = 0
        check = True
        while index < len(container.getElements()):
            elementIndex = container.getElement(index)
            if element.chanInitiat > elementIndex.chanInitiat:
                container.insertElement(index, element)
                check = False
                break
            index += 1

        if check:
            container.addElement(element)

    def firstSequence(self, player1, player2):
        self.sequence = SequenceOfMoves.sortForInitiative(player1.creatures.getWithoutRelations(), player2.creatures.getWithoutRelations())

        SequenceOfMoves.createStartMoveLine(self.sequence)

        lastCreature = self.sequence.getElement(self.sequence.getSize() - 1)
        self.lastCreature = lastCreature


    @property
    def lastCreature(self):
        return self.__lastCreature

    @lastCreature.setter
    def lastCreature(self, creature):
        self.__lastCreature = creature
