import turtle
import random

screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("#F7F1D4")
screen.setup(width = 1000, height = 400)

element = turtle.Turtle()
element.hideturtle()
element.speed(0)
element.pencolor("#EFD95E")

element_2 = turtle.Turtle()
element_2.hideturtle()
element_2.speed(0)
element_2.pencolor("black")

back = turtle.Turtle()
back.hideturtle()
back.speed(0)
back.pencolor("#CB1A1A")

lantern = turtle.Turtle()
lantern.hideturtle()
lantern.speed(0)
lantern.pencolor("black")


def background(x, y):
    back.penup()
    back.goto(x, y)
    back.pendown()
    back.setheading(0)
    back.fillcolor("#CB1A1A")
    back.begin_fill()
    for _ in range(2):
        back.forward(1000)
        back.left(90)
        back.forward(120)
        back.left(90)
    back.end_fill()


def el_1(x, y):
    element.penup()
    element.goto(x, y)
    element.pendown()

    element.forward(40)
    element.left(90)
    element.forward(40)
    element.left(90)
    element.forward(20)
    element.left(90)
    element.forward(40)
    element.right(90)
    element.forward(20)
    element.right(90)
    element.forward(20)
    element.right(90)
    element.forward(40)


def chinese_el_1(x, y):
    el_1(x, y - 40)
    element.right(90)
    el_1(x + 60, y)
    element.right(90)
    el_1(x + 100, y - 60)
    element.right(90)
    el_1(x + 40, y - 100)

    element.penup()
    element.goto(x + 30, y - 30)
    element.pendown()
    element.setheading(0)
    for _ in range(4):
        element.forward(40)
        element.right(90)


def chinese_el_2(x,y):
    element_2.setheading(55)
    for _ in range(4):
        element_2.penup()
        element_2.goto(x, y)
        element_2.right(90)
        element_2.forward(10)
        element_2.pendown()
        element_2.circle(8)

    element_2.penup()
    element_2.goto(x, y + 6)
    element_2.pendown()
    element_2.fillcolor("#CB1A1A")
    element_2.begin_fill()
    element_2.setheading(315)
    for _ in range(4):
        element_2.forward(8)
        element_2.right(90)
    element_2.end_fill()

    turtle.update()


def draw_lantern(x, y):
    top_color = random.choice(["#FD5E25", "#2A9D8F", "#E9C46A", "#2A718D", "#E76F51"])
    body_color = random.choice(["#FF4444", "#2A9D8F", "#F4A261", "#1D3557", "#E63946"])
    decoration_color = random.choice(["#FFD700", "#D864E7", "#A8DADC", "#F4A261", "#B9F74C"])

    lantern.penup()
    lantern.goto(x, y + 30)
    lantern.setheading(90)
    lantern.pendown()
    lantern.forward(20)

    lantern.penup()
    lantern.goto(x + 5, y + 25)
    lantern.pendown()
    lantern.circle(5)

    lantern.penup()
    lantern.goto(x + 10, y + 10)
    lantern.setheading(90)
    lantern.pendown()
    lantern.circle(10, 180)
    
    lantern.penup()
    lantern.goto(x, y)
    lantern.pendown()
    lantern.fillcolor(top_color)
    lantern.begin_fill()
    lantern.goto(x + 25, y)
    lantern.goto(x + 10, y + 10)
    lantern.goto(x - 10, y + 10)
    lantern.goto(x - 25, y)
    lantern.goto(x, y)
    lantern.end_fill()

    lantern.penup()
    lantern.goto(x, y)
    lantern.pendown()
    lantern.fillcolor(body_color)
    lantern.begin_fill()
    lantern.goto(x + 25, y)
    lantern.goto(x + 15, y - 70)
    lantern.goto(x - 15, y - 70)
    lantern.goto(x - 25, y)
    lantern.goto(x, y)
    lantern.end_fill()

    lantern.penup()
    lantern.goto(x + 15, y)
    lantern.setheading(265)
    lantern.pendown()
    lantern.forward(70)

    lantern.penup()
    lantern.goto(x - 15, y)
    lantern.setheading(275)
    lantern.pendown()
    lantern.forward(70)

    lantern.penup()
    lantern.goto(x, y - 90)
    lantern.setheading(90)
    lantern.pendown()
    lantern.forward(20)

    lantern.penup()
    lantern.goto(x, y - 90)
    lantern.pendown()
    lantern.fillcolor(decoration_color)
    lantern.begin_fill()
    lantern.setheading(315)
    for _ in range(4):
        lantern.forward(10)
        lantern.right(90)
    lantern.end_fill()
        
    turtle.update()


background(-500, 80)
background(-500, -200)
x = -490
y = 190
for _ in range(1, 10):
    chinese_el_1(x, y)
    x += 110

x = -490
y = -90
for _ in range(1, 10):
    chinese_el_1(x, y)
    x += 110

x = -440
y = 30
for _ in range(1, 10):
    draw_lantern(x, y)
    x += 110

x = -500
y = 50
for _ in range(1, 11):
    chinese_el_2(x, y)
    element_2.penup()
    element_2.goto(x, y - 30)
    element_2.pendown()
    element_2.setheading(270)
    element_2.forward(40)
    x += 110

x = -500
y = -50
for _ in range(1, 11):
    chinese_el_2(x, y)
    x += 110


turtle.done()