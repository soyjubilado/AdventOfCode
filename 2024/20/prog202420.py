#!/usr/bin/python3
# file created 2024-Dec-20 13:44
"""https://adventofcode.com/2024/day/20"""
from grid import Grid, Neighbors


DATA = 'data202420.txt'
# DATA = 'testdata202420.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


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
