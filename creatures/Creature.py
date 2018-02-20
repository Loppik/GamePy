import pygame

from creatures.Characteristics import *
from logic.Container import Container
from Walks import Walks
from creatures.FieldObject import FieldObject
import math
clock = pygame.time.Clock()


class Creature(FieldObject):
    def __init__(self, name, position, amount, fullHealth, attack, defense, initiative, direction):
        FieldObject.__init__(self, position, None)
        self.__name = name
        self.__characteristics = Characteristics(amount, fullHealth, attack, defense, initiative)
        self.chanInitiat = initiative
        self.__hero = None
        self.__walkArea = Container([])
        self.__cellsOnWhichCanMove = None
        self.__direction = direction # 0 - 7
        self.__status = 0
        self.__imageAngel = 0
        self.__imagesPack = None
        self.__imagesPackInv = None
        self.__spriteW = None
        self.__spriteH = None
        self.__images = Container([Container([]), Container([]), Container([]), Container([]), Container([]), Container([]), Container([]), Container([])])
        '''
            images[0] - up
            images[1] - up right
            image[2] - right
            image[3] - down right
            image[4] - down
            image[5] - down left
            image[6] - left
            image[7] - up left
            images[][0] - stay
            images[][1] - image[][4]- run
            images[][5] - image[][7]- shoot
        '''

    def getCorrectionCoefs(self):
        return self.__walkArea.getElements()

    def render(self, screen):
        self.renderAmountCreatures(screen)
        self.background = self.__images.getElement(self.direction).getElement(self.status)
        image = pygame.transform.rotate(self.background, self.imageAngel)
        image.get_rect(topleft=self.position.getElements())
        screen.blit(image, (self.getXcoordinate(),self.getYcoordinate()))

    def renderAmountCreatures(creature, screen):
        font = pygame.font.Font(None, 30)
        scoretext = font.render(str(creature.amount), 1, (255, 0, 0))
        screen.blit(scoretext, (creature.getXcoordinate()+50, creature.getYcoordinate()+50))

    def shoot(self, prey):
        log = ""
        log += self.name + " наносит " + str(self.attack) + " урона " + prey.name
        damage = self.attack
        if damage < prey.health:
            prey.health -= damage
        elif damage == prey.health:
            prey.amount -= 1
            prey.health = prey.fullHealth
        else:
            difference = damage - prey.health
            if difference >= prey.fullHealth:
                killedAmount = difference // prey.fullHealth
                log += ".Kill " + str(killedAmount)
                remainingHealth = difference % killedAmount
                log += ", remaining " + str(remainingHealth)
                prey.amount -= killedAmount

                if remainingHealth == 0:
                    prey.amount -= 1
                    prey.health = prey.fullHealth
                else:
                    prey.health = remainingHealth
            else:
                prey.amount -= 1
                prey.health = prey.fullHealth - difference

        return log

    def move(self, cellOnWhichMove, creatureCell):
        creatureCell.creature = None
        cellOnWhichMove.creature = self
        self.setXcoordinate(cellOnWhichMove.position.getElement(0))
        self.setYcoordinate(cellOnWhichMove.position.getElement(1))
        self.cellNumber = cellOnWhichMove.cellNumber

    def healthRecovery(self, healthRecov):
        if self.health + healthRecov > self.fullHealth:
            recovAmount = (self.health + healthRecov) // self.fullHealth
            remainingHealth = (self.health + healthRecov) % self.fullHealth
            self.amount += int(recovAmount)
            self.health = remainingHealth
        else:
            self.health += healthRecov

    def getInformation(self):
        return Container(["Name: " + str(self.name), "Amount: " + str(self.amount), "Health: " + str(self.health) + "/" + str(self.fullHealth),
                          "Attack: " + str(self.attack), "Initiative: " + str(self.initiative)])


    def renderShoot(self, this):
        startStatus = self.status
        i = 5
        while i <= 7:
            self.status = i
            this.update()
            pygame.time.Clock().tick(70)
            i += 1
        self.status = startStatus
        this.update()


    def changeAttackDirection(self, prey):
        dif = self.cellNumber - prey.cellNumber
        if dif == 12:
            self.direction = 0
        elif dif == 11:
            self.direction = 1
        elif dif == -1:
            self.direction = 2
        elif dif == -13:
            self.direction = 3
        elif dif == -12:
            self.direction = 4
        elif dif == -11:
            self.direction = 5
        elif dif == 1:
            self.direction = 6
        elif dif == 13:
            self.direction = 7

    def getAandB(self, finalPos):
        a = 0
        b = 0

        if self.direction == 0:
            b = self.getYcoordinate() - finalPos.getElement(1)

        # up right direction for move render
        if self.direction == 1:
            a = finalPos.getElement(0) - self.getXcoordinate()
            b = self.getYcoordinate() - finalPos.getElement(1)

        if self.direction == 2:
            a = finalPos.getElement(0) - self.getXcoordinate()


        # down right
        elif self.direction == 3:
            a = finalPos.getElement(0) - self.getXcoordinate()
            b = finalPos.getElement(1) - self.getYcoordinate()

        elif self.direction == 4:
            b = finalPos.getElement(1) - self.getYcoordinate()


        # down left
        elif self.direction == 5:
            a = self.getXcoordinate() - finalPos.getElement(0)
            b = finalPos.getElement(1) - self.getYcoordinate()

        elif self.direction == 6:
            a = self.getXcoordinate() - finalPos.getElement(0)


        # up left
        elif self.direction == 7:
            a = self.getXcoordinate() - finalPos.getElement(0)
            b = self.getYcoordinate() - finalPos.getElement(1)
        return a,b


    def changeMoveDirection(self, finalPos):
        dir = 0
        # up right direction for move render
        if finalPos.getElement(0) > self.getXcoordinate() and finalPos.getElement(1) < self.getYcoordinate():
            dir = 1
        elif finalPos.getElement(0) > self.getXcoordinate() and finalPos.getElement(1) == self.getYcoordinate():
            dir = 2
        # down right
        elif finalPos.getElement(0) > self.getXcoordinate() and finalPos.getElement(1) > self.getYcoordinate():
            dir = 3
        elif finalPos.getElement(0) == self.getXcoordinate() and finalPos.getElement(1) > self.getYcoordinate():
            dir = 4
        # down left
        elif finalPos.getElement(0) < self.getXcoordinate() and finalPos.getElement(1) > self.getYcoordinate():
            dir = 5
        elif finalPos.getElement(0) < self.getXcoordinate() and finalPos.getElement(1) == self.getYcoordinate():
            dir = 6
        # up left
        elif finalPos.getElement(0) < self.getXcoordinate() and finalPos.getElement(1) < self.getYcoordinate():
            dir = 7
        self.direction = dir

    def getAngel(self, a, c):
        sin = a / c
        angel = math.asin(sin) * 180 / math.pi
        return angel

    def moveStopCondition(self, finalPos):
        if self.direction == 0:
            return finalPos.getElement(0) == self.getXcoordinate() and finalPos.getElement(1) < self.getYcoordinate()

        if self.direction == 1:
            return finalPos.getElement(0) > self.getXcoordinate() and finalPos.getElement(1)  < self.getYcoordinate()

        if self.direction == 2:
            return finalPos.getElement(0) > self.getXcoordinate() and finalPos.getElement(1) == self.getYcoordinate()

        elif self.direction == 3:
            return finalPos.getElement(0) > self.getXcoordinate() and finalPos.getElement(1)  > self.getYcoordinate()

        if self.direction == 4:
            return finalPos.getElement(0) == self.getXcoordinate() and finalPos.getElement(1) > self.getYcoordinate()

        elif self.direction == 5:
            return finalPos.getElement(0) < self.getXcoordinate() and finalPos.getElement(1)  > self.getYcoordinate()

        if self.direction == 6:
            return finalPos.getElement(0) < self.getXcoordinate() and finalPos.getElement(1) == self.getYcoordinate()

        elif self.direction == 7:
            return finalPos.getElement(0) < self.getXcoordinate() and finalPos.getElement(1)  < self.getYcoordinate()



    def getCoefs(self, a, b, c, step):
        if a == 0 and b == 0:
            changeCoefX = 0
            changeCoefY = 0
        else:
            changeCoefX = a/(c / step)
            changeCoefY = b/(c / step)

            if self.direction == 0:
                changeCoefX = 0
                changeCoefY = -changeCoefY

            elif self.direction == 1:
                changeCoefY = -changeCoefY

            elif self.direction == 2:
                changeCoefY = 0

            elif self.direction == 4:
                changeCoefX = 0

            # down left
            elif self.direction == 5:
                changeCoefX = -changeCoefX

            elif self.direction == 6:
                changeCoefX = -changeCoefX
                changeCoefY = 0

            # up left
            elif self.direction == 7:
                changeCoefX = -changeCoefX
                changeCoefY = -changeCoefY

        return changeCoefX, changeCoefY

    def renderMove(self, this, finalPos):
        self.changeMoveDirection(finalPos)
        a, b = self.getAandB(finalPos)
        c = math.sqrt(a * a + b * b)

        self.imageAngel = 0
        i = 1
        step = 15
        changeCoefX, changeCoefY = self.getCoefs(a, b, c, step)
        while self.moveStopCondition(finalPos):
            if i == 5:
                i = 1
            self.status = i
            self.setXcoordinate(self.getXcoordinate() + changeCoefX)
            self.setYcoordinate(self.getYcoordinate() + changeCoefY)
            this.update()
            i += 1

        self.imageAngel = 0
        self.status = 0
        this.update()

    def checkOnDeath(self):
        if self.amount <= 0:
            self.amount = 0
            return True
        return False

    @property
    def name(self):
        return self.__name

    @property
    def amount(self):
        return self.__characteristics.amount

    @amount.setter
    def amount(self, amount):
        self.__characteristics.amount = amount

    @property
    def health(self):
        return self.__characteristics.health

    @health.setter
    def health(self, health):
        self.__characteristics.health = health

    @property
    def fullHealth(self):
        return self.__characteristics.fullHealth

    @property
    def attack(self):
        return self.__characteristics.attack

    @property
    def defense(self):
        return self.__characteristics.defense

    @property
    def initiative(self):
        return self.__characteristics.initiative

    @initiative.setter
    def initiative(self, initiative):
        self.__characteristics.initiative = initiative


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
    def imagesPackInv(self):
        return self.__imagesPackInv

    @imagesPackInv.setter
    def imagesPackInv(self, imagesPack):
        self.__imagesPackInv = imagesPack

    @property
    def spriteW(self):
        return self.__spriteW

    @spriteW.setter
    def spriteW(self, w):
        self.__spriteW = w

    @property
    def spriteH(self):
        return self.__spriteH

    @spriteH.setter
    def spriteH(self, h):
        self.__spriteH = h

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
