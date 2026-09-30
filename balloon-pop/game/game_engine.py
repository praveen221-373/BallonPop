"""
GameEngine.

Features:

Task 1:
    Fixed balloon click detection.

Task 2:
    Normal, Bonus and Penalty balloons.

Task 3:
    Three lives and game over.

Task 4:
    30-second countdown timer and restart.
"""

import random
import time

from game.balloon import Balloon
from game.click_detection import check_pop
from game.renderer import WIDTH, HEIGHT


SPAWN_INTERVAL_FRAMES = 45

STARTING_LIVES = 3

GAME_DURATION_SECONDS = 30


class GameEngine:

    def __init__(self):

        self.balloons = []

        self.frames_until_spawn = 0

        self.score = 0

        self.lives = STARTING_LIVES

        self.game_over = False

        self.start_time = time.time()

    def restart(self):

        self.balloons = []

        self.frames_until_spawn = 0

        self.score = 0

        self.lives = STARTING_LIVES

        self.game_over = False

        self.start_time = time.time()

    def get_remaining_time(self):

        elapsed_time = (
            time.time() -
            self.start_time
        )

        remaining_time = (
            GAME_DURATION_SECONDS -
            elapsed_time
        )

        return max(
            0,
            remaining_time
        )

    def _spawn_balloon(self):

        radius = random.randint(
            16,
            44
        )

        x = random.randint(
            radius + 10,
            WIDTH - radius - 10
        )

        speed = random.uniform(
            1.5,
            3.0
        )

        # Balloon probabilities:
        #
        # Normal  = 70%
        # Bonus   = 20%
        # Penalty = 10%

        roll = random.random()

        if roll < 0.70:

            balloon_type = "normal"

        elif roll < 0.90:

            balloon_type = "bonus"

        else:

            balloon_type = "penalty"

        balloon = Balloon(
            x=x,
            y=-radius,
            radius=radius,
            speed=speed,
            balloon_type=balloon_type
        )

        self.balloons.append(
            balloon
        )

    def handle_click(self, pos):

        if self.game_over:
            return

        popped = check_pop(
            self.balloons,
            pos
        )

        if popped is not None:

            self.balloons.remove(
                popped
            )

            self.score += (
                popped.points
            )

    def update(self):

        if self.game_over:
            return

        # Check timer.
        if self.get_remaining_time() <= 0:

            self.game_over = True

            self.balloons.clear()

            return

        # Spawn balloons.
        self.frames_until_spawn -= 1

        if self.frames_until_spawn <= 0:

            self._spawn_balloon()

            self.frames_until_spawn = (
                SPAWN_INTERVAL_FRAMES
            )

        # Move balloons.
        for balloon in self.balloons:

            balloon.update()

        # Check balloons that reached
        # the bottom.
        remaining_balloons = []

        for balloon in self.balloons:

            if balloon.is_past_bottom(
                HEIGHT
            ):

                self.lives -= 1

            else:

                remaining_balloons.append(
                    balloon
                )

        self.balloons = (
            remaining_balloons
        )

        # Check lives.
        if self.lives <= 0:

            self.lives = 0

            self.game_over = True

            self.balloons.clear()

    def draw(
        self,
        surface,
        font
    ):

        from game import renderer

        renderer.draw_scene(
            surface,
            self.balloons
        )

        # Score.
        renderer.draw_text(
            surface,
            font,
            f"Score: {self.score}",
            (10, 10)
        )

        # Lives.
        renderer.draw_text(
            surface,
            font,
            f"Lives: {self.lives}",
            (10, 40)
        )

        # Timer.
        remaining_time = (
            self.get_remaining_time()
        )

        renderer.draw_text(
            surface,
            font,
            f"Time: {remaining_time:.1f}s",
            (10, 70)
        )

        # Game-over screen.
        if self.game_over:

            renderer.draw_game_over(
                surface,
                font,
                self.score,
                remaining_time <= 0
            )