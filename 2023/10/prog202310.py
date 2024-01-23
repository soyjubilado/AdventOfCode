#!/usr/bin/python3
# file created 2023-Dec-10 08:48
"""https://adventofcode.com/2023/day/10"""

import sys
sys.path.insert(0, '../lib/')
from grid import Grid, PrintGrid

DATA = 'data202310.txt'
# DATA = 'testdata202310.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def OpenDirection(char, direction):
  """Return true if a cell is open in a certain direction."""
  if char is None:
    return False
  openness = {'north': lambda c: c in ['|', 'L', 'J'],
              'east': lambda c: c in ['-', 'L', 'F'],
              'south': lambda c: c in ['|', 'F', '7'],
              'west': lambda c: c in ['-', 'J', '7']}
  return openness[direction](char)


def Neighbor(coord, grid, direction):
  """Given coordinate, grid, and direction, return the neighbor in that
     direction if the neighbor exists in the grid."""
  x, y = coord
  compass = {'west': lambda x, y: (x-1, y),
             'east': lambda x, y: (x+1, y),
             'south': lambda x, y: (x, y+1),
             'north': lambda x, y: (x, y-1)}
  candidate = compass[direction](x, y)
  if candidate in grid:
    return candidate
  return None


def Opposite(char):
  """Given a direction, return the opposite."""
  opposites = {'north': 'south',
               'east': 'west',
               'south': 'north',
               'west': 'east'}
  return opposites[char]


def InferStartChar(coord, grid):
  """Given the coordinate of the 'S' infer the character there."""
  openness = []
  for d in ['north', 'east', 'south', 'west']:
    neighbor = Neighbor(coord, grid, d)
    if neighbor is None:
      op = False
    else:
      op = OpenDirection(grid[neighbor], Opposite(d))
    openness.append(op)
  openness_map = {(True, False, True, False): '|',
                  (True, False, False, True): 'J',
                  (True, True, False, False): 'L',
                  (False, True, True, False): 'F',
                  (False, True, False, True): '-',
                  (False, False, True, True): '7',
                 }
  return openness_map[tuple(openness)]


def StartOf(grid):
  """Locate start coordinate."""
  start = [c for c, v in grid.items() if v == 'S']
  assert len(start) == 1
  return start[0]


def StartDirection(start, grid):
  """Given the starting coordinate, return the first open direction."""
  for d in ['north', 'east', 'south', 'west']:
    if OpenDirection(grid[start], d):
      return d
  raise Exception


def NextDirection(coord, grid, prev_direction):
  """Given coordinate and previous direction, pick next direction."""
  me = grid[coord]
  for d in ['north', 'east', 'south', 'west']:
    if d != Opposite(prev_direction) and OpenDirection(me, d):
      return d
  return None


def PathCells(grid):
  """Return a list of all the cells in the path.
     GRID IS MODIFIED in that the 'S' of the start cell is replaced
     by the real character that is there via InferStartChar().
  """
  path_cells = []
  start = StartOf(grid)
  path_cells.append(start)
  start_char = InferStartChar(start, grid)
  # print(f'Replacing start character with {start_char}')
  grid[start] = start_char
  direction = StartDirection(start, grid)
  prev_coord = start
  current_coord = Neighbor(prev_coord, grid, direction)
  while current_coord != start:
    path_cells.append(current_coord)
    prev_coord = current_coord
    direction = NextDirection(current_coord, grid, direction)
    current_coord = Neighbor(prev_coord, grid, direction)
  return path_cells


def Part1(grid):
  """Part 1"""
  return (len(PathCells(grid)) + 1)//2


def LeftRightFrom(symbol, direction):
  """When you enter a cell with given symbol from 'direction', what
     directions are on the left side of the path, and what ones are on
     the right?  Returns a tuple of two lists, one of which may be
     empty."""
  assert symbol in ['F', 'J', 'L', '7', '|', '-']
  assert direction in ['north', 'east', 'south', 'west']
  answer = {('F', 'south'): (['west', 'north'], []),
            ('F', 'east'): ([], ['west', 'north']),
            ('J', 'west'): ([], ['south', 'east']),
            ('J', 'north'): (['south', 'east'], []),
            ('L', 'north'): ([], ['west', 'south']),
            ('L', 'east'): (['west', 'south'], []),
            ('7', 'west'): (['north', 'east'], []),
            ('7', 'south'): ([], ['north', 'east']),
            ('|', 'south'): (['west'], ['east']),
            ('|', 'north'): (['east'], ['west']),
            ('-', 'west'): (['north'], ['south']),
            ('-', 'east'): (['south'], ['north']),
           }
  return answer[(symbol, direction)]


class Explorer():
  """Explorer class to obviate global variables."""

  def __init__(self, grid):
    """Initialize the class."""
    self.grid = grid
    self.start = StartOf(grid)
    self.path_cells = PathCells(grid)
    self.inside_side = None
    self.end_seen = False

  def GetPoints(self, coord, d, grid, path_cells):
    """From a given coord, radiate out in direction d until you hit the
       end of the grid or a cell in path_cells. Return a list of all the
       points you traversed.
    """
    points = []
    cell = coord
    neighbor = Neighbor(cell, grid, d)
    while neighbor and neighbor not in path_cells:
      points.append(neighbor)
      cell = neighbor
      neighbor = Neighbor(cell, grid, d)
    self.end_seen = neighbor is None
    return points

  def Explore(self, coord, left_right, grid, path_cells):
    """Explore outwards from cell until you hit either another part of the
       path or the edge of the grid.
    Args:
      coord: tuple (int, int) starting coordinate
      left_right: tuple ([dir, dir], [dir, dir])
      grid: dict {coord: symbol}
      path_cells: dict {coord: symbol}
    Returns:
      tuple of two lists: ([left points], [right points])
    """
    left_points = []
    right_points = []
    left_dirs, right_dirs = left_right
    for d in left_dirs:
      if self.inside_side == 'right':
        continue
      left_points.extend(self.GetPoints(coord, d, grid, path_cells))
      if self.inside_side is None and self.end_seen:
        self.inside_side = 'right'
    for d in right_dirs:
      if self.inside_side == 'left':
        continue
      right_points.extend(self.GetPoints(coord, d, grid, path_cells))
      if self.inside_side is None and self.end_seen:
        self.inside_side = 'left'
    return left_points, right_points

  def InnerPoints(self):
    """Part 2: walk the path. At each cell, travel away from the cell
       on the left side and the right side until you reach either the edge of
       the world or another path cell. Collect all the points along the way
       into a left and right collection. Once the inner side is known (left or
       right) stop collecting information for the other side.
       Return the number of points on the inner side.
    """
    direction = StartDirection(self.start, self.grid)
    prev_coord = self.start
    current_coord = Neighbor(prev_coord, self.grid, direction)
    left_points = []
    right_points = []

    while current_coord != self.start:
      symbol = self.grid[current_coord]
      add_left, add_right = self.Explore(current_coord,
                                         LeftRightFrom(symbol,
                                                       Opposite(direction)
                                                      ),
                                         self.grid,
                                         self.path_cells
                                        )
      left_points.extend(add_left)
      right_points.extend(add_right)
      prev_coord = current_coord
      direction = NextDirection(current_coord, self.grid, direction)
      current_coord = Neighbor(prev_coord, self.grid, direction)

    assert self.inside_side in ['left', 'right']
    if self.inside_side == 'right':
      return len(set(right_points))
    return len(set(left_points))


def Part2(grid):
  """Part 2"""
  explorer = Explorer(grid)
  return explorer.InnerPoints()


def main():
  """main"""
  lines = GetData(DATA)
  grid = Grid(lines)
  print(f'Part 1: {Part1(grid)}')
  grid = Grid(lines)
  print(f'Part 2: {Part2(grid)}')


if __name__ == '__main__':
  main()
