from creatures.Human import Human
from ImagesMaker import ImagesMaker
import pygame
import math
clock = pygame.time.Clock()

class DeathKnight(Human):
    def __init__(self, name, position, amount, health, attack, defense, initiative, direction, belief, walkArea):
        Human.__init__(self, name, position, amount, health, attack, defense, initiative, direction, belief)
        self.imagesPack = "images/pers/death_knight.png"
        # images[0] - up
        # images[1] - up right
        # image[2] - right
        # image[3] - down right
        # image[4] - down
        # image[5] - down left
        # image[6] - left
        # image[7] - up left
        # images[][0] - stay
        # images[][1] - image[][4]- run
        # images[][5] - image[][7]- shoot
        ImagesMaker.subImages(self)
        self.model = self.images.getElement(self.direction).getElement(self.status).get_rect(topleft=self.position.getElements())
        self.walkArea = walkArea

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
        if self.direction == 1:
            return finalPos.getElement(0) > self.getXcoordinate() or finalPos.getElement(1)  < self.getYcoordinate()

        if self.direction == 2:
            return finalPos.getElement(0) > self.getXcoordinate() and finalPos.getElement(1) == self.getYcoordinate()

        elif self.direction == 3:
            return finalPos.getElement(0) > self.getXcoordinate() or finalPos.getElement(1)  > self.getYcoordinate()

        if self.direction == 4:
            return finalPos.getElement(0) == self.getXcoordinate() and finalPos.getElement(1) > self.getYcoordinate()

        elif self.direction == 5:
            return finalPos.getElement(0) < self.getXcoordinate() or finalPos.getElement(1)  > self.getYcoordinate()

        if self.direction == 6:
            return finalPos.getElement(0) < self.getXcoordinate() and finalPos.getElement(1) == self.getYcoordinate()

        elif self.direction == 7:
            return finalPos.getElement(0) < self.getXcoordinate() or finalPos.getElement(1)  < self.getYcoordinate()



    def getCoefs(self, a, b, c, step):
        changeCoefX = a/(c / step)
        changeCoefY = b/(c / step)

        if self.direction == 1:
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
        angel = self.getAngel(a, c)

        self.imageAngel = 0
        i = 1
        step = 5
        changeCoefX, changeCoefY = self.getCoefs(a, b, c, step)

        while self.moveStopCondition(finalPos):
            if i == 5:
                i = 1
            self.status = i
            self.setXcoordinate(self.getXcoordinate() + changeCoefX)
            self.setYcoordinate(self.getYcoordinate() + changeCoefY)
            this.update()

            # pygame.display.update(self.images.getElement(self.direction).getElement(self.status).get_rect(topleft=(self.position.getElement(0), self.position.getElement(1))))
            # self.render(this.screen)
            # clock.tick(60)

            i += 1

        self.imageAngel = 0
        self.status = 0
        this.update()









