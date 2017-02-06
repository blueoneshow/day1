import turtle

def draw_multicolor_square(t, sz):
        for i in ["red", "purple", "hotpink", "red"]:
                t.color(i)
                t.forward(sz)
                t.left(90)
                t.speed(10)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

john = turtle.Turtle()
john.pensize(3)

size = 100
for i in range(24):
        draw_multicolor_square(john, size)
        john.right(15)
        

window.exitonclick()
