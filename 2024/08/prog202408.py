#!/usr/bin/python3
# file created 2024-Dec-08 06:48
"""https://adventofcode.com/2024/day/08"""

from collections import defaultdict
from itertools import combinations
from math import gcd


DATA = 'data202408.txt'
# DATA = 'testdata202408.txt'


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


def GetMapping(grid):
  """Locations of all the antennae, keyed on the antenna frequency.
  Example: {'s': [(3, 0), (8, 2), (7, 3)],
            'w': [(19, 1), (14, 3), (9, 4), (20, 10)],}
  """
  my_map = defaultdict(list)
  for xy, value in grid.items():
    if value.isalpha() or value.isdigit():
      my_map[value].append(xy)
  return my_map


def Add_XY(xy1, xy2):
  """Add two XY coordinates."""
  x1, y1 = xy1
  x2, y2 = xy2
  return (x1 + x2, y1 + y2)


def Subtract_XY(xy1, xy2):
  """Subtract xy2 from xy1 coordinates."""
  x1, y1 = xy1
  x2, y2 = xy2
  return (x1 - x2, y1 - y2)


def Antinodes(coord1, coord2, _=None):
  """Given a pair of antennae, return the two antinodes for part 1."""
  delta2to1 = Subtract_XY(coord1, coord2)
  delta1to2 = Subtract_XY(coord2, coord1)
  return (Add_XY(coord1, delta2to1),
          Add_XY(coord2, delta1to2))


def AllAntinodes(coord1, coord2, grid):
  """Return all antinodes for given coordinate part in part 2.
  The assert statement ensures that the x difference and y difference
  are co-prime, otherwise we would need to reduce the by the gcd.
  """
  delta2to1 = Subtract_XY(coord1, coord2)
  assert gcd(abs(delta2to1[0]), abs(delta2to1[1])) == 1
  all_antinodes = {coord1, coord2}

  current = coord1
  while current in grid:
    all_antinodes.add(current)
    current = Add_XY(current, delta2to1)

  current = coord1
  while current in grid:
    all_antinodes.add(current)
    current = Subtract_XY(current, delta2to1)

  return all_antinodes


def Solver(grid, pt2=False):
  """Solver for both parts. For part 1, use Antinodes() to find the set of
     antinodes, and for part 2 use AllAntinodes()."""
  GetAntinodes = AllAntinodes if pt2 else Antinodes
  my_map = GetMapping(grid)
  antinodes = set()
  for antenna_type in my_map:
    antenna_pairs = combinations(my_map[antenna_type], 2)
    for pair in antenna_pairs:
      these_antinodes = GetAntinodes(*pair, grid)
      antinodes = antinodes.union(these_antinodes)

  return len([i for i in antinodes if i in grid])


def main():
  """main"""
  grid = Grid(GetData(DATA))
  print(f'Part 1: {Solver(grid.copy())}')
  print(f'Part 2: {Solver(grid.copy(), pt2=True)}')


if __name__ == '__main__':
  main()
