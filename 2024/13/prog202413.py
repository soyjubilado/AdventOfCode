#!/usr/bin/python3
# file created 2024-Dec-13 08:17
"""https://adventofcode.com/2024/day/13"""
from collections import namedtuple
from dataclasses import dataclass
import math
import re

Coord = namedtuple('XY', 'x y')
RE_NUM = re.compile(r'\d+')
DATA = 'data202413.txt'
# DATA = 'testdata202413.txt'

@dataclass
class Claw:
  """Represent claw machine with A button, B button, and prize location."""
  A: Coord
  B: Coord
  prize: Coord


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def ExtractNumbers(line):
  """Extract the numbers from a line."""
  if not line:
    return []
  nums = [int(i) for i in RE_NUM.findall(line)]
  assert len(nums) == 2
  return Coord(*nums)


def GetClawMachines(lines):
  """Parse lines into a list of Claw objects."""
  my_list = []
  num_lines = len(lines) + 1
  assert num_lines % 4 == 0
  for i in range((num_lines + 1) // 4):
    a = ExtractNumbers(lines[i * 4])
    b = ExtractNumbers(lines[i * 4 + 1])
    prize = ExtractNumbers(lines[i * 4 + 2])
    my_list.append(Claw(a, b, prize))
  return my_list


def SolvePt1(claw):
  """Try to return # of pushes for A and B, or None. This was used for
     part 1 originally, but failed for part 2. It is no longer called, but
     kept for historical purposes.
  """
  b_start = 100
  while (b_start > 0 and
         (b_start * claw.B.x > claw.prize.x or
          b_start * claw.B.y > claw.prize.y)):
    b_start -= 1
  for b_push in range(b_start, -1, -1):
    a_target = Coord(claw.prize.x - (b_push * claw.B.x),
                     claw.prize.y - (b_push * claw.B.y))
    a_push = 0
    while (a_push * claw.A.x < a_target.x and
           a_push * claw.A.y < a_target.y):
      a_push += 1
    if a_push * claw.A.x == a_target.x and a_push * claw.A.y == a_target.y:
      return a_push, b_push
  return None


def FindXY(claw):
  """Magic equation to find intersection of lines A and B, where B goes
  through origin and A goes through prize. if they intersect on an integer,
  return X, Y; else None.

  The equation was derived by using the equation for a line with slope m
  through a point (x1, y1)

    y - y1 = m(x - x1)

  I assumed the B line went through the origin, and the A line went through
  the claw prize. Their intersection gives a value that, if divisible cleanly,
  can yield the number of pushes required for each button. I did not try to
  reduce this equation, sorry.
  """
  ax = claw.A.x
  ay = claw.A.y
  bx = claw.B.x
  by = claw.B.y
  tx = claw.prize.x
  ty = claw.prize.y

  x = ((ay * tx) - (ty * ax)) * bx / ((ax * by) - bx * ay)
  y = (by * x / bx)

  # Check here to see if it's an integer point. However, this check fails
  # for very large numbers, so I re-do it in the calling function TryMath()
  # using modular division.
  if not math.isclose(y, round(y)) or not math.isclose(x, round(x)):
    return None

  return Coord(abs(round(x)), abs(round(y)))


def TryMath(c):
  """Find the number of pushes for A and B using math."""
  point = FindXY(c)
  if point is None:
    return None
  x, y = point

  # The isclose() approximation in FindXY() fails for huge numbers;
  # This kludge works to find unsolvable claw machines.
  if (x % c.B.x != 0) or (c.prize.x - x)% c.A.x != 0:
    return None

  b_push = x//c.B.x
  a_push = (c.prize.x - x)// c.A.x
  return a_push, b_push


def Part1(claw_machines):
  """Part 1."""
  total = 0
  for c in claw_machines:
    solution = TryMath(c)
    if solution is not None:
      a_pushes, b_pushes = solution
      cost = a_pushes * 3 + b_pushes
      total += cost
  return total


def Part2(claw_machines):
  """Part 2."""
  for c in claw_machines:
    new_prize_x = c.prize.x + 10000000000000
    new_prize_y = c.prize.y + 10000000000000
    c.prize = Coord(new_prize_x, new_prize_y)
  return Part1(claw_machines)


def main():
  """main"""
  lines = GetData(DATA)
  claw_machines = GetClawMachines(lines)
  print(f'Part 1: {Part1(claw_machines[:])}')
  print(f'Part 2: {Part2(claw_machines[:])}')


if __name__ == '__main__':
  main()
