from menu.Button import Button
from logic.Container import Container
import pygame

class FieldOfInformation(Button):
    def __init__(self, position):
        Button.__init__(self, position)
        self.creature = None
        self.background = pygame.image.load("images/waitButton.png")

    def render(self, screen):
        font = pygame.font.Font(None, 30)
        position = self.position.getElement(1)
        if self.creature:
            for characteristic in self.creature.getInformation().getElements():
                text = font.render(characteristic, 1, (0, 0, 0))
                screen.blit(text, (self.position.getElement(0), position))
                position += 20


    def onClick(self, creature):
        self.creature = None





