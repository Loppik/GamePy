import pygame, sys
from consts import Consts
from creatures.ElvenArcher import ElvenArcher
from logic.MapContainer import *
from Field import *
from Hero import Hero
from Walks import Walks
from EventFieldClick import EventFieldClick

cell = pygame.image.load("cell2.png")
activeCell = pygame.image.load("activeCell.jpg")


class Main:
    def __init__(self, screen):
        self.walkNow = 0
        self.wasWalk = True
        self.screen = screen
        self.working = True
        self.field = Field(screen, cell, activeCell)
        self.mainLoop()

    def renderPassiveCells(self):
        pygame.display.flip()
        screen.fill((255, 255, 255))

        mapContainerCellsCoordinates = Walks.mapContainerCellsCoordinates
        self.field.renderCells(mapContainerCellsCoordinates)


    def renderActiveCells(self, activeCells):
        self.field.renderActiveCells(activeCells)

    def events(self, event):
        # for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.working = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()

            creature = EventFieldClick.creatureOnWhichClick(self.field.creatures, mousePosition)
            if (creature):
                if (EventFieldClick.checkClickOnCreatureWhichWalksNow(creature, self.walkNow)):
                    self.wasWalk = False
                else:
                    print("Shoot " + creature.name + "!!!")
                    self.wasWalk = True
            else:
                cell = EventFieldClick.cellOnWhichClick(self.field.cells, mousePosition)
                EventFieldClick.moveCreatureInOtherPos(self.field, self.walkNow, cell)
                self.wasWalk = True

    @staticmethod
    def waitMousePress():
        event = 0
        while (1):
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                break
        return event

    @staticmethod
    def addCreatureToHero(creature, hero):
        creature.hero = hero
        hero.addCreature(creature)

    def mainLoop(self):
        # Creature units
        elf = ElvenArcher("Archer", 0, 5, 5, 5, 5, 5, Consts.WALK_3_CELL)
        elf2 = ElvenArcher("Archer2", 11, 5, 5, 5, 5, 5, Consts.WALK_3_CELL)
        self.field.creatures.addElement(elf)
        self.field.creatures.addElement(elf2)
        player1 = Hero("Player1", [])
        player2 = Hero("Player2", [])

        Main.addCreatureToHero(elf, player1)
        Main.addCreatureToHero(elf2, player2)

        # Create sequance of walks
        sequence = [player1.creatures.getElement(0), player2.creatures.getElement(0)]
        index = 0

        # Render
        elf.render(self.screen, Consts.RIGHT_DIRECTION)
        elf2.render(self.screen, Consts.DOWN_DIRECTION)
        self.renderPassiveCells()

        # Add creatures in memory of cells
        allCells = self.field.cells.getElements()
        allCells[elf.position].creature = elf
        allCells[elf2.position].creature = elf2

        while self.working:
            if self.wasWalk:
                self.walkNow = sequence[index]

            cellsOnWhichCreatureCanMove = Walks.identifyCellsOnWhichCreatureCanMove(self.walkNow, self.field.cells)
            self.renderActiveCells(cellsOnWhichCreatureCanMove)

            elf.render(self.screen, Consts.RIGHT_DIRECTION)
            elf2.render(self.screen, Consts.DOWN_DIRECTION)
            self.renderPassiveCells()


            event = self.waitMousePress()
            self.events(event)
            if index == len(sequence) - 1 and self.wasWalk:
                index = 0
            else:
                if self.wasWalk:
                    index += 1


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
