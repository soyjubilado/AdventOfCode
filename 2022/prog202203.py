#!/usr/bin/python3
#file created 2022-Dec-02 23:25
"""https://adventofcode.com/2022/day/3"""


DATA = 'data202203.txt'


def GetData(datafile):
  """Read data from datafile and return a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Priority(n):
  """Return priority for n. Raise exception if n not in [a-zA-Z]."""
  if 'A' <= n <= 'Z':
    return ord(n) - ord('A') + 27
  if 'a' <= n <= 'z':
    return ord(n) - ord('a') + 1
  raise Exception


def Part1():
  """Solve part 1: total priority of items that are in both halves
     of any given line."""
  lines = GetData(DATA)
  total = 0
  for l in lines:
    half = len(l) // 2
    left = l[:half]
    right = l[half:]
    item = [i for i in left if i in right]
    if item:
      total += Priority(item[0])
    else:
      print(f'{l} is bad input')
  print(f'Part 1 total: {total}')


def Part2():
  """Solve part 2: total priority of common items in each group of
     three lines."""
  lines = GetData(DATA)
  total = 0
  for g in range(len(lines)//3):
    group = lines[3*g:3*g+3]
    common = list({i for i in group[0] if i in group[1] and i in group[2]})
    total += Priority(common[0])
  print(f'Part 2 total: {total}')


def main():
  Part1()
  Part2()


if __name__ == '__main__':
  main()
