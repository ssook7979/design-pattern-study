from cmath import cos, sin
from mimetypes import init
from re import X


class Point:
    def __init__(self, x=0, y=y) -> None:
        self.x = X
        self.y = y

class PointFactory:
    def __init__(self, x, y) -> None:
        self.x = X
        self.y = y
    
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)
    
    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho  * sin(theta))