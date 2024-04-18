#!/usr/bin/python3
#file created 2022-Feb-21 14:54
"""https://adventofcode.com/2015/day/3"""

from collections import defaultdict
DATA = 'data201503.txt'
#DATA = 'testdata201503.txt'


def GetData(datafile):
  """Return first line of input data."""
  with open(datafile, 'r') as fh:
    all_input = next(fh).strip()
  return all_input


def NextLocation(coord, step):
  """Given a coordinate and a direction step, return the next coordinate."""
  x, y = coord
  if step == '<':
    x -= 1
  elif step == '>':
    x += 1
  elif step == '^':
    y += 1
  elif step == 'v':
    y -= 1
  else:
    raise Exception
  return (x, y)


def ListHouses(route):
  """Given a list of steps, return all the houses on the route."""
  all_houses = defaultdict(lambda: 0)
  last_loc = (0, 0)
  all_houses[last_loc] += 1
  for step in route:
    next_loc = NextLocation(last_loc, step)
    all_houses[next_loc] += 1
    last_loc = next_loc
  return all_houses


def main():
  line = GetData(DATA)
  # part 1
  print(f'part 1: {len(ListHouses(line))}')

  # part 2
  santa = []
  robot = []
  for idx, i in enumerate(line):
    if idx % 2:
      robot.append(i)
    else:
      santa.append(i)
  santa_houses = ListHouses(santa)
  robot_houses = ListHouses(robot)
  all_houses = set(santa_houses.keys()).union(set(robot_houses.keys()))
  print(f'part2: {len(all_houses)}')


if __name__ == '__main__':
  main()
