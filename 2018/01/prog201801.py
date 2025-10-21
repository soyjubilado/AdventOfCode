#!/usr/bin/python3
# file created 2025-Oct-21 15:50
"""https://adventofcode.com/2018/day/01"""
from itertools import cycle

DATA = 'data201801.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Part1(lines):
  """Part 1."""
  acc = 0
  for l in lines:
    acc += int(l.strip())
  return acc


def Part2(lines):
  """Part 2."""
  change = cycle([int(i.strip()) for i in lines])
  acc = 0
  frequencies = set([acc])
  while (acc := acc + next(change)) not in frequencies:
    frequencies.add(acc)
  return acc


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
