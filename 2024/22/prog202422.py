#!/usr/bin/python3
# file created 2024-Dec-22 06:41
"""https://adventofcode.com/2024/day/22"""

DATA = 'data202422.txt'
# DATA = 'testdata202422.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [int(i.strip()) for i in fh]
  return lines


def MixAndPrune(a, b):
  """Mix and prune."""
  return (a ^ b) % 16777216


def NewSecret(s):
  """Calculate the next secret from the previous one."""
  mul_64 = MixAndPrune(64 * s, s)
  div_32 = MixAndPrune(mul_64 // 32, mul_64)
  mul_2048 = MixAndPrune(2048 * div_32, div_32)
  return mul_2048


def SecretTimesN(s, n=2000):
  """Return the secret after N iterations."""
  for _ in range(n):
    s = NewSecret(s)
  return s


def Part1(lines):
  """Part 1."""
  return sum(SecretTimesN(s) for s in lines)


def Part2(lines):
  """Part 2."""
  return None


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
