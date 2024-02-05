#!/usr/bin/python3
# file created 2023-Feb-14 20:40
"""https://adventofcode.com/2016/day/7"""

DATA = 'data201607.txt'


class WordTooShort(Exception):
  """If a word is unexpectedly too short."""


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def SplitBrackets(lines):
  """Given input as a list of lines, return a list of tuples; each tuple
     contains the words outside brackets and the words inside brackets
     from the line."""
  parens_lists = []
  for l in lines:
    l = l.replace('[', ' ')
    l = l.replace(']', ' ')
    splitted = l.split(' ')
    nonparens = [w for idx, w in enumerate(splitted) if not idx % 2]
    parens = [w for idx, w in enumerate(splitted) if idx % 2]
    parens_lists.append((nonparens, parens))
  return parens_lists


def ContainsAbba(word):
  """If ABBA pattern exists in word, return the first instance of it;
     otherwise return False."""
  if len(word) < 4:
    raise WordTooShort
  for i in range(len(word)-3):
    if (word[i] == word[i+3] and
        word[i+1] == word[i+2] and
        word[i] != word[i+1]):
      return word[i:i+4]
  return False


def AllAba(word):
  """If ABA pattern exists in word, return all instances of it; else
     return empty list."""
  if len(word) < 3:
    raise WordTooShort
  all_aba = []
  for i in range(len(word)-2):
    if (word[i] == word[i+2] and
        word[i] != word[i+1]):
      all_aba.append(word[i:i+3])
  return all_aba


def Flipped(word):
  """Flip a word for part 2."""
  assert len(word) == 3
  assert word[0] == word[2]
  return word[1] + word[0] + word[1]


def Part1(lines):
  """Return count for part 1."""
  counter = 0
  parenthised = SplitBrackets(lines)
  for outside, inside in parenthised:
    outside_abba = [ContainsAbba(w) for w in outside if ContainsAbba(w)]
    inside_abba = [ContainsAbba(w) for w in inside if ContainsAbba(w)]
    if outside_abba and not inside_abba:
      counter += 1
  return counter


def Part2(lines):
  """Return a count for part 2."""
  counter = 0
  parenthised = SplitBrackets(lines)
  for outside, inside in parenthised:
    outside_aba = []
    inside_aba = []
    for word in outside:
      outside_aba.extend(AllAba(word))
    for word in inside:
      inside_aba.extend(AllAba(word))
    common = [w for w in inside_aba if Flipped(w) in outside_aba]
    counter += 1 if common else 0
  return counter


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
