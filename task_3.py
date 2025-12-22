class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        area =  self.height * self.width
        return area
    
    def perimeter(self):
        perimeter = 2 * self.height + self.width
        return perimeter
    
    def is_square(self):
        if self.height == self.width:
            return 'Это не квадрат'
        return 'Это квадрат'
    
    def rotate(self):
        self.width = self.height
        self.height = self.width
    
    
    