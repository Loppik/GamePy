class Characteristics:
    def __init__(self, amount, fullHealth, attack, defense, initiative):
        self.__amount = amount
        self.__health = fullHealth
        self.__fullHealth = fullHealth
        self.__attack = attack
        self.__defense = defense
        self.__initiative = initiative

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    @property
    def fullHealth(self):
        return self.__fullHealth

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