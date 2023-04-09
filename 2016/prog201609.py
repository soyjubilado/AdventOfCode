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


def ExtractParts(line):
  """Given a line, extract the parts needed by Length() and Unpack()"""
  open_paren = line.index('(')
  close_paren = line.index(')')

  prefix = line[:open_paren]
  items, repeat = [int(i) for i in line[open_paren + 1:close_paren].split('x')]
  substr = line[close_paren + 1: close_paren + 1 + items]
  suffix = line[close_paren + 1 + items:]
  return prefix, repeat, substr, suffix


def Length(line):
  """Recursively calculate the length of the unpacked line."""
  if '(' not in line:
    return len(line)
  prefix, repeat, substr, suffix = ExtractParts(line)
  return len(prefix) + (repeat * Length(substr)) + Length(suffix)


def Unpack(line):
  """Given a single line, unpack it once and return the resulting string."""
  if '(' not in line:
    return line
  prefix, repeat, substr, suffix = ExtractParts(line)
  return prefix + (substr * repeat) + Unpack(suffix)


def Solve(lines, part):
  """Solve Part 1 or Part 2"""
  fn1 = lambda x: len(Unpack(x))
  fn2 = lambda x: Length(x)
  fn = fn2 if part == 'Part 2' else fn1
  counter = 0
  for line in lines:
    linelen = fn(line)
    counter += linelen
  return counter


def main():
  """main"""
  lines = GetData(DATA)
  for part in ['Part 1', 'Part 2']:
    print(f'{part}: {Solve(lines, part)}')


if __name__ == '__main__':
  main()
