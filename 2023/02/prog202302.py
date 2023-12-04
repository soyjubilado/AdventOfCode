#!/usr/bin/python3
# file created 2023-Dec-02 16:59
"""https://adventofcode.com/2023/day/2"""

DATA = 'data202302.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def ParseLine(line):
  """Returns an ID and a list of dicts keyed on color."""
  game, all_hands = line.split(':')
  game_id = game.split()[1].strip()
  hands = [i.strip() for i in all_hands.split(';')]
  hands_list = []
  for hand in hands:
    colors_dict = {}
    segments = [i.strip() for i in hand.split(',')]
    for seg in segments:
      subseg = seg.split()
      num, color = int(subseg[0]), subseg[1]
      colors_dict[color] = num
    hands_list.append(colors_dict)
  return int(game_id), hands_list


def ExceedsMax(hands, max_cubes):
  """Does a given hand exceed the max allowable number of cubes?"""
  for hand in hands:
    for color in hand:
      if color in max_cubes and hand[color] > max_cubes[color]:
        return True
  return False


def PowerSet(hands):
  """Given a minimum set of cubes, multiply all the values together."""
  min_colors = {'red': 1, 'blue': 1, 'green': 1}
  for hand in hands:
    for color in min_colors:
      if hand.get(color, 1) > min_colors[color]:
        min_colors[color] = hand.get(color, 1)
  power = 1
  for color, val in min_colors.items():
    power *= val
  return power


def Part1(lines):
  """Part 1"""
  max_cubes = {'red': 12, 'green': 13, 'blue': 14}
  total = 0

  for line in lines:
    game_id, hands = ParseLine(line)
    if not ExceedsMax(hands, max_cubes):
      total += game_id
  return total


def Part2(lines):
  """Part 2"""
  power_sum = 0
  for line in lines:
    _, hands = ParseLine(line)
    power_sum += PowerSet(hands)
  return power_sum


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
