"""
Renderer.

All pygame drawing is handled here.
"""

import pygame


WIDTH = 700
HEIGHT = 500

WINDOW_SIZE = (
    WIDTH,
    HEIGHT
)

COLOR_BG = (
    200,
    230,
    245
)

COLOR_TEXT = (
    30,
    30,
    30
)


def draw_scene(
    surface,
    balloons
):

    surface.fill(
        COLOR_BG
    )

    for balloon in balloons:

        # Draw balloon.
        pygame.draw.circle(
            surface,
            balloon.color,
            (
                int(balloon.x),
                int(balloon.y)
            ),
            balloon.radius
        )

        # Draw balloon string.
        pygame.draw.line(
            surface,
            (
                120,
                120,
                120
            ),
            (
                balloon.x,
                balloon.y +
                balloon.radius
            ),
            (
                balloon.x,
                balloon.y +
                balloon.radius +
                12
            ),
            2
        )


def draw_text(
    surface,
    font,
    text,
    pos,
    color=COLOR_TEXT
):

    text_surface = font.render(
        text,
        True,
        color
    )

    surface.blit(
        text_surface,
        pos
    )


def draw_banner(
    surface,
    font,
    text
):

    text_surface = font.render(
        text,
        True,
        (
            180,
            40,
            40
        )
    )

    rect = text_surface.get_rect(
        center=(
            surface.get_width() // 2,
            surface.get_height() // 2
        )
    )

    surface.blit(
        text_surface,
        rect
    )


def draw_game_over(
    surface,
    font,
    score,
    timer_finished=False
):

    # Transparent dark overlay.
    overlay = pygame.Surface(
        (
            WIDTH,
            HEIGHT
        ),
        pygame.SRCALPHA
    )

    overlay.fill(
        (
            0,
            0,
            0,
            150
        )
    )

    surface.blit(
        overlay,
        (0, 0)
    )

    # Large title.
    game_over_font = pygame.font.SysFont(
        "consolas",
        42,
        bold=True
    )

    normal_font = pygame.font.SysFont(
        "consolas",
        24
    )

    if timer_finished:

        title = "TIME UP"

    else:

        title = "GAME OVER"

    title_text = game_over_font.render(
        title,
        True,
        (
            255,
            255,
            255
        )
    )

    score_text = normal_font.render(
        f"Final Score: {score}",
        True,
        (
            255,
            255,
            255
        )
    )

    restart_text = normal_font.render(
        "Press R to Restart",
        True,
        (
            255,
            255,
            255
        )
    )

    title_rect = title_text.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 - 60
        )
    )

    score_rect = score_text.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2
        )
    )

    restart_rect = restart_text.get_rect(
        center=(
            WIDTH // 2,
            HEIGHT // 2 + 50
        )
    )

    surface.blit(
        title_text,
        title_rect
    )

    surface.blit(
        score_text,
        score_rect
    )

    surface.blit(
        restart_text,
        restart_rect
    )