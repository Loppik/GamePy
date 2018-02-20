from creatures.Human import Human
from ImagesMaker import ImagesMaker

class Mage(Human):
    def __init__(self, name, position, amount, health, attack, defense, initiative, direction, belief, walkArea):
        Human.__init__(self, name, position, amount, health, attack, defense, initiative, direction, belief)
        self.imagesPack = "images/pers/mage.png"
        self.imagesPackInv = "images/pers/mage_inv.png"
        self.spriteH = 62
        self.spriteW = 74
        ImagesMaker.subImages(self)
        self.background = self.images.getElement(self.direction).getElement(self.status)
        self.walkArea = walkArea