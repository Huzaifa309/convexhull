# Convex Hull Visualizer (Pygame)

Interactive Pygame toolkit to explore convex hull and related geometric algorithms. Two menus launch different demos:
- `main.py`: CCW orientation demo, Line Sweep segment-intersection check, Algebraic orientation.
- `main2.py`: Brute Force hull, Jarvis March (Gift Wrapping), Graham Scan, Monotone Chain, Quickhull/Elimination.

## Requirements
- Python 3.9+ recommended
- Install deps: `pip install pygame`

## Running
- Main menu 1: `python main.py`
  - CCW: click points, press `Enter` to compute; shows hull and complexity.
  - Algebraic: click points, press `Enter` to classify orientation.
  - Line Sweep: click to place up to 4 points (two segments), press `A` to test intersection; “Reset” button clears.
- Main menu 2: `python main2.py`
  - Brute Force / Jarvis March / Graham Scan / Monotone Chain / Quickhull: click to add points; press `Enter` to build hull. Hull draws once computed; click again to start a fresh set.

## Controls (common)
- Left click: add a point (clears previous hull if one exists).
- `Enter`: run the selected algorithm (where applicable).
- Window close button: exit.

## Assets
- Background and button images in `assets/`; fonts in `assets/font.ttf`. Keep paths intact relative to the scripts.

## Files
- `main.py`, `main2.py`: Pygame menus that launch the demos.
- `button.py`: shared button widget.
- Algorithms: `bruteforce.py`, `jarvismarch.py`, `grahamscan.py`, `monotone.py`, `quickhull.py`, `ccww.py`, `algebricc.py`, `linesweep.py`.
- `Algo_report (1).pdf`: project report (see for theory/details).

## Notes
- Console prints include timing for many algorithms after each run.
- All demos assume a desktop environment where Pygame can open a window.