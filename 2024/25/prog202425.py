#!/usr/bin/python3
# file created 2024-Dec-25 06:15
"""https://adventofcode.com/2024/day/25"""
from collections import namedtuple
Coord = namedtuple('XY', 'x y')

DATA = 'data202425.txt'
# DATA = 'testdata202425.txt'


def Grid(lines):
  """Return a dictionary of coordinates."""
  grid = {}
  for y, line in enumerate(lines):
    for x, char in enumerate(line):
      grid[Coord(x, y)] = char
  return grid


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetKeys(lines):
  """Parse input lines into separate keys and locks."""
  keys = []
  locks = []
  for i in range(0, len(lines), 8):
    subgrid = Grid(lines[i:i+8])
    if subgrid[(0, 0)] == '#':
      locks.append(subgrid)
    elif subgrid[(0, 0)] == '.':
      keys.append(subgrid)
    else:
      raise Exception

  return keys, locks


def GridToTuple(grid):
  """Convert a 5x7 grid into a 5-tuple of heights."""
  answer = []
  for x in range(5):
    answer.append(len([c for c in grid if c.x == x and grid[c] == '#']) - 1)
  return tuple(answer)


def KeyFits(key, lock):
  """Does the key fits the lock?"""
  return all([a + b < 6 for a, b in zip(key, lock)])


def Part1(lines):
  """Part 1."""
  key_grids, lock_grids = GetKeys(lines)
  keys = [GridToTuple(key) for key in key_grids]
  locks = [GridToTuple(lock) for lock in lock_grids]

  answer = 0
  for k in keys:
    answer += len([l for l in locks if KeyFits(k, l)])
  return answer


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')


if __name__ == '__main__':
  main()
