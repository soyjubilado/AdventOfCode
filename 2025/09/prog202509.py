#!/usr/bin/python3
# file created 2025-Dec-09 06:43
"""https://adventofcode.com/2025/day/9"""

from itertools import combinations
DATA = 'data202509.txt'
# DATA = 'testdata202509.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
    points = [tuple(map(int, p.split(','))) for p in lines]
  return points


def Rectangle(pair):
  """Area of a rectangle using this pair of coordinates."""
  (x1, y1), (x2, y2) = pair
  return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


def Part1(points):
  """Part 1."""
  pairs = combinations(points, 2)
  return max(map(Rectangle, pairs))


def Part2(lines):
  """Part 2."""
  return None


def exploration(points):
  # ensure that it is one continuous cycle
  last = points[-1]
  for i, p in enumerate(points):
    print(i, end=' ')
    assert (last[0] == p[0]) or (last[1] == p[1])
    last = p

  # inspection of data shows that some points are inline with others.

  # how big is the mess?
  xs = [i[0] for i in points]
  ys = [i[1] for i in points]
  min_x = min(xs)
  max_x = max(xs)
  min_y = min(ys)
  max_y = max(ys)
  length = max_x - min_x
  height = max_y - min_y
  area = length * height
  print(f'\nsize of shape is {length} by {height} -> {area}')


def main():
  """main"""
  points = GetData(DATA)
  # print(f'Part 1: {Part1(points)}')
  # print(f'Part 2: {Part2(points)}')
  exploration(points)


if __name__ == '__main__':
  main()
