from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, perimeter=0, area=0):
        self.__perimeter = perimeter
        self.__area = area

    def get_perimeter(self):
        return self.__perimeter

    def get_area(self):
        return self.__area

    def set_perimeter(self, perimeter):
        self.__length = perimeter

    def set_area(self, area):
        self.__width = area

    @abstractmethod
    def calculate_perimeter(self): pass

    @abstractmethod
    def calculate_area(self): pass