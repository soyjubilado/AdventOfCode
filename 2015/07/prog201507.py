#!/usr/bin/python3
# file created 2024-Apr-18 00:41
"""https://adventofcode.com/2015/day/07"""

from functools import lru_cache

DATA = 'data201507.txt'
# DATA = 'testdata201507.txt'


OPERATIONS = {'AND': lambda x, y: x & y,
              'OR': lambda x, y: x | y,
              'LSHIFT': lambda x, y: x << y,
              'RSHIFT': lambda x, y: x >> y,
              'NOT': lambda x: 65535 - x,
             }

# use a global dict so that EvalX can be memoized.
WIRE_DICT = {}


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Op(*args):
  """Use the opcode on the arguments and return the result.
     The first item in *args is the opcode."""
  if len(args) == 1:
    try:
      return int(args[0])
    except ValueError:
      return args[0]
  op = args[0]
  arg = args[1:]
  return OPERATIONS[op](*arg)


def ParseLine(line):
  """Parse the line return a tuple in this order:
     (wire, opcode, arg1, arg2)
  """
  elems = line.split()
  wire = elems[-1:]   # start with just the wire name
  opargs = elems[:-2]  # everything but the last two tokens
  ops = [i for i in opargs if i in OPERATIONS]
  assert len(ops) <= 1
  args = [i for i in opargs if i not in OPERATIONS]
  wire.extend(ops)
  wire.extend(args)
  return tuple(wire)


@lru_cache(maxsize=None)
def EvalX(x):
  """Recursively evaluate wire x."""
  # if x is a number
  if x not in WIRE_DICT:
    return int(x)

  op_args = WIRE_DICT[x]
  expanded_args = [op_args[0]]

  # if x is another wire
  if expanded_args[0] not in OPERATIONS:
    return EvalX(expanded_args[0])

  expanded_args.extend([EvalX(i) for i in op_args[1:]])
  return Op(*expanded_args)


def Part1(lines):
  """Build the global dict, then run EvalX to find wire 'a' value."""
  global WIRE_DICT
  for line in lines:
    parsed = ParseLine(line)
    wire = parsed[0]
    op_args = parsed[1:]
    WIRE_DICT[wire] = op_args
  return EvalX('a')


def Part2(part_1_answer):
  """Part 2: replace wire B with answer from part 1."""
  global WIRE_DICT
  WIRE_DICT['b'] = (f'{part_1_answer}',)
  EvalX.cache_clear()
  return EvalX('a')


def main():
  """main"""
  lines = GetData(DATA)
  part_1_answer = Part1(lines)
  print(f'Part 1: {part_1_answer}')
  print(f'Part 2: {Part2(part_1_answer)}')


if __name__ == '__main__':
  main()
