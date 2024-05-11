#!/usr/bin/python3
#file created 2021-Dec-14 21:01
"""https://adventofcode.com/2021/day/15"""

from heapq import heappush, heappop
DATA = 'data202115.txt'
# DATA = 'testdata202115.txt'
# https://www.reddit.com/r/adventofcode/comments/rh01ay/\
# 2021_day_15_part_2_python_solution_off_by_7_but/honaac8/?context=3
# DATA = 'testdata202115ultimate.txt'


def GetData(datafile):
  """Parse input."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetGrid(lines):
  """Put input into a dictionary of coordinates."""
  grid = {}
  for row in range(len(lines)):
    for col in range(len(lines[0])):
      grid[(col, row)] = int(lines[row][col])
  return grid


def GetGrid5(lines):
  """Similar to GetGrid() but quintuple size for Part 2."""
  grid = {}
  for row in range(len(lines) * 5):
    row_iteration = row // len(lines)
    for col in range(len(lines[0] * 5)):
      col_iteration = col // len(lines[0])
      new_val = int(lines[row % len(lines)][col % len(lines[0])])
      new_val = (new_val + row_iteration + col_iteration - 1) % 9 + 1
      grid[(col, row)] = new_val
  return grid


def PrintGrid(grid, default_char='.'):
  """For debugging. This version puts spaces between the numbers."""
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
  """Returns a list of neighboring coordinates, only those on the grid.
     Excludes diagonal neighbors.
  """
  x, y = coords
  potential_neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
  return [c for c in potential_neighbors if c in grid]


def LowerRight(grid):
  """Returns the lowest rightmost value in the grid."""
  x_all = [x for x, y in grid]
  y_all = [y for x, y in grid]
  max_x = max(x_all)
  max_y = max(y_all)
  return (max_x, max_y)


def UpdateNeighbors(cell, cost_grid, grid):
  """Recursively fix neighbors if a shorter path has been found."""
  neighbors = [i for i in Neighbors(cell, grid) if i in cost_grid]
  this_cost = cost_grid[cell]
  neighbors2fix = [n for n in neighbors if cost_grid[n] > this_cost + grid[n]]
  if not neighbors2fix:
    return
  else:
    for badcell in neighbors2fix:
      cost_grid[badcell] = this_cost + grid[badcell]
      UpdateNeighbors(badcell, cost_grid, grid)


def CostGridNoDijkstra(grid, lower_right):
  """Fill out cost_grid with costs to get to each cell in grid"""
  cost_grid = {(0, 0): 0,}
  for row in range(lower_right[1] + 1):
    for col in range(lower_right[0] + 1):
      cell = (col, row)
      if cell == (0, 0):
        continue
      neighbors = [i for i in Neighbors(cell, grid) if i in cost_grid]
      this_cost = grid[cell] + min([cost_grid[c] for c in neighbors])
      cost_grid[cell] = this_cost
      # if any neighbors now have a higher cost than this cell plus its own
      # cost, update it to the cost of this cell plus the cost of itself.
      UpdateNeighbors(cell, cost_grid, grid)
  return cost_grid



def CostGrid(grid, lower_right):
  """Using Dijkstras algorithm with a priority queue."""
  cost_grid = {(0, 0): 0,}
  priority_q = [(0, (0, 0)),]
  while lower_right not in cost_grid:
    current_val, cell = heappop(priority_q)
    neighbors = [i for i in Neighbors(cell, grid) if i not in cost_grid]
    for n in neighbors:
      cost_grid[n] = current_val + grid[n]
      heappush(priority_q, (cost_grid[n], n))
    UpdateNeighbors(n, cost_grid, grid)
    # if any neighbors now have a higher cost than this cell plus its own
    # cost, update it to the cost of this cell plus the cost of itself.
  return cost_grid


def main():
  PART1 = False
  # PART1 = True
  lines = GetData(DATA)
  if PART1:
    grid = GetGrid(lines)
  else:
    grid = GetGrid5(lines)
  lower_right = LowerRight(grid)
  cost_grid = CostGrid(grid, lower_right)
  lowest_cost = cost_grid[lower_right]
  print(f'lowest cost: {lowest_cost}')


if __name__ == '__main__':
  main()
