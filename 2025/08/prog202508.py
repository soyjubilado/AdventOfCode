#!/usr/bin/python3
# file created 2025-Dec-08 07:52
"""https://adventofcode.com/2025/day/8"""

from itertools import combinations

DATA = 'data202508.txt'
# DATA = 'testdata202508.txt'
TESTDATA = 'testdata202508.txt'



def GetData(datafile):
  """Read input into a list of lines."""
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def LinesToTuples(lines):
  """Convert input lines to tuples of ints."""
  return [tuple(map(int, line.split(','))) for line in lines]


def Distance3d(two_coordinates):
  """Compute euclidian distance between two points in 3-space."""
  coord1, coord2 = two_coordinates
  x1, y1, z1 = coord1
  x2, y2, z2 = coord2
  return ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**(.5)


def ShortestNPairs(boxes, howmany=None):
  """Return N pairs of boxes with the shortest distances between them."""
  pairs = combinations(boxes, 2)
  return sorted(pairs, key=Distance3d)[:howmany]


def Unite(coord_a, coord_b, coords_dict):
  """Given two coordinates and a dictionary indexed on coordinates, mutate
     the dictionary so that the entries for coord_a and coord_b both point
     to the same set, which is now a union of the two."""
  set_a = coords_dict[coord_a]
  set_b = coords_dict[coord_b]
  if set_a is not set_b:
    combined_set = set_a.union(set_b)
    for c in combined_set:
      coords_dict[c] = combined_set
    return len(combined_set)
  return len(coords_dict[coord_a])


def Part1(boxes):
  """Part 1."""
  how_many = 10 if DATA == TESTDATA else 1000

  shortest_n = ShortestNPairs(boxes, howmany=how_many)
  coords_dict = {b: {b} for b in boxes}

  for a, b in shortest_n:
    Unite(a, b, coords_dict)

  # dedupe the sets
  final = []
  for s in coords_dict.values():
    if s not in final:
      final.append(s)

  sizes = sorted([len(i) for i in final], reverse=True)

  return sizes[0] * sizes[1] * sizes[2]


def Part2(boxes):
  """Part 2."""
  num_boxes = len(boxes)
  pairs = ShortestNPairs(boxes)
  coords_dict = {b: {b} for b in boxes}

  counter = 0
  for a, b in pairs:
    counter += 1
    union_size = Unite(a, b, coords_dict)
    if union_size == num_boxes:
      x1, _, _ = a
      x2, _, _ = b
      break

  return x1 * x2


def main():
  """main"""
  boxes = LinesToTuples(GetData(DATA))
  print(f'Part 1: {Part1(boxes)}')
  print(f'Part 2: {Part2(boxes)}')


if __name__ == '__main__':
  main()
