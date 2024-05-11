#!/usr/bin/python3

from collections import defaultdict

NUM_VERSES = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


def Score(start, rolls_list):
  """rolls_list is a list or iterable"""
  score = 0
  position = start
  for r in rolls_list:
    position = ((position + r - 1) % 10) + 1
    score += position
  return score
  

def Verses(rolls_list):
  """Given a list of rolls, return how many universes that represents."""
  verses = 1
  for i in rolls_list:
    verses *= NUM_VERSES[i]
  return verses


def testScore():
  tests = [[[10, [1]], 1],
           [[10, [9]], 9],
           [[10, [9, 1]], 19],
           [[10, [9, 1, 2]], 21],
           [[4, [9, 9, 9, 3]], 10],
           [[4, [9, 9, 9, 3, 9, 9, 9, 3]], 20],
          ]
  for c in tests:
    case, expected = c
    start, rolls = case
    actual = Score(start, rolls)
    passing = 'pass' if actual == expected else 'fail'
    print(f'{passing}: {case}: {actual} (expected {expected})')


def Gen21Rolls(start_pos=4):
  """Given a starting position on the board, generate all the possible rolls
  that will give a score of 21 or more."""
  reach_21 = []
  short_21 = [[3], [4], [5], [6], [7], [8], [9]]
  count = 1
  while short_21:
    for r in short_21[:]:
      if Score(start_pos, r) >= 21:
        reach_21.append(r)
        short_21.remove(r)
    still_short_21 = []
    for r in short_21[:]:
      for i in range(3, 10):
        r_copy = r[:]
        r_copy.append(i)
        still_short_21.append(r_copy)
    short_21 = still_short_21
    print(f'End of round {count}: {len(reach_21)}/{len(short_21)}')
    count += 1
  return reach_21


def TruncatedRolls(length, rolls_list):
  """Returned a de-duped list of rolls of length N-1 from the list, but
  only of rolls that are already of length N."""
  retval = set([])
  for r in rolls_list:
    if len(r) >= length:
      retval.add(tuple(r[:length - 1]))
  return [list(r) for r in retval]


def testTruncatedRolls():
  testcases = [[[[[1, 2, 3], [4, 5]], 3], [[1, 2]]],
              [[[[1, 2, 3], [4, 5]], 2], [[1], [4]]],
              ]
  for case, expected in testcases:
    rolls, length = case
    actual = TruncatedRolls(length, rolls)
    passing = 'pass' if actual == expected else 'fail'
    print(f'{passing}: {case} -> {actual} (expected: {expected})')


def main():
  # Generate all the possible routes to 21 points for both players.
  p1_rolls = Gen21Rolls(6)
  p2_rolls = Gen21Rolls(8)

  # create a dictionary keyed on (rolls_length, universes): how many
  p1_lengths = set([])
  p1_roll_dict = defaultdict(lambda: 0)
  for p1r in p1_rolls:
    p1_roll_dict[(len(p1r), Verses(p1r))] += 1
    p1_lengths.add(len(p1r))

  # Assuming player 1 is going to be the winner:
  # For every length roll in player 1's dictionary, create a dictionary of
  # player 2 rolls that don't reach 21. This is all p2_rolls of length L or
  # more, truncated to L-1 (because player 1 goes first) and then de-duped.
  answer = 0
  for le in p1_lengths:
    p2_roll_dict = defaultdict(lambda: 0)
    p2_subrolls = TruncatedRolls(le, p2_rolls)
    for p2r in p2_subrolls:
      p2_roll_dict[Verses(p2r)] += 1
  
    p1_verses = 0
    for key, how_many in p1_roll_dict.items():
      length, verses = key
      if length == le:
        p1_verses += verses * how_many

    p2_verses = 0
    for verses, how_many in p2_roll_dict.items():
      p2_verses += verses * how_many

    # add the number of p1 universes times number of p2 universes
    answer += p1_verses * p2_verses
  print(f'Wild ass guess: {answer}')


if __name__ == '__main__':
  # testTruncatedRolls()
  main()
