class Rectangle:
    def __init__(self, width, height):  # Constructor for the parent class
        self.width = width
        self.height = height

    def __str__(self):  
        return f'Rectangle(width={self.width}, height={self.height})' # returns the w and h in a str format

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**0.5) # diagonal = sqrt(width^2 + height ^2)

    def get_picture(self):
        if (self.width > 50 or self.height > 50):
            return "Too big for picture."
        string = (("*" * self.width) + "\n") * self.height  # uses '*' to print width by number of height times
        return string

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())


class Square(Rectangle):            #Subclass that inherits the props of the Rectangke (parent)
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})' 

    def set_side(self, side):
        self.width = side
        self.height = side