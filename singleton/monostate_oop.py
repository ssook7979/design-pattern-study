class Monostate:
    __shared_state = {}

    def __new__(cls, *args, **kwds):
        obj = super(Monostate, cls).__new__(cls, *args, *kwds)
        obj.__dict__ = cls.__shared_state
        return obj
        

class CEO(Monostate):

    def __init__(self):
        self.name = ''
        self.age = 0

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old'

if __name__ == '__main__':
    ceo1 = CEO()
    ceo2 = CEO()
    ceo2.name = 'John'
    ceo2.age = 77
    print(ceo1, ceo2, sep = ', ')
