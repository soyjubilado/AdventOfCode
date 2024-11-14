#!/usr/bin/python3
# file created 2024-Nov-11 14:52
"""https://adventofcode.com/2017/day/01"""

DATA = 'data201701.txt'
# DATA = 'testdata201701.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Part1(line):
  total = 0
  for idx, c in enumerate(line):
    if c == line[idx - 1]:
      total += int(c)
  return total


def Part2(line):
  length = len(line)
  offset = length // 2
  total = 0
  for idx, c in enumerate(line):
    halfway = (idx + offset) % length
    if c == line[halfway]:
      total += int(c)
  return total
  

def main():
  """main"""
  line = GetData(DATA)[0]
  print(f'Part 1: {Part1(line)}')
  print(f'Part 2: {Part2(line)}')


if __name__ == '__main__':
  main()
