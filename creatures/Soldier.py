from creatures.Human import Human
from ImagesMaker import ImagesMaker

class Soldier(Human):
    def __init__(self, name, position, amount, health, attack, defense, initiative, direction, belief, walkArea):
        Human.__init__(self, name, position, amount, health, attack, defense, initiative, direction, belief)
        self.imagesPack = "images/pers/soldier.png"
        self.imagesPackInv = "images/pers/soldier_inv.png"
        self.spriteH = 56.8
        self.spriteW = 74
        self.status = 2
        ImagesMaker.subImages(self)
        self.background = self.images.getElement(self.direction).getElement(self.status)
        self.walkArea = walkArea