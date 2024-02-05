#!/usr/bin/python3
# file created 2022-Dec-18 06:38
"""https://adventofcode.com/2022/day/18"""

DATA = 'data202218.txt'
# DATA = 'testdata202218.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetCubes(lines):
  """Convert input data into a list of coordinates."""
  retval = []
  for line in lines:
    x, y, z = [int(i) for i in line.split(',')]
    retval.append((x, y, z))
  return retval


def Neighbors(cube):
  """Given a point return list of neighbors on 6 sides (no diagonals)."""
  x, y, z = cube
  return [(x + 1, y, z), (x - 1, y, z),
          (x, y + 1, z), (x, y - 1, z),
          (x, y, z + 1), (x, y, z - 1),]


def Extent(cubes):
  """By looking at the min/max coordinate in every direction, figure out the
     coordinates of a box needed to contain the drop."""
  x_max = y_max = z_max = -float('inf')
  x_min = y_min = z_min = float('inf')
  for c in cubes:
    x, y, z = c
    x_max = max([x, x_max])
    y_max = max([y, y_max])
    z_max = max([z, z_max])
    x_min = min([x, x_min])
    y_min = min([y, y_min])
    z_min = min([z, z_min])
  return x_min - 2, x_max + 2, y_min - 2, y_max + 2, z_min - 2, z_max + 2


def BuildBox(x_min, x_max, y_min, y_max, z_min, z_max):
  """Build a box to contain the droplet. Returns a set of coordinates
     representing 6 sides of the box."""
  box = set([])
  for x in range(x_min, x_max + 1):
    for y in range(y_min, y_max + 1):
      box.add((x, y, z_min))
      box.add((x, y, z_max))
  for y in range(y_min, y_max + 1):
    for z in range(z_min, z_max + 1):
      box.add((x_min, y, z))
      box.add((x_max, y, z))
  for z in range(z_min, z_max + 1):
    for x in range(x_min, x_max + 1):
      box.add((x, y_min, z))
      box.add((x, y_max, z))
  return box


def Part1(cubes):
  """Count the cubes, subtract sides that are shared with a neighbor."""
  total_sides = 0
  for cube in cubes:
    neighbors = Neighbors(cube)
    sides = 6
    for n in neighbors:
      if n in cubes:
        sides -= 1
    total_sides += sides
  return total_sides


def GetNeighborsYSurfaces(point, box, cubes):
  """Given a point, a box containing the drop, and the set of cubes in the
     droplet, return the neighbors to that point and the number of surfaces
     shared with the droplet."""
  all_neighbors = Neighbors(point)
  neighbors = [n for n in all_neighbors if n not in box and n not in cubes]
  surfaces = len([n for n in all_neighbors if n in cubes])
  return neighbors, surfaces


def Part2(cubes):
  """Build a box around the droplet, flood fill it, and count the number of
     point sides shared with the droplet."""
  x_min, x_max, y_min, y_max, z_min, z_max = Extent(cubes)
  box = BuildBox(x_min, x_max, y_min, y_max, z_min, z_max)

  # flood fill the box
  surface_area = 0
  frontier = []
  start = (x_min + 1, y_min + 1, z_min + 1)
  frontier.append(start)
  while frontier:
    point = frontier.pop()
    neighbors, surfaces = GetNeighborsYSurfaces(point, box, cubes)
    for n in neighbors:
      box.add(n)
    frontier.extend(neighbors)
    surface_area += surfaces
  return surface_area


def main():
  """main"""
  lines = GetData(DATA)
  cubes = GetCubes(lines)
  print(f'Part 1: {Part1(cubes)}')
  print(f'Part 2: {Part2(cubes)}')


if __name__ == '__main__':
  main()
