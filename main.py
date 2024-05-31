"""
Documented using Cody

This is the main module of the Ping Pong game. It sets up the game screen, creates instances of the Paddle, Scoreboard, and Ball classes, and handles the game loop and scoring logic.

The game is played by two players, each controlling a paddle on the left and right sides of the screen. The objective is to hit the ball back and forth, trying to make the opponent miss the ball. When a player misses the ball, the opponent scores a point. The game continues until one player reaches a score of 10.

The game screen is set up using the turtle graphics library, and the keyboard input is handled to control the movement of the paddles. The ball's movement and collision detection with the paddles and walls are also handled in this module.

Functions:
    reset_score(): Resets the scores of both players to 0 and updates the scoreboard display.
    reset_all(): Resets the game by setting the ball, paddles, and scoreboard to their initial positions.

Usage:
    Run this module to start the Ping Pong game.
"""

from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from time import sleep as wait
from random import choice

scr = Screen()
scr.setup(width=1150, height=800)
scr.bgcolor("black")
scr.tracer(0)
scr.title("Ping Pong")

paddle_1 = Paddle()
paddle_2 = Paddle()
paddle_1.teleport(-565, 0)
paddle_2.teleport(555, 0)

ball = Ball()

main_board = Scoreboard()
scoreboard_1 = Scoreboard()
scoreboard_2 = Scoreboard()
score_1 = 0
score_2 = 0

scoreboard_1.set_text("0", -130, 300)
scoreboard_2.set_text("0", 120, 300)

scr.listen()
scr.onkeypress(paddle_1.go_up, "w")
scr.onkeyrelease(paddle_1.stop_up, "w")
scr.onkeypress(paddle_1.go_down, "s")
scr.onkeyrelease(paddle_1.stop_down, "s")
scr.onkeypress(paddle_1.go_up, "W")
scr.onkeyrelease(paddle_1.stop_up, "W")
scr.onkeypress(paddle_1.go_down, "S")
scr.onkeyrelease(paddle_1.stop_down, "S")

scr.onkeypress(paddle_2.go_up, "Up")
scr.onkeyrelease(paddle_2.stop_up, "Up")
scr.onkeypress(paddle_2.go_down, "Down")
scr.onkeyrelease(paddle_2.stop_down, "Down")

is_game = True

speed = 10

# 45 is top right
# 135 is top left
# 225 is bottom left
# 315 is bottom right

ball.turn_to(choice([45, 135, 225, 315]))


def reset_score():
    """
    Resets the scores of both players to 0 and updates the scoreboard display.

    Parameters:
    None

    Returns:
    None

    This function is called when the game needs to be reset, such as after a player wins. It sets the scores of both players to 0 and updates the scoreboard display accordingly.
    """
    global score_1
    global score_2

    score_1 = 0
    score_2 = 0
    scoreboard_1.set_text(score_1, -130, 300)
    scoreboard_2.set_text(score_2, 120, 300)


def reset_all():
    """
    Resets the game by setting the ball, paddles, and scoreboard to their initial positions.

    Parameters:
    None

    Returns:
    None

    This function is called when the game needs to be reset, such as after a player scores a point. It sets the speed of the ball to its initial value, positions the ball at the center of the screen, and sets its direction randomly. It also moves the paddles to their starting positions on the left and right sides of the screen.

    After the reset, the function waits for 5 seconds before starting the game again. During this time, it displays a countdown on the screen, starting from "5" and decrementing by one each second until it reaches "0". Once the countdown is complete, the function clears the scoreboard display and the game resumes.
    """
    global speed
    global score_1
    global score_2

    speed = 10

    ball.teleport(0, 0)
    ball.turn_to(choice([45, 135, 225, 315]))
    paddle_1.teleport(-565, 0)
    paddle_2.teleport(555, 0)

    scr.update()

    if (score_1 == 10) or (score_2 == 10):

        if score_1 == 10:
            reset_score()
            for i in range(5):
                main_board.set_text(f"Player 1 wins!\nStarting in {5 - i}..", 0, 140)
                for _ in range(60):
                    scr.update()
                    wait(1 / 60)

        elif score_2 == 10:
            reset_score()
            for i in range(5):
                main_board.set_text(f"Player 2 wins!\nStarting in {5 - i}..", 0, 140)
                for _ in range(60):
                    scr.update()
                    wait(1 / 60)

        main_board.set_text(f"", 0, 180)
        return

    for i in range(5):
        main_board.set_text(f"Starting in {5 - i}..", 0, 140)
        for _ in range(60):
            scr.update()
            wait(1 / 60)
    main_board.set_text(f"", 0, 180)


reset_all()

while True:
    is_game = True
    while is_game:
        paddle_1.move()
        paddle_2.move()

        ball.move(speed)

        # Check collision with paddle_1
        if (abs(ball.ycor() - paddle_1.ycor()) < 80) and (abs(paddle_1.xcor() - ball.xcor()) < 23) and (ball.heading() == 135):
            speed += 1
            ball.turn_to(ball.heading() - 90)
        if (abs(ball.ycor() - paddle_1.ycor()) < 80) and (abs(paddle_1.xcor() - ball.xcor()) < 23) and (ball.heading() == 225):
            speed += 1
            ball.turn_to(ball.heading() + 90)

        # Check collision with paddle_2
        if (abs(ball.ycor() - paddle_2.ycor()) < 80) and (abs(paddle_2.xcor() - ball.xcor()) < 23) and (ball.heading() == 45):
            speed += 1
            ball.turn_to(ball.heading() + 90)    
        if (abs(ball.ycor() - paddle_2.ycor()) < 80) and (abs(paddle_2.xcor() - ball.xcor()) < 23) and (ball.heading() == 315):
            speed += 1
            ball.turn_to(ball.heading() - 90)

        # Check collision with top and bottom walls
        if ball.ycor() > 370 or ball.ycor() < -370:
            ball.turn_to(360 - ball.heading())

        # Check if the ball crossed the left boundary
        if ball.xcor() < -575:
            score_2 += 1
            scoreboard_2.set_text(score_2, 120, 300)
            reset_all()

        # Check if the ball crossed the right boundary
        if ball.xcor() > 565:
            score_1 += 1
            scoreboard_1.set_text(score_1, -130, 300)
            reset_all()

        scr.update()
        wait(1 / 60)