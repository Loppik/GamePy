import pygame

from creatures.Characteristics import *
from logic.Container import Container
from Walks import Walks
from creatures.FieldObject import FieldObject


class Creature(FieldObject):
    def __init__(self, name, position, amount, fullHealth, attack, defense, initiative, direction):
        FieldObject.__init__(self, position, None)
        self.__name = name
        self.__characterisitcs = Characteristics(amount, fullHealth, attack, defense, initiative)
        self.__hero = None
        self.__walkArea = Container([])
        self.__cellsOnWhichCanMove = None
        self.__direction = direction # 0 - 7
        self.__status = 0
        self.__imageAngel = 0
        self.__imagesPack = None
        self.__images = Container([Container([]), Container([]), Container([]), Container([]), Container([]), Container([]), Container([]), Container([])])

    def getCorrectionCoefs(self):
        return self.__walkArea.getElements()

    def render(self, screen):
        self.renderAmountCreatures(screen)
        image = pygame.transform.rotate(self.__images.getElement(self.direction).getElement(self.status), self.imageAngel)
        self.model = image.get_rect(topleft=self.position.getElements())
        screen.blit(image, (self.getXcoordinate(),self.getYcoordinate()))

        # screen.blit(self.images[direction], Walks.identifyCoordinatesByCellNumber(self.position))

    def renderAmountCreatures(creature, screen):
        font = pygame.font.Font(None, 30)
        scoretext = font.render(str(creature.amount), 1, (255, 0, 0))
        screen.blit(scoretext, (creature.getXcoordinate()+50, creature.getYcoordinate()+50))

    def shoot(self, prey):
        print(self.name + " наносит " + str(self.attack) + " урона " + prey.name)
        damage = self.attack
        if damage < prey.health:
            prey.health -= damage
        elif damage == prey.health:
            prey.amount -= 1
            prey.health = prey.fullHealth
        else:
            difference = damage - prey.health  # 30
            if difference >= prey.fullHealth:
                killedAmount = difference // prey.fullHealth
                print("Kill " + str(killedAmount))
                remainingHealth = difference % killedAmount
                print("remaining " + str(remainingHealth))
                prey.amount -= killedAmount

                if remainingHealth == 0:
                    prey.amount -= 1
                    prey.health = prey.fullHealth
                else:
                    prey.health = remainingHealth
            else:
                prey.amount -= 1
                prey.health = prey.fullHealth - difference

        print(self.name + " Amount " + str(self.amount) + " HP = " + str(self.health))
        print(prey.name + " Amount " + str(prey.amount) + " HP = " + str(prey.health))

    def move(self, cellOnWhichMove):
        cellOnWhichMove.creature = self
        self.position = cellOnWhichMove.position
        self.cellNumber = cellOnWhichMove.cellNumber
        cellOnWhichMove.creature = self

    @property
    def name(self):
        return self.__name

    @property
    def amount(self):
        return self.__characterisitcs.amount

    @amount.setter
    def amount(self, amount):
        self.__characterisitcs.amount = amount

    @property
    def health(self):
        return self.__characterisitcs.health

    @health.setter
    def health(self, health):
        self.__characterisitcs.health = health

    @property
    def fullHealth(self):
        return self.__characterisitcs.fullHealth

    @property
    def attack(self):
        return self.__characterisitcs.attack

    @property
    def defense(self):
        return self.__characterisitcs.defense

    @property
    def initiative(self):
        return self.__characterisitcs.initiative

    @initiative.setter
    def initiative(self, initiative):
        self.__characterisitcs.initiative = initiative


    @property
    def hero(self):
        return self.__hero

    @hero.setter
    def hero(self, hero):
        self.__hero = hero

    @property
    def walkArea(self):
        return self.__walkArea

    @walkArea.setter
    def walkArea(self, walkArea):
        self.__walkArea = walkArea

    @property
    def cellsOnWhichCanMove(self):
        return self.__cellsOnWhichCanMove

    @cellsOnWhichCanMove.setter
    def cellsOnWhichCanMove(self, cells):
        self.__cellsOnWhichCanMove = cells

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @property
    def imagesPack(self):
        return self.__imagesPack

    @imagesPack.setter
    def imagesPack(self, imagesPack):
        self.__imagesPack = imagesPack

    @property
    def images(self):
        return self.__images

    @images.setter
    def images(self, images):
        self.__images = images

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def imageAngel(self):
        return self.__imageAngel

    @imageAngel.setter
    def imageAngel(self, angel):
        self.__imageAngel = angel
