from logic.Container import *
class SequanceOfMoves:
    @staticmethod
    def sortForInitiative(containerOfCreaturesPlayer1, containerOfCreaturesPlayer2):
        containerOfCreaturesBothPlayers = Container(containerOfCreaturesPlayer1)
        containerOfCreaturesBothPlayers.addElements(containerOfCreaturesPlayer2)

        containerOfCreaturesBothPlayers.getElements().sort()
        return containerOfCreaturesBothPlayers


    @staticmethod
    def determinateStartMoves():
        pass