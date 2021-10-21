# Classes Example

# Create some classes and projects

class Shape:
    """Represents a 2-dimensional polygon

    Attributes:
        num_sides: An integer count of the sides
        side_length: A float of side length
    """

    def __init__(self):
        """Creates a new shape with default value"""
        self.num_sides = 4
        self.side_length = 10.0

    def area(self) -> float:
        """Return the area of a square."""
        return self.side_length ** 2

    def perimeter(self) -> float:
        """return the perimeter of a square"""
        return self.num_sides * self.side_length


some_shape = Shape()
print(some_shape.num_sides)
print(some_shape.perimeter())
