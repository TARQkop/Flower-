import math
import random
import turtle

from stings.rose_geometry import leaf_outline_points, leaf_vein_segment, stem_x
from stings.rose_shapes import (
    draw_leaf_from_points,
    draw_leaf_vein,
    draw_petal,
    draw_spiral_center,
    draw_stem_curve,
    move_pen,
)
from stings.rose_settings import (
    BACKGROUND_COLOR,
    FRAME_DELAY_MS,
    LAYERS,
    PALETTE,
    RANDOM_SEED,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)


class RoseAnimator:
    def __init__(self):
        self.random = random.Random(RANDOM_SEED)
        self.screen = turtle.Screen()
        self.screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.title(WINDOW_TITLE)
        self.screen.tracer(0, 0)

        self.pen = turtle.Turtle(visible=False)
        self.pen.speed(0)
        self.frame = 0

        self.palette = PALETTE
        self.layers = LAYERS
        self.petal_noise = self._build_petal_noise()

    def _build_petal_noise(self):
        noise = []
        for _, count, _ in self.layers:
            layer_noise = []
            for _ in range(count):
                layer_noise.append(
                    {
                        "angle": self.random.uniform(-6, 6),
                        "heading": self.random.uniform(-8, 8),
                        "radius": self.random.uniform(-2.5, 3.5),
                    }
                )
            noise.append(layer_noise)
        return noise

    def move(self, x, y, heading=None):
        move_pen(self.pen, x, y, heading)

    def petal(self, length, color):
        draw_petal(self.pen, length, color)

    def draw_stem(self, sway):
        draw_stem_curve(self.pen, stem_x, sway)

    def draw_leaf(self, x, y, heading, length=74, bulge=16):
        upper, lower, dx, dy = leaf_outline_points(x, y, heading, length, bulge)
        draw_leaf_from_points(self.pen, upper, lower)
        sx, sy, ex, ey = leaf_vein_segment(x, y, dx, dy, length)
        draw_leaf_vein(self.pen, sx, sy, ex, ey)

    def draw_rose(self, cx, cy, sway_deg):
        for i, (petal_len, count, radius) in enumerate(self.layers):
            for n in range(count):
                petal_info = self.petal_noise[i][n]
                angle = (360 / count) * n + petal_info["angle"]
                x = cx + radius * math.cos(math.radians(angle))
                y = cy + radius * math.sin(math.radians(angle))
                heading = angle - 90 + petal_info["heading"] + sway_deg
                self.move(x, y, heading)
                self.petal(petal_len + petal_info["radius"], self.palette[i])

        draw_spiral_center(self.pen, cx, cy, sway_deg)

    def draw_scene(self):
        sway = math.sin(self.frame * 0.07) * 0.9

        self.draw_stem(sway)

        top_x = stem_x(70, sway)
        self.draw_rose(top_x - 6, 120, sway * 6)

        left_x = stem_x(-38, sway) - 2
        right_x = stem_x(-120, sway) + 8

        self.draw_leaf(left_x, -38, -154 + sway * 9, 62, 13)
        self.draw_leaf(right_x, -120, 31 + sway * 9, 74, 16)

    def animate(self):
        self.pen.clear()
        self.draw_scene()
        self.screen.update()
        self.frame += 1
        self.screen.ontimer(self.animate, FRAME_DELAY_MS)

    def run(self):
        self.animate()
        turtle.done()
