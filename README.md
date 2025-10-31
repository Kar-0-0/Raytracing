# Raytracer (Python + Pygame)

A small educational raytracer written in Python using Pygame for display. Focused on a minimal implementation with a single movable light source and one movable object to explore lighting, shadows, and simple animation.

## Features
- Basic ray-object intersections (sphere / plane)
- One movable light source (interactive)
- One movable object (animated)
- Low-resolution progressive preview via Pygame for fast feedback

## Requirements
- Python 3.8+
- pygame
- numpy (recommended)

Install dependencies:
```bash
python -m pip install pygame numpy
```

## Installation
1. Clone the repo or create a new project folder.
2. Add source files (e.g. `raytracer.py`, `scene.py`, `display.py`).
3. Install dependencies as above.

## Usage
Run the renderer:
```bash
python raytracer.py
```
Or as a module:
```bash
python -m raytracer
```

## Controls (preview window)
- Mouse click moves light source to location


## Performance tips
- Render at a lower resolution for the preview and upscale in Pygame.
- Use numpy for vector math and per-pixel operations.
- Tile or multiprocessing for CPU parallelism if rendering large frames.
- Limit samples and recursion depth during interactive use.

## Project layout (suggested)
- raytracer.py — runner / CLI / main loop

## Contributing
Keep changes modular. Add tests for intersection math and shading where feasible.

## License
MIT License — include full LICENSE file as needed.

Enjoy experimenting with light movement and simple animated objects!