#!/usr/bin/python3
#file created 2022-Dec-03 21:00
"""https://adventofcode.com/2022/day/4"""

DATA = 'data202204.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Part1(lines):
  """One range is fully within the other."""
  overlaps = []
  for l in lines:
    one, two = l.split(',')
    one_s, one_f = [int(i) for i in one.split('-')]
    two_s, two_f = [int(i) for i in two.split('-')]
    if (one_s <= two_s <= two_f <= one_f or
        two_s <= one_s <= one_f <= two_f):
      overlaps.append((one_s, one_f, two_s, two_f))
  print(f'Part 1: {len(overlaps)}')


def Part2(lines):
  """The two ranges overlap at least partially."""
  overlaps = []
  for l in lines:
    one, two = l.split(',')
    one_s, one_f = [int(i) for i in one.split('-')]
    two_s, two_f = [int(i) for i in two.split('-')]
    if (one_s <= two_s <= one_f or
        one_s <= two_f <= one_f or
        two_s <= one_s <= two_f or
        two_s <= one_f <= two_f):
      overlaps.append((one_s, one_f, two_s, two_f))
  print(f'Part 2: {len(overlaps)}')


def main():
  lines = GetData(DATA)
  Part1(lines)
  Part2(lines)


if __name__ == '__main__':
  main()
