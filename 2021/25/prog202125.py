#!/usr/bin/python3
# file created 2023-Mar-28 19:14
"""https://adventofcode.com/2021/day/25"""

DATA = 'data202125.txt'
# DATA = 'testdata202125.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


class Grid():
  """A grid class to represent the world. The state of the world is maintained
     in a dictionary of coordinates. The dictionary contains the coordinates
     of the cucumbers; empty spaces are not in the dict."""

  def __init__(self, lines):
    self.height = len(lines)
    self.width = len(lines[0])
    self.occupied = self.GetOccupied(lines)

  def GetOccupied(self, lines):
    """Build the dictionary of coordinates of occupied cells."""
    occupied = {}
    for row in range(self.height):
      for col in range(self.width):
        occupant = lines[row][col]
        if occupant != '.':
          occupied[(col, row)] = occupant
    return occupied

  def OneRight(self, x, y):
    """Return the cell to the right of (x, y), wrapping if needed."""
    x = (x + 1) % self.width
    return x, y

  def OneDown(self, x, y):
    """Return the cell below (x, y), wrapping if needed."""
    y = (y + 1) % self.height
    return x, y

  def PrintSelf(self):
    """Print the state of the world."""
    for y in range(self.height):
      this_row = ''
      for x in range(self.width):
        occ = self.occupied.get((x, y), '.')
        this_row += occ
      print(this_row)

  def StepOnce(self):
    """Execute one step and mutate the occupied dictionary as needed.
       Return the number of cucumbers that moved."""
    occupied = self.occupied
    easters = [i for i in occupied if occupied[i] == '>']
    southers = [i for i in occupied if occupied[i] == 'v']

    move_easters = [i for i in easters if self.OneRight(*i) not in occupied]
    for e in move_easters:
      occupied.pop(e)
      occupied[self.OneRight(*e)] = '>'

    move_southers = [i for i in southers if self.OneDown(*i) not in occupied]
    for s in move_southers:
      occupied.pop(s)
      occupied[self.OneDown(*s)] = 'v'

    return len(move_easters) + len(move_southers)


def main():
  """main"""
  lines = GetData(DATA)
  grid = Grid(lines)

  count = 1
  moved = grid.StepOnce()
  while moved:
    count += 1
    moved = grid.StepOnce()

  print(f'The cucumbers stop moving on step {count}.')


if __name__ == '__main__':
  main()
