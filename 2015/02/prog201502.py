#!/usr/bin/python3
# file created 2024-Apr-12 08:45
"""https://adventofcode.com/2015/day/02"""


DATA = 'data201502.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Part1(lines):
  """Part 1"""
  total = 0
  for l in lines:
    dims = sorted([int(i) for i in l.strip().split('x')])
    total += (dims[0] * dims[1] * 3)
    total += (dims[1] * dims[2] * 2)
    total += (dims[2] * dims[0] * 2)
  return total


def Part2(lines):
  """Part 2"""
  total = 0
  for l in lines:
    dims = sorted([int(i) for i in l.strip().split('x')])
    ribbon_base = 2 * (dims[0] + dims[1])
    cubic_feet = 1
    for i in dims:
      cubic_feet *= i
    total += ribbon_base + cubic_feet
  return total


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
