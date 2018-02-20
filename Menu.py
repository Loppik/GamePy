import pygame
from menu.Play import Play
from menu.Exit import Exit
from logic.Container import Container
from events.EventFieldClick import EventFieldClick
from Consts import Consts

class Menu():
    def __init__(self, screen):
        self.screen = screen

    def menu(self):
        exit = Exit(Container([400, 160]))
        play = Play(Container([400, 80]))
        menuButtons = Container([exit, play])
        while True:
            pygame.display.flip()
            screen.fill((255, 255, 255))
            for button in menuButtons.getElements():
                button.render(self.screen)
            pygame.display.flip()
            screen.fill((255, 255, 255))

            event = self.waitMousePress()
            self.clickOnButton(menuButtons)

    def clickOnButton(self, menuButtons):
        mousePosition = pygame.mouse.get_pos()
        object = EventFieldClick.objectInDownMenuWhichClick(menuButtons, mousePosition)
        if object:
            object.onClick(self)

    def waitMousePress(self):
        event = 0
        while (1):
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                break
        return event


pygame.init()
screen = pygame.display.set_mode((Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT))
menu = Menu(screen)
menu.menu()
