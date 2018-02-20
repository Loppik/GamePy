from menu.Button import Button
import pygame
from Game import Game

class Play(Button):
    def __init__(self, position):
        Button.__init__(self, position)
        self.background = pygame.image.load("images/defButton.png")

    def render(self, screen):
        font = pygame.font.Font(None, 100)
        text = font.render("Play", 1, (0, 0, 0))
        screen.blit(text, self.position.getElements())

    def onClick(self, this):
        game = Game(this.screen)
        game.game()