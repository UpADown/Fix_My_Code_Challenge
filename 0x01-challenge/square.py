#!/usr/bin/env python3
class square(object):
    """A class that represents a square with width and height attributes.

    Attributes:
        width (int): The width of the square.
        height (int): The height of the square.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the square with default or given width and height values.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.width = 0
        self.height = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Calculate and return the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: A string in the format "width/height".
        """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())

