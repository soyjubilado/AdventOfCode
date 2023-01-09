#!/usr/bin/env python3

from copy import deepcopy
import time
import math
from prog202222 import GetGrid, GetData, PrintGrid, AddCoords
from prog202222 import NewDir, GetMovement

DATA = 'data202222.txt'
# DATA = 'testdata202222.txt'


def GetTopLeftPoint(grid):
  """Just for starting out"""
  x_min = min([x for x, y in grid if y == 1])
  return x_min, 1


def PanelWidth(grid):
  panel_width = int(math.sqrt(len(grid) // 6))
  assert (panel_width**2) * 6 == len(grid)
  return panel_width


class EdgeWalker():
  """A class to walk and stitch the edges."""
  def __init__(self, grid):
    self.grid = deepcopy(grid)
    self.cube_mapping = {}

  def NextSpot(self, coord_head):
    """Not the same NextSpot as part 1"""
    coord, heading = coord_head
    additive = {'N': (0, -1),
                'E': (1, 0),
                'S': (0, 1),
                'W': (-1, 0)}
    if coord_head in self.cube_mapping:
      return self.cube_mapping[coord_head]
    spot = AddCoords(coord, additive[heading])
    return spot, heading

  def GetNextEdgePoint(self, coord_heading):
    """Get the next clockwise spot along the edge, and the direction facing
       out. For outer corners, the next spot is the same spot with a new
       orientation.
    Args:
      coord_heading: tuple: ((x, y), 'H')
      max_coord: tuple:  (x_max, y_max)

    Returns:
      ((x, y), 'H')

    """
    # These addends will move one spot to the right depending on your
    # heading.
    coord, heading = coord_heading
    x, y = coord
    additive = {'N': (1, 0), 'E': (0, 1), 'S': (-1, 0), 'W': (0, -1)}
    new_coords = AddCoords(coord, additive[heading])

    # if normal spot
    next_spot, _ = self.NextSpot((new_coords, heading))
    if new_coords in self.grid and self.grid.get(next_spot, ' ') == ' ':
      return new_coords, heading

    # if it's an outer corner, use old coords but change heading
    if new_coords not in self.grid:
      turn_right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
      return coord, turn_right[heading]
    
    # if it's an inner corner, move forward, then turn left for heading
    next_spot, _ = self.NextSpot((new_coords, heading))
    if next_spot in self.grid and self.grid[next_spot] != ' ':
      turn_left = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
      return next_spot, turn_left[heading]

  def GetEdge(self, start, heading):
    """Get a single edge of a given length. An edge is a list of tuples.
    Args:
      start: tuple: (x, y)
      heading: char 'H'
      length: int
    Returns:
      [((x, y),'H'), ...]
    """
    length = PanelWidth(self.grid)
    edge = [(start, heading),]
    current = start
    for _ in range(length - 1):
      next_point, next_heading = self.GetNextEdgePoint((current, heading))
      edge.append((next_point, heading))
      current = next_point
    return edge

  def Edges(self, start, heading):
    # return a set of exposed edges, each edge is a list of tuples starting
    # from 'start'
    edges = []
    panel_width = PanelWidth(self.grid)

    coord = GetTopLeftPoint(self.grid)
    coord_heading = (coord, 'N')
    while not [e for e in edges if coord_heading in e]:
      one_edge = self.GetEdge(coord, heading)
      edges.append(one_edge)
      coord_heading = self.GetNextEdgePoint(one_edge[-1])
      coord, heading = coord_heading
    return edges

  def IsStitchable(self, coord_heading):
    """returns the other stitchable point, or None."""
    coord, heading = coord_heading
    one_right = self.NextSpot((coord, NewDir(heading, 'R')))
    coord_r, head_r = one_right
    if coord_r not in self.grid:
      return None
    up_left = self.NextSpot((coord_r, NewDir(head_r, 'L')))
    coord_l, head_l = up_left
    if coord_l not in self.grid:
      return None
    return coord_l, NewDir(head_l, 'L')

  def GetStitchablePairs(self, edges):
    pairs = []
    for e in edges:
      last_point = e[-1]
      other_point = self.IsStitchable(last_point)
      if other_point:
        pairs.append((last_point, other_point))
    return pairs

  def Stitch(self, stitchable_pairs, edges):
    dir_map = {}
    opposite = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
    if not stitchable_pairs:
      raise Exception
    if len(stitchable_pairs) == 2:
      stitchable_pairs = stitchable_pairs[0:1]
    for a, b in stitchable_pairs:
      a_list = [i for i in edges if a in i][0]
      b_list = [i for i in edges if b in i][0]
      if a_list[0] != a:
        a_list.reverse()
        assert a_list[0] == a
      if b_list[0] != b:
        b_list.reverse()
        assert b_list[0] == b
      for a1, b1 in zip(a_list, b_list):
        a_coord, a_head = a1
        b_coord, b_head = b1
        dir_map[a1] = (b_coord, opposite[b_head])
        dir_map[b1] = (a_coord, opposite[a_head])
      fewer_edges = [e for e in edges if e != a_list and e != b_list]
      edges = fewer_edges
    return dir_map, fewer_edges

def MovePt2(coord_head, ew, mov):
  facing_char = {'N': '^', 'E': '>', 'S': 'v', 'W': '<'}
  here, facing = coord_head
  if mov in ['L', 'R']:
    ew.grid[here] = facing_char[facing]
    return here, NewDir(facing, mov)

  # not L or R
  steps = int(mov)
  for _ in range(steps):
    lookahead, new_facing = ew.NextSpot((here, facing))
    if ew.grid[lookahead] != '#':
      here = lookahead
      facing = new_facing
      ew.grid[here] = facing_char[facing]
  return here, facing


def main():
  lines = GetData(DATA)
  grid, max_coord = GetGrid(lines)
  start = GetTopLeftPoint(grid)
  ew = EdgeWalker(grid)
  edges = ew.Edges(start, 'N')

  stitchable_pairs = ew.GetStitchablePairs(edges)
  while stitchable_pairs and edges:
    cube_wrap_map, edges = ew.Stitch(stitchable_pairs, edges)
    ew.cube_mapping.update(cube_wrap_map)
    if not edges or not stitchable_pairs:
      break
    start, heading = edges[0][0]
    stitchable_pairs = ew.GetStitchablePairs(edges)

  movements = GetMovement(lines[-1].strip())
  coord_head = (GetTopLeftPoint(grid), 'E')
  for mov in movements:
    coord_head = MovePt2(coord_head, ew, mov)

  facing_val = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
  coord, heading = coord_head
  col, row = coord
  print(f'Part 2: {1000*row + 4*col + facing_val[heading]}')


main()
