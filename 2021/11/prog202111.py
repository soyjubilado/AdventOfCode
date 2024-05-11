#!/usr/bin/python3
#file created 2021-Dec-10 21:00
"""https://adventofcode.com/2021/day/11"""


DATA = 'data202111.txt'
# DATA = 'testdata202111.txt'
# DATA = 'testdata202111a.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def bold(my_str):
  """Make my_str bold!"""
  assert isinstance(my_str, str)
  return '\033[1m' + my_str + '\033[0m'


class Octopus(object):
  """Helper class to keep track of value and flash status."""

  def __init__(self, value):
    self.value = value
    self.has_flashed = False

  def Increment(self):
    self.value = (int(self.value) + 1) % 10
    if self.value == 0:
      self.has_flashed = True

  def Reset(self):
    self.has_flashed = False

  def __repr__(self):
    return str(self.value)


def GetGrid(lines):
  """Turns a list of strings into a dict of Octopuses keyed on coordinates"""
  grid = {}
  for y, row in enumerate(lines):
    for x, col in enumerate(row):
      grid[(x, y)] = Octopus(col)
  return grid


def Neighbors(coords, grid):
  """Returns a list of neighboring coordinates, only those on the grid.
     Includes diagonal neighbors.
  """
  x, y = coords
  potential_neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1),
                         (x-1, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1), ]
  return [c for c in potential_neighbors if c in grid]


def OneStep(grid):
  """Number of flashes after one step. grid is mutable and changes.
     Raises exception if all octopuses are flashing at once.
  """
  flashed = []
  flashing = []
  for coord in grid:
    grid[coord].Increment()
  flashing = [c for c in grid if grid[c].has_flashed]
  while flashing:
    flashed.extend(flashing)
    neighbors = []
    for c in flashing:
      grid[c].Reset()
      neighbors.extend([i for i in Neighbors(c, grid) if i not in flashed])
    for n in neighbors:
      if grid[n].value != 0:
        grid[n].Increment()
    flashing = [n for n in grid if grid[n].has_flashed]

  # for part 2, exit ungracefully if all octopuses are synchronized
  assert len(flashed) < len(grid)
  return len(flashed)


def PrintGrid(grid, rows, columns):
  for r in range(rows):
    row_str = ''
    for c in range(columns):
      numstr = str(grid[(c, r)])
      numstr = bold(numstr) if numstr == '0' else numstr
      row_str += numstr
    print(row_str)


def main():
  lines = GetData(DATA)
  grid = GetGrid(lines)
  print('Before any steps:')
  PrintGrid(grid, len(lines), len(lines[0]))
  print('no flashing at beginning')
  flashes = 0
  # for part 2, change range(100) to range(1000000)
  for i in range(100):
    print(f'\nafter step {i+1}:')
    flashes += OneStep(grid)
    PrintGrid(grid, len(lines), len(lines[0]))
    print(f'flashes so far: {flashes}')


if __name__ == '__main__':
  main()
