from abc import ABC


class Duck(ABC):
    def quack(self) -> None:
        NotImplementedError()

    def fly(self) -> None:
        NotImplementedError()

class MallardDuck(Duck):
    def quack(self) -> None:
        print("Quack")
    
    def fly(self) -> None:
        print("I'm flying!")

class Turkey(ABC):
    def gobble(self) -> None:
        NotImplementedError()

    def fly(self) -> None:
        NotImplementedError()  

class WildTurkey(Turkey):
    def gobble(self) -> None:
        print("Gobble gobble")
    
    def fly(self) -> None:
        print("I'm flying a short distance")

class TurkeyAdapter(Duck):
    def __init__(self, turkey) -> None:
        self.turkey = turkey

    def quack(self) -> None:
        self.turkey.gobble()

    def fly(self) -> None:
        for _ in range(5):
            self.turkey.fly()