#!/usr/bin/python3
# file created 2023-Jan-12 21:14
"""https://adventofcode.com/2016/day/3"""

DATA = 'data201603.txt'
# DATA = 'testdata201603.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Part1(lines):
  """Part 1"""
  counter = 0
  for line in lines:
    sides = sorted([int(i) for i in line.split()])
    if sides[0] + sides[1] > sides[2]:
      counter += 1
  return counter


def Part2(lines):
  """Part 2"""
  lines_per_group = 3
  items_per_line = 3
  all_groups = []
  for i in range(0, len(lines), lines_per_group):
    for j in range(items_per_line):
      group = sorted([int(lines[i].split()[j]),
                      int(lines[i+1].split()[j]),
                      int(lines[i+2].split()[j])])
      all_groups.append(group)
  counter = 0
  for sides in all_groups:
    if sides[0] + sides[1] > sides[2]:
      counter += 1
  return counter


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
