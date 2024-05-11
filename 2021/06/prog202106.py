#!/usr/bin/python3
"""https://adventofcode.com/2021/day/06"""

from collections import defaultdict
DATA = 'data06.txt'

def GetData(datafile):
  """Parse input"""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def TransformFishMap(fish_map, num_rounds):
  """Determine what the fish_map looks like after num_rounds."""
  for _ in range(num_rounds):
    prev_zero = fish_map[0]
    for n in range(1, 9):
      fish_map[n-1] = fish_map[n]
    fish_map[8] = prev_zero
    fish_map[6] += prev_zero
  return fish_map


def GenFishMap(fish_data):
  """Given a list of fish ages, create a map of how many of each age."""
  fish_map = defaultdict(lambda: 0)
  for i in fish_data:
    fish_map[i] += 1
  return fish_map


def main():
  lines = GetData(DATA)
  fish_data = [int(i) for i in lines[0].split(',')]

  for round_num, iterations in [(1, 80), (2, 256)]:
    print(f'Part {round_num}: {iterations} iterations')
    fish_map = GenFishMap(fish_data)
    new_map = TransformFishMap(fish_map, iterations)

    print(f'total: {sum(new_map.values())}')


main()
