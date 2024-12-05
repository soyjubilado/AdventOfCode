#!/usr/bin/python3
# file created 2024-Dec-04 21:03
"""https://adventofcode.com/2024/day/05"""


from functools import cmp_to_key
DATA = 'data202405.txt'
# DATA = 'testdata202405.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetRulesAndUpdates(lines):
  """Split input lines into rules and updates."""
  rules = []
  updates = []
  for line in lines:
    if '|' in line:
      r1, r2 = [int(i) for i in line.split('|')]
      rules.append((r1, r2))
    elif ',' in line:
      updates.append([int(i) for i in line.split(',')])
  return rules, updates


def BreaksRule(rule, update):
  """Return True if this update breaks this rule."""
  first, second = rule
  if not first in update or not second in update:
    return False
  if update.index(first) > update.index(second):
    return True
  return False


def BrokenRules(rules, update):
  """Return list of rules this update breaks, or empty set."""
  broken_rules = []
  for rule in rules:
    if BreaksRule(rule, update):
      broken_rules.append(rule)
  return broken_rules


def BrokenUpdates(rules, updates):
  """Return a list of the broken updates."""
  broken_updates = []
  for update in updates:
    if BrokenRules(rules, update):
      broken_updates.append(update)
  return broken_updates


def GenKeyCmp(rules):
  """Based on the rules, generate a comparison function for sorting."""
  def Cmp(a, b):
    forward_rules = rules
    reverse_rules = [(b, a) for a, b in rules]
    if (a, b) in forward_rules:
      return -1
    if (a, b) in reverse_rules:
      return 1
    return 0
  return Cmp


def Part1(lines):
  """Part 1."""
  total = 0
  rules, updates = GetRulesAndUpdates(lines)
  for update in updates:
    if not BrokenRules(rules, update):
      total += update[len(update)//2]
  return total


def Part2(lines):
  """Part 2."""
  rules, updates = GetRulesAndUpdates(lines)
  broken_updates = BrokenUpdates(rules, updates)
  sorting_key = cmp_to_key(GenKeyCmp(rules))
  total = 0
  for update in broken_updates:
    fixed = sorted(update, key=sorting_key)
    total += fixed[len(fixed)//2]
  return total


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
