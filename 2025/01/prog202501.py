#!/usr/bin/python3
# file created 2025-Nov-30 20:58
"""https://adventofcode.com/01/day/2025"""

DATA = 'data202501.txt'
# DATA = 'testdata202501.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Dest(current, direction, distance):
  """Return the destination."""
  calc_dest = (current + distance) if direction == 'R' else (current - distance)
  return calc_dest % 100


def Direction_Distance(line):
  """Parse direction and distance from data line."""
  return line[0], int(line[1:].strip())


def PassZeros(current, direction, distance):
  """How many times will this pass zero?"""
  zeros = distance // 100
  distance = distance % 100
  calc_dest = (current + distance) if direction == 'R' else (current - distance)
  if (current != 0 and calc_dest < 0) or calc_dest > 100:
    zeros += 1
  return zeros


def Solver(lines, part):
  """Solver for parts 1 and 2."""
  assert part in ['Part1', 'Part2']
  current = 50
  zeros = 0
  for line in lines:
    direction, distance = Direction_Distance(line)
    destination = Dest(current, direction, distance)
    zeros += 1 if destination == 0 else 0
    if part == 'Part2':
      zeros += PassZeros(current, direction, distance)
    current = destination
  return zeros


def Part1(lines):
  """Part 1."""
  return Solver(lines, 'Part1')


def Part2(lines):
  """Part 2."""
  return Solver(lines, 'Part2')


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
