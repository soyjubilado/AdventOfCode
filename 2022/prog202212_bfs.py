#!/usr/bin/python3
#file created 2022-Dec-12 15:29
"""https://adventofcode.com/2022/day/12"""

from collections import deque

DATA = 'data202212.txt'
# DATA = 'testdata202212.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetGrid(lines):
  """Put input into a dictionary of coordinates."""
  grid = {}
  start = dest = None
  for row, line in enumerate(lines):
    for col, letter in enumerate(line):
      if letter == 'S':
        start = (col, row)
        letter = 'a'
      elif letter == 'E':
        dest = (col, row)
        letter = 'z'
      grid[(col, row)] = letter

  return grid, start, dest


def Neighbors(coords, grid):
  """Returns a list of neighboring coordinates, only those on the grid,
     and only those that are a legal next move. Excludes diagonals.
  """
  x, y = coords
  potential_neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
  return [c for c in potential_neighbors if c in grid and
          ord(grid[c]) - 1 <= ord(grid[coords])]


def GetCost(grid, start, dest):
  """Search for the lowest cost path and return the cost."""
  cost_grid = {start: 0}
  frontier = deque([start])

  while dest not in cost_grid:
    here = frontier.popleft()
    current_cost = cost_grid[here]
    neighbors = Neighbors(here, grid)

    for neighbor in neighbors:
      if neighbor not in cost_grid:
        cost_grid[neighbor] = current_cost + 1
        frontier.append(neighbor)

  return cost_grid[dest]


def Part1():
  """Part 1"""
  lines = GetData(DATA)
  grid, start, destination = GetGrid(lines)
  print(f'Part 1: {GetCost(grid, start, destination)} from {start}')


def Part2():
  """Part 2 just tries every possible starting point."""
  lines = GetData(DATA)
  grid, start, destination = GetGrid(lines)

  # try every point on the graph that starts with 'a'
  all_starts = [c for c in grid if grid[c] == 'a']

  min_cost = GetCost(grid, start, destination)
  min_coords = start

  # Running GetCost() from an impossible starting point will throw
  # an exception. Just ignore these.
  for start in all_starts:
    try:
      cost = GetCost(grid, start, destination)
    except IndexError:
      continue
    if cost < min_cost:
      min_cost = cost
      min_coords = start
  print(f'Part 2: {min_cost} from {min_coords}')


def main():
  """main"""
  Part1()
  Part2()


if __name__ == '__main__':
  main()
