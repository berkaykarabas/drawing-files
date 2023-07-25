import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle Python")
turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
def shrinkingSquare(size):

    for i in range(4):
        turtle_instance.left(90)
        turtle_instance.forward(size)
        size = size - 5
shrinkingSquare(200)
shrinkingSquare(180)
shrinkingSquare(160)
shrinkingSquare(140)
shrinkingSquare(120)
shrinkingSquare(100)
shrinkingSquare(80)
shrinkingSquare(60)
shrinkingSquare(40)
shrinkingSquare(20)
shrinkingSquare(10)

turtle.done()