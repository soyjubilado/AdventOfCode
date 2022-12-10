#!/usr/bin/python3
#file created 2022-Dec-09 20:59
"""https://adventofcode.com/2022/day/10"""

DATA = 'data202210.txt'


class UnexpectedOperator(Exception):
  """opcode in input that is not addx or noop."""


def GetData(datafile):
  """Read data input to a list of strings."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def LineIterator(lines):
  """Iterator that loops over the lines indefinitely."""
  pointer = - 1
  line_length = len(lines)
  while True:
    pointer = (pointer + 1) % line_length
    yield lines[pointer]


def ClockAndRegister(lines):
  """Iterator that returns the next clock and register."""
  clock = 0
  instructions = LineIterator(lines)
  register = 1
  register_prev = register
  while True:
    # pylint: disable=stop-iteration-return
    # because both iterators loop indefinitely
    instr = next(instructions)
    if instr.startswith('noop'):
      value = 0
      cycles_per_op = 1
    elif instr.startswith('addx'):
      value = int(instr.split()[1])
      cycles_per_op = 2
    else:
      raise UnexpectedOperator

    for _ in range(cycles_per_op):
      clock += 1
      yield clock, register

    # don't update register until after the operation has finished
    register += value


def Part1(lines):
  """Update sum_strengths every 40 cycles starting at 20."""
  clock_and_register = ClockAndRegister(lines)
  sum_strengths = 0
  for _ in range(220):
    clock, register = next(clock_and_register)
    sum_strengths += 0 if (clock + 20) % 40 else clock * register
  return sum_strengths


def Part2(lines):
  """When clock % 40 and register (roughly) match, print the pixel."""
  clock_and_register = ClockAndRegister(lines)
  for n in range(1, 241):
    clock, register = next(clock_and_register)
    crt = clock % 40
    visible = (crt in (register, register + 1, register + 2))
    output = '0' if visible else ' '
    print(output, end='')
    if not n % 40:
      print()


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print('\nPart 2:\n')
  Part2(lines)


if __name__ == '__main__':
  main()
