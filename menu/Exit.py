from menu.Button import Button
import pygame

class Exit(Button):
    def __init__(self, position):
        Button.__init__(self, position)
        self.background = pygame.image.load("images/defButton.png")

    def render(self, screen):
        font = pygame.font.Font(None, 100)
        text = font.render("Exit", 1, (0, 0, 0))
        screen.blit(text, self.position.getElements())

    def onClick(self, field):
        exit(0)

