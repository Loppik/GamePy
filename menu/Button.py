from creatures.Object import Object

class Button(Object):
    def __init__(self, position):
        Object.__init__(self, position, None)

    def render(self, screen):
        screen.blit(self.background, self.getModel())

    def onClick(self, this):
        pass

