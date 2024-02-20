#!/usr/bin/python3
# file created 2023-Dec-11 16:17
"""https://adventofcode.com/2023/day/11"""

from itertools import combinations
from grid import Grid, PrintGrid


DATA = 'data202311.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def EmptyRowsColumns(grid, width, height):
  """Return a list of empty rows, empty columns."""
  empty_columns = []
  empty_rows = []
  for x in range(width):
    column = [grid[(x, y)] for y in range(height)]
    if len([i for i in column if i == '#']) == 0:
      empty_columns.append(x)

  for y in range(height):
    row = [grid[(x, y)] for x in range(width)]
    if len([i for i in row if i == '#']) == 0:
      empty_rows.append(y)

  return empty_rows, empty_columns


def between(b, x1, x2):
  """True if b is between x1 and x2"""
  if x1 > x2:
    x1, x2 = x2, x1
  return x1 < b < x2


def Solver(galaxy_pairs, empty_rows, empty_columns, expansion=2):
  """Solver for both parts."""
  total = 0
  for galaxy1, galaxy2 in list(galaxy_pairs):
    x1, y1 = galaxy1
    x2, y2 = galaxy2
    distance = abs(x2 - x1) + abs(y2 - y1)
    extra_rows = sum([1 for r in empty_rows if between(r, y1, y2)])
    extra_cols = sum([1 for c in empty_columns if between(c, x1, x2)])
    distance += (expansion - 1) * (extra_rows + extra_cols)
    total += distance
  return total


def main():
  """main"""
  lines = GetData(DATA)
  width = len(lines[0])
  height = len(lines)
  grid = Grid(lines)
  PrintGrid(grid)
  empty_rows, empty_columns = EmptyRowsColumns(grid, width, height)
  galaxies = [i for i in grid if grid[i] == '#']
  galaxy_pairs = list(combinations(galaxies, 2))
  print(f'answer Pt 1: {Solver(galaxy_pairs, empty_rows, empty_columns)}')
  print(f'answer Pt 2: '
        f'{Solver(galaxy_pairs, empty_rows, empty_columns, 1000000)}')


if __name__ == '__main__':
  main()
