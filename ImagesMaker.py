import pygame

class ImagesMaker:
    @staticmethod
    def subImages(creature):
        image = pygame.image.load(creature.imagesPack).convert_alpha()
        temp = 0
        for i in range(8):
            creature.images.getElement(0).addElement(image.subsurface(0,temp,72,72))
            creature.images.getElement(1).addElement(image.subsurface(72,temp,72,72))
            creature.images.getElement(2).addElement(image.subsurface(144,temp,72,72))
            creature.images.getElement(3).addElement(image.subsurface(216,temp,72,72))
            creature.images.getElement(4).addElement(image.subsurface(288,temp,72,72))
            # creature.images.getElement(5).addElement(image.subsurface(432,temp,72,72))
        # creature.images.getElement(6).addElement(image.subsurface(504,temp,72,72))
        # creature.images.getElement(7).addElement(image.subsurface(576,temp,72,72))
            temp += 72

        temp = 0
        image = pygame.image.load("images/pers/death_knight-inv.png").convert_alpha()
        for i in range(8):
            creature.images.getElement(5).addElement(image.subsurface(72, temp, 72, 72))
            creature.images.getElement(6).addElement(image.subsurface(144, temp, 72, 72))
            creature.images.getElement(7).addElement(image.subsurface(216, temp, 72, 72))
            temp += 72

