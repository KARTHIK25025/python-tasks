class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        area = self.length * self.width
        print(f"The area of the rectangle ({self.length}x{self.width}) is: {area}")
rect = Rectangle(10, 5)
rect.calculate_area()
