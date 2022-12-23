#!/usr/bin/python3
# file created 2022-Dec-22 21:12
"""https://adventofcode.com/2022/day/23"""

from collections import defaultdict
DATA = 'data202223.txt'
# DATA = 'testdata202223.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def NoNeighbors(cell, grid):
  """Return True of all 8 surrounding cells are empty."""
  x, y = cell
  neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1),
               (x-1, y),             (x+1, y),
               (x-1, y+1), (x, y+1), (x+1, y+1)]
  for n in neighbors:
    if n in grid:
      return False
  return True


def ProposedCell(cell, grid, cycle):
  """Given a cell, propose a place to move based on neighbors.
     The order of neighbors examined changed depending on cycle number.
  """

  if NoNeighbors(cell, grid):
    return None

  x, y = cell
  N = [(x, y-1), (x-1, y-1), (x+1, y-1)]
  S = [(x, y+1), (x-1, y+1), (x+1, y+1)]
  W = [(x-1, y), (x-1, y-1), (x-1, y+1)]
  E = [(x+1, y), (x+1, y-1), (x+1, y+1)]
  tries = [[N, S, W, E],
           [S, W, E, N],
           [W, E, N, S],
           [E, N, S, W],]

  try_these = tries[cycle % 4]
  for t in try_these:
    empty_cells = [neighbor for neighbor in t if neighbor not in grid]
    if len(empty_cells) == 3:
      return t[0]

  return None


def PrintGrid(grid, default_char='.'):
  """Print the grid with a '+' at (500,0)."""
  x_all = [x for x, y in grid]
  y_all = [y for x, y in grid]
  min_x = min(x_all)
  min_y = min(y_all)
  max_x = max(x_all)
  max_y = max(y_all)
  for y in range(min_y, max_y + 1):
    row_str = ''
    for x in range(min_x, max_x + 1):
      row_str += f'{str(grid.get((x, y), default_char))}'
    print(row_str)


def GetGrid(lines):
  """Create a grid from the input lines."""
  grid_dict = {}
  for row, line in enumerate(lines):
    for col, char in enumerate(line):
      if char == '#':
        grid_dict[(col, row)] = char
  return grid_dict


def EmptySpace(grid):
  """Count the empty spaces in the minimum rectangle encompassing the points."""
  x_all = [x for x, y in grid]
  y_all = [y for x, y in grid]
  min_x = min(x_all)
  min_y = min(y_all)
  max_x = max(x_all)
  max_y = max(y_all)
  area = (max_x - min_x + 1) * (max_y - min_y + 1)
  return area - len(grid)


def Solve(part):
  """Part1"""
  lines = GetData(DATA)
  grid = GetGrid(lines)
  num_elves = len(grid)

  max_cycles = 10 if part == 'Part 1' else 10000
  for cycle in range(max_cycles):
    num_proposals = defaultdict(lambda: 0)
    cell_destination = {}
    for cell in grid:
      proposed_cell = ProposedCell(cell, grid, cycle)
      cell_destination[cell] = proposed_cell
      num_proposals[proposed_cell] += 1

    if num_proposals[None] == num_elves:
      print(f'Part 2: {cycle + 1}')
      return

    new_grid = {}
    for cell in grid:
      proposed_cell = cell_destination[cell]
      if proposed_cell is not None and num_proposals[proposed_cell] == 1:
        new_grid[proposed_cell] = '#'
      else:
        new_grid[cell] = '#'

    grid = new_grid
    cycle += 1

  print(f'Part 1: {EmptySpace(grid)}')
 

def main():
  """main"""
  Solve('Part 1')
  Solve('Part 2')


if __name__ == '__main__':
  main()
