#!/usr/bin/python3
#file created 2022-Dec-07 20:59
"""https://adventofcode.com/2022/day/8"""

DATA = 'data202208.txt'
# DATA = 'testdata202208.txt'
WIDTH = None
HEIGHT = None


def GetData(datafile):
  """Parse input data."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetGrid(lines):
  """From a list of lines, return a dictionary keyed on coordinate.
     Upper left is 0,0; one to right is 1,0. This function sets the
     global variables WIDTH and HEIGHT."""
  global WIDTH
  global HEIGHT
  WIDTH = len(lines[0])
  HEIGHT = len(lines)
  grid_dict = {}
  for row, line in enumerate(lines):
    for col, value in enumerate(line):
      grid_dict[(col, row)] = value
  return grid_dict


def IsVisible(tree, grid):
  """Is a given tree visible from outside the forest."""
  x, y = tree
  tree_height = grid[tree]

  # trees on the periphery are always visible
  if x == 0 or y == 0:
    return True
  if x == WIDTH - 1 or y == HEIGHT - 1:
    return True

  # get the lines of trees to the right, left, top and bottom
  row_list = [(i, y) for i in range(WIDTH)]
  row_left = row_list[0:x]
  row_right = row_list[x+1:]
  col_list = [(x, i) for i in range(HEIGHT)]
  col_up = col_list[0:y]
  col_down = col_list[y+1:]

  # create lists of the heights of these trees
  heights_left = [grid[t] for t in row_left]
  heights_right = [grid[t] for t in row_right]
  heights_up = [grid[t] for t in col_up]
  heights_down = [grid[t] for t in col_down]

  tallest_in_each_direction = [max(heights_left), max(heights_right),
                               max(heights_up), max(heights_down)]

  # if the shortest of the tallest trees in all directions is shorter
  # than the current tree, the current tree is visible from somewhere.

  if min(tallest_in_each_direction) < tree_height:
    return True
  return False


def Scenicity(tree, grid):
  """How scenic is a given tree?"""
  x, y = tree
  tree_height = grid[tree]
  right = left = up = down = 0

  # right
  for col in range(x+1, WIDTH):
    right += 1
    if grid[(col, y)] >= tree_height:
      break
  # left
  for col in range(x-1, -1, -1):
    left += 1
    if grid[(col, y)] >= tree_height:
      break
  # down
  for row in range(y+1, HEIGHT):
    down += 1
    if grid[(x, row)] >= tree_height:
      break
  # up
  for row in range(y-1, -1, -1):
    up += 1
    if grid[(x, row)] >= tree_height:
      break
  return up * left * right * down


def Part1(grid):
  """Total number of visible trees."""
  num_visible = 0
  for tree in grid:
    if IsVisible(tree, grid):
      num_visible += 1
  print(f'Part 1: {num_visible}')


def PrintGrid(grid):
  """(0, 0), (1, 0), (2, 0)..."""
  for y in range(WIDTH):
    for x in range(HEIGHT):
      print(grid[(x, y)], end='')
    print()


def Part2(grid):
  """Highest scenic score in the forest."""
  highest_score = 0
  for tree in sorted(grid.keys()):
    this_score = Scenicity(tree, grid)
    if this_score > highest_score:
      highest_score = this_score
  print(f'Part 2: {highest_score}')


def main():
  """main"""
  lines = GetData(DATA)
  grid = GetGrid(lines)
  Part1(grid)
  Part2(grid)


if __name__ == '__main__':
  main()
