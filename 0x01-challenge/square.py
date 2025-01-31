#!/usr/bin/python3
""" Square module """


class Square():
    """ Square class """

    def __init__(self, *args, **kwargs):
        """ Initialization of the square class """
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def area(self):
        """ Area of the square """
        return (self.width * self.height)

    def perimeter(self):
        """ Perimeter of the square """
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """ String representation """
        return ("{}/{}".format(self.width, self.height))


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.perimeter())
