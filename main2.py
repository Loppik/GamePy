import math
import pygame
from creatures.ElvenArcher import ElvenArcher
from consts import Consts

pygame.init()
screen = pygame.display.set_mode((400,400))
class Main:
    @staticmethod
    def events(event):
        # for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        return True

    @staticmethod
    def waitMousePress():
        event = 0
        while (1):
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                break
        return event

    @staticmethod
    def main():
        elf = ElvenArcher("Archer1", 0, 3, 200, 90, 5, 5, 5, Consts.WALK_3_CELL)
        res = True
        xC = 0
        yC = 0
        while res:
            t = pygame.time.get_ticks() / 2 % 400  # scale and loop time
            x = int(t)
            print(x)
            y = math.sin(t / 50.0) * 100 + 200  # scale sine wave
            y = int(y)  # needs to be int
            # event = Main.waitMousePress()
            # res = Main.events(event)

            screen.fill((0, 0, 0))
            elf.render2(screen, Consts.RIGHT_DIRECTION, [xC, yC])

            pygame.display.flip()
            pygame.time.Clock().tick(30)
            xC += 1

Main.main()