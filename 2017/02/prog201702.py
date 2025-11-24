#!/usr/bin/python3
# file created 2025-Nov-22 21:24
"""https://adventofcode.com/2017/day/02"""
from itertools import combinations


DATA = 'data201702.txt'
# DATA = 'testdata201702.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def MapNumbers(lines):
  """Convert list of strings into list of lists of ints."""
  return [list(map(int, line.split())) for line in lines]


def DividesEvenly(a, b):
  """if a divides evenly into b or vice versa."""
  return max(a, b) % min(a, b) == 0


def Part1(lines):
  """Part 1."""
  return sum(map(lambda x: max(x) - min(x), MapNumbers(lines)))


def Part2(lines):
  """Part 2."""
  sheet = MapNumbers(lines)
  total = 0
  for line in sheet:
    for pair in combinations(line, 2):
      if DividesEvenly(*pair):
        total += max(pair) // min(pair)
        break
  return total


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
