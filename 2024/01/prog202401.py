#!/usr/bin/python3
# file created 2024-Dec-01 13:16
"""https://adventofcode.com/2024/day/01"""

DATA = 'data202401.txt'
# DATA = 'testdata202401.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip().split() for i in fh]
  return lines


def SeparateLists(lines):
  """parse, separate, and sort the two list columns"""
  list1 = []
  list2 = []
  list2_dict = {}
  for l1, l2 in lines:
    list1.append(int(l1))
    list2.append(int(l2))
    list2_dict[int(l2)] = list2_dict.get(int(l2), 0) + 1
  return sorted(list1), sorted(list2), list2_dict


def Part1(lines):
  """part 1"""
  list1, list2, _ = SeparateLists(lines)
  return sum(abs(val - list2[i]) for i, val in enumerate(list1))


def Part2(lines):
  """part 2"""
  list1, _, list2_dict = SeparateLists(lines)
  return sum(i * list2_dict.get(i, 0) for i in list1)


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
