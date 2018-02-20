import pygame

class Lightning:
    def __init__(self, damage):
        self.damage = damage
        self.position = None
        self.finalPos = None
        self.background = pygame.image.load("images/spells/arrow.png")

    def render(self, screen):
        screen.blit(self.background, self.background.get_rect(topleft=(self.position.getElement(0), self.position.getElement(1))))



