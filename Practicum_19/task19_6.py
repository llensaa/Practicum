import math

class Point:
    """Класс, представляющий точку на плоскости."""
    
    def __init__(self, coordinates=(0, 0)):
        """
        Инициализация точки.
        
        Параметры:
        coordinates - кортеж (x, y), по умолчанию (0, 0)
        """
        self.x = coordinates[0]
        self.y = coordinates[1]
    
    def get_x(self):
        """Возвращает координату x."""
        return self.x
    
    def get_y(self):
        """Возвращает координату y."""
        return self.y
    
    def distance(self, other):
        """
        Вычисляет расстояние до другой точки.
        
        Параметры:
        other - другая точка (объект Point)
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def sum(self, other):
        """
        Возвращает новую точку - сумму текущей и другой точки.
        
        Параметры:
        other - другая точка (объект Point)
        """
        return Point((self.x + other.x, self.y + other.y))
    
    def __str__(self):
        """Строковое представление точки."""
        return f"Point({self.x}, {self.y})"
