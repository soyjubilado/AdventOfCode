#!/usr/bin/python3
# file created 2024-Dec-06 06:43
"""https://adventofcode.com/2024/day/06"""

from time import sleep

DATA = 'data202406.txt'
# DATA = 'testdata202406.txt'


class OutOfBounds(Exception):
  """When things go off the grid."""


class LoopDetected(Exception):
  """Looping has been detected."""


def Grid(lines):
  """Return a dictionary of coordinates."""
  grid = {}
  for y, line in enumerate(lines):
    for x, char in enumerate(line):
      grid[(x, y)] = char
  return grid


def MinMaxXY(grid):
  """Return min_x, max_x, min_y, max_y"""
  x_all = [x for x, y in grid]
  y_all = [y for x, y in grid]
  return min(x_all), max(x_all), min(y_all), max(y_all)


def PrintGrid(grid, default_char='.', overlay=None):
  """Swiped from previous year."""
  min_x, max_x, min_y, max_y = MinMaxXY(grid)
  for y in range(min_y, max_y + 1):
    row_str = ''
    for x in range(min_x, max_x + 1):
      if overlay and (x, y) in overlay:
        row_str += overlay[(x, y)]
      else:
        row_str += f'{str(grid.get((x, y), default_char))}'
    print(row_str)


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def NextCell(this_cell, this_direction):
  """Given a cell and direction, calculate the next cell coordinates."""
  addx, addy = {'^': (0, -1),
                '>': (1, 0),
                'v': (0, 1),
                '<': (-1, 0)}[this_direction]
  x, y = this_cell
  return (x + addx, y + addy)


class Traveler():
  """I just want to travel the world."""

  def __init__(self, grid):
    """The grid should have the starting location embedded."""
    self.grid = grid
    self.location = self.GetLocation()
    self.direction = self.grid[self.location]
    self.visited = set([(self.location, self.direction)])

  def GetLocation(self):
    """Look the the grid for the location start. Assumes just one."""
    for coord in self.grid:
      if self.grid[coord] in ['^', '>', 'v', '<']:
        return coord
    raise OutOfBounds

  def NextDirection(self):
    """Assuming an obstacle, turn right and return that direction."""
    return {'^': '>',
            '>': 'v',
            'v': '<',
            '<': '^'}[self.direction]

  def NextCoord(self):
    """The next location that this traveler will go."""
    return NextCell(self.location, self.direction)

  def MoveOne(self):
    """Move a single cell, if possible; or turn, if not."""
    next_location = self.NextCoord()
    if not next_location in self.grid:
      raise OutOfBounds
    if (next_location, self.direction) in self.visited:
      raise LoopDetected
    if self.grid[next_location] == '#':
      self.direction = self.NextDirection()
      self.grid[self.location] = self.direction
    else:
      self.grid[self.location] = '.'
      self.location = next_location
      self.grid[next_location] = self.direction
      self.visited.add((self.location, self.direction))
      if not self.direction:
        raise Exception
    return self.location

  def MoveAll(self, visual=False):
    """Move until you would fall off the grid."""
    next_location = self.NextCoord()
    while next_location in self.grid:
      self.MoveOne()
      if visual:
        self.PrintVisual()
      next_location = self.NextCoord()

  def PrintVisual(self):
    """This will draw a fun visualization of the traveler moving. Only use for
    a grid that fits on your screen. Clear the screen first."""
    sleep(.05)
    print(f'\033[1;1f', end='')
    PrintGrid(self.grid)

  def PrintSelf(self):
    """Print the grid, including current location and direction of traveler."""
    PrintGrid(self.grid)


def Part1(traveler):
  """Part 1."""
  traveler.MoveAll()
  return len({coord for coord, direction in traveler.visited})


def Part2(og_grid, visited_cells):
  """Part 2."""
  answer = []
  previously_visited = {c for c, d in visited_cells}
  for try_coord in previously_visited:
    grid = og_grid.copy()
    if grid[try_coord] != '.':
      continue
    grid[try_coord] = '#'
    traveler = Traveler(grid)
    try:
      traveler.MoveAll()
    except LoopDetected:
      answer.append(try_coord)
  return len(answer)


def main():
  """main"""
  grid = Grid(GetData(DATA))
  og_traveler = Traveler(grid.copy())
  print(f'Part 1: {Part1(og_traveler)}')
  print(f'Part 2: {Part2(grid.copy(), og_traveler.visited)}')


if __name__ == '__main__':
  main()
