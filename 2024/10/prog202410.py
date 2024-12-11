#!/usr/bin/python3
# file created 2024-Dec-10 16:43
"""https://adventofcode.com/2024/day/10"""

from collections import namedtuple

DATA = 'data202410.txt'
# DATA = 'testdata202410.txt'
Coord = namedtuple('XY', 'x y')


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
      xy = Coord(x, y)
      grid[xy] = int(char)
  return grid


def Add(a, b):
  """Add two coordinates."""
  return Coord(a.x + b.x, a.y + b.y)


def Neighbors(xy):
  """Returns neighbors of this cell, even if they are not in the grid."""
  addends = [Coord(-1, 0),
             Coord(1, 0),
             Coord(0, 1),
             Coord(0, -1)]
  return [Add(xy, a) for a in addends]


def Trailpaths(grid, xy, level):
  """Return number of paths to a peak"""
  neighbor_coords = Neighbors(xy)
  neighbors = [c for c in neighbor_coords if c in grid
               and grid[c] == level + 1]
  if not neighbors:
    return 0
  if level == 8:
    return len(neighbors)

  return sum([Trailpaths(grid, n, level+1) for n in neighbors])


def Traildestinations(grid, xy, level):
  """Return the set of peaks reachable from xy"""
  neighbor_coords = Neighbors(xy)
  neighbors = [c for c in neighbor_coords if c in grid
               and grid[c] == level + 1]

  if not neighbors:
    return set()
  if level == 8:
    return set(neighbors)

  peaks = set()
  for n in neighbors:
    peaks = peaks.union(Traildestinations(grid, n, level+1))
  return peaks


def Part1(grid, trail_heads):
  """Part 1."""
  return sum([len(Traildestinations(grid, th, 0)) for th in trail_heads])


def Part2(grid, trail_heads):
  """Part 2."""
  return sum([Trailpaths(grid, th, 0) for th in trail_heads])


def main():
  """main"""
  lines = GetData(DATA)
  grid = Grid(lines)
  trail_heads = [xy for xy, val in grid.items() if val == 0]
  print(f'Part 1: {Part1(grid, trail_heads)}')
  print(f'Part 2: {Part2(grid, trail_heads)}')


if __name__ == '__main__':
  main()
