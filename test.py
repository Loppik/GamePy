from creatures.Creature import *
from creatures.Characteristics import *
from creatures.Elf import *
from creatures.Human import *
from Hero import *
from logic.SequenceOfMoves import *

def main():
    elvenArcher = Human("Elven archer", 10,10,10,10,10)
    fire = Human("Fire", 15,15,15,15,15)
    angel = Human("Angel", 17,17,17,17,17)
    knight = Human("Knight", 20, 20, 20, 20, 20)

    player1 = Hero("Alex", [elvenArcher, fire])
    player2 = Hero("Bot", [angel, knight])

    SequanceOfMoves.sortForInitiative(player1.getAllCreatures(), player2.getAllCreatures())



main()