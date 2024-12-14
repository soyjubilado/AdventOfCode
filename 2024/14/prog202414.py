#!/usr/bin/python3
# file created 2024-Dec-14 09:35
"""https://adventofcode.com/2024/day/14"""

from collections import namedtuple
from functools import reduce
from operator import mul
from time import sleep
import re

RE_XY = re.compile(r'-?\d+,-?\d+')
Coord = namedtuple('XY', 'x y')

DATA = 'data202414.txt'
GRID_DIM = Coord(101, 103)
# DATA = 'testdata202414.txt'
# GRID_DIM = Coord(11, 7)



def PrintGrid(grid, default_char='.', overlay=None):
  """Swiped from previous year."""
  # return to top left: print(f'\033[1;1f', end='')

  def MinMaxXY(grid):
    """Return min_x, max_x, min_y, max_y"""
    x_all = [x for x, y in grid]
    y_all = [y for x, y in grid]
    return min(x_all), max(x_all), min(y_all), max(y_all)

  min_x, max_x, min_y, max_y = MinMaxXY(grid)
  for y in range(min_y, max_y + 1):
    row_str = ''
    for x in range(min_x, max_x + 1):
      if overlay and (x, y) in overlay:
        row_str += overlay[(x, y)]
      else:
        row_str += f'{str(grid.get((x, y), default_char))}'
    print(row_str)




class Robot():
  """Represent a robot."""
  def __init__(self, location, velocity, grid_dimensions):
    self.location = location
    self.velocity = velocity
    self.grid_dimensions = grid_dimensions

  def __repr__(self):
    return f'R({self.location}, {self.velocity})'

  def Quadrant(self):
    """What quadrant is this robot in?"""
    x, y = self.location
    half_x, half_y = self.grid_dimensions.x//2, self.grid_dimensions.y//2
    # end_x, end_y = self.grid_dimensions.x, self.grid_dimensions.y
    if x < half_x and y < half_y:
      return 1
    if x < half_x and y > half_y:
      return 3
    if x > half_x and y < half_y:
      return 2
    if x > half_x and y > half_y:
      return 4
    return 0

  def Move(self, n=1):
    """move self n times"""
    for _ in range(n):
      self.location = AddMod(self.location, self.velocity,
                             self.grid_dimensions)
    return self.location

  def GetPeriod(self):
    """Get the period of this robot. Turns out they're all 101 * 103."""
    start = Coord(self.location.x, self.location.y)
    count = 1
    self.Move()
    while self.location != start:
      self.Move()
      count += 1
    return count


def Add(a, b):
  """Add two coordinates."""
  return Coord(a.x + b.x, a.y + b.y)


def AddMod(a, b, grid_dimensions=Coord(1, 1)):
  """Add two coordinates mod the grid dimensions."""
  return Coord((a.x + b.x) % grid_dimensions.x,
               (a.y + b.y) % grid_dimensions.y)


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def ParseLines(lines, grid_dimensions):
  """parse lines into robots"""
  robot_list = []
  for l in lines:
    location_str, velocity_str = RE_XY.findall(l)
    location = Coord(*[int(i) for i in location_str.split(',')])
    velocity = Coord(*[int(i) for i in velocity_str.split(',')])
    robot_list.append(Robot(location, velocity, grid_dimensions))
  return robot_list


def Part1(lines):
  """Part 1."""
  robots = ParseLines(lines, GRID_DIM)
  quadrant = {i: 0 for i in [0, 1, 2, 3, 4]}
  for r in robots:
    r.Move(100)
    q = r.Quadrant()
    quadrant[q] += 1
  return reduce(mul, [v for k, v in quadrant.items() if k != 0])


def EmptyGrid(char='.'):
  """Return a grid of the proper size."""
  grid = {}
  for x in range(GRID_DIM.x):
    for y in range(GRID_DIM.y):
      coord = Coord(x, y)
      grid[coord] = char
  return grid


def Quadrants(robots):
  """Return a map of the number of robots in each quadrant"""
  quadrant_map = {i: 0 for i in [0, 1, 2, 3, 4]}
  for r in robots:
    q = r.Quadrant()
    quadrant_map[q] += 1
  return quadrant_map


def Part2(lines):
  """Part 2."""
  # max 10403

  robots = ParseLines(lines, GRID_DIM)
  grid = EmptyGrid(' ')
  seconds = 0

  skip_to = 7519
  while seconds < skip_to:
    seconds += 1
    for r in robots:
      r.Move(1)

  max_iterations = 10403
  while seconds < max_iterations:
    seconds += 1
    for r in robots:
      r.Move(1)
    overlay = {r.location: '*' for r in robots}
    PrintGrid(grid, overlay=overlay)
    print(f'\n{seconds}')
    # sleep between .2 and .5
    sleep(.5)
    print(f'\033[1;1f', end='')

  return seconds


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  # print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
