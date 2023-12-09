#!/usr/bin/python3
# file created 2023-Dec-09 07:33
"""https://adventofcode.com/2023/day/9"""

DATA = 'data202309.txt'
# DATA = 'testdata202309.txt'


def GetData(datafile):
  """Read input into a list of lists."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
    items = [[int(i) for i in line.strip().split()] for line in lines]
  return items


def NextItem(series):
  """Return the next item in the series."""
  if len(set(series)) == 1:
    return series[0]
  subseries = [series[i] - series[i-1] for i in range(1, len(series))]
  return series[-1] + NextItem(subseries)


def PrevItem(series):
  """Return the previous item in the series."""
  if len(set(series)) == 1:
    return series[0]
  subseries = [series[i] - series[i-1] for i in range(1, len(series))]
  return series[0] - PrevItem(subseries)


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {sum(NextItem(i) for i in lines)}')
  print(f'Part 2: {sum(PrevItem(i) for i in lines)}')


if __name__ == '__main__':
  main()
