#!/usr/bin/python3
# file created 2024-Dec-23 21:07
"""https://adventofcode.com/2024/day/24"""
from operator import and_, or_, xor

DATA = 'data202424.txt'
# DATA = 'testdata202424.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines

def Circuit(lines):
  """From the input lines, create a dictionary representing the circuit."""
  circuit = {}
  for l in lines:
    if ':' in l:
      k, v = l.split(':')
      circuit[k] = int(v.strip())
    elif '->' in l:
      tokens = l.split()
      circuit[tokens[-1]] = tokens[:3]
  return circuit


def Op(x):
  """Map the proper operator to the description."""
  return {'XOR': xor,
          'AND': and_,
          'OR': or_}[x]


def EvalLine(tag, circuit):
  """Evaluate a given line, recursively through the circuit."""
  if isinstance(circuit[tag], int):
    return circuit[tag]
  a, op, b = circuit[tag]
  return Op(op)(EvalLine(a, circuit), EvalLine(b, circuit))


def Part1(lines):
  """Part 1."""
  circuit = Circuit(lines)
  keys = [k for k in circuit if k.startswith('z')]
  answer_list = []
  for k in sorted(keys, reverse=True):
    answer_list.append(str(EvalLine(k, circuit)))
  return int(''.join(answer_list), 2)


def Part2(lines):
  """Part 2."""
  return None


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
