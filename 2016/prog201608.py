#!/usr/bin/python3
# file created 2023-Mar-05 16:24
"""https://adventofcode.com/2016/day/8"""

DATA = 'data201608.txt'
# DATA = 'testdata201608.txt'


class Grid():
  """A grid class that includes methods for row/column rotation."""
  def __init__(self, width=50, height=6):
    self.width = width
    self.height = height
    self.grid = {(c, r): ' ' for r in range(height) for c in range(width)}

  def Print(self):
    """Print the grid."""
    counter = 0
    for row in range(self.height):
      for col in range(self.width):
        print(f'{self.grid[(col, row)]}', end='')
        if self.grid[(col, row)] == '#':
          counter += 1
      print()
    return counter

  def Rect(self, w, h):
    """Draw a w by h rectangle in upper left corner."""
    for y in range(h):
      for x in range(w):
        self.grid[(x, y)] = '#'

  def RotCol(self, col, dist):
    """Rotate col by dist."""
    start_state = [self.grid[(col, y)] for y in range(self.height)]
    rotated = start_state[-dist:]
    rotated.extend(start_state[:len(start_state) - dist])
    for y, _ in enumerate(rotated):
      self.grid[(col, y)] = rotated[y]

  def RotRow(self, row, dist):
    """Rotate row by dist."""
    start_state = [self.grid[(x, row)] for x in range(self.width)]
    rotated = start_state[-dist:]
    rotated.extend(start_state[:len(start_state) - dist])
    for x, _ in enumerate(rotated):
      self.grid[(x, row)] = rotated[x]


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def ParseData(lines, grid):
  """Parse the lines of data and execute them."""
  for l in lines:
    tokens = l.split()
    if tokens[0] == 'rect':
      w_h = tokens[1].split('x')
      width, height = [int(i) for i in w_h]
      grid.Rect(width, height)
    else:
      dist = int(tokens[-1])
      col_row = int(tokens[2].split('=')[-1])
      func = grid.RotRow if tokens[1] == 'row' else grid.RotCol
      func(col_row, dist)


def main():
  """main"""
  lines = GetData(DATA)
  g = Grid()
  ParseData(lines, g)
  print(f'Part 1: {g.Print()}')


if __name__ == '__main__':
  main()
