#!/usr/bin/python3
# file created 2025-Dec-05 09:20
"""https://adventofcode.com/2025/day/05"""

DATA = 'data202505.txt'
# DATA = 'testdata202505.txt'


class Interval():
  """A range class. Don't call it 'range' though."""

  def __init__(self, interval_str):
    """initialize"""
    self.low, self.high = map(int, interval_str.split('-'))
    assert self.low <= self.high

  def __eq__(self, other):
    """test for equality"""
    return self.low == other.low and self.high == other.high

  def __str__(self):
    """string representation"""
    return f'({self.low}, {self.high})'

  def contains(self, n):
    """this range contains n"""
    return self.low <= n <= self.high

  def overlaps(self, other):
    """range 'other' overlaps this one in some way"""
    return other.high >= self.low and other.low <= self.high

  def subsume(self, other):
    """subsume other range into this one."""
    assert self.overlaps(other)
    self.low = min(self.low, other.low)
    self.high = max(self.high, other.high)

  def size(self):
    """items in this range."""
    return self.high - self.low + 1


def GetData(datafile):
  """Read input into a list of lines."""
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Part1(lines):
  """Part 1."""
  raw_intervals = [line.strip() for line in lines if '-' in line]
  intervals = [Interval(l) for l in raw_intervals]
  ingredients = [int(l.strip()) for l in lines if '-' not in l
                 and len(l.strip()) != 0]
  total = 0
  for i in ingredients:
    if any([x.contains(i) for x in intervals]):
      total += 1
  return total


def Mash(intervals):
  """mash up these intervals"""
  mashup = []
  for i in intervals[:]:
    for m in mashup:
      if m.overlaps(i):
        m.subsume(i)
        break
    else:
      mashup.append(i)
  return mashup


def Part2(lines):
  """Part 2."""
  raw_intervals = [line.strip() for line in lines if '-' in line]
  intervals = [Interval(i) for i in raw_intervals]
  mashup = Mash(intervals)

  while len(mashup) < len(intervals):
    intervals = mashup
    mashup = Mash(intervals)

  return sum(i.size() for i in mashup)


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
