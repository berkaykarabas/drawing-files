import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Python Turtle2")
turtle_instance = turtle.Turtle()
turtle_instance.color("green")
turtle_colors = ["red", "yellow","blue","green","orange","yellow"]
for i in range(6):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.left(i)
    turtle_instance.circle(-10*i)

    turtle_instance.right(i)
turtle.done()