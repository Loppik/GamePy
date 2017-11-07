class Characteristics:
    def __init__(self, health, attack, defense, initiative):
        self.__health = health
        self.__attack = attack
        self.__defense = defense
        self.__initiative = initiative

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, attack):
        self.__attack = attack

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, defense):
        self.__defense = defense

    @property
    def initiative(self):
        return self.__initiative

    @initiative.setter
    def initiative(self, initiative):
        self.__initiative = initiative