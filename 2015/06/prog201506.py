#!/usr/bin/python3
# file created 2024-Apr-22 20:32
"""https://adventofcode.com/2015/day/06"""

from itertools import product

DATA = 'data201506.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def ParseLines(lines):
  """Parse input to return a list [operation, 'x1,y1', 'x2,y2']
     where operation is in ['on', 'off', 'toggle']
  """
  instructions = []
  for l in lines:
    line = l.strip().split()
    if line[0] == 'turn':
      line = line[1:]
    instructions.append(line[0:2] + line[3:])
  return instructions


def GetRanges(instruction_line):
  """Given ParseLines() output, return a range values for x and y"""
  x1, y1 = [int(i) for i in instruction_line[1].split(',')]
  x2, y2 = [int(i) for i in instruction_line[2].split(',')]
  return (x1, x2 + 1), (y1, y2 + 1)


def Part1(lines):
  """Part 1"""
  operate = {'on': set.union,
             'off': set.difference,
             'toggle': set.symmetric_difference,
            }
  on_cells = set([])
  for i in ParseLines(lines):
    op = i[0]
    x_range, y_range = GetRanges(i)
    # print(f'{op} range({x_range}) range({y_range})')
    cells = set(product(range(*x_range), range(*y_range)))
    on_cells = operate[op](on_cells, cells)

  return len(on_cells)


def Part2(lines):
  """Part 2"""
  on_cells = {}
  for i in ParseLines(lines):
    op = i[0]
    x_range, y_range = GetRanges(i)
    # print(f'{op} range({x_range}) range({y_range})')
    cells = set(product(range(*x_range), range(*y_range)))
    if op in ['on', 'toggle']:
      increment = 1 if op == 'on' else 2
      for cell in cells:
        on_cells[cell] = on_cells.get(cell, 0) + increment
    else:
      for cell in cells:
        if cell in on_cells:
          brightness = on_cells[cell] - 1
          if brightness < 1:
            del on_cells[cell]
          else:
            on_cells[cell] = brightness

  return sum(on_cells.values())


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
