#!/usr/bin/python3
# file created 2024-Dec-10 21:05
"""https://adventofcode.com/2024/day/11"""

from functools import lru_cache
DATA = 'data202411.txt'
# DATA = 'testdata202411.txt'


def GetData(datafile):
  """Read input into a list of integers."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  assert len(lines) == 1
  nums = [int(i) for i in lines[0].split()]
  return nums


@lru_cache
def Blink(number):
  """Return a list of new number(s), given a single number."""
  if number == 0:
    return [1]
  if not len(str(number)) % 2:
    str_num = str(number)
    half = len(str_num)//2
    return [int(str_num[:half]), int(str_num[half:])]
  return [number * 2024]


@lru_cache(maxsize=None)
def BlinkSingleLen(num, rounds):
  """Return the length of the list after n rounds, starting with
     a single number (not a list)."""
  if rounds == 0:
    return 1
  if rounds == 1:
    return len(Blink(num))

  return sum([BlinkSingleLen(n, rounds - 1) for n in Blink(num)])


def Solver(nums, rounds):
  """Solver for both parts, pass in the requisite number of rounds."""
  total = 0
  for i in nums:
    subtotal = BlinkSingleLen(i, rounds)
    print(f'    {i} -> {subtotal}')
    total += subtotal
  return total


def main():
  """main"""
  nums = GetData(DATA)
  print(f'Part 1: {Solver(nums, 25)}')
  print()
  print(f'Part 2: {Solver(nums, 75)}')


if __name__ == '__main__':
  main()
