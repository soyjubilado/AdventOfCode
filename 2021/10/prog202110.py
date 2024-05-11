#!/usr/bin/python3
#file created 2021-Dec-09 20:59
"""https://adventofcode.com/2021/day/10"""

DATA = 'data202110.txt'
# DATA = 'testdata202110.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetFirstIllegal(line):
  """Finds the first non-matching character, returns it and the
     remaining stack of non-matched characters."""
  retval = None
  stack = []
  for char in line:
    if char in ['(', '[', '{', '<']:
      stack.append(char)
    else:
      left = stack.pop()
      if not Matches(left, char):
        retval = char
        break
  return retval, stack


def Matches(left, right):
  """Checks if left and right are a matching pair."""
  pairs = {'(': ')',
           '[': ']',
           '{': '}',
           '<': '>',
          }
  if pairs[left] == right:
    return True
  return False


def Part1():
  Points = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0,}
  lines = GetData(DATA)
  score = 0
  for line in lines:
    first_illegal, _ = GetFirstIllegal(line)
    score += Points[first_illegal]
  print(f'Part 1: {score}')


def GetLineScore(stack):
  """Calculate score for an incomplete line in Part 2."""
  Points = {'(': 1, '[': 2, '{': 3, '<': 4,}
  score = 0
  for i in reversed(stack):
    score = score * 5 + Points[i]
  return score


def Part2():
  lines = GetData(DATA)
  score_list = []
  for line in lines:
    first_illegal, stack = GetFirstIllegal(line)
    if first_illegal is None:
      line_score = GetLineScore(stack)
      score_list.append(line_score)
  scores = sorted(score_list)
  items = len(scores)
  print(f'Part 2: {scores[items//2]}')


def main():
  Part1()
  Part2()


if __name__ == '__main__':
  main()
