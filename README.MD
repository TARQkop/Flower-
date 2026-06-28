# 🌹 Rose Animation

> A procedural animated rose built with Python Turtle and object-oriented design.



![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Turtle](https://img.shields.io/badge/Library-Turtle%20%28built--in%29-orange)

<p align="center">
    <img src="images/rose.png" width="700" alt="Rose Animation">
</p>

---

## ✨ Features

- 🎨 Multi-layered procedural rose drawing with gradient color palette
- 🏗️ Clean, extensible OOP architecture
- 📐 Dedicated geometry module for leaf and stem calculations
- 🌀 Smooth animation simulating a rose swaying in the wind
- ⚙️ Fully customizable parameters via a single settings file

---

## 📂 Project Structure

```
Flower/
├── rose.py                  # Entry point
└── stings/
    ├── rose_animator.py     # Main animation controller
    ├── rose_geometry.py     # Math & geometry logic
    ├── rose_shapes.py       # Drawing primitives
    └── rose_settings.py     # Configuration constants
```

### Module Descriptions

| File | Responsibility |
|---|---|
| `rose.py` | Instantiates `RoseAnimator` and starts the animation loop |
| `rose_animator.py` | Orchestrates the full scene (rose, stem, leaves) and manages animation frames |
| `rose_geometry.py` | Computes stem path, leaf outline points, and leaf vein segments |
| `rose_shapes.py` | Draws petals, stem, leaves, and spiral center using Turtle primitives |
| `rose_settings.py` | Holds window dimensions, color palette, petal layers, and frame timing |

---

## ▶️ Running the Project

```bash
python rose.py
```

---

## ⚙️ Requirements

- Python **3.10** or later
- `turtle` — built into Python's standard library, no installation needed

---

## 🎛️ Customization

All configuration lives in `stings/rose_settings.py`:

```python
# Window dimensions
WINDOW_WIDTH  = 1000
WINDOW_HEIGHT = 760

# Background color
BACKGROUND_COLOR = "#101820"

# Petal color palette (inner → outer)
PALETTE = ["#5a0011", "#7f1225", "#a4132b", "#c9183a", "#e5385c", "#ff5d73"]

# Rose layers: (petal_length, petal_count, radius)
LAYERS = [
    (24, 5,  0),
    (34, 8,  7),
    (44, 11, 13),
    (54, 14, 20),
    (64, 18, 29),
    (74, 22, 38),
]

# Animation speed (milliseconds per frame)
FRAME_DELAY_MS = 33   # ≈ 30 FPS

# Fixed random seed for reproducible petal noise
RANDOM_SEED = 7
```

---

## 🧠 How It Works

1. **`RoseAnimator`** sets up the Turtle screen and pre-generates fixed random noise for each petal.
2. Every frame, a `sway` angle is calculated using a sine function to simulate wind motion.
3. **`rose_geometry`** computes the curved stem path and leaf outline/vein coordinates.
4. **`rose_shapes`** draws each element — petals, stem, leaves, and the golden spiral center.
5. `screen.ontimer()` recursively calls `animate()` to drive the continuous animation loop.

---
## 📄 License

This project is licensed under the **MIT License** — see the `LICENSE` file for details.
