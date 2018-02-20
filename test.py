from creatures.Creature import *
from creatures.Characteristics import *
from creatures.Elf import *
from creatures.Human import *
from Hero import *
from logic.SequenceOfMoves import *
from Consts import Consts
from creatures.DeathKnight import DeathKnight

def main():
    elvenArcher = DeathKnight("Archer2", Container([70,350]), 3, 200, 90, 5, 15, 2, 5, Consts.WALK_3_CELL)
    fire = DeathKnight("Archer4", Container([70,350]), 3, 200, 90, 5, 11, 2, 5, Consts.WALK_3_CELL)
    angel = DeathKnight("Archer3", Container([70,350]), 3, 200, 90, 5, 13, 2, 5, Consts.WALK_3_CELL)
    knight = DeathKnight("Archer1", Container([70,350]), 3, 200, 90, 5, 17, 2, 5, Consts.WALK_3_CELL)

    player1 = Hero("Alex", [elvenArcher, fire])
    player2 = Hero("Bot", [angel, knight])


    containerOfCreaturesBothPlayers = SequenceOfMoves.sortForInitiative(player1.getAllCreatures(), player2.getAllCreatures())
    # for creature in containerOfCreaturesBothPlayers.getElements():
    #     print(creature.name)
    SequenceOfMoves.createStartMoveLine(containerOfCreaturesBothPlayers)
    #print(containerOfCreaturesBothPlayers.getElement(1).initiative)
    containerOfCreaturesBothPlayers.getElement(0).initiative = 1.9
    containerOfCreaturesBothPlayers.getElement(1).initiative = 1.8
    containerOfCreaturesBothPlayers.getElement(2).initiative = 1.3
    containerOfCreaturesBothPlayers.getElement(3).initiative = 1.0
    lastCreature = containerOfCreaturesBothPlayers.getElement(containerOfCreaturesBothPlayers.getSize() - 1)
    i = 0
    while i < 16:
        crMove = SequenceOfMoves.determinateMove(containerOfCreaturesBothPlayers)
        if crMove == lastCreature:
            containerOfCreaturesBothPlayers.getElement(0).initiative += 1.9
            containerOfCreaturesBothPlayers.getElement(1).initiative += 1.8
            containerOfCreaturesBothPlayers.getElement(2).initiative += 1.3
            containerOfCreaturesBothPlayers.getElement(3).initiative += 1.0
        print(crMove.name)
        i += 1


pygame.init()
screen = pygame.display.set_mode((Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT))
main()