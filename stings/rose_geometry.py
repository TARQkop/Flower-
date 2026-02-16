import math


def stem_x(y, sway):
    return 5 + 0.085 * (y + 240) + 8 * math.sin((y + 240) / 98 + sway)


def leaf_outline_points(x, y, heading, length, bulge, steps=26):
    angle = math.radians(heading)
    dx, dy = math.cos(angle), math.sin(angle)
    nx, ny = -dy, dx

    upper = []
    lower = []

    for i in range(steps):
        t = i / (steps - 1)
        cx = x + dx * length * t
        cy = y + dy * length * t
        offset = bulge * math.sin(math.pi * t)
        upper.append((cx + nx * offset, cy + ny * offset))
        lower.append((cx - nx * offset, cy - ny * offset))

    return upper, lower, dx, dy


def leaf_vein_segment(x, y, dx, dy, length, start=0.16, end=0.86):
    sx = x + dx * length * start
    sy = y + dy * length * start
    ex = x + dx * length * end
    ey = y + dy * length * end
    return sx, sy, ex, ey
