from abc import ABC
from pydoc import _OldStyleClass


class Beverage(ABC):
    def __init__(self) -> None:
        self._description = ""
        self._cost = 0
    
    @property
    def description(self):
        return self._description

    @property
    def cost(self):
        return self._cost

class Condiment(Beverage):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

class Milk(Condiment):
    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)
        self._description = beverage.description + ", milk"
        self._cost = beverage.cost + 500

class Mocha(Condiment):
    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)
        self._description = beverage.description + ", mocha"
        self._cost = beverage.cost + 300

class Soy(Condiment):
    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)
        self._description = beverage.description + ", soy"
        self._cost = beverage.cost + 700

class whip(Condiment):
    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)
        self._description = beverage.description + ", whip"
        self._cost = beverage.cost + 500

class Espresso(Beverage):
    def __init__(self) -> None:
        self._description = "Espresso"
        self._cost = 1000

class HouseBlend(Beverage):
    def __init__(self) -> None:
        self._description = "House Blend"
        self._cost = 1000
        
class DarkRoast(Beverage):
    def __init__(self) -> None:
        self._description = "Dark Roast"
        self._cost = 1500

class Decaf(Beverage):
    def __init__(self) -> None:
        self._description = "Decaffein"
        self._cost = 2000
