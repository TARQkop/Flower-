def move_pen(pen, x, y, heading=None):
    pen.penup()
    pen.goto(x, y)
    if heading is not None:
        pen.setheading(heading)
    pen.pendown()


def draw_petal(pen, length, color):
    pen.color(color, color)
    pen.begin_fill()
    pen.circle(length, 62)
    pen.left(118)
    pen.circle(length, 62)
    pen.left(118)
    pen.end_fill()


def draw_stem_curve(pen, x_fn, sway, y_start=-250, y_end=70, step=3):
    pen.pensize(9)
    pen.color("#1b4332")

    y = y_start
    x = x_fn(y, sway)
    move_pen(pen, x, y)
    while y <= y_end:
        y += step
        x = x_fn(y, sway)
        pen.goto(x, y)


def draw_leaf_from_points(pen, upper, lower, fill_color="#2d6a4f"):
    pen.pensize(2)
    pen.color(fill_color, fill_color)
    move_pen(pen, upper[0][0], upper[0][1])
    pen.begin_fill()

    for px, py in upper[1:]:
        pen.goto(px, py)
    for px, py in reversed(lower):
        pen.goto(px, py)

    pen.end_fill()


def draw_leaf_vein(pen, sx, sy, ex, ey, color="#95d5b2"):
    move_pen(pen, sx, sy)
    pen.pensize(2)
    pen.color(color)
    pen.goto(ex, ey)


def draw_spiral_center(pen, cx, cy, sway_deg):
    move_pen(pen, cx - 8, cy - 1, 20 + sway_deg)
    pen.pensize(3)
    pen.color("#ffd6a5")
    for i in range(42):
        pen.forward(1.3 + i * 0.17)
        pen.left(19)
