#!/usr/bin/python3
# file created 2022-Dec-21 20:54
# This only works for Part 1. Part 2 needs to be debugged.
"""https://adventofcode.com/2022/day/22"""

DATA = 'data202222.txt'
# DATA = 'testdata202222.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.rstrip() for i in fh]
  return lines


def GetGrid(lines):
  """From a list of lines, return a dictionary keyed on coordinate.
     Upper left is 1,1; one to right is 2,1. Do not add a cell if it
     contains empty space."""
  grid_dict = {}
  for row, line in enumerate(lines):
    if len(line.strip()) == 0:
      break
    for col, value in enumerate(line):
      if value != ' ':
        grid_dict[(col + 1, row + 1)] = value

  max_row = len(lines) - 2
  max_col = max([len(l) for l in lines[:-3]])
  return grid_dict, (max_col, max_row)


def PrintGrid(grid, default_char = ' '):
  """Print the grid with a '+' at (500,0)."""
  assert ' ' not in grid.values()
  x_all = [x for x, y in grid]
  y_all = [y for x, y in grid]
  min_x = min(x_all)
  min_y = min(y_all)
  max_x = max(x_all)
  max_y = max(y_all)
  for y in range(min_y, max_y + 1):
    row_str = ''
    for x in range(min_x, max_x + 1):
      row_str += f'{str(grid.get((x, y), default_char))}'
    print(row_str.rstrip())


def GetMovement(line):
  """Tokenize the last line of input, which contains movement instructions."""
  line = line.replace('L', ' L ')
  line = line.replace('R', ' R ')
  linetokens = line.split()
  return linetokens


def GetStart(grid):
  """Find the starting point -- the first spot in the first row."""
  row = 1
  coords = sorted([c for c in grid if c[1] == row])
  return coords[0]


def NewDir(old_dir, turn):
  """Given a current direction and 'L' or 'R' return the new direction."""
  lookup = {('N', 'L'): 'W',
            ('E', 'L'): 'N',
            ('S', 'L'): 'E',
            ('W', 'L'): 'S',
            ('N', 'R'): 'E',
            ('E', 'R'): 'S',
            ('S', 'R'): 'W',
            ('W', 'R'): 'N',}
  return lookup[(old_dir, turn)]


def AddCoords(coord1, coord2):
  """Add two coordinates like vectors."""
  x1, y1 = coord1
  x2, y2 = coord2
  return (x1 + x2, y1 + y2)


def CubeWrap(spot, facing):
  """You hit a corner of the cube. Geometry is particular to my input."""
  x, y = spot
  # vertical movements, N S
  if 1 <= x <= 50 and facing == 'N':
    assert y == 101
    x_new = 51
    y_new = 50 + x
    facing_new = 'E'
  elif 1 <= x <= 50 and facing == 'S':
    assert y == 200
    x_new = x + 100
    y_new = 1
    facing_new = 'S'
  elif 51 <= x <= 100 and facing == 'S':
    assert y == 150
    x_new = 50
    y_new = 100 + x
    facing_new = 'W'

  elif 51 <= x <= 100 and facing == 'N':
    assert y == 1
    x_new = 1
    y_new = 100 + x
    facing_new = 'E'
  elif 101 <= x <= 150 and facing == 'S':
    assert y == 50
    x_new = 100
    y_new = x - 50
    facing_new = 'W'
  elif 101 <= x <= 150 and facing == 'N':
    assert y == 1
    x_new = x - 100
    y_new = 200
    facing_new = 'N'

  # horizontal movements, E W
  elif 1 <= y <= 50 and facing == 'E':
    assert x == 150
    x_new = 100
    y_new = 151 - y
    facing_new = 'W'
  elif 1 <= y <= 50 and facing == 'W':
    assert x == 51
    x_new = 1
    y_new = 151 - y
    facing_new = 'E'
  elif 51 <= y <= 100 and facing == 'E':
    assert x == 100
    x_new = 50 + y
    y_new = 50
    facing_new = 'N'
  elif 51 <= y <= 100 and facing == 'W':
    assert x == 51
    x_new = y - 50
    y_new = 101
    facing_new = 'S'
  elif 101 <= y <= 150 and facing == 'E':
    assert x == 100
    x_new = 150
    y_new = 151 - y
    facing_new = 'W'
  elif 101 <= y <= 150 and facing == 'W':
    assert x == 1
    x_new = 51
    y_new = 151 - y
    facing_new = 'E'
  elif 151 <= y <= 200 and facing == 'E':
    assert x == 50
    x_new = y - 100
    y_new = 150
    facing_new = 'N'
  elif 151 <= y <= 200 and facing == 'W':
    assert x == 1
    x_new = y - 100
    y_new = 1
    facing_new = 'S'
  else:
    print(f'uncaught condition: {x},{y}, {facing}')
    import sys
    sys.exit()

  return (x_new, y_new), facing_new


def NextSpot2(start, facing, grid):
  """Find the next spot, given the current spot and a direction. The next
     spot may be wrapped around."""
  x, y = start
  additive = {'N': (0, -1),
              'E': (1, 0),
              'S': (0, 1),
              'W': (-1, 0)}
  spot = AddCoords(start, additive[facing])
  # Wraparound
  if spot not in grid:
    return CubeWrap(start, facing)
  return spot, facing


def NextSpot(start, facing, grid, max_coord):
  """Find the next spot, given the current spot and a direction. The next
     spot may be wrapped around."""
  x, y = start
  max_x, max_y = max_coord
  additive = {'N': (0, -1),
              'E': (1, 0),
              'S': (0, 1),
              'W': (-1, 0)}
  spot = AddCoords(start, additive[facing])
  # Wraparound
  if spot not in grid:
    new_start_from_facing = {'N': (x, max_y),
                             'E': (0, y),
                             'S': (x, 0),
                             'W': (max_x, y),}
    spot = new_start_from_facing[facing]
    while spot not in grid:
      spot = AddCoords(spot, additive[facing])
  return spot, facing


def Move2(start, facing, mov, grid, max_coord):
  """Given a starting spot and direction, execute the mov operation, which
     is either to move forward a number of spots, or turn left or right. If
     you hit a wall, finish out the instruction by doing nothing."""
  facing_char = {'N': '^', 'E': '>', 'S': 'v', 'W': '<'}
  here = start
  grid[here] = facing_char[facing]
  if mov in ['L', 'R']:
    grid[here] = facing_char[facing]
    return here, NewDir(facing, mov)

  # not L or R
  steps = int(mov)
  for _ in range(steps):
    lookahead, facing = NextSpot2(here, facing, grid)
    if grid[lookahead] != '#':
      here = lookahead
      grid[here] = facing_char[facing]
  return here, facing


def Move(start, facing, mov, grid, max_coord):
  """Given a starting spot and direction, execute the mov operation, which
     is either to move forward a number of spots, or turn left or right. If
     you hit a wall, finish out the instruction by doing nothing."""
  facing_char = {'N': '^', 'E': '>', 'S': 'v', 'W': '<'}
  here = start
  grid[here] = facing_char[facing]
  if mov in ['L', 'R']:
    grid[here] = facing_char[facing]
    return here, NewDir(facing, mov)

  steps = int(mov)
  for _ in range(steps):
    lookahead, facing = NextSpot(here, facing, grid, max_coord)
    if grid[lookahead] != '#':
      here = lookahead
      grid[here] = facing_char[facing]
  return here, facing


def Part1():
  """part 1"""
  lines = GetData(DATA)
  grid, max_coord = GetGrid(lines)
  movements = GetMovement(lines[-1].strip())
  start = GetStart(grid)
  facing = 'E'

  for mov in movements:
    start, facing = Move(start, facing, mov, grid, max_coord)
    # print(f'{start}, {facing}')

  facing_val = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
  col, row = start
  print(f'Part 1: {1000*row + 4*col + facing_val[facing]}')
  # print(f'max coordinate: {max_coord}')


def testNextSpot2(grid):
  testcases = [ 
               [[(100, 101), 'E'], [(150, 50), 'W']],
               [[(50, 151), 'E'], [(51, 150), 'N']],
               [[(50, 200), 'S'], [(150, 1), 'S']],
               [[(100, 51), 'E'], [(101, 50), 'N']],
               [[(100, 101), 'E'], [(150, 50), 'W']],
               [[(1, 151), 'W'], [(51, 1), 'S']],
               [[(50, 101), 'N'], [(51, 100), 'E']],
               [[(1, 101), 'W'], [(51, 50), 'E']],

               [[(150, 50), 'E'], [(100, 101), 'W']],
               [[(51, 150), 'S'], [(50, 151), 'W']], 
               [[(150, 1), 'N'],  [(50, 200), 'N']], 
               [[(101, 50), 'S'], [(100, 51), 'W']], 
               [[(150, 50), 'E'], [(100, 101), 'W']],
               [[(51, 1), 'N'],   [(1, 151), 'E']],  
               [[(51, 100), 'W'], [(50, 101), 'S']], 
               [[(51, 50), 'W'],  [(1, 101), 'E']],  
              ]
  for case in testcases:
    send, expect = case
    point, facing = send
    point_ex, facing_ex = expect
    actual_point, actual_face = NextSpot2(point, facing, grid)
    passing = actual_point == point_ex and actual_face == facing_ex
    if passing:
      print(f'pass: {case}')
    else:
      print(f'fail: expected {point_ex} {facing_ex} but got '
            f'{actual_point} {actual_face}')


def Part2():
  """part 2"""
  lines = GetData(DATA)
  grid, max_coord = GetGrid(lines)
  movements = GetMovement(lines[-1].strip())
  start = GetStart(grid)
  facing = 'E'

  testNextSpot2(grid)

  for mov in movements:
    start, facing = Move2(start, facing, mov, grid, max_coord)
    # print(f'{start}, {facing}')

  facing_val = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
  col, row = start
  print(f'Part 2: {1000*row + 4*col + facing_val[facing]}')
  # 14336 is too low
  # 140395 is too high


def main():
  """main"""
  Part1()
  Part2()


if __name__ == '__main__':
  main()
