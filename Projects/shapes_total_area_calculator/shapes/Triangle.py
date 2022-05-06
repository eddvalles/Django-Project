from Shape import Shape
from math import sqrt

class Triangle(Shape):
    def __init__(self, a=0, b=0, c=0):
        self.__a = a
        self.__b = b
        self.__c = c

        super().__init__(self.calculate_perimeter(), self.calculate_area())

    def get_side_a(self): return self.__a

    def get_side_b(self): return self.__b

    def get_side_c(self): return self.__c

    def calculate_area(self):
        semiperimeter = (self.get_side_a() + self.get_side_b() + self.get_side_c()) / 2
        area = sqrt(semiperimeter * (semiperimeter - self.get_side_a())) * (semiperimeter - self.get_side_b()) * \
               (semiperimeter - self.get_side_c())
        return area

    def calculate_perimeter(self):
        perimeter = self.get_side_a() + self.get_side_b() + self.get_side_c()
        return perimeter

c = Triangle()