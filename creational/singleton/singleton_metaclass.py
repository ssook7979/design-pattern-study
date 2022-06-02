from typing import Any


class Singleton(type):
    _instances = {}
    # metaclass의 call에 대해 https://alphahackerhan.tistory.com/34
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, *kwds)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self) -> None:
        print('Loading database')
        
if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)