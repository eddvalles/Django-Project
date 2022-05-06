from Shape import Shape
from math import (
    pi as PI
)

class Circle(Shape):
    def __init__(self, radius=0):
        self.__radius = radius
        super().__init__(self.calculate_perimeter(), self.calculate_area())

    def get_radius(self):
        return self.__radius

    def calculate_perimeter(self):
        circumference = 2 * PI * self.get_radius()
        return circumference

    def calculate_area(self):
        area = PI * self.get_radius() * self.get_radius()
        return area