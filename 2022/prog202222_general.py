#!/usr/bin/env python3
"""Solve Part 2 without hard-coding the edges."""

from copy import deepcopy
import math
from prog202222 import GetGrid, GetData, AddCoords, NewDir, GetMovement

DATA = 'data202222.txt'
# DATA = 'testdata202222.txt'


def GetTopLeftPoint(grid):
  """Just for starting out"""
  x_min = min([x for x, y in grid if y == 1])
  return x_min, 1


def PanelWidth(grid):
  """The width of one side of the cube."""
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
    return None

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
      next_point, _ = self.GetNextEdgePoint((current, heading))
      edge.append((next_point, heading))
      current = next_point
    return edge

  def Edges(self):
    """return a set of exposed edges, each edge is a list of tuples starting
    from 'start'
    """
    edges = []
    heading = 'N'
    coord = GetTopLeftPoint(self.grid)
    coord_heading = (coord, heading)
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
    """Look at last point in each edge and return stitchable pairs."""
    pairs = []
    for e in edges:
      last_point = e[-1]
      other_point = self.IsStitchable(last_point)
      if other_point:
        pairs.append((last_point, other_point))
    return pairs

  def GetOppositePairs(self, edges):
    """For part 1, get pairs of edge points on opposite sides of the shape."""
    pairs = []
    # coords to add to back away from edge
    additive = {'N': (0, 1), 'E': (-1, 0), 'S': (0, -1), 'W': (1, 0)}
    opposite = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}

    done_edges = []
    for e in edges:
      if e in done_edges:
        continue
      last_point = e[-1]
      coord, heading = last_point
      while coord in self.grid:
        prev = coord
        coord = AddCoords(coord, additive[heading])
      opposite_point = (prev, opposite[heading])
      # what edge is opposite_point in?
      opposite_edge = [i for i in edges if opposite_point in i][0]
      done_edges.append(e)
      done_edges.append(opposite_edge)
      the_pair = (last_point, (prev, opposite[heading]))
      pairs.append(the_pair)
    return pairs

  def Stitch(self, stitchable_pairs, edges):
    """Stitch edges starting at the stitchable pairs."""
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
      fewer_edges = [e for e in edges if e not in (a_list, b_list)]
      edges = fewer_edges
    return dir_map, fewer_edges

  def GenInternalMap(self, part):
    """Generate self.cube_mapping"""
    edges = self.Edges()

    if part == 'Part 2':
      acquire_pairs = self.GetStitchablePairs
    elif part == 'Part 1':
      acquire_pairs = self.GetOppositePairs
    else:
      raise Exception

    stitchable_pairs = acquire_pairs(edges)
    while stitchable_pairs and edges:
      cube_wrap_map, edges = self.Stitch(stitchable_pairs, edges)
      self.cube_mapping.update(cube_wrap_map)
      if not edges or not stitchable_pairs:
        break
      stitchable_pairs = acquire_pairs(edges)


def Move(coord_head, ew, mov):
  """Move according to mov directive"""
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


def Solve(part):
  """Solve part 1 or part 2."""
  assert part in ('Part 1', 'Part 2')
  lines = GetData(DATA)
  grid, _ = GetGrid(lines)
  movements = GetMovement(lines[-1].strip())

  ew = EdgeWalker(grid)
  ew.GenInternalMap(part)

  coord_head = (GetTopLeftPoint(grid), 'E')
  for mov in movements:
    coord_head = Move(coord_head, ew, mov)

  facing_val = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
  coord, heading = coord_head
  col, row = coord
  return 1000*row + 4*col + facing_val[heading]


def main():
  """main"""
  for part in ['Part 1', 'Part 2']:
    print(f'{part}: {Solve(part)}')


main()
