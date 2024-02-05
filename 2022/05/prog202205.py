#!/usr/bin/python3
#file created 2022-Dec-04 20:59
"""https://adventofcode.com/2022/day/5"""

from collections import defaultdict

DATA = 'data202205.txt'
COLUMNS = 9


def GetData(datafile):
  """Get data file as a list. Do not strip newlines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = list(fh)
  return lines


def LastRow(lines):
  """Index of first row that starts with ' 1', which indicates the bottom
     of the stacks."""
  for idx, line in enumerate(lines):
    if line.startswith(' 1'):
      break
  return idx


def ParseStarting(lines):
  """Parse the starting state from the first lines of input.
  Return both the columns dictionary and the list of moves.
  """
  # For top lines until you hit a line starting with space,
  # extract chars at index 1, 5, 9, ... etc and put in a dictionary
  # keyed on column.
  column_dict = defaultdict(lambda: [])
  last_row = LastRow(lines)
  for line in lines[:last_row]:
    for col in range(1, COLUMNS+1):
      idx = 4*col - 3
      letter = line[idx]
      if letter != ' ':
        column_dict[col].append(letter)
  for c in column_dict:
    column_dict[c] = list(reversed(column_dict[c]))

  return column_dict, [x.strip() for x in lines[last_row + 2:]]


def Solve(lines, part):
  """Solve either part 1 or part 2 by popping the items from source
     column, putting on a pallet, and appending to destination. The
     only difference with part 2 is to reverse the pallet."""
  assert part in ['Part 1', 'Part 2']
  cols, move_lines = ParseStarting(lines)
  for l in move_lines:
    tokens = l.split()
    move = int(tokens[1])
    from_col = int(tokens[3])
    to_col = int(tokens[5])

    pallet = []
    for _ in range(move):
      pallet.append(cols[from_col].pop())
    if part == 'Part 2':
      pallet.reverse()
    cols[to_col].extend(pallet)

  answer = ''
  for c in sorted(cols.keys()):
    answer += cols[c][-1]
  print(f'{part}: {answer}')


def main():
  lines = GetData(DATA)
  Solve(lines, 'Part 1')
  Solve(lines, 'Part 2')


if __name__ == '__main__':
  main()
