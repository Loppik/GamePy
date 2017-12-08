class Button:
    def __init__(self, position):
        self.__position = position
        self.__background = None

    def render(self, screen):
        screen.blit(self.background, self.getModel())

    def getModel(self):
        return self.background.get_rect(topleft=self.position)


    def onClick(self, field):
        pass

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, background):
        self.__background = background