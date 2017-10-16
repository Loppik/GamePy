from creatures.Elf import Elf
from consts import Consts
import pygame

class ElvenArcher(Elf):
    def __init__(self, name, position, health, attack, defense, initiative, luck):
        Elf.__init__(self, name, position, health, attack, defense, initiative, luck)
        self.imagesPack = ["images/pers/elven_archer.png"]
        self.images = [pygame.image.load(self.imagesPack[0]).convert_alpha().subsurface(0,0,72,72),
                       pygame.image.load(self.imagesPack[0]).convert_alpha().subsurface(144,0,72,72),
                       pygame.image.load(self.imagesPack[0]).convert_alpha().subsurface(288,0,72,72)]

    def render(self, screen):
        screen.blit(self.images[Consts.RIGHT_DIRECTION], self.position)
