import pygame
from menu.Button import Button

class Wait(Button):
    def __init__(self, position):
        Button.__init__(self, position)
        self.background = pygame.image.load("images/waitButton.png")

    def onClick(self, field):
        print("Wait")
