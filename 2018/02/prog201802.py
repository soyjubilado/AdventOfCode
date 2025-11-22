#!/usr/bin/python3
# file created 2025-Jun-30 18:34
"""https://adventofcode.com/2018/day/02"""
from collections import Counter

DATA = 'data201802.txt'
# DATA = 'testdata201802.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def CommonLetters(str1, str2):
  """Letters common between str1 and str2."""
  answer = []
  for i, c in enumerate(str1):
    if str2[i] == c:
      answer.append(c)
  return ''.join(answer)


def DifferingLetters(str1, str2):
  """Number of differing letters between str1 and str2."""
  assert len(str1) == len(str2)
  total = 0
  for i, c in enumerate(str1):
    total += 1 if c != str2[i] else 0
  return total


def FindCloseMatch(lines):
  """For part 2, find two lines that differ by just one character."""
  for i, l in enumerate(lines):
    for l2 in lines[i+1:]:
      if DifferingLetters(l, l2) == 1:
        return l, l2
  raise Exception # not found


def Part1(lines):
  """Part 1."""
  twos = 0
  threes = 0
  for line in lines:
    c = Counter(line)
    threes += 1 if 3 in c.values() else 0
    twos += 1 if 2 in c.values() else 0
  return twos * threes


def Part2(lines):
  """Part 2."""
  return CommonLetters(*FindCloseMatch(lines))


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
