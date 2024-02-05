#!/usr/bin/env python3
"""Solve Part 3 as proposed here:
   https://www.reddit.com/r/adventofcode/comments/zuso8x/2022_day_22_part_3/
"""

from prog202222 import Solve

# download the file and put the file name here.
PART3_DATA = 'data202222_part3.txt'


def GetAllCases(filename):
  """Return a list of lists; each sub list is the equivalent of GetData()."""

  with open(filename) as fh:
    all_lines = fh.readlines()
  lines = iter(all_lines)
  all_cases = []

  while True:
    this_case = []
    try:
      line = next(lines)
      while len(line.strip()) != 0:
        this_case.append(line.rstrip())
        line = next(lines)
      this_case.append(line.rstrip())  # print the blank
      line = next(lines)               # get the next line
      this_case.append(line.rstrip())  # print that one
      all_cases.append(this_case)
      _ = next(lines)
    except StopIteration:
      break
  return all_cases


def main():
  """main"""
  cases = GetAllCases(PART3_DATA)
  running_total = 0
  counter = 0
  for lines in cases:
    subtotal = Solve('Part 2', lines)
    running_total += subtotal
    print(f'{counter:>2}: {subtotal:>6}, running total: {running_total}')
    counter += 1


if __name__ == '__main__':
  main()
