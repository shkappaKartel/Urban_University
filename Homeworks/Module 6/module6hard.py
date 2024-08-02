
class Figure:

    class Circle:
        def __init__(self, color, *sides):
            self.__sides = []
            self.__color = color
            self.filled = False
            self.sides.count = 0

            self.set_sides(*sides)

        def get_color(self):
            return self.__color

        def is_valid_color(self, r, g, b):
            return all(0 <= value <= 255 for value in [r, g, b])

        def set_color(self, r, g, b):
            if self.is_valid_color(r, g ,b):
                self.__color = (r, g, b)

        def __is_valid_sides(self, __sides):
