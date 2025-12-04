#!/usr/bin/python3
# file created 2025-Dec-03 19:04
"""https://adventofcode.com/2025/day/03"""

DATA = 'data202503.txt'
# DATA = 'testdata202503.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def MaxJoltageN(line, n):
  """Recursively solve the max joltage problem.
     n is the number of batteries to activate minus 1"""
  nums = list(map(int, line))
  max_left = max(nums[:-n])
  index_left = nums[:-1].index(max_left)
  if n == 1:
    max_right = str(max(nums[index_left + 1:]))
  else:
    max_right = MaxJoltageN(line[index_left + 1:], n - 1)
  return str(max_left) + max_right


def Solver(lines, num_batteries):
  """Same solver for parts 1 and 2; activate different number of batteries."""
  return sum(int(MaxJoltageN(line, num_batteries-1)) for line in lines)


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Solver(lines, 2)}')
  print(f'Part 2: {Solver(lines, 12)}')


if __name__ == '__main__':
  main()
