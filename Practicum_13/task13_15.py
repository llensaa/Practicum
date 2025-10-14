import turtle
import random

screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("#DDD")
screen.setup(width = 800, height = 600)

builder = turtle.Turtle()
builder.hideturtle()
builder.speed(0)

star_turtle = turtle.Turtle()
star_turtle.hideturtle()
star_turtle.speed(0)
star_turtle.penup()

moon_turtle = turtle.Turtle()
moon_turtle.hideturtle()
moon_turtle.speed(0)
moon_turtle.penup()

def draw_building(x, width, height, color):
    builder.penup()
    builder.goto(x, -300)
    builder.pendown()
    builder.pencolor(color)
    builder.fillcolor(color)
    builder.begin_fill()
    for _ in range(2):
        builder.forward(width)
        builder.left(90)
        builder.forward(height)
        builder.left(90)
    builder.end_fill()
    draw_windows(x, width, height)

def draw_windows(x, width, height):
    min_win_w, max_win_w = 5, 8
    min_win_h, max_win_h = 10, 14

    cols = int(width // (max_win_w + 4))
    rows = int(height // (max_win_h + 6))

    left = x
    bottom = -300

    for row in range(rows):
        for col in range(cols):
            if random.random() < 0.5:
                wx = left + col * (width / cols)
                wy = bottom + row * (height / rows)
                cell_w = width / cols
                cell_h = height / rows
                win_w = min(random.randint(min_win_w, max_win_w), cell_w - 2)
                win_h = min(random.randint(min_win_h, max_win_h), cell_h - 2)

                shift_x = (cell_w - win_w) / 2
                shift_y = (cell_h - win_h) / 2

                builder.penup()
                builder.goto(wx + shift_x, wy + shift_y)
                builder.pendown()
                builder.fillcolor("#FFD700")
                builder.begin_fill()
                for _ in range(2):
                    builder.forward(win_w)
                    builder.left(90)
                    builder.forward(win_h)
                    builder.left(90)
                builder.end_fill()


def draw_star(x, y, size):
    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()
    star_turtle.fillcolor("white")
    star_turtle.begin_fill()
    star_turtle.circle(size)
    star_turtle.end_fill()
    star_turtle.penup()

def draw_starry_sky(count):
    for _ in range(count):
        x = random.randint(-380, 380)
        y = random.randint(50, 290)
        size = random.randint(2, 4)
        draw_star(x, y, size)

def draw_moon():
    moon_turtle.penup()
    moon_turtle.goto(150, 200)
    moon_turtle.pendown()
    moon_turtle.pencolor("orange")
    moon_turtle.fillcolor("orange")
    moon_turtle.begin_fill()
    moon_turtle.circle(40)
    moon_turtle.end_fill()
    moon_turtle.penup()
    moon_turtle.goto(170, 210)
    moon_turtle.pendown()
    moon_turtle.pencolor("#DDD")
    moon_turtle.fillcolor("#DDD")
    moon_turtle.begin_fill()
    moon_turtle.circle(35)
    moon_turtle.end_fill()
    moon_turtle.penup()


def draw_cityscape():
    x = -400
    while x < 400:
        width = random.randint(40, 80)
        height = random.randint(320, 450)
        color = ("#26183b")
        draw_building(x, width, height, color)
        x += width - random.randint(0, 20)

    x = -400
    while x < 400:
        width = random.randint(40, 80)
        height = random.randint(200, 320)
        color = ("#392350")
        draw_building(x, width, height, color)
        x += width - random.randint(0, 20)

    x = -400
    while x < 400:
        width = random.randint(40, 80)
        height = random.randint(80, 200)
        color = ("#755d9a")
        draw_building(x, width, height, color)
        x += width - random.randint(0, 20)


draw_starry_sky(80)
draw_moon()
draw_cityscape()

turtle.done()
