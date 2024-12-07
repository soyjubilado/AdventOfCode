#!/usr/bin/python3
# file created 2024-Dec-01 15:01
"""https://adventofcode.com/2024/day/02"""

DATA = 'data202402.txt'
# DATA = 'testdata202402.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  nums = []
  with open(datafile, 'r') as fh:
    for line in fh:
      nums.append([int(i) for i in line.strip().split()])
  return nums


def IsSafe(nums):
  """Check whether this list of ints is safe."""
  diffs = [v - nums[i] for i, v in enumerate(nums[1:])]
  if all([1 <= i <= 3 for i in diffs]):
    return True
  if all([-3 <= i <= -1 for i in diffs]):
    return True
  return False


def IsEverSafe(nums):
  """Check whether this list of ints is safe, or can be safe if
     one item is removed."""
  if IsSafe(nums):
    return True
  for i in range(len(nums)):
    minus_one = nums[0:i] + nums[i+1:]
    if IsSafe(minus_one):
      return True
  return False


def Part1(nums):
  """Part 1."""
  return sum(1 for n in nums if IsSafe(n))


def Part2(nums):
  """Part 2."""
  return sum(1 for n in nums if IsEverSafe(n))


def main():
  """main"""
  nums = GetData(DATA)
  print(f'Part 1: {Part1(nums)}')
  print(f'Part 2: {Part2(nums)}')


if __name__ == '__main__':
  main()
