#!/usr/bin/python3
# file created 2025-Dec-04 17:43
"""https://adventofcode.com/2025/day/04"""

import grid
DATA = 'data202504.txt'
# DATA = 'testdata202504.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Neighbors(coords):
  """List the neighbors of this xy coordinate."""
  x, y = coords
  return [(x-1, y-1), (x, y-1), (x+1, y-1),
          (x-1, y), (x+1, y),
          (x-1, y+1), (x, y+1), (x+1, y+1)]


def Removeables(warehouse):
  """Return a list of removeable locations."""
  overlay = {}
  for coords, value in warehouse.items():
    if value != '@':
      continue
    neighbors = Neighbors(coords)
    num_neighbors = len([i for i in neighbors if i in warehouse and
                         warehouse[i] == '@'])
    if num_neighbors < 4:
      overlay[coords] = 'x'
  return overlay


def Part1(lines):
  """Part 1."""
  warehouse = grid.Grid(lines)
  overlay = Removeables(warehouse)
  return len(overlay)


def Part2(lines):
  """Part 2."""
  warehouse = grid.Grid(lines)
  overlay = Removeables(warehouse)
  removed = 0
  while overlay:
    removed += len(overlay)
    for coord in overlay:
      warehouse[coord] = '.'
    overlay = Removeables(warehouse)
  return removed


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
