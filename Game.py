from Field import *
from Hero import Hero
from SocketIO import *
from Walks import Walks
from Consts import Consts

from creatures.DeathKnight import DeathKnight
from creatures.ElvenArcher import ElvenArcher
from creatures.Soldier import Soldier
from creatures.Mage import Mage
from creatures.Griffin import Griffin
from creatures.Orc import Orc

from events.EventMouseMotion import EventMouseMotion

from menu.Defense import Defense
from menu.FieldOfInformation import FieldOfInformation
from menu.Spellbook import Spellbook
from menu.ShootLog import ShootLog

from spells.Lightning import Lightning

from logic.SequenceOfMoves import SequenceOfMoves

cell = pygame.image.load("images/passiveCell.png")
activeCell = pygame.image.load("images/activeCell.png")
background = pygame.image.load("images/Back2.png")

class Game:
    def __init__(self, screen):
        self.walkNow = 0
        self.wasWalk = True
        self.screen = screen
        self.working = True
        self.objects = Container([])
        self.shiftToNewCell = 0
        self.sequenceOfMoves = None
        self.players = Container([])
        self.field = Field(screen, cell, activeCell)

    def update(self):
        self.renderActiveCells()

        for object in self.objects.getElements():
            if isinstance(object, SequenceOfMoves):
                object.render(self.screen, self.walkNow)
            else:
                object.render(self.screen)

        for creature in self.field.creatures.getElements():
            creature.render(self.screen)

        self.renderCells()

    def renderActiveCells(self):
        for cell in self.field.cells.getElements():
            if cell.status == 1:
                cell.renderCell(self.screen)

    def renderMoveCell(self, prey):
        xCoord = prey.getXccordinate()
        yCoord = prey.getYccordinate()
        for coef in Consts.WALK_2_CELL.getElements():
            x = xCoord + coef.getElement(0)
            y = yCoord + coef.getElement(1)
            cell = Walks.identifyCellByCoordinates(x, y, self.field.cells)
            if cell.status == 3:
                cell.renderCell(self.screen)

    def renderCells(self):
        pygame.display.flip()
        self.screen.fill((255, 255, 255))
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
                if creatureOnWhichMoveCursor != self.walkNow and Walks.checkOnDifTeam(self.walkNow, creatureOnWhichMoveCursor):
                    attackSide = EventMouseMotion.identifyAttackSide(creatureOnWhichMoveCursor.getXcoordinate(), creatureOnWhichMoveCursor.getYcoordinate(), mousePosition)
                    shiftToNewCell = EventMouseMotion.identifyShiftToNewCell(attackSide)
                    newCellNumber = shiftToNewCell + creatureOnWhichMoveCursor.cellNumber
                    self.shiftToNewCell = shiftToNewCell
                    if Walks.identifyCoordinatesByCellNumber(newCellNumber) and Walks.checkOnOpportunityToMove(self.walkNow, creatureOnWhichMoveCursor, self.shiftToNewCell):
                        if self.shiftToNewCell != newCellNumber:
                            if creatureOnWhichMoveCursor and self.getMoveStatusCell():
                                moveCell = self.getMoveStatusCell()
                                self.setActiveStatusCell(moveCell)
                            else:
                                cell = self.field.getCellInCells(newCellNumber)
                                self.setMoveStatusCell(cell)
                                self.update()

    def mousePressEvent(self, event):
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

    def eventClickOnCreature(self, creatureOnWhichClick):
        if creatureOnWhichClick != self.walkNow and Walks.checkOnOpportunityToMove(self.walkNow, creatureOnWhichClick, self.shiftToNewCell) and Walks.checkOnDifTeam(self.walkNow, creatureOnWhichClick):
            newCellNumber = self.shiftToNewCell + creatureOnWhichClick.cellNumber
            newPosition = Walks.identifyCoordinatesByCellNumber(newCellNumber)

            self.walkNow.renderMove(self, newPosition)
            self.walkNow.setXcoordinate(newPosition.getElement(0))
            self.walkNow.setYcoordinate(newPosition.getElement(1))
            cell = self.field.getCellInCells(self.walkNow.cellNumber)
            cell.creature = None
            self.walkNow.cellNumber = newCellNumber
            cell = self.field.getCellInCells(newCellNumber)
            cell.creature = self.walkNow

            self.walkNow.changeAttackDirection(creatureOnWhichClick)
            self.walkNow.renderShoot(self)
            shootLog = self.walkNow.shoot(creatureOnWhichClick)
            self.objects.getElement(1).log = shootLog

            if creatureOnWhichClick.checkOnDeath():
                hero = creatureOnWhichClick.hero
                hero.creatures.remove(creatureOnWhichClick)
                cell = self.field.getCellInCells(creatureOnWhichClick.cellNumber)
                cell.creature = None
                self.field.creatures.remove(creatureOnWhichClick)
                if creatureOnWhichClick in self.sequenceOfMoves.sequence.getElements():
                    self.sequenceOfMoves.sequence.remove(creatureOnWhichClick)

            self.wasWalk = True

    def eventClickOnCell(self, cell):
        self.walkNow.renderMove(self, cell.position)
        creatureCell = self.field.getCellInCells(self.walkNow.cellNumber)
        self.walkNow.move(cell, creatureCell)
        self.wasWalk = True

    def eventClickOnObject(self, object):
        object.onClick(self.walkNow)
        if object != self.objects.getElement(0) and object != self.objects.getElement(1):
            self.wasWalk = True

    def mouseRightClick(self):
        mousePosition = pygame.mouse.get_pos()
        self.wasWalk = False

        creatureOnWhichClick = EventFieldClick.creatureOnWhichMouseCursor(self.field.creatures, mousePosition)
        if creatureOnWhichClick:
            self.objects.getElement(0).creature = creatureOnWhichClick
            self.update()


    def waitMousePress(self):
        event = 0
        while (1):
            event = pygame.event.wait()
            if event.type == pygame.MOUSEMOTION:
                self.mouseMotionEvent(event)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.mouseRightClick()
            elif event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                break
        return event


    @staticmethod
    def addCreatureToHero(creature, hero):
        creature.hero = hero
        hero.addCreature(creature)

    def checkOnEnd(self):
        lastPlayer = self.players.getElement(1)
        for player in self.players.getElements():
            if player.creatures.getSize() == 0:
                result = lastPlayer.name
                self.gameRes(result)

                self.working = False
            lastPlayer = player

    def game(self):
        self.createCells()

        # Creature units
        griffin = Griffin("Griffin", Container([70,350]), 1, 20, 90, 5, 13, 2, 5, Consts.WALK_2_CELL)
        griffin.cellNumber = Walks.identifyCellByCoordinates(griffin.getXcoordinate(), griffin.getYcoordinate(), self.field.cells).cellNumber
        orc = Orc("Orc", Container([700, 350]), 1, 60, 60, 5, 13, 6, 5, Consts.WALK_3_CELL)
        orc.cellNumber = Walks.identifyCellByCoordinates(orc.getXcoordinate(), orc.getYcoordinate(), self.field.cells).cellNumber
        mage = Mage("Mage", Container([70, 70]), 1, 60, 60, 5, 13, 2, 5, Consts.WALK_2_CELL)
        mage.cellNumber = Walks.identifyCellByCoordinates(mage.getXcoordinate(), mage.getYcoordinate(), self.field.cells).cellNumber
        knight = DeathKnight("Knight", Container([700, 70]), 1, 60, 60, 5, 13, 6, 5, Consts.WALK_3_CELL)
        knight.cellNumber = Walks.identifyCellByCoordinates(knight.getXcoordinate(), knight.getYcoordinate(), self.field.cells).cellNumber
        soldier = Soldier("Soldier", Container([70, 210]), 1, 60, 60, 5, 13, 2, 5, Consts.WALK_3_CELL)
        soldier.cellNumber = Walks.identifyCellByCoordinates(soldier.getXcoordinate(), soldier.getYcoordinate(), self.field.cells).cellNumber

        self.field.creatures.addElement(griffin)
        self.field.creatures.addElement(orc)
        self.field.creatures.addElement(mage)
        self.field.creatures.addElement(knight)
        self.field.creatures.addElement(soldier)
        player1 = Hero("Alex", [])
        player2 = Hero("Nick", [])

        self.players.addElement(player1)
        self.players.addElement(player2)

        Game.addCreatureToHero(griffin, player1)
        Game.addCreatureToHero(mage, player1)
        Game.addCreatureToHero(soldier, player1)
        Game.addCreatureToHero(knight, player2)
        Game.addCreatureToHero(orc, player2)

        # Sequence of moves
        sequenceOfMoves = SequenceOfMoves(Container([0, 600]))
        sequenceOfMoves.firstSequence(player1, player2)
        self.sequenceOfMoves = sequenceOfMoves

        # Add creatures in memory of cells
        allCells = self.field.cells.getElements()
        allCells[griffin.cellNumber].creature = griffin
        allCells[knight.cellNumber].creature = knight
        allCells[soldier.cellNumber].creature = soldier
        allCells[mage.cellNumber].creature = mage
        allCells[orc.cellNumber].creature = orc

        # Right down menu
        defenseButton = Defense(Container([850, 10]))
        fieldOfInformation = FieldOfInformation(Container([850, 160]))
        shootLog = ShootLog(Container([20, 670]))

        # Spells
        lightning = Lightning(700)
        spells = Container([])
        spells.addElement(lightning)

        # spellbook = Spellbook(Container([850, 310]), spells)
        # self.objects.addElement(waitButton)
        self.objects.addElement(fieldOfInformation)
        self.objects.addElement(shootLog)
        self.objects.addElement(defenseButton)
        self.objects.addElement(sequenceOfMoves)

        check = True
        while self.working:
            if self.wasWalk:
                crMove = sequenceOfMoves.determinateMove()
                if crMove == sequenceOfMoves.lastCreature:
                    for creature in self.sequenceOfMoves.sequence.getElements():
                        creature.chanInitiat += creature.initiative
                self.walkNow = crMove

            if check:
                self.update()
                check = False

            cellsOnWhichCreatureCanMove = Walks.identifyCellsOnWhichCreatureCanMove(self.walkNow, self.walkNow.getCorrectionCoefs(), self.field.cells)
            self.walkNow.cellsOnWhichCanMove = cellsOnWhichCreatureCanMove
            self.setActiveStatusCells(cellsOnWhichCreatureCanMove)
            self.update()

            event = self.waitMousePress()
            self.mousePressEvent(event)

            self.setPassiveStatusCells(cellsOnWhichCreatureCanMove)
            self.update()

            self.checkOnEnd()

    def gameRes(self, str):
        pygame.display.flip()
        self.screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 50)
        text = font.render("Victory!", 1, (0, 0, 0))
        self.screen.blit(text, (420, 100))
        font = pygame.font.Font(None, 100)
        text = font.render(str, 1, (0, 0, 0))
        self.screen.blit(text, (400, 140))
        pygame.display.flip()
        self.screen.fill((255, 255, 255))
        while (1):
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                break






