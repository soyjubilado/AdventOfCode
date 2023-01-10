#!/usr/bin/env python3
"""Solve Part 3 as proposed here:
   https://www.reddit.com/r/adventofcode/comments/zuso8x/2022_day_22_part_3/
"""

import os
from prog202222_general import Solve

# download the file and put the file name here.
PART3_DATA = 'data202222_part3.txt'


def SplitIntoSubFiles(filename):
  """Split filename into a bunch of smaller files."""

  with open(filename) as fh:
    all_lines = fh.readlines()
  lines = iter(all_lines)
  counter = 0
  prefix = 'craycray_'
  fname = f'{prefix}{counter:>02}.txt'
  all_files = []

  while True:
    all_files.append(fname)
    # If filename exists already, raise assertion error
    assert not os.path.isfile(fname)
    with open(fname, 'w') as fh:
      try:
        line = next(lines)
        while len(line.strip()) != 0:
          fh.write(line)
          line = next(lines)
        fh.write(line)     # print the blank
        line = next(lines) # get the next line
        fh.write(line)     # print that one
        _ = next(lines)
      except StopIteration:
        break
    counter += 1
    fname = f'{prefix}{counter:>02}.txt'

  return all_files


def main():
  """main"""
  files = SplitIntoSubFiles(PART3_DATA)
  running_total = 0
  for f in files:
    subtotal = Solve('Part 2', f)
    running_total += subtotal
    print(f'{f}: {subtotal}, running total: {running_total}')
    # remove each file when done
    os.unlink(f)


if __name__ == '__main__':
  main()
