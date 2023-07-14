import turtle

wn = turtle.Screen()
wn.title("Pingy-Pongy")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)
color_list = ["yellow", "green", "orange"]

pad_1_color_index =0
pad_2_color_index = 0
score_1 = 0
score_2 = 0
score_1_limit = 1
score_2_limit = 1

pad_1 = turtle.Turtle()
pad_1.speed(0)
pad_1.shape("square")
pad_1.color("magenta")
pad_1.shapesize(stretch_wid=5,stretch_len=1)
pad_1.penup()
pad_1.goto(-350,0)

pad_2 = turtle.Turtle()
pad_2.speed(0)
pad_2.shape("square")
pad_2.color("magenta")
pad_2.shapesize(stretch_wid=5,stretch_len=1)
pad_2.penup()
pad_2.goto(+350,0)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("triangle")
ball.color("pink")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25
ball.dy = -0.25

pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.hideturtle()
pen.goto(0,260)
pen.write("Lefty :0 Righty: 0", align="center",font=("Arial",16,"normal "))

def pad_1_up():
    y = pad_1.ycor()
    y +=20
    pad_1.sety(y)

def pad_1_down():
    y = pad_1.ycor()
    y -=20
    pad_1.sety(y)

def pad_2_up():
    y = pad_2.ycor()
    y +=20
    pad_2.sety(y)

def pad_2_down():
    y = pad_2.ycor()
    y -=20
    pad_2.sety(y)


wn.listen()
wn.onkeypress(pad_1_up, "w")
wn.onkeypress(pad_1_down, "s")
wn.onkeypress(pad_2_up, "Up")
wn.onkeypress(pad_2_down, "Down")


while True:
    wn.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        score_1 +=1
        pen.clear()
        pen.write("Lefty :{} Righty: {}".format(score_1,score_2), align="center",font=("Arial",16,"normal "))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Lefty :{} Righty: {}".format(score_1,score_2), align="center",font=("Arial",16,"normal "))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_2.ycor() + 40 and ball.ycor() > pad_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        pad_2_color_index = (pad_2_color_index + 1) % len(color_list)  # Increment color index
        pad_2.color(color_list[pad_2_color_index])
    
    if (ball.xcor() < -340 and ball.xcor() > - 350) and (ball.ycor() < pad_1.ycor() + 40 and ball.ycor() > pad_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        pad_1_color_index = (pad_1_color_index + 1) % len(color_list)  # Increment color index
        pad_1.color(color_list[pad_1_color_index])

    if score_1 == score_1_limit or score_2 == score_2_limit:
        wn.bgcolor("gray")
        ball.dx = 0
        ball.dy = 0
        ball.goto(0,0)
        winner = " "
        if score_1 == score_1_limit:
            winner = "Lefty"
        else:
            winner = "Righty"
        pad_1.hideturtle()
        pad_2.hideturtle()
        ball.hideturtle()
        pen.hideturtle()
        pen.color("black")
        pen.goto(0,0)
        pen.write("Game Over\n{}wins!".format(winner),align = "center",font = ("Arial",16,"bold"))