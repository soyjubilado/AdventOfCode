#!/usr/bin/python3
#file created 2022-Dec-04 13:20
"""https://adventofcode.com/2016/day/1"""

DATA = 'data201601.txt'


def GetData(datafile):
  """Parse input data and return list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def NewDirection(current, turn):
  """Given a current heading an a turn, return the new heading."""
  nextdir = {('N', 'R'): 'E',
             ('N', 'L'): 'W',
             ('E', 'R'): 'S',
             ('E', 'L'): 'N',
             ('S', 'R'): 'W',
             ('S', 'L'): 'E',
             ('W', 'R'): 'N',
             ('W', 'L'): 'S',}
  return nextdir[(current, turn)]


def Walk(coords, direction, dist):
  """Given a location, direction, and distance, return coordinates of
     the new location."""
  x, y = coords
  if direction == 'N':
    return x, y + dist
  if direction == 'E':
    return x + dist, y
  if direction == 'S':
    return x, y - dist
  if direction == 'W':
    return x - dist, y
  return None


def WalkPath(coords, direction, dist):
  """Given a location, direction, and distance, return coordinates of
     all the points between the curren and new locations, inclusive."""
  x, y = coords
  if direction == 'N':
    return [(x, y+z) for z in range(1, dist+1)]
  if direction == 'E':
    return [(x+z, y) for z in range(1, dist+1)]
  if direction == 'S':
    return [(x, y-z) for z in range(1, dist+1)]
  if direction == 'W':
    return [(x-z, y) for z in range(1, dist+1)]
  return None


def Part1(all_turns):
  """all_turns is a list of all the input data split out by commas."""
  coords = (0, 0)
  heading = 'N'

  for instr in all_turns:
    turn = instr[0]
    dist = int(instr[1:])
    heading = NewDirection(heading, turn)
    coords = Walk(coords, heading, dist)
  x, y = coords
  return x, y


def Part2(all_turns):
  """all_turns is a list of all the input data split out by commas."""
  coords = (0, 0)
  heading = 'N'
  seen = [coords]
  found = False
  loc = None

  for instr in all_turns:
    turn = instr[0]
    dist = int(instr[1:])
    # print(f'facing {heading}, {coords} + {instr} -> ', end='')
    heading = NewDirection(heading, turn)
    path_coords = WalkPath(coords, heading, dist)
    coords = path_coords[-1]

    for loc in path_coords:
      if loc not in seen:
        seen.append(loc)
      else:
        found = True
        break
    if found:
      break

  x, y = loc
  return x, y


def main():
  lines = GetData(DATA)
  all_turns = []
  for l in lines:
    all_turns.extend([i.strip() for i in l.split(',')])
  x, y = Part1(all_turns)
  print(f'{x} + {y} = {x + y}')
  x, y = Part2(all_turns)
  print(f'{x} + {y} = {x + y}')


if __name__ == '__main__':
  main()
