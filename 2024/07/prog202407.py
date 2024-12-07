#!/usr/bin/python3
# file created 2024-Dec-07 07:08
"""https://adventofcode.com/2024/day/07"""

DATA = 'data202407.txt'
# DATA = 'testdata202407.txt'


def GetData(datafile):
  """Read input into [target, [numbers]]."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]

  data = []
  for line in lines:
    first, last = line.split(':')
    target = int(first.strip())
    nums = [int(i) for i in last.strip().split()]
    data.append((target, nums))
  return data


def Combine(num1, num2):
  """Combine the digits of num1 and num2."""
  return int(str(num1) + str(num2))


def CanUncombine(num1, num2):
  """Return true if num1 ends with num2.
     Exmaple: (156, 6) can be uncombined to 15."""
  if num1 in (num2, -num2):
    return False
  return str(num1).endswith(str(num2))


def Uncombine(num1, num2):
  """If str(num1) ends with str(num2), return num1 with that part removed."""
  assert CanUncombine(num1, num2)
  return int(str(num1)[:-len(str(num2))])


def Ways2Reach(target, numbers, pt2=False):
  """Count the number of ways for these numbers to reach the target.
     For part 2, set pt2=True to include the '||' operator."""
  nums = numbers[:]
  x = nums.pop()
  count = 0
  if len(nums) == 1:
    if nums[0] * x == target:
      count += 1
    if nums[0] + x == target:
      count += 1
    if pt2 and Combine(nums[0], x) == target:
      count += 1
    return count

  if target % x == 0:
    count += Ways2Reach(target//x, nums, pt2)
  if pt2 and CanUncombine(target, x):
    count += Ways2Reach(Uncombine(target, x), nums, pt2)
  count += Ways2Reach(target-x, nums, pt2)
  return count


def Part1(data):
  """Part 1."""
  return sum(target for target, nums in data if Ways2Reach(target, nums))


def Part2(data):
  """Part 2."""
  return sum(target for target, nums in data
             if Ways2Reach(target, nums, pt2=True))


def main():
  """main"""
  data = GetData(DATA)
  print(f'Part 1: {Part1(data)}')
  print(f'Part 2: {Part2(data)}')


if __name__ == '__main__':
  main()
