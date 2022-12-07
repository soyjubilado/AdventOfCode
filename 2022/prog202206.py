#!/usr/bin/python3
#file created 2022-Dec-05 20:55
"""https://adventofcode.com/2022/day/6"""

DATA = 'data202206.txt'


class NoSolution(Exception):
  """No solution for a given input."""


def GetData(datafile):
  """Parse input file, return the one line that's in it."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines[0]


def Solver(line, width):
  """Step through the line taking N=width characters at a time. Index is
     pointed at the last character. Check for duplicates by casting it to
     a set; if the size of the set == width, that's the index we're seeking.
  """
  for i in range(width, len(line) + 1):
    set_of_N = set(list(line[i-width:i]))
    if len(set_of_N) == width:
      return i
  raise NoSolution


def main():
  line = GetData(DATA)
  print(f'Part 1: {Solver(line, 4)}')
  print(f'Part 2: {Solver(line, 14)}')


if __name__ == '__main__':
  main()
