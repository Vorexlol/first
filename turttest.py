import turtle as trt
import os
import random

colors = {
    1 : 'red',
    2 : 'orange',
    3 : 'yellow',
    4 : 'green',
    5 : "blue"
}



wn =trt.Screen()
wn.title =('tester')
wn.setup(width=1250,height=1250)
wn.bgcolor('light grey')
wn.tracer(0)

pen = trt.Turtle()
pen.speed(1)
pen.shape('square')
pen.color('black')
pen.penup()
pen.goto(0,500)
pen.hideturtle()

ball = trt.Turtle()
ball.speed(1)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx =1
ball.dy =1.1
ball.hideturtle()

def move_up():
    y = ball.ycor()
    y += 20
    ball.sety(y)
    
def move_down():
    y = ball.ycor()
    y -= 20
    ball.sety(y)
    
def move_right():
    y = ball.xcor()
    y += 20
    ball.setx(y)
    
def move_left():
    y = ball.xcor()
    y -= 20
    ball.setx(y)
    
def color_rand():
    rng = random.randint(1,5)
    return colors[rng]

wn.listen()
wn.onkeypress(move_up,'w')
wn.onkeypress(move_down,'s')
wn.onkeypress(move_right,'d')
wn.onkeypress(move_left,'a')
i= 0
r=0
c=0
while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    ball.pd()
    
    if ball.ycor() > 600:
        ball.sety(600)
        ball.dy *= -1
   
    if ball.ycor() < -600:
        ball.sety(-600)
        ball.dy *= -1
     
    if ball.xcor() > 600:
        ball.setx(600)
        ball.dx *= -1
  
    if ball.xcor() < -600:
        ball.setx(-600)
        ball.dx *= -1
      
    if i >= 50000:
        ball.clear()
        ball.pendown()
        i=0
        r += 1
        pen.clear()
        pen.write(f'resets : {r}',align='center')
    else:
        i += 1
    
    if c >= 20:
        ball.color(color_rand())
        c = 0
    else:
        c +=1