import math

class Point:
    
    def __init__(self, coordinates=(0, 0)):
        self.x = coordinates[0]
        self.y = coordinates[1]
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Segment:
    
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.one_intersection = self._check_one_axis_intersection()
    
    def _check_one_axis_intersection(self):
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
    
    def __init__(self):
        self.segments = []
    
    def add_segment(self, segment):
        self.segments.append(segment)
    
    def axis_intersection(self):
        count = 0
        for segment in self.segments:
            if segment.one_intersection:
                count += 1
        return count
    
    def __str__(self):
        return f"CoordinateSystem with {len(self.segments)} segments"