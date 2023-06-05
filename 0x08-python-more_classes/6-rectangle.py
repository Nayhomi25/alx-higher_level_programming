#!/usr/bin/python3
""" A class definition """


class Rectangle:
    """ Defines a class Rectangle
        Args:
            private instance attribute Width
            private instance attribute Height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ instantiation with width and height """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def height(self):
        """retrieves the attribute width"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """The propery of height as the breadth of Rectancle
        Raises:
            TypeError: if height != int
            ValueError: height < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        """retrieves the attribute width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """The propery of width as the lenght of Rectancle
        Raises:
            TypeError: if width != int
            ValueError: width < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def area(self):
        """Get the area of a Rectangle
        Returns: Width * height
        """

        return self.__width * self.__height

    def perimeter(self):
        """Get the perimeter of a Rectangle
        Returns: (width + height) * 2
        """

        pm = (self.__width + self.__height) * 2

        if self.__height == 0 or self.__width == 0:
            pm = 0

        return(pm)

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for x in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if x != self.__height - 1:
                rec.append("\n")
        return("".join(rec))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """ Prints a message after every deletion of an instance """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
