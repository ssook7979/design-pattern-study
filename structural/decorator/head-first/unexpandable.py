from abc import ABC


class Beverage(ABC):
    def __init__(self) -> None:
        self._description = ""
        self._milk = False
        self._soy = False
        self._mocha = False
        self._whip = False
        self._cost = 0
    
    @property
    def description(self):
        return self._description

    @property
    def cost(self):
        return self._cost
    
    @property
    def milk(self):
        return self._milk
    
    @property
    def soy(self):
        return self._soy

    @property
    def mocha(self):
        return self._mocha

    @property
    def whip(self):
        return self._whip

class HouseBlend(Beverage):
    pass

class DarkRoast(Beverage):
    pass

class Decaf(Beverage):
    pass

class Espresso(Beverage):
    pass


