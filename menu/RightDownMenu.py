import pygame
from logic.Container import Container

class RightDownMenu:
    def __init__(self):
        self.defenseButton = pygame.image.load("images/defButton.png")
        self.position = (850,10)
        self.buttons = Container([])
        self.buttons.addElement(self.defenseButton)

