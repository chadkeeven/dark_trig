import turtle

window = turtle.Screen()
window.bgcolor("red")

brad = turtle.Turtle()
brad.speed(4)
brad.shape("turtle")

angie = turtle.Turtle()
angie.speed(1)

sally = turtle.Turtle()
sally.speed(0)

def draw_square(name):
        sides = 0
        shape = 4
        while sides < shape:
            name.forward(100)
            name.right(90)
            sides += 1


def draw_circle_with_squares(name):
    count = 0
    angle_interval = 10
    while count < 360:
        draw_square(name)
        name.right(angle_interval) 
        count = count + angle_interval   

def draw_circle(name):
    name.shape("turtle")
    name.color("blue")
    name.circle(50)

def draw_triangle(name):
    name.shape("arrow")
    name.color("yellow")
    
    name.forward(75)
    name.right(120)
    name.forward(150)
    name.right(120)
    name.forward(150)
    name.right(120)
    name.forward(75)

def flower(name):
    count = 0
    angle_interval = 5
    while count < 360:
        draw_triangle(name)
        name.right(angle_interval) 
        count = count + angle_interval
    name.right(90)
    name.forward(300)

def upward_tri(name):
    name.left(180)
    name.forward(75)
    name.right(120)
    name.forward(150)
    name.right(120)
    name.forward(150)
    name.right(120)
    name.forward(75)
    name.right(60)
    name.forward(75)
    name.right(120)
    name.forward(75)
    name.right(120)
    name.forward(75)
    name.right(120)
    name.forward(37.5)
    name.left(60)
    name.forward(37.5)
    name.left(120)
    name.forward(37.5)
    name.left(120)
    name.forward(37.5)
    name.left(60)
    name.forward(37.5)
    name.right(120)
    name.forward(37.5)
    name.left(120)
    name.forward(37.5)
    name.right(120)
    name.forward(37.5)
    name.right(120)
    name.forward(37.5)
    name.left(120)
    name.forward(37.5)
    name.right(120)
    name.forward(37.5)
    name.left(120)
    name.forward(37.5)
    name.right(120)
    name.forward(37.5)
    name.right(120)
    name.forward(37.5)



    
#draw_circle_with_squares(brad)
#draw_square(brad)
#draw_circle(angie)
#draw_triangle(sally)
#flower(sally)
upward_tri(brad)

window.exitonclick()
