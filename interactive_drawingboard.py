import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Drawing Board")

turtle_instance = turtle.Turtle()
def turtle_foward():
    turtle_instance.forward(100)
def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading()-10)
def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading()+10)
def clear_screen():
    turtle_instance.clear()
def goback_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_foward,key="space")
drawing_board.onkey(fun=rotate_angle_left,key="Up")
drawing_board.onkey(fun=rotate_angle_right,key="Down")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=goback_home,key="h")
turtle.mainloop()