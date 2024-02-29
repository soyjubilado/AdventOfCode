#!/usr/bin/python3
# file created 2024-Feb-27 16:39
"""https://adventofcode.com/2023/day/16"""

from grid import GridWrap, MinMaxXY

DATA = 'data202316.txt'
# DATA = 'testdata202316.txt'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


class Beam():
  """Represents a beam moving through the grid."""

  def __init__(self, grid, start, direction, visited=None):
    self.grid = grid
    self.current = start
    self.direction = direction
    self.sub_beams = []
    self.finished = False
    if visited:
      self.visited = visited
    else:
      self.visited = set([])
    if start in grid:
      self.visited.add((start, direction))
    self.looped = False

  def __str__(self):
    return f'{self.current} {self.direction} {self.grid[self.current]}'

  def next_cell(self):
    """From the current cell and direction, what's the next cell."""
    motion = {NORTH: lambda x, y: (x, y - 1),
              SOUTH: lambda x, y: (x, y + 1),
              EAST: lambda x, y: (x + 1, y),
              WEST: lambda x, y: (x - 1, y),}
    return motion[self.direction](*self.current)

  def set_done(self):
    """Set state if beam is finished."""
    self.finished = True

  def move_one(self):
    """Move self one cell."""
    if self.finished:
      return

    next_cell = self.next_cell()
    # went off grid
    if next_cell not in self.grid:
      self.set_done()
      return

    # loop detected
    if (next_cell, self.direction) in self.visited:
      self.set_done()
      return

    # next cell is valid
    assert next_cell in self.grid
    self.visited.add((next_cell, self.direction))
    self.current = next_cell
    cell_char = self.grid[next_cell]
    self.direction, sub_beam = self.new_dir_y_subbeam(cell_char)
    if sub_beam:
      self.sub_beams.append(sub_beam)

  def move_all(self, depth=0):
    """Move beam until it finishes."""
    while not self.finished:
      self.move_one()
    for b in self.sub_beams:
      b.move_all(depth=depth + 1)

  def new_dir_y_subbeam(self, cell_char):
    """Return new direction and subbeam if any."""
    dir_map = {'/': {NORTH: EAST, SOUTH: WEST, EAST: NORTH, WEST: SOUTH},
               '\\': {NORTH: WEST, SOUTH: EAST, EAST: SOUTH, WEST: NORTH},
               '|': {NORTH: NORTH, SOUTH: SOUTH, EAST: SOUTH, WEST: NORTH},
               '-': {NORTH: EAST, SOUTH: WEST, EAST: EAST, WEST: WEST},
               '.': {NORTH: NORTH, SOUTH: SOUTH, EAST: EAST, WEST: WEST},
              }
    sb_dir = {'/': {NORTH: None, SOUTH: None, EAST: None, WEST: None},
              '\\': {NORTH: None, SOUTH: None, EAST: None, WEST: None},
              '.': {NORTH: None, SOUTH: None, EAST: None, WEST: None},
              '|': {NORTH: None, SOUTH: None, EAST: NORTH, WEST: SOUTH},
              '-': {NORTH: WEST, SOUTH: EAST, EAST: None, WEST: None},
             }
    new_direction = dir_map[cell_char][self.direction]
    subbeam_direction = sb_dir[cell_char][self.direction]
    if subbeam_direction:
      sub_beam = Beam(self.grid, self.current, subbeam_direction,
                      visited=self.visited)
    else:
      sub_beam = None
    return new_direction, sub_beam


def Part2(grid):
  """Part 2"""
  _, max_x, _, max_y = MinMaxXY(grid)
  top = [((x, -1), SOUTH) for x in range(max_x + 1)]
  left = [((-1, y), EAST) for y in range(max_y + 1)]
  bottom = [((x, max_y+1), NORTH) for x in range(max_x + 1)]
  right = [((max_x+1, y), WEST) for y in range(max_y + 1)]
  all_starts = []
  all_starts.extend(top)
  all_starts.extend(left)
  all_starts.extend(bottom)
  all_starts.extend(right)
  max_energized = 0
  num_starts = len(all_starts)
  counter = 0
  for start, direction in all_starts:
    num_energized = Part1(grid, start, direction)
    max_energized = max(num_energized, max_energized)
    counter += 1
    print(f'{counter} of {num_starts}')
  return max_energized


def Part1(grid, start, direction):
  """Part 1"""
  beam = Beam(grid, start, direction)
  beam.move_all()
  deduped = set(c for c, _ in beam.visited)
  return len(deduped)


def main():
  """main"""
  lines = GetData(DATA)
  grid = GridWrap(lines)
  print(f'Part 1: {Part1(grid, (-1, 0), EAST)}')
  # print(f'Part 2: {Part2(grid)}')


if __name__ == '__main__':
  main()
