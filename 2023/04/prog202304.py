#!/usr/bin/python3
# file created 2023-Dec-04 07:29
"""https://adventofcode.com/2023/day/4"""

DATA = 'data202304.txt'
# DATA = 'testdata202304.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GameCards(line):
  """Return the card number, set of winning numbers, set of your numbers"""
  card_num_str, cards_str = line.split(':')
  card_num = int(card_num_str.split()[1])

  winners_str, yours_str = cards_str.split('|')
  winners = {int(i) for i in winners_str.split()}
  yours = {int(i) for i in yours_str.split()}

  return card_num, winners, yours


def Part1(lines):
  """Part 1"""
  total = 0
  for line in lines:
    _, winners, yours = GameCards(line)
    matches = len(winners.intersection(yours))
    if matches > 0:
      total += 2**(matches - 1)
  return total


def Part2(lines):
  """Part 2"""
  cards_dict = {i: 1 for i in range(1, (len(lines)+1))}
  for line in lines:
    card_num, winners, yours = GameCards(line)
    matches = len(winners.intersection(yours))
    if matches > 0:
      start = card_num + 1
      end = start + matches
      for i in range(start, end):
        addend = cards_dict[card_num]
        cards_dict[i] += addend

  return sum(cards_dict.values())


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
