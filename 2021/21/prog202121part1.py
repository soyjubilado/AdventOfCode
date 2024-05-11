#!/usr/bin/python3
#file created 2021-Dec-20 20:58
"""https://adventofcode.com/2021/day/21"""

from random import randint
DATA = 'data202121.txt'
#DATA = 'testdata202121.txt'


class Die(object):

  def __init__(self):
    self.rolls = 0
    self.roll_index = 0


class Pt1Die(Die):
  def Roll(self):
    while True:
      i = self.roll_index
      value = (i % 100 + 1) + ((i+1) % 100 + 1) + ((i+2) % 100 + 1)
      desc = f'{i % 100 + 1} + {(i+1) % 100 + 1} + {(i+2) % 100 + 1} = {value}'
      self.rolls += 3
      i += 3
      if i > 100:
        i = i - 100
      self.roll_index = i
      yield value, desc


def Play():
  winner = None
  player1 = 'Player1'
  player2 = 'Player2'
  winning_score = 1000
  play1_pos = 4
  play1_score = 0
  play1_roll_list = []

  play2_pos = 8
  play2_score = 0
  play2_roll_list = []
  print(f'Player 1 starts at {play1_pos}, Player 2 at {play2_pos}')
  d = Pt1Die()
  die_roll = d.Roll()
  while play1_score < winning_score and play2_score < winning_score:
    p1_roll, p1_desc = next(die_roll)
    play1_roll_list.append(p1_roll)
    play1_pos = ((play1_pos + p1_roll - 1) % 10) + 1
    play1_score += play1_pos
    print(f'player 1 rolls {p1_desc} moves to {play1_pos} for {play1_score}')
    if play1_score >= winning_score:
      print(f'player 1 wins with {play1_score}')
      print(f'die was rolled {d.rolls} times')
      print(f'player 2 had {play2_score} points')
      print(f'{play2_score} * {d.rolls} = {play2_score * d.rolls}')
      winner = player1
      return winner, tuple(play1_roll_list), tuple(play2_roll_list)

    p2_roll, p2_desc = next(die_roll)
    play2_roll_list.append(p2_roll)
    play2_pos = ((play2_pos + p2_roll - 1) % 10) + 1
    play2_score += play2_pos
    print(f'player 2 rolls {p2_desc} moves to {play2_pos} for {play2_score}')

  print(f'player 2 wins with {play2_score}')
  print(f'die was rolled {d.rolls} times')
  print(f'player 1 had {play1_score} points')
  print(f'{play1_score} * {d.rolls} = {play1_score * d.rolls}')
  winner = player2
  return winner, tuple(play1_roll_list), tuple(play2_roll_list)
    

def main():
  Play()


if __name__ == '__main__':
  main()
