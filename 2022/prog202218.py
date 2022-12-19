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
  """Convert input data from strings to a list of coordinates."""
  retval = []
  for line in lines:
    x, y, z = [int(i) for i in line.split(',')]
    retval.append((x, y, z))
  return retval


def Neighbors(cube):
  """The six neighbors of a cube."""
  x, y, z = cube
  return [(x + 1, y, z), (x - 1, y, z),
          (x, y + 1, z), (x, y - 1, z),
          (x, y, z + 1), (x, y, z - 1),]


def Extent(cubes):
  """Dimensions of the area in question."""
  x_max = y_max = z_max = -float('inf')
  x_min = y_min = z_min = float('inf')
  for x, y, z in cubes:
    x_max = max([x, x_max]) + 1
    y_max = max([y, y_max]) + 1
    z_max = max([z, z_max]) + 1
    x_min = min([x, x_min]) - 1
    y_min = min([y, y_min]) - 1
    z_min = min([z, z_min]) - 1
  return x_min, x_max, y_min, y_max, z_min, z_max


def AbutsCube(point, cubes):
  """True if one of point's neighbors, or neighbors neighbors, is in cubes."""
  cube_neighbors = [n for n in Neighbors(point) if n in cubes]
  if len(cube_neighbors) > 0:
    return True

  non_cube_neighbors = {n for n in Neighbors(point) if n not in cubes}
  for n in non_cube_neighbors:
    cube_neighbors = [c for c in Neighbors(n) if c in cubes]
    if len(cube_neighbors) > 0:
      return True
  return False


def GetNeighborsYSurfaces(point, cubes):
  """Starting with a point just outside cubes, but touching a cube in cubes,
     get all its neighbors who either touch the cube or who have a neighbor
     that touches the cube ."""
  all_neighbors = Neighbors(point)
  neighbors = [n for n in all_neighbors if n not in cubes and
               AbutsCube(n, cubes)]
  surfaces = len([n for n in all_neighbors if n in cubes])
  return neighbors, surfaces


def FindStart(cubes):
  """Find a cube that is on the outside. Return the empty space adjacent
     to that cube, on the outside of the droplet."""
  x, y, z = cubes[0]
  x_all = sorted([n for n in cubes if n[1] == y and n[2] == z])
  x, y, z = x_all[0]
  start = x-1, y, z
  assert start not in cubes
  return start


def Part1(cubes):
  """Brute force: Look at every cube. Look at all its neighbors. For every
     neighbor that it has, subtract one from the number of sides of that cube.
     Add the total number of sides up."""
  total_sides = 0
  for cube in cubes:
    neighbors = Neighbors(cube)
    sides = 6
    for n in neighbors:
      if n in cubes:
        sides -= 1
    total_sides += sides
  return total_sides


def Part2(cubes):
  """Start at a point abutting the drop. Slowly expand a shroud around the
     drop by adding points to the points along the edge. Keep track of the
     number of shared sides between the shroud and the drop. After there are
     no more points to add to the shroud, you're done.
  """
  surface_area = 0
  shroud = []
  frontier = []
  start = FindStart(cubes)
  frontier.append(start)
  shroud.append(start)
  while frontier:
    point = frontier.pop()
    neighbors, surfaces = GetNeighborsYSurfaces(point, cubes)
    frontier.extend([n for n in neighbors if n not in shroud])
    shroud.extend(neighbors)
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
