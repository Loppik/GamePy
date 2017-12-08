from Field import *
from Hero import Hero
from SocketIO import *
from Walks import Walks
from consts import Consts

from creatures.DeathKnight import DeathKnight
from creatures.ElvenArcher import ElvenArcher

from events.EventMouseMotion import EventMouseMotion

from menu.Defense import Defense
from menu.Wait import Wait
from menu.Spellbook import Spellbook

from spells.Lightning import Lightning

cell = pygame.image.load("cell2.png")
activeCell = pygame.image.load("activeCell.jpg")
attackCell = pygame.image.load("attackCell.jpg")
background = pygame.image.load("images/backgroundDesert.png")


class Main:
    def __init__(self, screen):
        self.walkNow = 0
        self.wasWalk = True
        self.screen = screen
        self.working = True
        self.objects = Container([])
        self.shiftToNewCell = 0
        self.creatureOnCursor = 0
        self.field = Field(screen, cell, activeCell)
        self.mainLoop()

    def texts(self, score):
        font = pygame.font.Font(None, 30)
        scoretext = font.render("Score:" + str(score), 1, (255, 255, 255))
        screen.blit(scoretext, (500, 457))

    def update(self):
        self.renderActiveCells()
        for object in self.objects.getElements():
            object.render(self.screen)
        for creature in self.field.creatures.getElements():
            creature.render(self.screen)
        self.renderCells()

    def renderActiveCells(self):
        for cell in self.field.cells.getElements():
            if cell.status == 1:
                cell.renderCell(self.screen)

    def renderCells(self):
        pygame.display.flip()
        screen.fill((255, 255, 255))
        screen.blit(background, background.get_rect())
        self.field.renderCells()

    def setPassiveStatusCells(self, pasiveCells):
        for activeCell in pasiveCells.getElements():
            cell = self.field.getCellInCells(activeCell.cellNumber)
            cell.status = Consts.PASSIVE_CELL
            cell.updateBackground()

    def setPassiveStatusCell(self, cell):
            cell.status = Consts.PASSIVE_CELL
            cell.updateBackground()


    def setActiveStatusCells(self, activeCells):
        for passiveCell in activeCells.getElements():
            cell = self.field.getCellInCells(passiveCell.cellNumber)
            cell.status = Consts.ACTIVE_CELL
            cell.updateBackground()

    def setActiveStatusCell(self, cell):
            cell.status = Consts.ACTIVE_CELL
            cell.updateBackground()

    @staticmethod
    def setMoveStatusCell(cell):
        cell.status = Consts.MOVE_CELL
        cell.updateBackground()

    def getMoveStatusCell(self):
        for cell in self.field.cells.getElements():
            if cell.status == 3:
                return cell
        return 0

    def booleanMoveStatus(self):
        for cell in self.field.cells.getElements():
            if cell.status == 3:
                return True
        return False

    def createCells(self):
        mapContainerCellsCoordinates = Walks.mapContainerCellsCoordinates
        self.field.createCells(mapContainerCellsCoordinates)

    def mouseMotionEvent(self, event):
        if event.type == pygame.MOUSEMOTION:
            mousePosition = pygame.mouse.get_pos()
            creatureOnWhichMoveCursor = EventFieldClick.creatureOnWhichMouseCursor(self.field.creatures, mousePosition)
            if creatureOnWhichMoveCursor:
                if not EventFieldClick.checkOnCompareTwoCreatures(creatureOnWhichMoveCursor, self.walkNow):
                    self.creatureOnCursor = creatureOnWhichMoveCursor

                    attackSide = EventMouseMotion.identifyAttackSide(creatureOnWhichMoveCursor.getXcoordinate(), creatureOnWhichMoveCursor.getYcoordinate(), mousePosition)
                    shiftToNewCell = EventMouseMotion.identifyShiftToNewCell(attackSide)
                    newCellNumber = shiftToNewCell + creatureOnWhichMoveCursor.cellNumber
                    self.shiftToNewCell = shiftToNewCell
                    # self.field.cells.getElement(creatureOnWhichMoveCursor.cellNumber + shiftToNewCell).cellBackground = attackCell
                    # self.field.cells.getElement(creatureOnWhichMoveCursor.cellNumber + shiftToNewCell).model = attackCell.get_rect(topleft=self.field.cells.getElement(creatureOnWhichMoveCursor.cellNumber + shiftToNewCell).position.getElements())
                    # self.shiftToNewCell = shiftToNewCell
                    # self.renderActiveCells(self.walkNow.cellsOnWhichCanMove)
                    # self.renderPassiveCells()
                    if Walks.identifyCoordinatesByCellNumber(newCellNumber) and Walks.checkOnOpportunityToMove(self.walkNow, creatureOnWhichMoveCursor, self.shiftToNewCell):
                        if self.shiftToNewCell != newCellNumber:
                            if self.creatureOnCursor and self.getMoveStatusCell():
                                self.creatureOnCursor = 0
                                moveCell = self.getMoveStatusCell()
                                self.setActiveStatusCell(moveCell)
                            else:
                                cell = self.field.getCellInCells(newCellNumber)
                                Main.setMoveStatusCell(cell)
                                #self.field.cells.setElement(newCellNumber, cell)
                                # Render all
                                #Main.update(self, self.walkNow.cellsOnWhichCanMove)
                                self.update()



            # else:
            #     if self.creatureOnCursor and self.booleanMoveStatus():
            #         self.creatureOnCursor = 0
            #         moveCell = self.getMoveStatusCell()
            #         self.setPassiveStatusCell(moveCell)





    def mousePressEvent(self, event):
        #for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.working = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()
            self.wasWalk = False

            creatureOnWhichClick = EventFieldClick.creatureOnWhichMouseCursor(self.field.creatures, mousePosition)
            if creatureOnWhichClick:
                self.eventClickOnCreature(creatureOnWhichClick)
                return

            cell = EventFieldClick.cellOnWhichClick(self.field.cells, mousePosition)
            if cell and Walks.checkCellOnExistenceInContainer(cell, self.walkNow.cellsOnWhichCanMove):
                self.eventClickOnCell(cell)
                return

            object = EventFieldClick.objectInDownMenuWhichClick(self.objects, mousePosition)
            if object:
                self.eventClickOnObject(object)
                return

    def eventClickOnCreature(self, creatureOnWhichClick):
        print("Shift " +  str(self.shiftToNewCell))
        if not EventFieldClick.checkOnCompareTwoCreatures(creatureOnWhichClick, self.walkNow) and Walks.checkOnOpportunityToMove(self.walkNow, creatureOnWhichClick, self.shiftToNewCell):
            # asdasd
            newCellNumber = self.shiftToNewCell + creatureOnWhichClick.cellNumber
            newPosition = Walks.identifyCoordinatesByCellNumber(newCellNumber)

            self.walkNow.renderMove(self, newPosition)

            self.walkNow.cellNumber = newCellNumber
            self.walkNow.position = newPosition
            # asdasd
            self.walkNow.changeAttackDirection(creatureOnWhichClick)
            self.walkNow.renderShoot(self)
            self.walkNow.shoot(creatureOnWhichClick)
            self.wasWalk = True

    def eventClickOnCell(self, cell):
        self.walkNow.renderMove(self, cell.position)
        self.walkNow.move(cell)
        self.wasWalk = True

    def eventClickOnObject(self, object):
        object.onClick(self)
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
        elf = DeathKnight("Archer1", Container([70,70]), 3, 200, 90, 5, 5, 2, 5, Consts.WALK_3_CELL)
        elf.cellNumber = Walks.identifyCellByCoordinates(elf.getXcoordinate(), elf.getYcoordinate(), self.field.cells).cellNumber
        knight = DeathKnight("Knight", Container([770, 0]), 7, 60, 60, 5, 5, 6, 5, Consts.WALK_3_CELL)
        knight.cellNumber = Walks.identifyCellByCoordinates(knight.getXcoordinate(), knight.getYcoordinate(), self.field.cells).cellNumber

        self.field.creatures.addElement(elf)
        self.field.creatures.addElement(knight)
        player1 = Hero("Player1", [])
        player2 = Hero("Player2", [])

        Main.addCreatureToHero(elf, player1)
        Main.addCreatureToHero(knight, player2)

        # Create sequance of walks
        sequence = [player1.creatures.getElement(0), player2.creatures.getElement(0)]
        index = 0

        # Add creatures in memory of cells
        allCells = self.field.cells.getElements()
        allCells[elf.cellNumber].creature = elf
        allCells[knight.cellNumber].creature = knight

        # Right down menu
        defenseButton = Defense((850, 10))
        waitButton = Wait((850, 160))

        # Spells
        lightning = Lightning(700)
        spells = Container([])
        spells.addElement(lightning)

        spellbook = Spellbook((850, 310), spells)
        self.objects.addElement(waitButton)
        self.objects.addElement(defenseButton)
        self.objects.addElement(spellbook)

        # Render
        self.update()

        # create socket
        #socket = Socket(3000, self.field)

        while self.working:
            if self.wasWalk:
                self.walkNow = sequence[index]

            cellsOnWhichCreatureCanMove = Walks.identifyCellsOnWhichCreatureCanMove(self.walkNow, self.walkNow.getCorrectionCoefs(), self.field.cells)
            self.walkNow.cellsOnWhichCanMove = cellsOnWhichCreatureCanMove
            self.setActiveStatusCells(cellsOnWhichCreatureCanMove)
            self.update()

            event = self.waitMousePress()
            self.mousePressEvent(event)

            # Socket
            #socket.socket.wait(seconds=5)
            #
            # socket.socketOn()
            # socket.emit(self.walkNow.name, self.walkNow.cellNumber, self.field)

            self.setPassiveStatusCells(cellsOnWhichCreatureCanMove)
            self.update()

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
