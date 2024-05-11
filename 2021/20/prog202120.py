#!/usr/bin/python3
#file created 2021-Dec-19 20:56
"""https://adventofcode.com/2021/day/20

At first glance, this problem appeared to be a simple version of cellular
automata. In fact, someone on the forum figured out the enhancement algorithm
needed to turn it specifically into the game of life.

The trick was that in the example, a pixel surrounded by empty pixels was empty
in the next round. But if the enhancement algorithm has "#" as the first
element, that means an empty pixel surrounded by empty pixels this round will
be a lit pixel the next round. And the grid is infinite. In this case, we
needed a way to swap the "default" value of a non-mapped pixel for every other
round.

The other problem this brings up is that the grid necessarily expands outward
with each round. There's probably a way to fix this.
"""

from copy import deepcopy
DATA = 'data202120.txt'
# DATA = 'testdata202120.txt'


def GetData(datafile):
  """Parse input."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetGrid(lines):
  """Put input into a dictionary of coordinates."""
  grid = {}
  for row in range(len(lines)):
    for col in range(len(lines[0])):
      grid[(col, row)] = lines[row][col]
  return grid


def PrintGrid(grid):
  """For debugging. This version puts spaces between the numbers."""
  x_all = [x for x, y in grid]
  y_all = [y for x, y in grid]
  min_x = min(x_all)
  min_y = min(y_all)
  max_x = max(x_all)
  max_y = max(y_all)
  for y in range(min_y, max_y + 1):
    row_str = ''
    for x in range(min_x, max_x + 1):
      row_str += f'{grid.get((x, y), "?")}'
    print(row_str)


def NeighborCoords(coords):
  """Returns a list of 9x9 square centered on coords.
  """
  x, y = coords
  neighbor_coords = [(x-1, y-1), (x, y-1), (x+1, y-1),
                     (x-1, y), (x, y), (x+1, y),
                     (x-1, y+1), (x, y+1), (x+1, y+1)]
  return neighbor_coords


def Enhance(coords, grid, enhancement, default='.'):
  """Figure out what the pixel is by those that surround it."""
  idx_str = ''
  for c in NeighborCoords(coords):
    idx_str += '1' if grid.get(c, default) == '#' else '0'
  idx_num = int(idx_str, 2)
  return enhancement[idx_num]


def main():
  lines = GetData(DATA)
  grid = GetGrid(lines[2:])
  enhancement = lines[0]

  Part1_rounds = 2
  Part2_rounds = 50

  for i in range(Part1_rounds):
    print(f'round {i}')

    # This is the big hack for when enhancement[0] == '#'
    default_char = '#' if i % 2 else '.'

    new_grid = {}
    coordinate_set = set([])
    # Check all the elements just outside the border of the current grid
    # This means the grid grows with each iteration.
    for c in grid:
      for n in NeighborCoords(c):
        coordinate_set.add(n)

    for c in coordinate_set:
      new_c_val = Enhance(c, grid, enhancement, default=default_char)
      new_grid[c] = new_c_val

    grid = deepcopy(new_grid)

    PrintGrid(grid)
    print()
  print(sum([1 for i in grid.values() if i == '#']))


if __name__ == '__main__':
  main()
