from creatures.Elf import Elf
from ImagesMaker import ImagesMaker
import pygame

class ElvenArcher(Elf):
    def __init__(self, name, position, amount, health, attack, defense, initiative, direction, luck, walkArea):
        Elf.__init__(self, name, position, amount, health, attack, defense, initiative, direction, luck)
        self.imagesPack = "images/pers/elven_archer.png"
        self.imagesPackInv = "images/pers/elven_archer_inv.png"
        self.spriteH = 72
        self.spriteW = 72
        ImagesMaker.subImages(self)
        self.background = self.images.getElement(self.direction).getElement(self.status)
        self.walkArea = walkArea





