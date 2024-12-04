#!/usr/bin/python3
# file created 2024-Dec-02 20:59
"""https://adventofcode.com/2024/day/03"""

import re


DATA = 'data202403.txt'
# DATA = 'testdata202403.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def EvaluateMul(m):
  """Evaluate the mul(a,b) operation and return the result."""
  a, b = [int(i) for i in m[4:-1].split(',')]
  return a * b


def GetAllInstructions(lines):
  """Return a single list of all the extracted ops:
     These include 'mul(a,b)' 'do()' and "don't()".
  """
  re_do_dont = re.compile(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')
  all_instructions = []
  for l in lines:
    these_instructions = re_do_dont.findall(l)
    all_instructions.extend(these_instructions)
  return all_instructions


def Part1(lines):
  """Part 1"""
  re_mul = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
  total = 0
  for l in lines:
    muls = re_mul.findall(l)
    for m in muls:
      total += EvaluateMul(m)
  return total


def Part2(lines):
  """Part 2"""
  all_instructions = GetAllInstructions(lines)
  doing = True
  total = 0
  for op in all_instructions:
    if op == "don't()":
      doing = False
    if op == "do()":
      doing = True
    if op.startswith('mul') and doing:
      total += EvaluateMul(op)
  return total


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
