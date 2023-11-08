#!/usr/bin/python3

"""Square class Module"""

# Import the Rectangle class from the "9-rectangle" module
Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """Square class

    This class represents a square, which is a specific type of rectangle
    where all four sides are of equal length.

    Attributes:
        __size (int): The size of the square's sides.

    Methods:
        __init__(self, size): Initializes a square with the specified size.
        area(self): Calculates and returns the area of the square.
        __str__(self): Returns a string representation of the square.

    Inherits from:
        Rectangle: The Square class inherits attributes and methods from
        the Rectangle class.

    """

    def __init__(self, size):
        """Initialize a square with the given size.

        Args:
            size (int): The size of the square's sides.

        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: A string in the format "[Square] {size/size}".

        """
        return "[Square] {}/{}".format(self.__size, self.__size)

