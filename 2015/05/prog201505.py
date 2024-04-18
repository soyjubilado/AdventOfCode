#!/usr/bin/python3
"""
https://adventofcode.com/2015/day/5

It contains at least three vowels (aeiou only), like
aei, xazegov, or aeiouaeiouaeiou.

It contains at least one letter that appears twice
in a row, like xx, abcdde (dd), or aabbccdd (aa, bb,
cc, or dd).

It does not contain the strings ab, cd, pq, or xy,
even if they are part of one of the other
requirements.
"""
import re
from collections import defaultdict

DATA = 'data201505.txt'
VOWELS = set(['a', 'e', 'i', 'o', 'u'])
BADWORDS_RE = [re.compile(r'ab'),
               re.compile(r'cd'),
               re.compile(r'pq'),
               re.compile(r'xy'),
              ]


def ThreeVowels(my_str):
  """At least three vowels."""
  my_vowels = []
  for x in my_str:
    if x in VOWELS:
      my_vowels.append(x)
  return len(my_vowels) >= 3


def DoubleLetter(my_str):
  """A double letter."""
  for n in range(1, len(my_str)):
    if my_str[n] == my_str[n-1]:
      return True
  return False


def BadWords(my_str):
  """Contains bad words."""
  for bw_re in BADWORDS_RE:
    if bw_re.search(my_str):
      return True
  return False


def IsNicePt1(my_str):
  """Considered nice for part 1."""
  return not BadWords(my_str) and ThreeVowels(my_str) and DoubleLetter(my_str)


def PairIndices(my_str):
  """Return a dictionary of all the pairs, their indices."""
  pairs = defaultdict(lambda: [])
  for idx in range(len(my_str) - 1):
    pair = my_str[idx:idx+2]
    pairs[pair].append(idx)
  return pairs


def MoreThan2Nonconsecutive(my_list):
  """Return true if a list contains at least 2 nonconsecutive ints."""
  if len(my_list) < 2:
    return False
  if len(my_list) > 2:
    return True
  if my_list[1] - my_list[0] > 1:
    return True
  return False


def TwoLettersTwice(my_str):
  """my_str contains two letters twice, non-overlapping"""
  pair_indices = PairIndices(my_str)
  for indices in pair_indices.values():
    if MoreThan2Nonconsecutive(indices):
      return True
  return False


def PairSepSingle(my_str):
  """my_str contains same letter separated by a letter"""
  for i in range(2, len(my_str)):
    if my_str[i] == my_str[i-2]:
      return True
  return False


def IsNicePt2(my_str):
  """Word is nice by part 2 definition."""
  if TwoLettersTwice(my_str) and PairSepSingle(my_str):
    return True
  return False


def Part2(lines):
  """Part 2"""
  counter = 0
  for l in lines:
    if IsNicePt2(l):
      counter += 1
  return counter


def Part1(lines):
  """Part 1"""
  counter = 0
  for l in lines:
    if IsNicePt1(l):
      counter += 1
  return counter


def main():
  """Main"""
  with open(DATA, 'r') as fh:
    lines = [i.strip() for i in fh]
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
