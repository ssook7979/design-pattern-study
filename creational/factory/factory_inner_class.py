from cmath import cos, sin


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    class PointFactory:
        def __init__(self, x, y) -> None:
            self.x = x
            self.y = y
        
        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)
        
        @staticmethod
        def new_polar_point(rho, theta):
            return Point(rho * cos(theta), rho  * sin(theta))

    factory = PointFactory()

if __name__ == "__main__":
    p = Point(2,3)
    p2 = p.factory.new_cartesian_point(1,2)