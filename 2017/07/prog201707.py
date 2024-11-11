#!/usr/bin/python3
#file created 2022-Mar-16 15:50
"""https://adventofcode.com/2017/day/7"""

from collections import defaultdict
DATA = 'data201707.txt'
# DATA = 'testdata201707.txt'


def GetData(datafile):
  """Read the input file."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def WeightsAndChildren(lines):
  """Given the input, create two dictionaries:
     (1) names and weights
     (2) names and children
  """
  weights = {}
  children = {}
  for line in lines:
    items = [i.strip() for i in line.split()]
    weights[items[0]] = int(items[1][1:-1])
    if len(items) > 2:
      children[items[0]] = [i.replace(',', '') for i in items[3:]]
  return weights, children


def ParentsOf(children):
  """Given a dictionary of names and children, create a dictionary
     of children and parents."""
  parents = {}
  for p in children:
    for child in children[p]:
      parents[child] = p
  return parents


class Node():
  """A node in the tree."""

  def __init__(self, name, weights, children):
    """Recursively build the whole tree at once."""
    self.name = name
    self.weight = weights[name]
    self.total_weight = None
    self.children = []
    if name in children:
      for child in children[name]:
        child_node = Node(child, weights, children)
        self.children.append(child_node)

  def Print(self, indent=0):
    """Recursively print the tree."""
    print(f'{" " * indent}{self.name} ({self.weight})')
    for c in self.children:
      c.Print(indent + 1)

  def TotalWeight(self):
    """Only call this after the tree has been created."""
    total = self.weight
    for c in self.children:
      total += c.TotalWeight()
    self.total_weight = total
    return total


def Part2(tree, weight_delta=0):
  """Part 2 is recursive."""
  weights = defaultdict(lambda: [])
  children = tree.children
  for c in children:
    weights[c.total_weight].append(c.name)
  badweights = [w for w in weights if len(weights[w]) == 1]
  if not badweights:
    print(f'tree balanced below {tree.name}, my weight is {tree.weight}')
    print(f'  my ideal weight is {tree.weight + weight_delta}')
  else:
    goodweights = [w for w in weights if len(weights[w]) > 1]
    print(f'siblings have weight {goodweights[0]} not {badweights[0]}')
    weight_delta = goodweights[0] - badweights[0]
    bad_children = [c for c in children if c.total_weight == badweights[0]]
    Part2(bad_children[0], weight_delta)


def main():
  """main program"""
  lines = GetData(DATA)
  weights, children = WeightsAndChildren(lines)
  parents = ParentsOf(children)
  heads = [i for i in weights if not i in parents]
  assert len(heads) == 1
  head = heads[0]
  print(f'answer to Part 1: {head}')
  tree = Node(head, weights, children)
  print(f'Total weight of tree: {tree.TotalWeight()}')
  Part2(tree)


if __name__ == '__main__':
  main()
