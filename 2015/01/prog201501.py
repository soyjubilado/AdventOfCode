#!/usr/bin/python3
#file created 2022-Feb-22 20:29
"""https://adventofcode.com/2015/day/1"""

DATA = 'data201501.txt'
# DATA = 'testdata201501.txt'


def GetData(datafile):
  with open(datafile, 'r') as fh:
    line = next(fh).strip()
  return line


def main():
  line = GetData(DATA)
  # part 1
  up = line.count('(')
  down = line.count(')')
  print(f'Part 1: {up - down}')

  # part 2
  floor = 0
  for idx, instr in enumerate(line):
    if instr == '(':
      floor += 1
    elif instr == ')':
      floor -= 1
    else:
      raise Exception
    if floor == -1:
      print(f'Part 2: {idx + 1}')
      break


if __name__ == '__main__':
  main()
