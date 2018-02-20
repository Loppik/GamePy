from creatures.Human import Human
from ImagesMaker import ImagesMaker

class DeathKnight(Human):
    def __init__(self, name, position, amount, health, attack, defense, initiative, direction, belief, walkArea):
        Human.__init__(self, name, position, amount, health, attack, defense, initiative, direction, belief)
        self.imagesPack = "images/pers/death_knight.png"
        self.imagesPackInv = "images/pers/death_knight_inv.png"
        self.spriteH = 72
        self.spriteW = 72
        ImagesMaker.subImages(self)
        self.background = self.images.getElement(self.direction).getElement(self.status)
        self.walkArea = walkArea











