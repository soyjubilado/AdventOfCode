#!/usr/bin/python3
#file created 2022-Dec-07 19:33
# 11 minutes to part 1, 23 minutes to part 2
"""https://adventofcode.com/2016/day/2"""

DATA = 'data201602.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def U(n):
  return n if n in [1, 2, 3] else n - 3

def R(n):
  return n if n in [3, 6, 9] else n + 1

def D(n):
  return n if n in [7, 8, 9] else n + 3

def L(n):
  return n if n in [1, 4, 7] else n - 1


def Part1(lines):
  MOVE = {'U': U, 'R': R, 'D': D, 'L': L}
  answer = []
  current = 5
  for line in lines:
    for d in line:
      current = MOVE[d](current)
    answer.append(current)
  print(answer)


def U2(n):
  if n in [5, 2, 1, 4, 9]:
    return n
  elif n in [6, 7, 8, 10, 11, 12]:
    return n - 4
  return n - 2

def R2(n):
  if n in [1, 4, 9, 12, 13]:
    return n
  return n + 1

def D2(n):
  if n in [5, 10, 13, 12, 9]:
    return n
  elif n in [2, 3, 4, 6, 7, 8]:
    return n + 4
  return n + 2

def L2(n):
  if n in [1, 2, 5, 10, 13]:
    return n
  return n - 1


def Part2(lines):
  MOVE2 = {'U': U2, 'R': R2, 'D': D2, 'L': L2}
  answer = []
  current = 5
  for line in lines:
    for d in line:
      current = MOVE2[d](current)
    answer.append(current)
  # print(answer)
  a_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D'}
  answer_str = [a_dict.get(i, i) for i in answer]
  print(answer_str)


def main():
  lines = GetData(DATA)
  Part1(lines)
  Part2(lines)


if __name__ == '__main__':
  main()
