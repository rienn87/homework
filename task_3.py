class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        return (self.height * self.width)
    
    def perimeter(self):
        return 2*(self.height + self.width)
    
    def is_square(self):
        return True if (self.height == self.width) else False 
    
    def rotate(self):
        temp = self.width
        self.width = self.height
        self.height = temp
    

a = Rectangle(11, 10)
print(f"это квадрат? - {a.is_square()}")
print(f"площадь: {a.area()}")
print(f"периметр: {a.perimeter()}")