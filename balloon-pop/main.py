"""
Balloon Pop

Run with:
    python main.py

Controls:
    Mouse click - pop balloons
    R - restart after game over
    ESC - quit
"""

import pygame

from game.game_engine import GameEngine
from game.renderer import WINDOW_SIZE


def main():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Balloon Pop")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 22)

    engine = GameEngine()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_r:
                    engine.restart()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                engine.handle_click(event.pos)

        engine.update()

        engine.draw(
            screen,
            font
        )

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()