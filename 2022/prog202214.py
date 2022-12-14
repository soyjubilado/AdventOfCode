#!/usr/bin/python3
#file created 2022-Dec-13 20:59
"""https://adventofcode.com/2022/day/14"""

from collections import defaultdict
DATA = 'data202214.txt'
# DATA = 'testdata202214.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def CornerToCorner(here, there):
  """Return a list of all the points from here to there, inclusive. Assumes the
     two points are on a line. If not, and if you take out the assert, it fills
     in all the points of the rectangle defined by the two corners."""
  retval = []
  x_here, y_here = here
  x_there, y_there = there
  assert x_here == x_there or y_here == y_there
  x_start, x_end = (x_here, x_there) if x_there > x_here else (x_there, x_here)
  y_start, y_end = (y_here, y_there) if y_there > y_here else (y_there, y_here)
  for x in range(x_start, x_end + 1):
    for y in range(y_start, y_end + 1):
      retval.append((x, y))
  return retval


def GetGrid(lines):
  """Convert the input list to a dictionary of coordinates."""
  grid = defaultdict(lambda: '.')
  for line in lines:
    corners = line.split(' -> ')
    prev_corner = None

    for corner in corners:
      here = tuple([int(i) for i in corner.split(',')])
      if prev_corner is not None:
        for coord in CornerToCorner(prev_corner, here):
          grid[coord] = '#'
      prev_corner = here
  return grid


def PrintGrid(grid, default_char='.'):
  """Print the grid with a '+' at (500,0)."""
  overlay = {(500, 0): '+'}
  x_all = [x for x, y in grid] + [x for x, y in overlay]
  y_all = [y for x, y in grid] + [y for x, y in overlay]
  min_x = min(x_all)
  min_y = min(y_all)
  max_x = max(x_all)
  max_y = max(y_all)
  for y in range(min_y, max_y + 1):
    row_str = ''
    for x in range(min_x, max_x + 1):
      if (x, y) in overlay:
        row_str += f'{overlay[(x, y)]}'
      else:
        row_str += f'{str(grid.get((x, y), default_char))}'
    print(row_str)


def NextSpot(grid, here, abyss_level, is_part_2=False):
  """Given a current location 'here', and a grid, find the next open spot for
     the grain of sand. This will be directly below, below and to the left, or
     below and to the right. If there are no open spots, return None."""
  x, y = here
  if is_part_2 and y+1 == abyss_level:
    return None
  for coords in [(x, y+1), (x-1, y+1), (x+1, y+1)]:
    if grid[coords] == '.':
      return coords
  return None


def AddOneGrain(grid, abyss_level, is_part_2=False):
  """Add next grain to the grid.
     Returns True successful."""
  here = (500, 0)
  start = here
  next_spot = NextSpot(grid, here, abyss_level, is_part_2)
  while next_spot is not None and next_spot[1] < abyss_level:
    here = next_spot
    next_spot = NextSpot(grid, here, abyss_level, is_part_2)

  if next_spot is None and next_spot != here:
    grid[here] = 'o'
    if here != start:
      return True

  return False


def Solve(part):
  """Part 1: infinite abyss"""
  is_part_2 = (part == 'Part 2')
  lines = GetData(DATA)
  grid = GetGrid(lines)
  abyss_level = max([y for _, y in grid]) + 2
  added_another = AddOneGrain(grid, abyss_level)
  while added_another:
    added_another = AddOneGrain(grid, abyss_level, is_part_2)
  print(f'{part}: {list(grid.values()).count("o")}')


def main():
  """main"""
  Solve('Part 1')
  Solve('Part 2')


if __name__ == '__main__':
  main()
