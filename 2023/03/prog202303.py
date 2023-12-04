#!/usr/bin/python3
# file created 2023-Dec-03 14:25
"""https://adventofcode.com/2023/day/3"""

DATA = 'data202303.txt'
# DATA = 'testdata202303.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


class Number:
  """A number class representing a potential part number."""

  def __init__(self, grid, coords_list):
    # coords must be a list of tuples
    self.coords = sorted(coords_list)
    self.value = self.GetValue(grid)
    self.has_adjacent_symbol = self.HasAdjacentSymbol(grid)
    self.neighbors = self.Neighbors()

  def GetValue(self, grid):
    """The value of the number converted from characters."""
    total = 0
    for n in self.coords:
      total = 10 * total + int(grid[n])
    return total

  def HasAdjacentSymbol(self, grid):
    """True if there is an adjacent symbol to this number."""
    for cell in self.coords:
      if HasAdjacentSymbol(grid, cell):
        return True
    return False

  def Neighbors(self):
    """does not care if neighbor coords are in grid"""
    all_neighbors = set([])
    for coord in self.coords:
      for xy in Neighbors(coord):
        all_neighbors.add(xy)
    return all_neighbors

  def __repr__(self):
    return f'<{self.value} at {self.coords}>'


def Neighbors(cell):
  """Given a cell, return a list of all its neighbors."""
  x, y = cell
  neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1),
               (x-1, y), (x+1, y),
               (x-1, y+1), (x, y+1), (x+1, y+1)]
  return neighbors


def HasAdjacentSymbol(grid, cell):
  """Given a grid and cell, return True if there is an adjacent symbol."""
  allowed = '0123456789.'
  neighbors = Neighbors(cell)
  for n in neighbors:
    if n in grid and grid[n] not in allowed:
      return True
  return False


def GrepNumbers(grid, line, row_num):
  """Given a line and grid, return a list of Number objects."""
  x = 0
  y = row_num
  end = len(line)
  numbers = []
  while x < end:
    number_coordinates = []
    while x < end and line[x].isdigit():
      number_coordinates.append((x, y))
      x += 1
    if number_coordinates:
      newNumber = Number(grid, number_coordinates)
      numbers.append(newNumber)
    while x < end and not line[x].isdigit():
      x += 1
  return numbers


def Grid(lines):
  """Return a dictionary of coordinates."""
  grid = {}
  for y, line in enumerate(lines):
    for x, char in enumerate(line):
      grid[(x, y)] = char
  return grid


def PrintGrid(grid, default_char=' '):
  """Swiped from previous year."""
  x_all = [x for x, y in grid]
  y_all = [y for x, y in grid]
  max_x = max(x_all)
  max_y = max(y_all)
  min_x = min(x_all)
  min_y = min(y_all)
  for y in range(min_y, max_y + 1):
    row_str = ''
    for x in range(min_x, max_x + 1):
      row_str += f'{str(grid.get((x, y), default_char))}'
    print(row_str)


def Part1(grid, lines):
  """Part 1"""
  all_num_objects = []
  for y, line in enumerate(lines):
    numbers = GrepNumbers(grid, line, y)
    all_num_objects.extend(numbers)
  return sum(n.value for n in all_num_objects if n.has_adjacent_symbol)


def Part2(grid, lines):
  """Part 2"""
  all_num_objects = []
  total = 0
  for y, line in enumerate(lines):
    numbers = GrepNumbers(grid, line, y)
    all_num_objects.extend(numbers)

  for xy, char in grid.items():
    if char != '*':
      continue
    adjacent_numbers = [n for n in all_num_objects if xy in n.neighbors]
    if len(adjacent_numbers) != 2:
      continue
    ratio = adjacent_numbers[0].value * adjacent_numbers[1].value
    total += ratio
  return total


def main():
  """main"""
  lines = GetData(DATA)
  grid = Grid(lines)
  print(f'Part 1: {Part1(grid, lines)}')
  print(f'Part 2: {Part2(grid, lines)}')


if __name__ == '__main__':
  main()
