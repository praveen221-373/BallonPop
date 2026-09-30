"""
Balloon class.

Balloon types:

Normal:
    +10 points

Bonus:
    +30 points

Penalty:
    -20 points
"""

import pygame


class Balloon:

    def __init__(
        self,
        x,
        y,
        radius,
        speed,
        balloon_type="normal"
    ):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

        self.balloon_type = balloon_type

        if balloon_type == "normal":

            self.color = (
                220,
                90,
                120
            )

            self.points = 10

        elif balloon_type == "bonus":

            self.color = (
                255,
                215,
                0
            )

            self.points = 30

        elif balloon_type == "penalty":

            self.color = (
                70,
                70,
                70
            )

            self.points = -20

        else:

            self.color = (
                220,
                90,
                120
            )

            self.points = 10

    def update(self):

        self.y += self.speed

    def is_past_bottom(self, height):

        return (
            self.y - self.radius > height
        )

    def get_rect(self):

        return pygame.Rect(
            int(self.x - self.radius),
            int(self.y - self.radius),
            self.radius * 2,
            self.radius * 2
        )