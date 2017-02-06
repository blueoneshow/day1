import turtle

def draw_square(t,size):
    for i in range(4):
            t.forward(size)
            t.left(90)
    
window = turtle.Screen()
john = turtle.Turtle()

john.pensize(3)


for i in range (5):
    draw_square(john,50)
    john.penup()
    john.forward(45)
    john.pendown()

window.exitonclick()

