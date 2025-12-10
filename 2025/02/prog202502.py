#!/usr/bin/python3
# file created 2025-Dec-08 16:40
"""https://adventofcode.com/2025/day/2"""

import re
DATA = 'data202502.txt'
DATA = 'testdata202502.txt'

def GetData(datafile):
  """Read input into a list of lines."""
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def IDsToRanges(lines):
  """Convert line input to start/end tuples."""
  answer = []
  for line in lines:
    str_ranges = [i.split('-') for i in line.split(',') if i]
    answer.extend(str_ranges)

  return [tuple(map(int, s)) for s in answer]


def Solver(lines, bad_regex):
  """Solver for both parts; pass in the lines and the regex to use."""
  id_ranges = IDsToRanges(lines)
  total = 0
  for start, end in id_ranges:
    for i in range(start, end+1):
      if bad_regex.match(str(i)):
        total += i
  return total


def main():
  """main"""
  lines = GetData(DATA)
  PART1_RE = re.compile(r'^([0-9]+)\1$')
  PART2_RE = re.compile(r'^([0-9]+)\1{1,}$')

  print(f'Part 1: {Solver(lines, PART1_RE)}')
  print(f'Part 2: {Solver(lines, PART2_RE)}')


if __name__ == '__main__':
  main()
