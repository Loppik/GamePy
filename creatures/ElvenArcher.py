from creatures.Elf import Elf
from consts import Consts
import pygame
from Walks import *

class ElvenArcher(Elf):
    def __init__(self, name, position, amount, health, attack, defense, initiative, direction, luck, walkArea):
        Elf.__init__(self, name, position, amount, health, attack, defense, initiative, direction, luck)
        self.imagesPack = ["images/pers/elven_archer.png"]
        self.images = [pygame.image.load(self.imagesPack[0]).convert_alpha().subsurface(0,0,72,72),
                       pygame.image.load(self.imagesPack[0]).convert_alpha().subsurface(144,0,72,72),
                       pygame.image.load(self.imagesPack[0]).convert_alpha().subsurface(288,0,72,72),
                       pygame.image.load(self.imagesPack[0]).convert_alpha().subsurface(0,288,72,72),
                       pygame.image.load(self.imagesPack[0]).convert_alpha().subsurface(288,288,72,72)]
        self.model = self.images[0].get_rect(topleft=self.position.getElements())
        self.walkArea = walkArea





