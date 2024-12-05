#!/usr/bin/python3
# file created 2024-Dec-03 20:49
"""https://adventofcode.com/2024/day/04"""

DATA = 'data202404.txt'
# DATA = 'testdata202404.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Grid(lines):
  """Return a dictionary of coordinates."""
  grid = {}
  for y, line in enumerate(lines):
    for x, char in enumerate(line):
      grid[(x, y)] = char
  return grid


def xmas_exists(x, y, x_add, y_add, grid):
  """For part 1, check whether xmas exists in a given direction, the direction
     is given by (x_add, y_add) which is repeatedly added to (x, y)."""
  if grid[(x, y)] != 'X':
    return False
  for target in ['M', 'A', 'S']:
    x += x_add
    y += y_add
    if (x, y) not in grid or grid[(x, y)] != target:
      return False
  return True


def num_xmases(x, y, grid):
  """For part 1, given a particular coordinate, count how many xmas radiate
     out from that point. There are 8 directions to check."""
  if grid[(x, y)] != 'X':
    return 0

  total = 0
  directions = [(-1, -1), (0, -1), (1, -1),
                (-1, 0), (1, 0),
                (-1, 1), (0, 1), (1, 1)]

  for x_add, y_add in directions:
    if xmas_exists(x, y, x_add, y_add, grid):
      total += 1
  return total


def makes_x(x, y, grid):
  """Check whether this point is the center of an XMAS cross for pt 2."""
  if grid[(x, y)] != 'A':
    return False
  corners = [(x-1, y-1), (x+1, y-1),
             (x-1, y+1), (x+1, y+1)]
  a1, b1, b2, a2 = corners
  for coord in corners:
    if coord not in grid:
      return False
  if (sorted([grid[a1], grid[a2]]) != ['M', 'S'] or
      sorted([grid[b1], grid[b2]]) != ['M', 'S']):
    return False
  return True


def Part1(grid):
  """Part 1."""
  return sum([num_xmases(x, y, grid) for x, y in grid])


def Part2(grid):
  """Part 2."""
  return sum([1 for x, y in grid if makes_x(x, y, grid)])


def main():
  """main"""
  lines = GetData(DATA)
  grid = Grid(lines)
  print(f'Part 1: {Part1(grid)}')
  print(f'Part 2: {Part2(grid)}')


if __name__ == '__main__':
  main()
