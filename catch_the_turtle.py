import time
import turtle
import random
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle")
FONT = ('Arial', 30, 'normal')
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score = 1
score_turtle.penup()
score_turtle.setposition(0, 250)
#score_turtle.write(arg="Your score is :",move=False,align="center",font=("bold",18))
turtle_interihance = turtle.Turtle("turtle")
#time_turtle.write(arg="Time is :".format(time),move=False,align="center",font=("bold",18))
def turtle_random():
    def handle_click(x, y):
        global score
        score += 1
        score_turtle.write(arg=f"Your score is :{score}", move=False, align="center", font=FONT)
    turtle_interihance.onclick(fun=handle_click,btn=1)

    i=0
    while i <= 50:
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        turtle_interihance.ht
        turtle_interihance.setheading(random_x)
        turtle_interihance.penup()
        turtle_interihance.setposition(random_x,random_y)
        time.sleep(0.02)
        i+=1
def countdown(time):
    turtle_time = turtle.Turtle()
    turtle_time.penup()
    turtle_time.setposition(0, 275)
    turtle_time.hideturtle()
    turtle_time.ht
    turtle_time.clear()
    if time > 0:

        turtle_time.write(arg=f"Time:{time}", align='center', font=FONT)
        turtle_screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        turtle_screen.clear()
        turtle_time.write("Game Over", align='center', font=FONT)
        turtle_screen.onclick(lambda x, y: countdown(30))
countdown(9),turtle_random()


turtle.mainloop()