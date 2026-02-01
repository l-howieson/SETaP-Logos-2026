import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("purple")

def filled_rectangle(w, h, outline, fill):
    t.color(outline, fill)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

# Green rectangles
t.penup(); t.goto(-400, -200); t.pendown(); filled_rectangle(60, 160, "black", "#1E7F43")
t.penup(); t.goto(-340, -200); t.pendown(); filled_rectangle(60, 200, "black", "#58D68D")
t.penup(); t.goto(-280, -200); t.pendown(); filled_rectangle(60, 260, "black", "#1E7F43")
t.penup(); t.goto(-220, -200); t.pendown(); filled_rectangle(60, 320, "black", "#58D68D")
t.penup(); t.goto(-160, -200); t.pendown(); filled_rectangle(60, 380, "black", "#1E7F43")
t.penup(); t.goto(-100, -200); t.pendown(); filled_rectangle(60, 440, "black", "#58D68D")
t.penup(); t.goto(-40,  -200); t.pendown(); filled_rectangle(60, 360, "black", "#1E7F43")
t.penup(); t.goto(20,   -200); t.pendown(); filled_rectangle(60, 300, "black", "#58D68D")
t.penup(); t.goto(80,   -200); t.pendown(); filled_rectangle(60, 240, "black", "#1E7F43")
t.penup(); t.goto(140,  -200); t.pendown(); filled_rectangle(60, 190, "black", "#58D68D")
t.penup(); t.goto(200,  -200); t.pendown(); filled_rectangle(60, 140, "black", "#1E7F43")

# White circle
t.pensize(8)
t.pencolor("white")
t.penup()
t.goto(-70, -30)
t.pendown()
t.circle(50)

# Arrows
t.pensize(8)
t.pencolor("black")

t.penup()
t.goto(-360, -10)
t.pendown()
t.goto(-190, 160)

t.penup()
t.goto(-190, 160)
t.pendown()
t.goto(-215, 155)

t.penup()
t.goto(-190, 160)
t.pendown()
t.goto(-185, 130)

t.penup()
t.goto(80, 160)
t.pendown()
t.goto(250, 40)

t.penup()
t.goto(250, 40)
t.pendown()
t.goto(233, 64)

t.penup()
t.goto(250, 40)
t.pendown()
t.goto(221, 48)

# White rectangle border
t.pensize(8)
t.pencolor("white")
t.penup()
t.goto(-400, -200)
t.pendown()
t.goto(260, -200)
t.goto(260, 240)
t.goto(-400, 240)
t.goto(-400, -200)

turtle.done()
