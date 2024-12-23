#!/usr/bin/python3
# file created 2024-Dec-23 08:36
"""https://adventofcode.com/2024/day/23"""
from functools import lru_cache
from itertools import combinations


CONNECT = None
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
  """Return a list of triply connected computers for part 1."""
  all_triples = set()
  tees = [k for k in connect if k.startswith('t')]
  for k in tees:
    other_pairs = combinations(connect[k], 2)
    for a, b in other_pairs:
      if b in connect[a]:
        all_triples.add(frozenset([k, a, b]))
  return all_triples


@lru_cache(maxsize=None)
def MaxClique(my_frozen_set):
  """Return the largest fully-connected set from my_set.
  Relies on global dictionary CONNECT.
  """
  if len(my_frozen_set) < 2:
    return set(my_frozen_set)
  if len(my_frozen_set) == 2:
    c1, c2 = my_frozen_set
    if c2 in CONNECT[c1]:
      return set(my_frozen_set)
    return {c1}

  # more than 2 items left
  candidates = []
  for i in my_frozen_set:
    subset = set(my_frozen_set)
    subset.remove(i)
    sub_subset = set(j for j in subset if j in CONNECT[i])
    if not sub_subset:
      this_cand = {i}
      candidates.append(this_cand)
      continue
    this_cand = {i}
    this_cand = this_cand.union(MaxClique(frozenset(sub_subset)))
    candidates.append(this_cand)
  candidates.sort(key=lambda x: len(x))
  return candidates[-1]


def Part1(lines):
  """Part 1."""
  connect = GetConnected(lines)
  triples = GetTriples(connect)
  return len(triples)


def Part2(lines):
  """Part 2."""
  global CONNECT
  connected = GetConnected(lines)
  CONNECT = {k: frozenset(v) for k, v in connected.items()}
  cliques = []
  for k, v in CONNECT.items():
    this_set = set([k])
    this_set = this_set.union(MaxClique(CONNECT[k]))
    cliques.append(this_set)
  
  cliques = list(set(frozenset(c) for c in cliques))
  cliques.sort(key=lambda x: len(x))
  answer = sorted(list(cliques[-1]))
   
  return ','.join(answer)


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
