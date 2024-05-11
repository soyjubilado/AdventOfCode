#!/usr/bin/python3
"""https://adventofcode.com/2021/day/05"""

from collections import defaultdict
DATA = 'data05.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetLinePairs(lines):
  """Returns list of tuple tuples [((x1, y1), (x2, y2)), ((),()), ...]"""
  line_pairs = []
  for line in lines:
    coord1, _, coord2 = line.strip().split()
    c1 = (int(coord1.split(',')[0]), int(coord1.split(',')[1]))
    c2 = (int(coord2.split(',')[0]), int(coord2.split(',')[1]))
    line_pairs.append((c1, c2))
  return line_pairs


def PointsBetween(coord_tuple, part_2=False):
  """Given two points, return a list of all the points between those two
     points, inclusive. If part_2 is True, do this for diagonals too."""
  retval = []
  x1, y1 = coord_tuple[0]
  x2, y2 = coord_tuple[1]
  if x1 == x2:
    for y in range(min(y1, y2), max(y1, y2) + 1):
      retval.append((x1, y))
  elif y1 == y2:
    for x in range(min(x1, x2), max(x1, x2) + 1):
      retval.append((x, y1))
  elif part_2:
    # this is brittle if data are not valid
    xstep = 1 if x2 > x1 else -1
    ystep = 1 if y2 > y1 else -1
    x_end = x2 + 1 if xstep == 1 else x2 - 1
    y_end = y2 + 1 if ystep == 1 else y2 - 1
    x_coords = list(range(x1, x_end, xstep))
    y_coords = list(range(y1, y_end, ystep))
    assert len(x_coords) == len(y_coords)
    retval = list(zip(x_coords, y_coords))
  return retval


def testPointsBetween():
  """Unit test for PointsBetween."""
  tests = [[((1, 1), (1, 3)), [(1, 1), (1, 2), (1, 3)]],
           [((1, 1), (3, 1)), [(1, 1), (2, 1), (3, 1)]],
           [((1, 1), (3, 3)), [(1, 1), (2, 2), (3, 3)]],
           [((3, 3), (1, 1)), [(3, 3), (2, 2), (1, 1)]],
          ]

  for case in tests:
    c, expected = case
    actual = PointsBetween(c)
    passing = 'pass' if actual == expected else 'fail'
    print(f'{passing}: {c} -> {actual} (expected {expected})')


def Solver(part_2=False):
  """Solves Part 1 if part_2 == False, else solves Part 2."""
  lines = GetData(DATA)
  line_pairs = GetLinePairs(lines)
  all_points = []
  for pair in line_pairs:
    points_between = PointsBetween(pair, part_2=part_2)
    all_points.extend(points_between)

  points_dict = defaultdict(lambda: 0)
  for p in all_points:
    points_dict[p] += 1

  intersections = [i for i in points_dict if points_dict[i] > 1]
  part = '1' if not part_2 else '2'
  print(f'{len(all_points)} total points for part {part}')
  print(f'{len(intersections)} intersections in part {part}\n')


def main():
  print()
  Solver(part_2=False)
  Solver(part_2=True)


if __name__ == '__main__':
  main()
