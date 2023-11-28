import turtle
import time
from random import randint

drawing_board = turtle.Screen()
drawing_board.title("Catch The Turtle!")
drawing_board.bgcolor("#BFFDC1")

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")


def mouse_click_x(x, y):
    turtle.onscreenclick(mouse_click_x)
    return x


def mouse_click_y(x, y):
    turtle.onscreenclick(mouse_click_y)
    return y


def mouse_click_2(x, y):
    print(x, y)
    print(f"Turtle position: {turtle_instance.pos()}")


turtle_score = turtle.Turtle()
turtle_score.ht()
turtle_score.penup()
turtle_score.setpos(0, 280)
score = 0
turtle_score.write(f"Score:{score} ", align="center", font=("Arial", 20, "normal"))


def click_on_turtle(x, y):
    global score
    for i in range(int(turtle_instance.xcor() - 8), int(turtle_instance.xcor() + 17)):
        if i == x:
            for j in range(int(turtle_instance.ycor() - 10), int(turtle_instance.ycor() + 10)):
                if j == y:
                    score = score + 1
                    turtle_score.clear()
                    turtle_score.write(f"Score:{score} ", align="center", font=("Arial", 20, "normal"))


turtle.onscreenclick(click_on_turtle)

turtle_time = turtle.Turtle()
turtle_time.ht()
turtle_time.penup()
turtle_time.setpos(0, 250)

turtle_instance.penup()
turtle_instance.speed(0)
for t in range(30, 0, -1):
    turtle_time.clear()
    turtle_time.write(f"Timer:{t} ", align="center", font=("Arial", 20, "normal"))
    turtle_instance.ht()
    turtle_instance.setx(randint(-300, 300))
    turtle_instance.sety(randint(-300, 250))
    turtle_instance.st()
    time.sleep(1)

turtle_instance.ht()
turtle_time.clear()
turtle_time.write("Time is up! ", align="center", font=("Arial", 20, "normal"))
turtle.done()
