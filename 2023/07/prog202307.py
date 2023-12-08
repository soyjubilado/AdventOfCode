#!/usr/bin/python3
# file created 2023-Dec-07 06:25
"""https://adventofcode.com/2023/day/7"""

DATA = 'data202307.txt'
# DATA = 'testdata202307.txt'

# Two kinds of decks, one with Jack, one with Jokers
CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
JCARDS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


# for debugging output
KIND_NAME = {1: 'five of a kind',
             2: 'four of a kind',
             3: 'full house',
             4: 'three of a kind',
             5: 'two pair',
             6: 'pair',
             7: 'milpitas',}


class ModeNotFound(Exception):
  """Unable to find Mode."""


class BadProgrammer(Exception):
  """Probably specified part not in ['Part1', 'Part2']"""


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Mode(hand):
  """The most common card in the hand that is not 'J'
  Assume that there is a 'J' and that it is not all 'J'.
  """
  card_dict = {c: hand.count(c) for c in set(hand) if c != 'J'}
  max_count = max(card_dict.values())
  for c in set(hand):
    if c != 'J' and card_dict[c] == max_count:
      return c
  raise ModeNotFound


def ReplaceJokers(hand):
  """Replace all 'J' with the mode card in hand that is not J"""
  if 'J' not in hand:
    return hand[:]
  if hand.count('J') == len(hand):
    return hand[:]
  return hand.replace('J', Mode(hand))


class Hand:
  """Class for a hand of cards."""

  def __init__(self, line, part='Part1'):
    """Initialize the object."""
    hand, bid = line.split()
    self.SetCardsValues(part)
    self.hand = hand
    self.bid = int(bid)
    self.strength = self.Strength(part)
    self.secondary_key = [self.card_value[c] for c in self.hand]
    self.sorter = (self.strength, self.secondary_key)

  def SetCardsValues(self, part):
    """self.card_value is the order in which cards are valued."""
    if part == 'Part1':
      deck = CARDS
    elif part == 'Part2':
      deck = JCARDS
    else:
      raise BadProgrammer
    self.card_value = {val: idx+1 for idx, val in enumerate(deck)}

  def Strength(self, part):
    """Relative strength of hand."""
    hand = self.hand[:]
    if part == 'Part2':
      hand = ReplaceJokers(hand)

    # a list of the counts of the different values in the hand
    cardcount = [hand.count(i) for i in set(hand)]
    if max(cardcount) == 5:
      retval = 1
    elif max(cardcount) == 4:
      retval = 2
    elif max(cardcount) == 3 and len(cardcount) == 2:
      retval = 3
    elif max(cardcount) == 3:
      retval = 4
    elif max(cardcount) == 2 and len(cardcount) == 3:
      retval = 5
    elif max(cardcount) == 2:
      retval = 6
    elif max(cardcount) == 1:
      retval = 7
    else:
      retval = None
    if retval:
      return retval
    raise BadProgrammer

  def __repr__(self):
    return f'({self.hand}, {self.bid}, ({self.strength}, {self.secondary_key})'


def Solve(lines, part='Part1'):
  """Part 1"""
  hands = [Hand(line, part) for line in lines]
  sorted_hands = sorted(hands, key=lambda h: h.sorter, reverse=True)
  answer = 0
  for idx, h in enumerate(sorted_hands):
    answer += (idx + 1) * h.bid
  return answer


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Solve(lines)}')
  print(f'Part 2: {Solve(lines, part="Part2")}')


if __name__ == '__main__':
  main()
