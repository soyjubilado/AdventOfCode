#!/usr/bin/python3
# file created 2024-Dec-20 13:44
"""https://adventofcode.com/2024/day/20"""
from collections import namedtuple
Coord = namedtuple('XY', 'x y')


DATA = 'data202420.txt'
# DATA = 'testdata202420.txt'


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
      grid[Coord(x, y)] = char
  return grid


def Add(a, b):
  """Add two coordinates."""
  return Coord(a.x + b.x, a.y + b.y)


def Neighbors(xy, grid=None):
  """Returns neighbors of this cell. If grid is given, only return neighbors
     which are in the grid."""
  addends = [Coord(-1, 0),
             Coord(1, 0),
             Coord(0, 1),
             Coord(0, -1)]
  if not grid:
    return [Add(xy, a) for a in addends]
  return [Add(xy, a) for a in addends if Add(xy, a) in grid]


def WalkPath(grid):
  """Return a dictionary representing the path. The keys are the coordinates,
     and the values are the number of seconds to get to that point.
  """
  path = {}
  count = 0
  start = [i for i in grid if grid[i] == 'S'][0]
  end = [i for i in grid if grid[i] == 'E'][0]
  current = start
  while current != end:
    path[current] = count
    count += 1
    next_step = [i for i in Neighbors(current, grid)
                 if grid[i] in {'.', 'E'} and i not in path]
    assert len(next_step) == 1
    current = next_step[0]
  path[end] = count + 1
  return path


def Evaluate(c, path):
  """Give a value for the cheat. This is high by one if the cheat
     gets you directly to the end.
  """
  path_neighbors = [path[n] for n in Neighbors(c) if n in path]
  if len(path_neighbors) < 2:
    return 0
  return max(path_neighbors) - min(path_neighbors) - 2


def Part1(og_grid):
  """Part 1."""
  grid = og_grid.copy()
  path = WalkPath(grid)
  candidates = [c for c in grid if grid[c] == '#'
                and any(x in path for x in Neighbors(c, grid))]
  return sum([1 for c in candidates if Evaluate(c, path) >= 100])


def Part2(grid):
  """Part 2."""
  return None


def main():
  """main"""
  lines = GetData(DATA)
  grid = Grid(lines)
  print(f'Part 1: {Part1(grid)}')
  print(f'Part 2: {Part2(grid)}')


if __name__ == '__main__':
  main()
