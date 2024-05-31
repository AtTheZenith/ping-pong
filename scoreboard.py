"""This module defines the Scoreboard class, which is responsible for displaying the scores in the Ping Pong game.

The Scoreboard class inherits from the Turtle class from the turtle graphics library. It creates a turtle object with a specific color and font, and provides a method to set the text to be displayed on the screen.

Methods:
    set_text(text, xpos, ypos): Clears the previous text and displays the given text at the specified x and y coordinates.
"""

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        """
        Initializes a new instance of the Scoreboard class.

        Sets up the scoreboard's appearance (color, font) and hides the turtle object.
        """
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("White")
        self.write("", align="center", font=("Segoe UI", 36, "normal"))

    def set_text(self, text, xpos, ypos):
        """
        Clears the previous text and displays the given text at the specified x and y coordinates.

        Args:
            text (str): The text to be displayed on the screen.
            xpos (float): The x-coordinate where the text should be displayed.
            ypos (float): The y-coordinate where the text should be displayed.
        """
        self.clear()
        self.goto(xpos, ypos)
        self.write(text, align="center", font=("Segoe UI", 36, "normal"))
