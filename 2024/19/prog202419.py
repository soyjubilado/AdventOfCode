#!/usr/bin/python3
# file created 2024-Dec-19 13:22
"""https://adventofcode.com/2024/day/19"""
from functools import lru_cache

DATA = 'data202419.txt'
# DATA = 'testdata202419.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def ListToTowels(line):
  """Parse the first line of input into a list of towel patterns."""
  return frozenset([w.strip() for w in line.split(',')])


@lru_cache(maxsize=None)
def Comprises(whole, towels):
  """Recursively figure out how many ways this whole design can be made."""
  candidates = {p for p in towels if whole.startswith(p)}
  if not whole:
    return 1
  if not candidates:
    return 0
  return sum([Comprises(whole[len(n):], towels) for n in candidates])


def Part1(designs, towels):
  """Part 1."""
  return sum([1 for d in designs if Comprises(d, towels)])


def Part2(designs, towels):
  """Part 2."""
  return sum([Comprises(d, towels) for d in designs])


def main():
  """main"""
  lines = GetData(DATA)
  towels = ListToTowels(lines[0])
  designs = lines[2:]
  print(f'Part 1: {Part1(designs, towels)}')
  print(f'Part 2: {Part2(designs, towels)}')


if __name__ == '__main__':
  main()
