"""
This module defines the Ball class, which represents the ball in the Ping Pong game.

The Ball class inherits from the Turtle class from the turtle graphics library. It creates a circular turtle object with a specific color and provides methods to move the ball and change its direction.

Methods:
    move(speed): Moves the ball forward by the specified speed.
    turn_to(angle): Changes the ball's heading to the specified angle.
"""

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        """
        Initializes a new instance of the Ball class.

        Sets up the ball's appearance (shape, color) and initial speed.
        """
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.penup()
        self.speed(0)

    def move(self, speed):
        """
        Moves the ball forward by the specified speed.

        Args:
            speed (float): The speed at which the ball should move.
        """
        self.forward(speed)

    def turn_to(self, angle):
        """
        Changes the ball's heading to the specified angle.

        Args:
            angle (float): The angle (in degrees) to which the ball's heading should be set.
        """
        self.setheading(angle)