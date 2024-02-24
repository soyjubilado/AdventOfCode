#!/usr/bin/python3
# file created 2024-Feb-20 16:01
"""https://adventofcode.com/2023/day/13"""

from grid import Grid, MinMaxXY, PrintGrid

DATA = 'data202313.txt'
# DATA = 'testdata202313.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GenGrids(lines):
  """Given input lines, create a list of grids."""
  grids = []
  group_of_lines = []
  for line in lines:
    if line.strip():
      group_of_lines.append(line)
    else:
      grids.append(Grid(group_of_lines))
      group_of_lines = []
  grids.append(Grid(group_of_lines))
  return grids


def IsHorizReflection(grid, r_high):
  """Given a grid and a row r_high, return true if that row is the first row
     past the reflection point of a "perfect" reflection per the problem
     description.
  """
  _, max_x, _, max_y = MinMaxXY(grid)
  r_low = r_high - 1

  while r_high <= max_y and r_low >= 0:
    row_high = [grid[(x, r_high)] for x in range(max_x + 1)]
    row_low = [grid[(x, r_low)] for x in range(max_x + 1)]
    if row_high != row_low:
      return False
    r_high += 1
    r_low -= 1
  return True


def IsVertReflection(grid, c_high):
  """Given a grid and a column c_high, return true if that column is the first
     column past the reflection point of a "perfect" reflection per the problem
     description.
  """
  _, max_x, _, max_y = MinMaxXY(grid)
  c_low = c_high - 1

  while c_high <= max_x and c_low >= 0:
    col_high = [grid[(c_high, y)] for y in range(max_y + 1)]
    col_low = [grid[(c_low, y)] for y in range(max_y + 1)]
    if col_high != col_low:
      return False
    c_high += 1
    c_low -= 1
  return True


def IndexOfHorizReflection(grid):
  """Given a grid, return a list of the number of rows above the horizontal
     reflection, if there is one. If there is more than one reflection
     (possible in part 2), then the list will have more than one element. If
     there is no reflection, return [0].
  """
  min_x, max_x, min_y, max_y = MinMaxXY(grid)
  assert min_x == min_y == 0
  prev_row = [grid[(x, 1)] for x in range(max_x + 1)]
  indices = []

  for r in range(1, max_y + 1):
    row = [grid[(x, r)] for x in range(max_x + 1)]
    if row == prev_row and IsHorizReflection(grid, r):
      indices.append(r * 100)
    prev_row = row

  return indices if len(indices) > 0 else [0]


def IndexOfVertReflection(grid):
  """Given a grid, return a list of the number of columns left of the vertical
     reflection, if there is one. If there is more than one reflection
     (possible in part 2), then the list will have more than one element. If
     there is no reflection, return [0].
  """
  min_x, max_x, min_y, max_y = MinMaxXY(grid)
  assert min_x == min_y == 0
  indices = []

  prev_col = [grid[(1, y)] for y in range(max_y + 1)]

  for c in range(1, max_x + 1):
    col = [grid[(c, y)] for y in range(max_y + 1)]
    if col == prev_col and IsVertReflection(grid, c):
      indices.append(c)
    prev_col = col

  return indices if len(indices) > 0 else [0]


def Part_1(grids, verbose=False):
  """Part 1"""
  total = 0
  for g in grids:
    v = IndexOfVertReflection(g)
    vert = 0 if not v else v[0]
    h = IndexOfHorizReflection(g)
    horiz = 0 if not h else h[0]
    if verbose:
      print('-----------------------------------------------')
      print(f'{vert=} {horiz=}')
      PrintGrid(g)
      print()
    total += vert + horiz
  return total


def flip(char):
  """Flip # to . or vice versa."""
  if char == '#':
    return '.'
  if char == '.':
    return '#'
  raise Exception


def this_is_different(orig_horiz, new_horiz, orig_vert, new_vert):
  """evaluation function for determining if this is the grid we want."""
  if new_horiz == orig_horiz and new_vert == orig_vert:
    return 0

  if new_horiz == orig_horiz and new_vert != orig_vert:
    new_val = [i for i in new_vert if i not in orig_vert]
    assert len(new_val) == 1
    return new_val[0]

  if new_horiz != orig_horiz and new_vert == orig_vert:
    new_val = [i for i in new_horiz if i not in orig_horiz]
    assert len(new_val) == 1
    return new_val[0]

  raise Exception


def Part_2(grids, verbose=False):
  """Part 2"""
  total = 0
  counter = 0
  for g in grids:
    counter += 1
    orig_horiz = IndexOfHorizReflection(g)
    orig_vert = IndexOfVertReflection(g)
    for coord in g:
      g[coord] = flip(g[coord])
      new_horiz = IndexOfHorizReflection(g)
      new_vert = IndexOfVertReflection(g)
      new_val = this_is_different(orig_horiz, new_horiz, orig_vert, new_vert)
      if new_val:
        total += new_val
        if verbose:
          print('-----------------------------------------------')
          print(f'{orig_horiz=}{new_horiz=} {orig_vert=}{new_vert=} {new_val=}')
          PrintGrid(g)
          print()
        break
      g[coord] = flip(g[coord])
  return total


def main():
  """main"""
  lines = iter(GetData(DATA))
  grids = GenGrids(lines)
  print(f'Part 1: {Part_1(grids, verbose=False)}')
  print(f'Part 2: {Part_2(grids, verbose=False)}')


if __name__ == '__main__':
  main()
