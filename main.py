import pygame, sys
from consts import Consts
from creatures.ElvenArcher import ElvenArcher


map_cell_pos = [0, 70, 140, 210, 280, 350, 420, 490, 560, 630, 700, 770, 840]


cell = pygame.image.load("cell2.png")
cell1 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[0]))
cell2 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[1]))
cell3 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[2]))
cell4 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell5 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[4]))
cell6 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[5]))
cell7 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[6]))
cell8 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[7]))
cell9 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[8]))
cell10 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[9]))
cell11 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[10]))
cell12 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell13 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell14 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell15 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell16 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell17 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell18 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell19 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell20 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))

class Main:
    def __init__(self, screen):
        self.screen = screen
        self.working = True
        self.elf = ElvenArcher("Archer", (0,0),5,5,5,5,5)
        self.mainLoop()

    def render(self):
        pygame.display.flip()
        screen.fill((255, 255, 255))


        screen.blit(cell, cell1)
        screen.blit(cell, cell2)
        screen.blit(cell, cell3)
        screen.blit(cell, cell4)
        screen.blit(cell, cell5)
        screen.blit(cell, cell6)
        screen.blit(cell, cell7)
        screen.blit(cell, cell8)
        screen.blit(cell, cell9)
        screen.blit(cell, cell10)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.working = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if cell1.collidepoint(mouse_pos):
                    self.elf.position = (0,0)

                if cell2.collidepoint(mouse_pos):
                    self.elf.position = (0,60)

                if cell3.collidepoint(mouse_pos):
                    self.elf.position = (0,120)


    def mainLoop(self):
        while self.working:
            self.elf.render(self.screen)
            self.render()
            self.events()

pygame.init()
screen = pygame.display.set_mode((Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT))
game = Main(screen)


# map_cell_pos = [0, 70, 140, 210, 280, 350, 420, 490, 560, 630, 700, 770, 840]
#
#
# cell = pygame.image.load("cell2.png")
# cell1 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[0]))
# cell2 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[1]))
# cell3 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[2]))
# cell4 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
# cell5 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[4]))
# cell6 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[5]))
# cell7 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[6]))
# cell8 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[7]))
# cell9 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[8]))
# cell10 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[9]))
# cell11 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[10]))
# cell12 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
# cell13 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
# cell14 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
# cell15 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
# cell16 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
# cell17 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
# cell18 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
# cell19 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
# cell20 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
#
# pers = pygame.image.load("pers.png")
# pers1 = pers.get_rect(topleft=(0,0))
#
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_pos = pygame.mouse.get_pos()
#
#             if cell1.collidepoint(mouse_pos):
#                 print("1")
#
#
#     screen.fill((255, 255, 255))
#
#
#     screen.blit(cell, cell1)
#     screen.blit(cell, cell2)
#     screen.blit(cell, cell3)
#     screen.blit(cell, cell4)
#     screen.blit(cell, cell5)
#     screen.blit(cell, cell6)
#     screen.blit(cell, cell7)
#     screen.blit(cell, cell8)
#     screen.blit(cell, cell9)
#     screen.blit(cell, cell10)
#
#     screen.blit(pers, pers1)
#
#     pygame.display.flip()