#!/usr/bin/python3
"""https://adventofcode.com/2021/day/04"""

DATA = 'data04.txt'
# DATA = 'testdata04.txt'

BINGOS = [set([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]),
          set([(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]),
          set([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]),
          set([(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]),
          set([(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]),

          set([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]),
          set([(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]),
          set([(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)]),
          set([(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)]),
          set([(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]),

          # set([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
          # set([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]),
         ]


def GetData(datafile):
  """Parse input file."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


class BingoBoard(object):
  """Object representing one bingo board."""

  def __init__(self, board_list):
    self.bing_dict = self.BuildDict(board_list)
    self.played_marks = set([])
    self.bingo_set = None

  def BuildDict(self, board_list):
    """From raw input build a dictionary of coordinates and values."""
    list_list = []
    for line in board_list:
      list_list.append([int(i) for i in line.strip().split()])
    my_dict = {}
    for y in range(5):
      for x in range(5):
        my_dict[(x, y)] = list_list[x][y]
    return my_dict

  def PlayNumber(self, num):
    """Given a number, play it on this board."""
    for coord in self.bing_dict:
      if self.bing_dict[coord] == num:
        self.played_marks.add(coord)

  def HasBingo(self):
    """Return true if this board has a bingo."""
    for bingo_set in BINGOS:
      if bingo_set.issubset(self.played_marks):
        self.bingo_set = bingo_set
        return True
    return False

  def PrintBoard(self):
    """Print this board."""
    for y in range(5):
      for x in range(5):
        marked = '.' if (y, x) in self.played_marks else ' '
        print(f'{marked}{self.bing_dict[(y, x)]:<2} ', end=' ')
      print()
    print()

  def Score(self):
    """Sum of the non-marked coordinates on this board."""
    score = 0
    for coord in self.bing_dict:
      if coord not in self.played_marks:
        score += self.bing_dict[coord]
    return score


def PlayDrawPt1(bingo_boards, num):
  """For part 2, play this number on all the boards. Quit if winner found."""
  for b in bingo_boards:
    b.PlayNumber(num)
    if b.HasBingo():
      return b
  return None


def PlayDrawPt2(bingo_boards, num):
  """Plays a number, removes winning boards, returns those boards."""
  winners = []
  for b in bingo_boards:
    b.PlayNumber(num)
    if b.HasBingo():
      winners.append(b)
  for w in winners:
    bingo_boards.remove(w)
  return winners


def PrintAnswer(winning_board, last_number):
  """Print answer for part 1 or part 2."""
  winning_board.PrintBoard()
  board_score = winning_board.Score()
  print(f'board score: {board_score}')
  print(f'last number called: {last_number}')
  print(f'{board_score} x {last_number} -> {board_score * last_number}')


def GetBingoBoards(board_lines):
  """Parse input boards. Requires blank line on the last line."""
  num_boards = len(board_lines) // 6
  assert not len(board_lines) % 6
  boards = []
  for i in range(num_boards):
    boards.append(board_lines[i*6:i*6+5])

  bingo_boards = []
  for b in boards:
    new_board = BingoBoard(b)
    bingo_boards.append(new_board)
    # new_board.PrintBoard()
  return bingo_boards


def Part1():
  """Run Part 1 to completion."""
  lines = GetData(DATA)
  draws = [int(i) for i in lines[0].split(',')]
  bingo_boards = GetBingoBoards(lines[2:])

  for i in draws:
    print(f'playing {i}')
    result = PlayDrawPt1(bingo_boards, i)
    if result:
      print(f'winning board:')
      PrintAnswer(result, i)
      break


def Part2():
  """Run Part 2 to completion."""
  lines = GetData(DATA)
  draws = iter([int(i) for i in lines[0].split(',')])
  bingo_boards = GetBingoBoards(lines[2:])
  num_boards = len(bingo_boards)
  print(f'There are {num_boards} boards.')
  winning_boards = []

  while len(winning_boards) < num_boards:
    i = next(draws)
    print(f'playing draw: {i}')
    winning_boards.extend(PlayDrawPt2(bingo_boards, i))
    print(f'boards left: {num_boards - len(winning_boards)}')

  last_winner = winning_boards[-1]
  last_draw = i
  PrintAnswer(last_winner, last_draw)


Part2()
