""" freeCodeCamp polygon area calculator project
for the Scientific Computing with Python Certification.
This program will take inputs and display square
and rectangle models with '*' characters
ref: """


class Rectangle:
    """Superclass of Square"""

    def __init__(self, width, height):
        """Create width, height variables for Rectangle objects"""
        self.width = width
        self.height = height

    def __str__(self):
        """String representation of superclass or subclass instance"""
        if type(self).__name__ == "Square":
            return f"Square(side={self.width})"
        else:
            return f"{type(self).__name__}(width={self.width}, height={self.height})"

    # Setters
    def set_width(self, num):
        """Setter assigns arg value num to width"""
        self.width = num

    def set_height(self, num):
        """Setter assigns arg value num to height"""
        self.height = num

    # Getters
    def get_area(self):
        """Getter returns Rectangle object's area"""
        return self.width * self.height

    def get_perimeter(self):
        """Getter returns Rectangle object's perimeter"""
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """Gettter returns Rectangle object's diagonal length"""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """Getter returns picture of rectangel using '*' chars"""
        if self.width <= 50 and self.height <= 50:
            return "\n".join(("*" * self.width) for row in range(self.height)) + "\n"
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        """Arg: shape as object of Rectangle or Square
        Returns: number of times shape arg fits inside shape
        object being operated on (with no rotations)
        """
        return self.get_area() // shape.get_area()


class Square(Rectangle):
    """Subclass of Rectangle"""

    def __init__(self, side):
        """Instantiates Square object using super()
        to call Rectangle's constructor and store
        side length in Rectangle's height, width vars"""
        super().__init__(side, side)

    # Setters
    def set_side(self, side):
        """Store Square object side length
        in Rectangle's width, height variables"""
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width):
        """Store Square object side length
        in Rectangle's width, height variables"""
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height):
        """Store Square object side length
        in Rectangle's width, height variables"""
        super().set_width(height)
        super().set_height(height)
