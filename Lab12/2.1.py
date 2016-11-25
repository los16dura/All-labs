__author__ = 'los16dura'
class Shape:
    h = 0
    a = 0

    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        pass

class Triangle(Shape):
    def area(self):
        super().area()
        return 0.5*self.a*self.h

    class Rectangle(Shape):
     def area(self):
        super().area()
        return self.a*self.h

tr1 = Triangle(int(input()) , int(input()))
print(tr1.area())