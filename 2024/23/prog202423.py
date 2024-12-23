#!/usr/bin/python3
# file created 2024-Dec-23 08:36
"""https://adventofcode.com/2024/day/23"""
from itertools import combinations

DATA = 'data202423.txt'
# DATA = 'testdata202423.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetConnected(lines):
  """Return a dictionary of every node and its connectivity to others."""
  connect = {}
  for l in lines:
    c1, c2 = l.split('-')
    connect[c1] = connect.get(c1, set())
    connect[c1].add(c2)
    connect[c2] = connect.get(c2, set())
    connect[c2].add(c1)
  return connect


def GetTriples(connect):
  """Return a list of triply connected computers."""
  all_triples = set()
  tees = [k for k in connect if k.startswith('t')]
  for k in tees:
    other_pairs = combinations(connect[k], 2)
    for a, b in other_pairs:
      if b in connect[a]:
        all_triples.add(frozenset([k, a, b]))
  return all_triples


def Part1(lines):
  """Part 1."""
  connect = GetConnected(lines)
  triples = GetTriples(connect)
  return len(triples)


def Part2(lines):
  """Part 2."""
  return None


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  # print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
