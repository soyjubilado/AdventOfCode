#!/usr/bin/python3
# file created 2023-Dec-06 11:22
"""https://adventofcode.com/2023/day/6"""

from math import sqrt, ceil
DATA = 'data202306.txt'
# DATA = 'testdata202306.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetRaces(lines):
  """From lines, return a list of races (time, distance_record)."""
  line0 = [int(i.strip()) for i in lines[0].split()[1:]]
  line1 = [int(i.strip()) for i in lines[1].split()[1:]]
  return list(zip(line0, line1))


def GetBigRace(lines):
  """From lines, return the big race for part 2."""
  time = int(lines[0].split(':')[1].replace(' ', ''))
  distance = int(lines[1].split(':')[1].replace(' ', ''))
  return time, distance


def BruteForceNumWays(race):
  """Brute force method to determine number of ways to win."""
  time, record = race
  i = 0
  low = 0
  high = 0
  while (time - i) * i <= record:
    i += 1
  low = i
  while (time - i) * i > record:
    i += 1
  high = i
  return low, high


def MathNumWays(race):
  """Mathy way to determine number of ways. It uses the quadratic formula to
     get close to the edge cases, and then brute force to zero in on the exact
     start and end of the range."""
  time, record = race
  lower = ceil((time - sqrt(time * time - 4 * record))/2)
  upper = ceil((time + sqrt(time * time - 4 * record))/2)

  # fudge factor
  fudge = 2
  i = lower - fudge
  while (time - i) * i <= record:
    i += 1
  low = i

  i = upper - fudge
  while (time - i) * i > record:
    i += 1
  high = i

  return low, high


def Part1(races):
  """Part 1"""
  answer = 1
  for race in races:
    low, high = MathNumWays(race)
    answer *= (high - low)
  return answer

def Part2(race):
  """Part 2"""
  low, high = MathNumWays(race)
  return high - low


def main():
  """main"""
  lines = GetData(DATA)
  races = GetRaces(lines)
  big_race = GetBigRace(lines)
  print(f'Part 1: {Part1(races)}')
  print(f'Part 2:: {Part2(big_race)}')


if __name__ == '__main__':
  main()
