from creatures.Human import Human
from ImagesMaker import ImagesMaker

class Orc(Human):
    def __init__(self, name, position, amount, health, attack, defense, initiative, direction, belief, walkArea):
        Human.__init__(self, name, position, amount, health, attack, defense, initiative, direction, belief)
        self.imagesPack = "images/pers/orc.png"
        self.imagesPackInv = "images/pers/orc_inv.png"
        self.spriteH = 55
        self.spriteW = 60
        self.status = 2
        ImagesMaker.subImages(self)
        self.background = self.images.getElement(self.direction).getElement(self.status)
        self.walkArea = walkArea