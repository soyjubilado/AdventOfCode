#!/usr/bin/python3
# file created 2024-Apr-26 14:32
"""https://adventofcode.com/2015/day/08"""

DATA = 'data201508.txt'
# DATA = 'testdata201508.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Part1(lines):
  """Part 1"""
  total = 0
  for line in lines:
    total += len(line)
    total -= len(eval(line))
  return total


def Part2(lines):
  """Part 2"""
  total = 0
  for line in lines:
    total += 2 + line.count('\\') + line.count('\"')
  return total


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
