import math

class Point:
    """Класс, представляющий точку на плоскости."""
    
    def __init__(self, coordinates=(0, 0)):
        self.x = coordinates[0]
        self.y = coordinates[1]
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Segment:
    """Класс, представляющий отрезок на плоскости."""
    
    def __init__(self, point1, point2):
        """
        Инициализация отрезка двумя точками.
        
        Параметры:
        point1, point2 - объекты Point
        """
        self.point1 = point1
        self.point2 = point2
        self.one_intersection = self._check_one_axis_intersection()
    
    def _check_one_axis_intersection(self):
        """
        Проверяет, пересекает ли отрезок только одну ось координат.
        """
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y
        
        cross_x = False
        if y1 * y2 < 0:
            cross_x = True

        cross_y = False
        if x1 * x2 < 0:
            cross_y = True

        return cross_x != cross_y
    
    def __str__(self):
        return f"Segment({self.point1}, {self.point2})"


class СoordinateSystem:
    """Класс, представляющий систему координат с отрезками."""
    
    def __init__(self):
        """Инициализация пустой плоскости."""
        self.segments = []
    
    def add_segment(self, segment):
        """
        Добавляет отрезок на плоскость.
        
        Параметры:
        segment - объект Segment
        """
        self.segments.append(segment)
    
    def axis_intersection(self):
        """
        Возвращает количество отрезков, пересекающих только одну ось.
        """
        count = 0
        for segment in self.segments:
            if segment.one_intersection:
                count += 1
        return count
    
    def __str__(self):
        return f"CoordinateSystem with {len(self.segments)} segments"
