#!/usr/bin/python3
#file created 2022-Dec-01 20:36
"""https://adventofcode.com/2022/day/2"""

DATA = 'data202202.txt'


def Score(them, us):
  ShapeScore = {'X': 1,
                'Y': 2,
                'Z': 3,}
  score = ShapeScore[us]

  Ties = {'A': 'X', 'B': 'Y', 'C': 'Z'}
  Wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
  Loss = {'A': 'Z', 'B': 'X', 'C': 'Y'}

  if Ties[them] == us:
    score += 3
  elif Wins[them] == us:
    score += 6
  else:
    pass

  return score


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Part1():
  lines = GetData(DATA)
  total = 0
  for l in lines:
    them, us = l.split()
    score = Score(them, us)
    # print(f'{them} {us} -> {score}')
    total += score 
  print(f'Part 1 total: {total}')


def Part2():
  shape_value = {('A', 'X'): 3, # rock scissors
                 ('A', 'Y'): 1, # rock rock
                 ('A', 'Z'): 2, # rock paper
                 ('B', 'X'): 1, # paper rock
                 ('B', 'Y'): 2, # paper paper
                 ('B', 'Z'): 3, # paper scissors
                 ('C', 'X'): 2, # scissors paper
                 ('C', 'Y'): 3, # scissors scissors
                 ('C', 'Z'): 1, # scissors rock
                }

  lines = GetData(DATA)
  total = 0
  goal_score = {'X': 0, 'Y': 3, 'Z': 6}

  for l in lines:
    them, goal = l.split()
    score = shape_value[(them, goal)]
    score += goal_score[goal]
    # print(f'{them} {goal} -> {score}')
    total += score 
  print(f'Part 2 total: {total}')


def main():
  Part1()
  Part2()


if __name__ == '__main__':
  main()
