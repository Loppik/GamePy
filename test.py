from creatures.Creature import *
from creatures.Characteristics import *
from creatures.Elf import *
from creatures.Human import *
from Hero import *
from logic.SequenceOfMoves import *

def main():
    elvenArcher = Human("Elven archer", 10,10,10,10,10)
    fire = Human("Fire", 15,15,15,11,15)
    angel = Human("Angel", 17,17,17,16,17)
    knight = Human("Knight", 20, 20, 20, 18, 20)

    player1 = Hero("Alex", [elvenArcher, fire])
    player2 = Hero("Bot", [angel, knight])


    containerOfCreaturesBothPlayers = SequanceOfMoves.sortForInitiative(player1.getAllCreatures(), player2.getAllCreatures())
    # for creature in containerOfCreaturesBothPlayers.getElements():
    #     print(creature.name)
    SequanceOfMoves.createStartMoveLine(containerOfCreaturesBothPlayers)
    #print(containerOfCreaturesBothPlayers.getElement(1).initiative)
    containerOfCreaturesBothPlayers.getElement(0).initiative = 2.4
    containerOfCreaturesBothPlayers.getElement(1).initiative = 1.8
    containerOfCreaturesBothPlayers.getElement(2).initiative = 1.3
    containerOfCreaturesBothPlayers.getElement(3).initiative = 1.0
    i = 0
    while i < 8:
        crMove = SequanceOfMoves.determinateMove(containerOfCreaturesBothPlayers)
        print(crMove.name)
        i += 1


main()