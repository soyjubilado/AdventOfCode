#!/usr/bin/python3
#file created 2021-Dec-08 21:00
"""https://adventofcode.com/2021/day/9"""

DATA = 'data202109.txt'
# DATA = 'testdata202109.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GenGrid(lines):
  """Turns a list of lines into a dictionary."""
  grid = {}
  for y, row in enumerate(lines):
    for x, val in enumerate(row):
      grid[(x, y)] = int(val)
  return grid


def Neighbors(coords, grid):
  """Returns a list of neighboring coordinates, only those on the grid."""
  x, y = coords
  potential_neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
  return [c for c in potential_neighbors if c in grid]


def CountLowPoints(grid):
  risk_level = 0
  low_points = []
  for coords in grid:
    x, y = coords
    val = grid[coords]
    neighbor_vals = [grid[n] for n in Neighbors(coords, grid)]
    any_higher_neighbor_vals = [v for v in neighbor_vals if v<= val] 
    if not any_higher_neighbor_vals:
      risk_level += (val + 1)
      low_points.append(coords)
  return risk_level, low_points


def NumBasinMembers(coord, grid):

  def AddMembers(coord, grid, basin_set):
    if coord not in basin_set:
      basin_set.add(coord)
    for c in Neighbors(coord, grid):
      if grid[c] < 9 and c not in basin_set:
        AddMembers(c, grid, basin_set)

  basin = set([])
  AddMembers(coord, grid, basin)
  return len(basin)


def main():
  lines = GetData(DATA)
  grid = GenGrid(lines)
  pt1_answer, low_points = CountLowPoints(grid)
  print(f'part 1 answer: {pt1_answer}')
  all_basin_sizes = sorted([NumBasinMembers(c, grid) for c in low_points],
                           reverse=True)
  pt2_answer = 1
  for i in all_basin_sizes[0:3]:
    pt2_answer *= i
  print(f'Part 2 answer: {pt2_answer}')


if __name__ == '__main__':
  main()
