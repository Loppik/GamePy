import pygame

class ImagesMaker:
    @staticmethod
    def subImages(creature):
        image = pygame.image.load(creature.imagesPack).convert_alpha()
        h = 0
        w = creature.spriteW
        hSprite = creature.spriteH
        for i in range(8):
            creature.images.getElement(0).addElement(image.subsurface(0, h, w, hSprite))
            creature.images.getElement(1).addElement(image.subsurface(w, h, w, hSprite))
            creature.images.getElement(2).addElement(image.subsurface(w*2, h, w, hSprite))
            creature.images.getElement(3).addElement(image.subsurface(w*3, h, w, hSprite))
            creature.images.getElement(4).addElement(image.subsurface(w*4, h, w, hSprite))
            h += creature.spriteH

        image = pygame.image.load(creature.imagesPackInv).convert_alpha()
        h = 0
        w = creature.spriteW
        hSprite = creature.spriteH
        for i in range(8):
            creature.images.getElement(5).addElement(image.subsurface(w, h, w, hSprite))
            creature.images.getElement(6).addElement(image.subsurface(w*2, h, w, hSprite))
            creature.images.getElement(7).addElement(image.subsurface(w*3, h, w, hSprite))
            h += creature.spriteH

