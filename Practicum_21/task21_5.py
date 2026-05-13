import turtle
import random


class Molecule:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.size = random.randint(5, 12)
        self.color = random.choice(["red", "blue", "green", "orange", "purple"])

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def bounce(self, width, height):
        if self.x > width or self.x < -width:
            self.vx *= -1
        if self.y > height or self.y < -height:
            self.vy *= -1

    def draw(self, pen):
        pen.penup()
        pen.goto(self.x, self.y)
        pen.pendown()
        pen.dot(self.size, self.color)

screen = turtle.Screen()
screen.setup(700, 700)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

molecules = [Molecule(random.randint(-200, 200),
                      random.randint(-200, 200))
             for _ in range(15)]

WIDTH, HEIGHT = 300, 300

while True:
    pen.clear()

    for m in molecules:
        m.move()
        m.bounce(WIDTH, HEIGHT)
        m.draw(pen)

    screen.update()