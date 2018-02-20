from menu.Button import Button
import pygame

class ShootLog(Button):
    def __init__(self, position):
        Button.__init__(self, position)
        self.log = None
        self.background = pygame.image.load("images/waitButton.png")

    def render(self, screen):
        font = pygame.font.Font(None, 20)
        if self.log:
            text = font.render(self.log, 1, (0, 0, 0))
            screen.blit(text, self.position.getElements())
