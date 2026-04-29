import math

class Point:
    
    def __init__(self, coordinates=(0, 0)):
        self.x = coordinates[0]
        self.y = coordinates[1]
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def sum(self, other):
        return Point((self.x + other.x, self.y + other.y))
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"