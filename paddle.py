"""
This module defines the Paddle class, which represents a paddle in the Ping Pong game.

The Paddle class inherits from the Turtle class from the turtle graphics library. It creates a rectangular turtle object with a specific size and color, and provides methods to control the movement of the paddle.

Attributes:
    going (dict): A dictionary that stores the current state of the paddle's movement (up or down).

Methods:
    go_up(): Sets the paddle to move upwards.
    stop_up(): Stops the paddle from moving upwards.
    go_down(): Sets the paddle to move downwards.
    stop_down(): Stops the paddle from moving downwards.
    move(): Moves the paddle based on its current state (up or down) and the screen boundaries.
"""

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        """
        Initializes a new instance of the Paddle class.

        Sets up the paddle's appearance (shape, color, size) and initial heading. Also initializes the going dictionary to track the paddle's movement state.
        """
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(1.5, 8, 0)
        self.setheading(90)
        self.going = {"Up": False, "Down": False}

    def go_up(self):
        """
        Sets the paddle to move upwards.
        """
        self.going["Up"] = True

    def stop_up(self):
        """
        Stops the paddle from moving upwards.
        """
        self.going["Up"] = False

    def go_down(self):
        """
        Sets the paddle to move downwards.
        """
        self.going["Down"] = True

    def stop_down(self):
        """
        Stops the paddle from moving downwards.
        """
        self.going["Down"] = False

    def move(self):
        """
        Moves the paddle based on its current state (up or down) and the screen boundaries.

        If the paddle is set to move upwards and its y-coordinate is less than 320, it moves forward by 10 units.
        If the paddle is set to move downwards and its y-coordinate is greater than -320, it moves backward by 10 units.
        """
        if self.going["Up"] and self.ycor() < 320:
            self.forward(10)
        if self.going["Down"] and self.ycor() > -320:
            self.backward(10)