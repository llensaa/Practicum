import math


class GeometricObject:
    def __init__(self, x=0.0, y=0.0, color='black', filled=False):
        self._x = float(x)
        self._y = float(y)
        self.color = color
        self.filled = filled

    def set_coordinate(self, x, y):
        self._x = float(x)
        self._y = float(y)

    def set_color(self, color):
        self.color = color

    def set_filled(self, filled):
        self.filled = filled

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_color(self):
        return self.color

    def is_filled(self):
        return self.filled

    def __str__(self):
        filled_str = "filled" if self.filled else "no filled"
        return f"({self._x}, {self._y}) {self.color} {filled_str}"

    def __repr__(self):
        filled_str = "filled" if self.filled else "no filled"
        return f"({self._x}, {self._y}) {self.color} {filled_str}"


class Rectangle(GeometricObject):
    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0,
                 color='black', filled=False):
        super().__init__(x, y, color, filled)
        self.width = float(width)
        self.height = float(height)

    def set_width(self, width):
        if width > 0:
            self.width = float(width)
        else:
            self.width = 0.0

    def set_height(self, height):
        if height > 0:
            self.height = float(height)
        else:
            self.height = 0.0

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        filled_str = "filled" if self.filled else "no filled"
        return (f"width: {self.width}\nheight: {self.height}\n"
                f"({self._x}, {self._y})\ncolor: {self.color}\n"
                f"filled: {filled_str}")

    def __repr__(self):
        filled_str = "filled" if self.filled else "no filled"
        return (f"width: {self.width} height: {self.height} "
                f"({self._x}, {self._y}) {self.color} {filled_str}")


class Circle(GeometricObject):
    def __init__(self, x=0.0, y=0.0, radius=0.0, color='black', filled=False):
        super().__init__(x, y, color, filled)
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = float(value)
        else:
            self._radius = 0.0

    def get_area(self):
        return math.pi * self._radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self._radius

    def get_diameter(self):
        return 2 * self._radius

    def __str__(self):
        filled_str = "filled" if self.filled else "no filled"
        return (f"radius: {self._radius}\n({self._x}, {self._y})\n"
                f"color: {self.color}\nfilled: {filled_str}")

    def __repr__(self):
        filled_str = "filled" if self.filled else "no filled"
        return (f"radius: {self._radius} ({self._x}, {self._y}) "
                f"{self.color} {filled_str}")