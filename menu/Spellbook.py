import pygame
from menu.Button import Button
from events.EventFieldClick import EventFieldClick
from logic.Container import Container

class Spellbook(Button):
    def __init__(self, position, spells):
        Button.__init__(self, position)
        self.background = pygame.image.load("images/spellbook.png")
        self.openBackground = pygame.image.load("images/openSpellbook.png")
        self.spells = spells

    @staticmethod
    def waitMousePress():
        event = 0
        while (1):
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                break
        return event

    def renderOpen(self, this):
        this.screen.blit(self.openBackground, self.openBackground.get_rect(topleft=(200,200)))
        pygame.display.update(self.openBackground.get_rect(topleft=(200,200)))

    def onClick(self, this):
        print("Spell!!!")
        self.renderOpen(this)
        event = Spellbook.waitMousePress()
        mousePosition = pygame.mouse.get_pos()
        creatureOnWhichClick = EventFieldClick.creatureOnWhichMouseCursor(this.field.creatures, mousePosition)
        if creatureOnWhichClick:
            spell = self.spells.getElement(0)
            spell.position = Container([])
            xCoordinate = this.walkNow.position.getElement(0)
            yCoordinate = this.walkNow.position.getElement(1)
            spell.position.addElement(xCoordinate + 30)
            spell.position.addElement(yCoordinate - 30)
            spell.finalPos = creatureOnWhichClick.position
            this.objects.addElement(spell)
            while spell.position.getElement(0) < spell.finalPos.getElement(0):
                spell.position.setElement(0, spell.position.getElement(0) + 30)
                this.update()
            this.objects.removeElement(3)
            print("end")
            # this.objects.addElement(spell)
            # pygame.time.Clock().tick(100)
            pygame.display.flip()





