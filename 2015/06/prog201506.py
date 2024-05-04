#!/usr/bin/python3
# file created 2024-Apr-22 20:32
"""https://adventofcode.com/2015/day/06"""


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


def GetRangeIterable(instruction_line):
  """Given ParseLines() output, return an iterable of (x, y) cells"""
  x1, y1 = [int(i) for i in instruction_line[1].split(',')]
  x2, y2 = [int(i) for i in instruction_line[2].split(',')]
  for x in range(x1, x2 + 1):
    for y in range(y1, y2 + 1):
      yield (x, y)


def Part1(lines):
  """Part 1"""
  on_cells = set([])
  for i in ParseLines(lines):
    op = i[0]
    range_iter = GetRangeIterable(i)
    for cell in range_iter:
      if op == 'on' and cell not in on_cells:
        on_cells.add(cell)
      elif op == 'off' and cell in on_cells:
        on_cells.remove(cell)
      elif op == 'toggle' and cell in on_cells:
        on_cells.remove(cell)
      elif op == 'toggle' and cell not in on_cells:
        on_cells.add(cell)
      else:
        pass

  return len(on_cells)


def Part2(lines):
  """Part 2"""
  on_cells = {}
  for i in ParseLines(lines):
    op = i[0]
    range_iter = GetRangeIterable(i)

    for cell in range_iter:
      if op in ['on', 'toggle']:
        increment = 1 if op == 'on' else 2
        on_cells[cell] = on_cells.get(cell, 0) + increment
      else:
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
