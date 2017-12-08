import pygame
from menu.Button import Button

class Defense(Button):
    def __init__(self, position):
        Button.__init__(self, position)
        self.background = pygame.image.load("images/defButton.png")

    def onClick(self, field):
        print("Defense")

