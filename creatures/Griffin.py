from creatures.Human import Human
from ImagesMaker import ImagesMaker

class Griffin(Human):
    def __init__(self, name, position, amount, health, attack, defense, initiative, direction, belief, walkArea):
        Human.__init__(self, name, position, amount, health, attack, defense, initiative, direction, belief)
        self.imagesPack = "images/pers/griffin.png"
        self.imagesPackInv = "images/pers/griffin_inv.png"
        self.spriteH = 82
        self.spriteW = 80
        ImagesMaker.subImages(self)
        self.background = self.images.getElement(self.direction).getElement(self.status)
        self.walkArea = walkArea