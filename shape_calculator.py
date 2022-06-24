import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*(self.width+self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** .5

    def get_picture(self):
        blank = ''
        picture = ''
        if self.width <= 50 and self.height <= 50:
            for i in range(self.height):
                picture += f'{blank:*^{self.width}}\n'
        else:
            picture = 'Too big for picture.'
        return picture

    def get_amount_inside(self, arg):
        return math.floor(self.get_area() / arg.get_area())

    def __repr__(self):
        output = f'{self.__class__.__name__}(width={self.width}, height={self.height})'
        return output

class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)

    def __repr__(self):
        output = f'{self.__class__.__name__}(side={self.width})'
        return output

