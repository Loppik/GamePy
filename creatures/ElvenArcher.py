from creatures.Elf import Elf
from consts import Consts
import pygame
from Walks import *

class ElvenArcher(Elf):
    def __init__(self, name, position, amount, health, attack, defense, initiative, luck, walkArea):
        Elf.__init__(self, name, position, amount, health, attack, defense, initiative, luck)
        self.__imagesPack = ["images/pers/elven_archer.png"]
        self.__images = [pygame.image.load(self.__imagesPack[0]).convert_alpha().subsurface(0,0,72,72),
                       pygame.image.load(self.__imagesPack[0]).convert_alpha().subsurface(144,0,72,72),
                       pygame.image.load(self.__imagesPack[0]).convert_alpha().subsurface(288,0,72,72)]
        self.model = self.__images[0].get_rect(topleft=self.position.getElements())
        self.walkArea = walkArea

    def render2(self, screen, direction, coordinates):
        self.renderAmountCreatures(screen)
        self.model = self.__images[direction].get_rect(topleft=self.position)
        screen.blit(self.__images[direction], self.__images[direction].get_rect(topleft=(coordinates[0], coordinates[1])))


    def render(self, screen, direction):
        self.renderAmountCreatures(screen)
        self.model = self.__images[direction].get_rect(topleft=self.position.getElements())
        screen.blit(self.__images[direction], self.__images[direction].get_rect(topleft=self.position.getElements()))

        #screen.blit(self.images[direction], Walks.identifyCoordinatesByCellNumber(self.position))

    @property
    def imagesPack(self):
        return self.__imagesPack

    @property
    def images(self):
        return self.__images




