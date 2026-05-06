class Circle:
    pi = 3.1415
    all_circles = []

    def __init__(self, radius=1):
        self.radius = radius
        Circle.all_circles.append(self)

    def area(self):
        return Circle.pi * self.radius ** 2

    @staticmethod
    def total_area():
        total = 0
        for circle in Circle.all_circles:
            total += circle.area()
        return total

    def __repr__(self):
        return f"Circle (radius={self.radius})"