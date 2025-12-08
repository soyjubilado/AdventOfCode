#!/usr/bin/python3
# file created 2025-Dec-07 09:18
"""https://adventofcode.com/2025/day/07"""

from functools import lru_cache
import grid as g


DATA = 'data202507.txt'
# DATA = 'testdata202507.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def SplitterClosure(my_grid):
  """Use a closure to avoid a global my_grid."""

  @lru_cache(maxsize=None)
  def HitSplitterFunc(coord):
    """Starting on the grid from the current coordinate, return the set of
       beam splitters that it hits."""
    x, y = coord
    next_y = y + 1
    while (x, next_y) in my_grid and my_grid[(x, next_y)] != '^':
      next_y += 1

    if (x, next_y) not in my_grid:
      return set()
    splitter_coord = (x, next_y)
    left = (x - 1, next_y)
    right = (x + 1, next_y)
    answer = set()
    answer.add(splitter_coord)
    answer = answer.union(HitSplitterFunc(left))
    answer = answer.union(HitSplitterFunc(right))
    return answer

  return HitSplitterFunc


def PathsToHereClosure(grid, splitters):
  """Using a closure to avoid global grid and splitters list."""

  @lru_cache(maxsize=None)
  def PathsToHere(coord):
    """For a given xy coordinate, how many paths end here?"""
    x, y = coord
    paths = 0
    y -= 1
    above = (x, y)
    while above in grid and grid[above] == '.':
      above_right = (x+1, y)
      above_left = (x-1, y)
      if above_right in splitters:
        xx, yy = above_right
        paths += PathsToHere((xx, yy-1))
      if above_left in splitters:
        xx, yy = above_left
        paths += PathsToHere((xx, yy-1))
      y -= 1
      above = (x, y)

    if above in grid and grid[above] == 'S':
      paths += 1
    return paths

  return PathsToHere


def Part1(my_grid):
  """Part 1."""
  start = [c for c, v in my_grid.items() if v == 'S'][0]
  splitters_hit = SplitterClosure(my_grid)(start)
  return splitters_hit


def Part2(my_grid, splitters):
  """Part 2."""
  _, max_x, _, max_y = g.MinMaxXY(my_grid)
  bottom_row = [(x, max_y) for x in range(max_x + 1)]
  total = 0
  for coord in bottom_row:
    paths_to_here = PathsToHereClosure(my_grid, splitters)(coord)
    # print(f'{coord}: {paths_to_here}')
    total += paths_to_here
  return total


def main():
  """main"""
  lines = GetData(DATA)
  my_grid = g.Grid(lines)
  splitters = Part1(my_grid)
  print(f'Part 1: {len(splitters)}')
  print(f'Part 2: {Part2(my_grid, splitters)}')


if __name__ == '__main__':
  main()
