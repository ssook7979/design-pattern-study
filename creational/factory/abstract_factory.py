from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('Drinking tea')

class Coffee(HotDrink):
    def consume(self):
        print('Drinking coffee')

class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Preparing {amount}ml of tea.')
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Preparing {amount}ml of coffee.')
        return Coffee()

class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()
    
    factories = []
    initialized = False

    def __init__(self) -> None:
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self, idx, amount):
        print('Available drinks: ')
        for f in self.factories:
            print(f[0])
        
        return self.factories[idx][1].prepare(amount)

if __name__ == '__main__':
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()