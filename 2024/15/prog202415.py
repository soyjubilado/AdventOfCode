#!/usr/bin/python3
# file created 2024-Dec-15 08:30
"""https://adventofcode.com/2024/day/15"""
from time import sleep
from grid import Coord, Add, Grid, PrintGrid, ClearScreen, Reset

DATA = 'data202415.txt'
# DATA = 'testdata202415.txt'


def Nop(*_, **_):
  """A null function."""


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Direction(symbol):
  """Return a coordinate to add for the direction given by a symbol."""
  return {'^': Coord(0, -1),
          '>': Coord(1, 0),
          'v': Coord(0, 1),
          '<': Coord(-1, 0)}[symbol]


def ParseData(lines):
  """Parse the data into field and moves."""
  field = []
  moves = []
  for line in lines:
    if line.startswith('#'):
      field.append(line)
    elif len(line) == 0:
      pass
    else:
      moves.extend(list(line))
  return field, moves


def Move(grid, c, direction):
  """Try to move in one direction. This either a box or robot. If the
     destination is a box, and it moves, then you can move too."""
  this = grid[c]
  dest = Add(c, direction)
  if grid[dest] == '#':
    return False
  if grid[dest] == '.':
    grid[dest] = this
    grid[c] = '.'
    return True
  if grid[dest] == 'O':
    if not Move(grid, dest, direction):
      return False
    grid[dest] = this
    grid[c] = '.'
    return True
  raise Exception


def Display(grid, delay=.001):
  """Display the grid for visualization."""
  Reset()
  PrintGrid(grid)
  sleep(delay)


def MoveAll(grid, moves, visual=False):
  """Run all the moves. If visual is True, display the grid realtime."""
  if visual:
    ClearScreen()
    DisplayFunc = Display
  else:
    DisplayFunc = Nop

  robot_xy = [c for c in grid if grid[c] == '@'][0]
  for d in moves:
    if Move(grid, robot_xy, Direction(d)):
      robot_xy = Add(robot_xy, Direction(d))
      DisplayFunc(grid)

  return grid


def Part1(field, moves):
  """Part 1."""
  grid = Grid(field)
  grid = MoveAll(grid, moves)
  return sum([(100 * c.y) + c.x for c in grid if grid[c] == 'O'])


def Part2(field, moves):
  """Part 2."""
  return None


def main():
  """main"""
  lines = GetData(DATA)
  field, moves = ParseData(lines)
  print(f'Part 1: {Part1(field, moves)}')
  # print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
