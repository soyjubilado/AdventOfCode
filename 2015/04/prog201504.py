#!/usr/bin/python3
#file created 2022-Feb-23 14:22
"""https://adventofcode.com/2015/day/4"""

import hashlib
DATA = 'data201504.txt'


def GetData(datafile):
  """Read data from input file"""
  with open(datafile, 'r') as fh:
    line = next(fh).strip()
  return line


def Solver(line, starting_zeros):
  """Return answer string given a line of input and starting zeros"""
  num = 1
  my_string = line + str(num)
  my_hash = hashlib.md5(my_string.encode()).hexdigest()
  while not str(my_hash).startswith(starting_zeros):
    num += 1
    my_string = line + str(num)
    my_hash = hashlib.md5(my_string.encode()).hexdigest()

  return f'{num} -> {my_string} -> {my_hash}'


def main():
  """main"""
  line = GetData(DATA)
  print(f'Part 1: {Solver(line, "00000")}')
  print(f'Part 2: {Solver(line, "000000")}')


if __name__ == '__main__':
  main()
