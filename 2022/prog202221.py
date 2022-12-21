#!/usr/bin/python3
# file created 2022-Dec-21 08:11
"""https://adventofcode.com/2022/day/21"""

DATA = 'data202221.txt'
# DATA = 'testdata202221.txt'

class SuspiciousDivision(Exception):
  """Non-integer division happened."""


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Add(a, b):
  """Add two numbers."""
  return a + b


def Subtract(a, b):
  """Subtract b from a."""
  return a - b


def Multiply(a, b):
  """Multiply two numbers."""
  return a * b


def Divide(a, b):
  """Divide a by b."""
  if a % b:
    raise SuspiciousDivision
  return a // b


def CharToOp(c):
  """Return a funtion based on the operator character."""
  optable = {'+': Add, '-': Subtract, '*': Multiply, '/': Divide}
  return optable[c]


class Monkey():
  """A monkey node class."""
  def __init__(self, name, value=None, op=None, peons=None):
    self.name = name
    self.value = value
    self.op = op
    self.peons = peons

  def __str__(self):
    return (f'name: {self.name} value: {self.value} op:{self.op}, '
            f'peons: {self.peons}')

  def Print(self, md, depth=0):
    """Print tree recursively with indentation."""
    space = '  ' * depth
    print(f'{space}{self.name} {md[self.name]}')
    if self.peons:
      for p in self.peons:
        p.Print(md, depth=depth + 1)

  def Value(self):
    """Recursively return the value of the tree from this node."""
    if self.value is not None:
      return self.value
    return self.op(self.peons[0].Value(), self.peons[1].Value())

  def Find(self, name):
    """Find the named monkey."""
    if self.name == name:
      return self
    if self.peons is None:
      return False
    return self.peons[0].Find(name) or self.peons[1].Find(name)


def BuildMonkeyDict(lines):
  """Build a dictionary of the input, keyed on monkey name."""
  monkey_dict = {}
  for line in lines:
    tokens = line.split(':')
    name = tokens[0]
    remaining_tokens = [t.strip() for t in tokens[1].split()]
    monkey_dict[name] = remaining_tokens
  return monkey_dict


def TreeFromDict(name, md):
  """Build a tree of monkeys starting with the named monkey."""
  if len(md[name]) == 1:
    return Monkey(name, value=int(md[name][0]))
  tokens = md[name]
  return Monkey(name, op=CharToOp(tokens[1]),
                peons=[TreeFromDict(tokens[0], md),
                       TreeFromDict(tokens[2], md)])

def Part1():
  """Just report the value of the tree."""
  lines = GetData(DATA)
  md = BuildMonkeyDict(lines)
  monkey_tree = TreeFromDict('root', md)
  print(f'Part 1: {monkey_tree.Value()}')


def Part2():
  """This doesn't actually solve part 2."""
  lines = GetData(DATA)
  md = BuildMonkeyDict(lines)
  peon1 = TreeFromDict(md['root'][0], md)
  peon2 = TreeFromDict(md['root'][2], md)
  print(f'peon1 is {peon1.name} worth {peon1.Value()}')
  print(f'peon2 is {peon2.name} worth {peon2.Value()}')
  if peon1.Find('humn'):
    human = peon1.Find('humn')
    target_value = peon2.Value()
    print(f'The human is under {peon1.name}')
    print(f'The target value is {target_value}')
  else:
    human = peon2.Find('humn')
    target_value = peon1.Value()
    print(f'The human is under {peon2.name}')
    print(f'The target value is {target_value}')

  # from here, I kept changing this base number and incrementing until
  # I found the answer through exhaustive searching. I'm sure this was
  # the wrong way to do it.
  # human.value = 3349136384441
  human.value = 2906
  peon1_value = float('inf')

  while peon1_value > target_value:
    human.value += 1
    try:
      peon1_value = peon1.Value()
    except SuspiciousDivision:
      continue
    print(f'{human.value} -> {peon1_value}')
    if peon1_value == target_value:
      print(f'human needs to shout {human.value}')
      break


def main():
  """main"""
  Part2()


if __name__ == '__main__':
  main()
