#!/usr/bin/python3
# file created 2023-Apr-04 07:00
"""https://adventofcode.com/2016/day/9"""

DATA = 'data201609.txt'
# DATA = 'testdata201609.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Length(line):
  """Recursively calculate the length of the unpacked line."""
  if '(' not in line:
    return len(line)

  count = 0
  open_paren = line.index('(')
  close_paren = line.index(')')
  count += open_paren

  prefix = line[:open_paren]
  items, repeat = [int(i) for i in line[open_paren + 1:close_paren].split('x')]
  substr = line[close_paren + 1: close_paren + 1 + items]
  suffix = line[close_paren + 1 + items:]

  return len(prefix) + (repeat * Length(substr)) + Length(suffix)


def Unpack(line):
  """Given a single line, unpack it once and return the resulting string."""
  retval = ''
  l = iter(line)
  try:
    while True:
      # get preface
      c = next(l)
      while c != '(':
        retval += c
        c = next(l)
      c = next(l) # discard '('

      # get and parse instruction
      instr = ''
      while c != ')':
        instr += c
        c = next(l)
      items, repeat = [int(i) for i in instr.split('x')]

      # build the item_string, append to answer
      item_str = ''
      for _ in range(items):
        c = next(l)
        item_str += c
      item_str *= repeat
      retval += item_str

  except StopIteration:
    pass

  return retval


def Part1(lines):
  """Solve Part 1"""
  counter = 0
  for line in lines:
    linelen = len(Unpack(line))
    counter += linelen
  return counter


def Part2(lines):
  """Solve Part 2"""
  counter = 0
  for line in lines:
    linelen = Length(line)
    counter += linelen
  return counter


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
