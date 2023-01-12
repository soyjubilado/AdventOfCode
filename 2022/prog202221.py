#!/usr/bin/python3
# file created 2022-Dec-21 08:11
"""https://adventofcode.com/2022/day/21"""

DATA = 'data202221.txt'
# DATA = 'testdata202221.txt'


# Note: integer division is used here due to known clean input
Add = lambda a, b: a + b
Subtract = lambda a, b: a - b
Multiply = lambda a, b: a * b
Divide = lambda a, b: a // b
Minuend = lambda subtrahend, difference: subtrahend + difference
Subtrahend = lambda minuend, difference: minuend - difference
Divisor = lambda dividend, quotient: dividend // quotient
Dividend = lambda divisor, quotient: divisor * quotient
Factor = lambda factor, product: product // factor
Addend = lambda addend, summation: summation - addend


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def CharToOp(c):
  """Return a function based on the operator character."""
  optable = {'+': Add,
             '-': Subtract,
             '*': Multiply,
             '/': Divide,
             None: None}
  return optable[c]


class Monkey():
  """A monkey node class."""
  def __init__(self, name, value=None, op_symbol=None, peons=None):
    self.name = name
    self.value = value
    self.op_symbol = op_symbol
    self.op = CharToOp(op_symbol)
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
    """Find the named monkey and return a reference to it or None."""
    if self.name == name:
      return self
    if self.peons is None:
      return None
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
  return Monkey(name, op_symbol=tokens[1],
                peons=[TreeFromDict(tokens[0], md),
                       TreeFromDict(tokens[2], md)])


def GetMonkeyTree(input_file):
  """Return the root node of a monkey tree given the input file name."""
  lines = GetData(input_file)
  md = BuildMonkeyDict(lines)
  return TreeFromDict('root', md)


def OrderPeons(monkey):
  """Of the two peons in this node, return the one that is the ancestor
     of the human, the other one, and the index of the first."""
  if not monkey.peons:
    raise Exception
  if monkey.peons[0].Find('humn'):
    return monkey.peons[0], monkey.peons[1], 0
  if monkey.peons[1].Find('humn'):
    return monkey.peons[1], monkey.peons[0], 1
  raise Exception


def SubPeonAndTargetValue(monkey, target):
  """This is the heavy lifting function for part 2. Given a monkey and a
     target value that this monkey should have, calculate the value that
     the human ancestor peon below this monkey should have."""
  human_peon, other_peon, human_idx = OrderPeons(monkey)
  if monkey.op_symbol == '+':
    new_target = Addend(other_peon.Value(), target)
  elif monkey.op_symbol == '*':
    new_target = Factor(other_peon.Value(), target)
  elif monkey.op_symbol == '/' and human_idx == 0:
    new_target = Dividend(other_peon.Value(), target)
  elif monkey.op_symbol == '/' and human_idx == 1:
    new_target = Divisor(other_peon.Value(), target)
  elif monkey.op_symbol == '-' and human_idx == 0:
    new_target = Minuend(other_peon.Value(), target)
  elif monkey.op_symbol == '-' and human_idx == 1:
    new_target = Subtrahend(other_peon.Value(), target)
  else:
    print(f'Error: {monkey.name} {monkey.op_symbol}')
    raise Exception
  return human_peon, new_target


def Part1():
  """Just report the value of the tree."""
  monkey_tree = GetMonkeyTree(DATA)
  print(f'Part 1: {monkey_tree.Value()}')


def Part2():
  """The starting node is human_peon, the peon of root that is the
     ancestor of humn. The starting target is the value of the tree
     starting at the other peon. As you traverse down the tree we
     keep descending the branch where humn is, and calculate what value
     we need at each step down the tree."""
  root = GetMonkeyTree(DATA)
  human_peon, other_peon, _ = OrderPeons(root)
  target_value = other_peon.Value()
  peon, target = SubPeonAndTargetValue(human_peon, target_value)

  while peon.name != 'humn':
    peon, target = SubPeonAndTargetValue(peon, target)
  print(f'Part 2: {target}')


def main():
  """main"""
  Part1()
  Part2()


if __name__ == '__main__':
  main()
