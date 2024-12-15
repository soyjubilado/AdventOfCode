"""Grid structure and related functions."""
from collections import namedtuple
import subprocess
Coord = namedtuple('XY', 'x y')


def ClearScreen():
  """Clear the screen."""
  subprocess.run(['clear'], check=False)


def Reset():
  """Move cursor to upper left."""
  print(f'\033[1;1f', end='')


def Grid(lines):
  """Return a dictionary of coordinates."""
  grid = {}
  for y, line in enumerate(lines):
    for x, char in enumerate(line):
      grid[Coord(x, y)] = char
  return grid


def Add(a, b):
  """Add two coordinates."""
  return Coord(a.x + b.x, a.y + b.y)


def PrintGrid(grid, default_char='.', overlay=None,
              left_border=1, top_border=1):
  """Print the grid. Requires MinMaxXY()."""
  def MinMaxXY(grid):
    """Return min_x, max_x, min_y, max_y"""
    x_all = [x for x, y in grid]
    y_all = [y for x, y in grid]
    return min(x_all), max(x_all), min(y_all), max(y_all)

  min_x, max_x, min_y, max_y = MinMaxXY(grid)
  for _ in range(top_border):
    print()
  for y in range(min_y, max_y + 1):
    row_str = '' + (' ' * left_border)
    for x in range(min_x, max_x + 1):
      if overlay and (x, y) in overlay:
        row_str += overlay[(x, y)]
      else:
        row_str += f'{str(grid.get((x, y), default_char))}'
    print(row_str)
  print()
