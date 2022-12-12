#!/usr/bin/python3
#file created 2022-Dec-11 20:59
"""https://adventofcode.com/2022/day/12"""
from heapq import heappush, heappop

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
  start = destination = None
  for row, line in enumerate(lines):
    for col, letter in enumerate(line):
      contents = letter
      if contents == 'S':
        start = (col, row)
        contents = 'a'
      elif contents == 'E':
        destination = (col, row)
        contents = 'z'
      grid[(col, row)] = contents
  return grid, start, destination


def PrintGrid(grid, default_char='.'):
  """Print the grid"""
  x_all = [x for x, y in grid]
  y_all = [y for x, y in grid]
  min_x = min(x_all)
  min_y = min(y_all)
  max_x = max(x_all)
  max_y = max(y_all)
  for y in range(min_y, max_y + 1):
    row_str = ''
    for x in range(min_x, max_x + 1):
      row_str += f'{str(grid.get((x, y), default_char)):>4}'
    print(row_str)


def Neighbors(coords, grid):
  """Returns a list of neighboring coordinates, only those on the grid,
     and only those that are a legal next move. Excludes diagonals.
  """
  x, y = coords
  potential_neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
  return [c for c in potential_neighbors if c in grid and
          ord(grid[c]) - 1 <= ord(grid[coords])]


def CostGrid(grid, start, destination):
  """Borrowed code from 2021 Day 15. Dijkstras but, all edge values are 1.
     This will raise one of two exceptions if the destination is not
     reachable from the start: IndexError or UnboundLocalError.
     Do not copy this function -- use 2021 Day 15 instead, it is more generic.
  """
  cost_grid = {start: 0,}
  priority_q = [(0, start),]
  while destination not in cost_grid:
    current_val, cell = heappop(priority_q)
    neighbors = [i for i in Neighbors(cell, grid) if i not in cost_grid]
    for n in neighbors:
      cost_grid[n] = current_val + 1
      heappush(priority_q, (cost_grid[n], n))
  return cost_grid


def GetCost(grid, start, destination):
  """Calling CostGrid will return a dictionary of costs keyed on coordinate."""
  cost_grid = CostGrid(grid, start, destination)
  lowest_cost = cost_grid[destination]
  return lowest_cost


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
    except (IndexError, UnboundLocalError):
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
