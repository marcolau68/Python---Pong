# Pong

import turtle
import random
import time

# Screen
board = turtle.Screen()
board.title('Pong')
board.bgcolor('black')
board.setup(width=800, height=600)

# Player1
player1 = turtle.Turtle()
player1.hideturtle()
player1.color('white')
player1.shape('square')
player1.shapesize(stretch_wid=1, stretch_len=5)
player1.setheading(90)
player1.speed(0)
player1.penup()
player1.goto(380, 0)
player1.showturtle()


def player1_up():
    player1.setheading(90)
    player1.forward(25)


def player1_down():
    player1.setheading(270)
    player1.forward(25)


turtle.listen()
turtle.onkey(player1_up, 'Up')
turtle.onkey(player1_down, 'Down')

# Player2
player2 = turtle.Turtle()
player2.hideturtle()
player2.color('white')
player2.shape('square')
player2.shapesize(stretch_wid=1, stretch_len=5)
player2.setheading(90)
player2.speed(0)
player2.penup()
player2.goto(-390, 0)
player2.showturtle()


def player2_up():
    player2.setheading(90)
    player2.forward(25)


def player2_down():
    player2.setheading(270)
    player2.forward(25)


turtle.listen()
turtle.onkey(player2_up, 'w')
turtle.onkey(player2_down, 's')

# ball
ball = turtle.Turtle()
ball.penup()
ball.color('red')
ball.shape('circle')
ball.goto(0, 0)
ball.speed(0)

initial_angle = 30
angle = initial_angle
ball.setheading(angle)


# ball movement

def ball_player_distance():
    global angle

    if abs(player1.xcor() - ball.xcor()) < 20 and abs(player1.ycor() - ball.ycor()) < 60:
        angle = 540 - int(angle)
        ball.setheading(angle)
    elif abs(player2.xcor() - ball.xcor()) < 20 and abs(player2.ycor() - ball.ycor()) < 60:
        angle = 540 - int(angle)
        ball.setheading(angle)
    elif ball.ycor() >= 290:
        angle = 360 - angle
        ball.setheading(angle)
    elif ball.ycor() <= -290:
        angle = 360 - angle
        ball.setheading(angle)


# Score
player1_score = 0
player2_score = 0

scoreboard = turtle.Turtle()
scoreboard.color('white')
scoreboard.penup()
scoreboard.speed(0)
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write('Player 1: 0   Player 2: 0', align='center', font=('Courier', 24, 'normal'))

# Mainloop


while True:
    ball.forward(4)
    ball_player_distance()

    if ball.xcor() >= 400:
        ball.hideturtle()
        player1_score += 1
        scoreboard.clear()
        scoreboard.write('Player 1: %s    Player 2: %s' % (player1_score, player2_score), align='center',
                         font=('Courier', 24, 'normal'))
        ball.goto(0, 0)
        ball.showturtle()
        time.sleep(1)
        angle = random.randint(290, 430)
        ball.setheading(angle)

    elif ball.xcor() <= -400:
        ball.hideturtle()
        player2_score += 1
        scoreboard.clear()
        scoreboard.write('Player 1: %s    Player 2: %s' % (player1_score, player2_score), align='center',
                         font=('Courier', 24, 'normal'))
        ball.goto(0, 0)
        ball.showturtle()
        time.sleep(1)
        angle = random.randint(200, 250)
        ball.setheading(angle)

turtle.mainloop()
