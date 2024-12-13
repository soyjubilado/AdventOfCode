#!/usr/bin/python3
# file created 2024-Dec-12 07:29
"""https://adventofcode.com/2024/day/12"""

from collections import namedtuple
DATA = 'data202412.txt'
# DATA = 'testdata202412.txt'
Coord = namedtuple('XY', 'x y')

def Add(a, b):
  """Add two coordinates."""
  return Coord(a.x + b.x, a.y + b.y)


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Grid(lines):
  """Return a dictionary of coordinates."""
  grid = {}
  for y, line in enumerate(lines):
    for x, char in enumerate(line):
      grid[Coord(x, y)] = char
  return grid


def Neighbors(xy, grid=None):
  """Returns neighbors of this cell. Diagonals do not count.
     If grid is given, only return neighbors that are in the grid."""
  addends = [Coord(-1, 0),
             Coord(1, 0),
             Coord(0, 1),
             Coord(0, -1)]
  if grid is None:
    return [Add(xy, a) for a in addends]

  neighbors = []
  for a in addends:
    n = Add(xy, a)
    if n in grid:
      neighbors.append(n)
  return neighbors


def UpdateGroup(coord, grid, plant_groups, coord_to_groups):
  """Given a single coordinate, find all the other coordinates in that
     region with the same plant, and add them to a plant group, and add
     them to the coord_to_groups map.
  """
  plant = grid[coord]
  if coord in coord_to_groups:
    return

  this_group = set([coord])
  plant_group = plant_groups.get(plant, [])
  plant_group.append(this_group)
  plant_groups[plant] = plant_group

  coord_to_groups[coord] = this_group
  frontier = [n for n in Neighbors(coord, grid) if grid[n] == plant
              and n not in coord_to_groups]

  while frontier:
    coord = frontier.pop()
    coord_to_groups[coord] = this_group
    this_group.add(coord)
    frontier.extend([n for n in Neighbors(coord, grid) if grid[n] == plant
                     and n not in coord_to_groups])


def MapRegions(grid):
  """Create two dictionaries:
    {coord: set([group_the_coord_is_in])}
    {plant: [group1, group2, group3, ...]} # a list of sets

  The groups in the second dictionary are the same objects as the groups in
  the first -- they're two indices to the same data.
  """
  coord_to_group = dict()
  plant_groups = dict()
  for coord in grid:
    UpdateGroup(coord, grid, plant_groups, coord_to_group)
  return plant_groups


def PerimeterLength(plant, group, grid):
  """For part one, return the length of the perimeter of this group."""
  p = 0
  for c in group:
    p += len([n for n in Neighbors(c) if n not in grid or grid[n] != plant])
  return p


def PerimeterTiles(plant, group, grid, edge_type):
  """Edge_type will be one of ['upper', 'left', 'right', 'lower']"""
  addend = {'upper': Coord(0, -1),
            'left': Coord(-1, 0),
            'right': Coord(1, 0),
            'lower': Coord(0, 1),}[edge_type]
  answer = []
  for c in group:
    neighbor = Add(c, addend)
    if neighbor not in grid or grid[neighbor] != plant:
      answer.append(c)
  return answer


def Part1(grid):
  """Part 1."""
  total = 0
  plants = MapRegions(grid)
  for p, p_groups in plants.items():
    for group in p_groups:
      size = len(group)
      perimeter = PerimeterLength(p, group, grid)
      cost = size * perimeter
      total += size * perimeter

  return total


def SplitGroup(group, edge_type):
  """Split a group of edge candidates into contiguous ranges."""
  assert len(group) == len(set(group))
  if edge_type in ['right', 'left']:
    AreContiguous = lambda a, b: a.y + 1 == b.y
    sort_key = lambda c: c.y
  elif edge_type in ['upper', 'lower']:
    AreContiguous = lambda a, b: a.x + 1 == b.x
    sort_key = lambda c: c.x

  answer = []
  group = sorted(group, key=sort_key)
  subgroup = [group[0]]

  for next_item in group[1:]:
    if AreContiguous(subgroup[-1], next_item):
      subgroup.append(next_item)
    else:
      answer.append(subgroup)
      subgroup = [next_item]

  answer.append(subgroup)
  return answer


def CountEdges(plant, region, grid):
  """Given a plant, a region for those plants, and the grid, return the number
     of edges for that region as defined for part 2."""
  answer = 0
  for edge_type in ['upper', 'lower', 'left', 'right']:
    tiles = PerimeterTiles(plant, region, grid, edge_type)
    vertical = edge_type in ['left', 'right']
    if vertical:
      all_x = sorted(list(set(c.x for c in tiles)))
      columns = []
      for x in all_x:
        columns.append([c for c in tiles if c.x == x])
    else:
      all_y = sorted(list(set(c.y for c in tiles)))
      columns = [[c for c in tiles if c.y == y] for y in all_y]

    for c in columns:
      groups = SplitGroup(c, edge_type)
      num_edges = len(groups)
      answer += num_edges
  return answer


def Part2(grid):
  """Part 2.
  Plan for part 2:
    - get four groups of edge candidates: left, right, upper, and lower edges.
    - for each group, separate into rows or columns depending on type.
    - for each subgroup, groupify by putting contiguous tiles together.
    - the number of subgroups is the number of edges.
  """
  answer = 0
  plants = MapRegions(grid)
  for plant, plantgroups in plants.items():
    for region in plantgroups:
      area = len(region)
      edges = CountEdges(plant, region, grid)
      answer += area * edges
  return answer


def main():
  """main"""
  grid = Grid(GetData(DATA))
  print(f'Part 1: {Part1(grid)}')
  print(f'Part 2: {Part2(grid)}')


if __name__ == '__main__':
  main()
