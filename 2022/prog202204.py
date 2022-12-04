#!/usr/bin/python3
#file created 2022-Dec-03 21:00
"""https://adventofcode.com/2022/day/4"""

DATA = 'data202204.txt'


def GetData(datafile) -> list:
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def ParseLineToNumbers(line) -> tuple:
  """'1-2,3-4' -> (1,2,3,4)"""
  one, two = line.split(',')
  one_s, one_f = [int(i) for i in one.split('-')]
  two_s, two_f = [int(i) for i in two.split('-')]
  return one_s, one_f, two_s, two_f


def WhollyContained(one_s, one_f, two_s, two_f) -> bool:
  """One range is fully within the other."""
  return (one_s <= two_s <= two_f <= one_f or
          two_s <= one_s <= one_f <= two_f)


def OverlapAtAll(one_s, one_f, two_s, two_f) -> bool:
  """The two ranges overlap at least partially."""
  return (one_s <= two_s <= one_f or
          one_s <= two_f <= one_f or
          two_s <= one_s <= two_f or
          two_s <= one_f <= two_f)


def Solve(lines, part) -> None:
  """Print out the answer.
  Args:
    lines: (list of str) lines of input
    part: 'Part 1' or 'Part 2'
  """
  overlaps = []
  CriteriaMet = WhollyContained if part == 'Part 1' else OverlapAtAll
  for l in lines:
    one_s, one_f, two_s, two_f = ParseLineToNumbers(l)
    if CriteriaMet(one_s, one_f, two_s, two_f):
      overlaps.append((one_s, one_f, two_s, two_f))
  print(f'{part}: {len(overlaps)}')


def main():
  lines = GetData(DATA)
  Solve(lines, 'Part 1')
  Solve(lines, 'Part 2')


if __name__ == '__main__':
  main()
