from Shape import Shape

class Rectangle(Shape):
    def __init__(self, length=0, width=0):
        self.__length = length
        self.__width = width

        super().__init__(self.calculate_perimeter(), self.calculate_area())

    def get_length(self): return self.__length

    def get_width(self): return self.__width

    def calculate_area(self):
        area = self.get_length() * self.get_width()
        return area

    def calculate_perimeter(self):
        perimeter = self.get_length() * 2 + self.get_width() * 2
        return perimeter
