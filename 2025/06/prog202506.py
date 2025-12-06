#!/usr/bin/python3
# file created 2025-Dec-06 07:46
"""https://adventofcode.com/2025/day/06"""

from operator import mul, add
from functools import reduce

DATA = 'data202506.txt'
DATA = 'testdata202506.txt'
OP = {'*': mul, '+': add}


def GetData(datafile):
  """Read input into a list of lines."""
  with open(datafile, 'r') as fh:
    lines = [l.replace('\n', '') for l in fh]
  return lines


def ParseDataPt1(lines):
  """Read input into a list of lines."""
  result = []
  for line in lines:
    split_line = line.split()
    result.append([i for i in split_line if i])
  expected_len = len(result[0])
  for l in result[1:]:
    assert len(l) == expected_len
  return result


def Part1(lines):
  """Part 1."""
  parsed_data = ParseDataPt1(lines)
  combined = []
  for i in range(len(parsed_data[0])):
    combined.append([line[i] for line in parsed_data])

  total = 0
  for problem in combined:
    numbers = map(int, problem[:-1])
    op = OP[problem[-1]]
    answer = reduce(op, numbers)
    total += answer
  return total


def SquareUpLines(lines):
  """Pad lines with space to make them equal length."""
  length = max([len(line) for line in lines])
  answer = []

  for line in lines:
    while len(line) < length:
      line += ' '
    answer.append(line)

  return answer


def RotateData(lines):
  """Rotate everything counterclockwise"""
  done = []
  problem = []
  lines = SquareUpLines(lines)

  for i in range(len(lines[0])):
    newline = ''.join(line[i] for line in lines)
    if newline.strip():
      problem.append(newline)
    else:
      done.append(''.join(problem[::-1]))
      problem = []
  done.append(''.join(problem[::-1]))
  return done[::-1]


def Part2(lines):
  """Part 2."""
  problems = RotateData(lines)
  total = 0
  for p in problems:
    op = OP[p[-1]]
    numbers = [int(i) for i in p[:-1].strip().split() if i.strip()]
    answer = reduce(op, numbers)
    total += answer
  return total


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
