#!/usr/bin/python3
#file created 2022-Dec-10 22:16
"""https://adventofcode.com/2022/day/11"""

from collections import deque, defaultdict

DATA = 'data202211.txt'
# DATA = 'testdata202211.txt'

Times = lambda x, y: x * y
Plus = lambda x, y: x + y
Square = lambda x, y: x * x


class UndefinedOperation(Exception):
  """undefined opeation in the input file."""


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


class Monkey():
  """A monkey object."""

  def __init__(self, name, starting, operation, oparg,
               divis_val, dest_T, dest_F):
    self.name = name
    self.bag = deque(starting)
    self.operation = operation
    self.oparg = oparg
    self.divisibility = divis_val
    self.dest_if_true = dest_T
    self.dest_if_false = dest_F
    self.inspected = len(self.bag)

  def __str__(self):
    retval = [f'Monkey {self.name}']
    retval.append(f'  bag: {self.bag}')
    retval.append(f'  operation: {self.operation}')
    retval.append(f'  oparg: {self.oparg}')
    retval.append(f'  divisibility: {self.divisibility}')
    retval.append(f'  dest_if_true: {self.dest_if_true}')
    retval.append(f'  dest_if_false: {self.dest_if_false}')
    return '\n'.join(retval)

  def Test(self, item):
    """Test whether item is divisible by self.divisibility; return the
       destination that results."""
    if not item % self.divisibility:
      return self.dest_if_true
    return self.dest_if_false

  def SetInspectation(self):
    """Keep track of number of items in bag before monkey handles them."""
    self.inspected = len(self.bag)

  def AddToBag(self, item):
    """Add an item to the monkey's bag."""
    self.bag.append(item)


def CommonDivisibility(monkeys):
  """Given a barrel of monkeys, determine the product of all their
     "divisibility" values. This becomes the modulo to keep the worry a
     manageable size in part 2."""
  answer = 1
  for m in monkeys:
    answer *= m.divisibility
  return answer


def RunRound(monkeys, inspect_dict, puzzle_part=None):
  """Run one round of monkeys. Update inspect_dict with how many items each
     monkey handled during this round."""
  lcm_monkeys = CommonDivisibility(monkeys)
  for idx, m in enumerate(monkeys):
    inspect_dict[idx] += len(m.bag)
    for _ in range(len(m.bag)):
      item = m.bag.popleft()
      item = m.operation(item, m.oparg)

      # adjustment changes depending on Part 1 or Part 2
      if puzzle_part == 'Part 1':
        item //= 3
      elif puzzle_part == 'Part 2':
        item %= lcm_monkeys

      destination = m.Test(item)
      monkeys[destination].AddToBag(item)
  return monkeys


def GetMonkeys(lines):
  """Parse input line and produce a list of monkeys."""
  lines_per_monkey_definition = 6
  monkey = []
  num_monkeys = (len(lines) + 1) // (lines_per_monkey_definition + 1)
  for num in range(num_monkeys):
    idx = num * (lines_per_monkey_definition + 1)
    name = lines[idx]
    start_str = lines[idx + 1].split(':')[1]
    start = [int(i.strip()) for i in start_str.split(',')]
    opline = lines[idx+2].split()
    if opline[-1] == 'old' and opline[-2] == '*':
      op = Square
    elif opline[-2] == '+':
      op = Plus
    elif opline[-2] == '*':
      op = Times
    else:
      raise UndefinedOperation
    oparg = '0' if not opline[-1].isnumeric() else int(opline[-1])
    divis_val = int(lines[idx+3].split()[-1])
    dest_T = int(lines[idx+4].split()[-1])
    dest_F = int(lines[idx+5].split()[-1])
    monkey.append(Monkey(name, start, op, oparg, divis_val, dest_T, dest_F))
  return monkey


def Solver(part):
  """Solve either Part 1 or Part 2 of the puzzle."""
  num_rounds = 10000 if part == 'Part 2' else 20
  lines = GetData(DATA)
  monkeys = GetMonkeys(lines)
  monkey_handle_map = defaultdict(lambda: 0)

  for _ in range(num_rounds):
    RunRound(monkeys, monkey_handle_map, part)

  top_scores = list(reversed(sorted(monkey_handle_map.values())))
  print(f'{part}: {top_scores[0] * top_scores[1]}')


def main():
  """main"""
  Solver('Part 1')
  Solver('Part 2')


if __name__ == '__main__':
  main()
