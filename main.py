import pygame

from Field import *
from Hero import Hero
from Walks import Walks
from consts import Consts
from creatures.ElvenArcher import ElvenArcher
from events.EventFieldClick import EventFieldClick
from events.EventShoot import EventShoot
from events.EventMouseMotion import EventMouseMotion


from creatures import Creature

cell = pygame.image.load("cell2.png")
activeCell = pygame.image.load("activeCell.jpg")
attackCell = pygame.image.load("attackCell.jpg")


class Main:
    def __init__(self, screen):
        self.walkNow = 0
        self.wasWalk = True
        self.screen = screen
        self.working = True
        self.creatures = []
        self.shiftToNewCell = 0
        self.field = Field(screen, cell, activeCell)
        self.mainLoop()

    def texts(self, score):
        font = pygame.font.Font(None, 30)
        scoretext = font.render("Score:" + str(score), 1, (255, 255, 255))
        screen.blit(scoretext, (500, 457))

    def renderPassiveCells(self):
        pygame.display.flip()
        screen.fill((255, 255, 255))

        self.field.renderCells()

    def renderActiveCells(self, activeCells):
        self.field.renderActiveCells(activeCells)

    def createCells(self):
        mapContainerCellsCoordinates = Walks.mapContainerCellsCoordinates
        self.field.createCells(mapContainerCellsCoordinates)

    def mouseMotionEvent(self, event):
        if event.type == pygame.MOUSEMOTION:
            mousePosition = pygame.mouse.get_pos()
            creatureOnWhichMoveCursor = EventFieldClick.creatureOnWhichMouseCursor(self.field.creatures, mousePosition)
            if creatureOnWhichMoveCursor :
                if not EventFieldClick.checkOnCompareTwoCreatures(creatureOnWhichMoveCursor, self.walkNow):
                    attackSide = EventMouseMotion.identifyAttackSide(creatureOnWhichMoveCursor.getXcoordinate(), creatureOnWhichMoveCursor.getYcoordinate(), mousePosition)
                    shiftToNewCell = EventMouseMotion.identifyShiftToNewCell(attackSide)
                    newCellNumber = shiftToNewCell + creatureOnWhichMoveCursor.cellNumber

                    # self.field.cells.getElement(creatureOnWhichMoveCursor.cellNumber + shiftToNewCell).cellBackground = attackCell
                    # self.field.cells.getElement(creatureOnWhichMoveCursor.cellNumber + shiftToNewCell).model = attackCell.get_rect(topleft=self.field.cells.getElement(creatureOnWhichMoveCursor.cellNumber + shiftToNewCell).position.getElements())
                    # self.shiftToNewCell = shiftToNewCell
                    # self.renderActiveCells(self.walkNow.cellsOnWhichCanMove)
                    # self.renderPassiveCells()
                    if Walks.identifyCoordinatesByCellNumber(newCellNumber):
                        cell = Cell(attackCell, Container([Walks.identifyCoordinatesByCellNumber(newCellNumber).getElement(0),Walks.identifyCoordinatesByCellNumber(newCellNumber).getElement(1)]))
                        cell.cellNumber = newCellNumber

                        # Render all
                        self.renderActiveCells(self.walkNow.cellsOnWhichCanMove)
                        cell.renderCell(self.screen)
                        self.creatures[0].render(self.screen, Consts.RIGHT_DIRECTION)
                        self.creatures[1].render(self.screen, Consts.DOWN_DIRECTION)
                        self.renderPassiveCells()
                    else:
                        pass


    def mousePressEvent(self, event):
        #for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.working = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()

            self.wasWalk = False
            creatureOnWhichClick = EventFieldClick.creatureOnWhichMouseCursor(self.field.creatures, mousePosition)
            if creatureOnWhichClick:
                if not EventFieldClick.checkOnCompareTwoCreatures(creatureOnWhichClick, self.walkNow):
                    #asdasd
                    self.walkNow.cellNumber = creatureOnWhichClick.cellNumber + self.shiftToNewCell
                    self.walkNow.position = Walks.identifyCoordinatesByCellNumber(self.walkNow.cellNumber)
                    #asdasd
                    EventShoot.shoot(self.walkNow, creatureOnWhichClick)
                    self.wasWalk = True
                    return

            cell = EventFieldClick.cellOnWhichClick(self.field.cells, mousePosition)
            if cell and Walks.checkCellOnExistenceInContainer(cell, self.walkNow.cellsOnWhichCanMove):
                EventFieldClick.moveCreatureInOtherPos(self.field, self.walkNow, cell)
                self.wasWalk = True


    def waitMousePress(self):
        event = 0
        while (1):
            event = pygame.event.wait()
            if event.type == pygame.MOUSEMOTION:
                self.mouseMotionEvent(event)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                break
        return event

    @staticmethod
    def addCreatureToHero(creature, hero):
        creature.hero = hero
        hero.addCreature(creature)

    def mainLoop(self):
        # Create cells
        self.createCells()

        # Creature units
        elf = ElvenArcher("Archer1", Container([0,0]), 3, 200, 90, 5, 5, 5, Consts.WALK_3_CELL)
        elf.cellNumber = Walks.identifyCellByCoordinates(elf.getXcoordinate(), elf.getYcoordinate(), self.field.cells).cellNumber
        elf2 = ElvenArcher("Archer2", Container([770,0]), 7, 60, 60, 5, 5, 5, Consts.WALK_3_CELL)
        elf2.cellNumber = Walks.identifyCellByCoordinates(elf2.getXcoordinate(), elf2.getYcoordinate(), self.field.cells).cellNumber
        print(elf2.cellNumber)
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
        allCells[elf.cellNumber].creature = elf
        allCells[elf2.cellNumber].creature = elf2

        self.creatures = [elf, elf2]

        while self.working:
            if self.wasWalk:
                self.walkNow = sequence[index]

            cellsOnWhichCreatureCanMove = Walks.identifyCellsOnWhichCreatureCanMove(self.walkNow, self.walkNow.getCorrectionCoefs(), self.field.cells)
            self.renderActiveCells(cellsOnWhichCreatureCanMove)
            self.walkNow.cellsOnWhichCanMove = cellsOnWhichCreatureCanMove
            elf.render(self.screen, Consts.RIGHT_DIRECTION)
            elf2.render(self.screen, Consts.DOWN_DIRECTION)
            self.renderPassiveCells()

            event = self.waitMousePress()
            self.mousePressEvent(event)
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
