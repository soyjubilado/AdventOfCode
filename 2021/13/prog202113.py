#!/usr/bin/python3
#file created 2021-Dec-12 21:00
"""https://adventofcode.com/2021/day/13"""

DOT = '#'
DATA = 'data202113.txt'
# DATA = 'testdata202113.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetGrid(gridlines):
  gdict = {}
  for line in gridlines:
    x, y = [int(i) for i in line.split(',')]
    gdict[(x, y)] = DOT
  return gdict


def PrintGrid(grid, default_char='.'):
  x_all = [x for x, y in grid]
  y_all = [y for x, y in grid]
  min_x = min(x_all)
  min_y = min(y_all)
  max_x = max(x_all)
  max_y = max(y_all)
  for y in range(min_y, max_y + 1):
    row_str = ''
    for x in range(min_x, max_x + 1):
      row_str += grid.get((x, y), default_char)
    print(row_str)


def FoldUp(grid, y_line):
  removals = []
  add_grid = []
  for x, y in grid:
    if y > y_line:
      if grid[(x, y)] == DOT:
        add_grid.append((x, 2 * y_line - y))
      removals.append((x, y))
    elif y == y_line:
      removals.append((x, y))

  for x, y in add_grid:
    grid[(x, y)] = DOT
  for x, y in removals:
    del(grid[(x, y)])


def FoldLeft(grid, x_line):
  removals = []
  add_grid = []
  for x, y in grid:
    if x > x_line:
      if grid[(x, y)] == DOT:
        add_grid.append((2 * x_line - x, y))
      removals.append((x, y))
    elif x == x_line:
      removals.append((x, y))

  for x, y in add_grid:
    grid[(x, y)] = DOT
  for x, y in removals:
    del(grid[(x, y)])


def FoldGrid(grid, instruction):
  direction, axis = instruction.split('=')
  if direction == 'fold along x':
    FoldLeft(grid, int(axis))
  elif direction == 'fold along y':
    FoldUp(grid, int(axis))
  else:
    raise Exception


def main():
  lines = GetData(DATA)
  split_idx = lines.index('')
  gridlines = lines[:split_idx]
  instructions = lines[split_idx+1:]
  grid = GetGrid(gridlines)

  for instruction in instructions:
    FoldGrid(grid, instruction)
    print(f'dots left: {sum([1 for n in grid.values() if n == DOT])}')
  PrintGrid(grid)


if __name__ == '__main__':
  main()
