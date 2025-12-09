#!/usr/bin/python3
# file created 2025-Dec-08 16:40
"""https://adventofcode.com/2025/day/2"""

import re
DATA = 'data202502.txt'
# DATA = 'testdata202502.txt'
INVALID_RE = re.compile(r'^([0-9]+)\1{1,}$')


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


def IsInvalid(num):
  """Use regex for repeated characters for part 2."""
  return INVALID_RE.match(str(num)) is not None


def Part1(lines):
  """Part 1."""
  id_ranges = IDsToRanges(lines)
  total = 0
  for start, end in id_ranges:
    for i in range(start, end+1):
      if len(str(i)) % 2:
        continue
      half = len(str(i))//2
      if str(i)[:half] == str(i)[half:]:
        total += i
  return total


def Part2(lines):
  """Part 2."""
  id_ranges = IDsToRanges(lines)
  total = 0
  for start, end in id_ranges:
    for i in range(start, end+1):
      if IsInvalid(i):
        total += i
  return total


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
