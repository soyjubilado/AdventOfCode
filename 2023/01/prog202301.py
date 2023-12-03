#!/usr/bin/python3
# file created 2023-Nov-30 19:21
"""https://adventofcode.com/2023/day/1"""

DATA = 'data202301.txt'
# DATA = 'testdata202301.txt'

NUMBERS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
           'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,}

def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def RightmostWordIdx(line):
  """Return rightmost word and index"""
  highest_word = None
  highest_idx = -1
  for n in NUMBERS:
    idx = line.rfind(n)
    if idx > highest_idx:
      highest_idx = idx
      highest_word = n

  return highest_word, highest_idx


def LeftmostWordIdx(line):
  """Return the leftmost word and index."""
  lowest_idx = len(line)
  lowest_word = None
  for n in NUMBERS:
    idx = line.find(n)
    if 0 <= idx < lowest_idx:
      lowest_idx = idx
      lowest_word = n

  return lowest_word, lowest_idx


def FirstDigitIdx(line):
  """Return first digit and index of it."""
  for i in range(len(line)):
    if line[i].isdigit():
      return int(line[i]), i
  return None, None


def LastDigitIdx(line):
  """Return last digit and index of it."""
  for i in range(len(line)-1, -1, -1):
    if line[i].isdigit():
      return int(line[i]), i
  return None, None


def Part1(lines):
  """Part 1."""
  total = 0
  for line in lines:
    first_digit, _ = FirstDigitIdx(line)
    last_digit, _ = LastDigitIdx(line)
    total += 10 * first_digit + last_digit
  return total


def Calibration(line):
  """Return calibration number and tuple derived from this line, part 2."""
  funcs = [RightmostWordIdx, LeftmostWordIdx, FirstDigitIdx, LastDigitIdx,]
  num_list = []
  for f in funcs:
    num, idx = f(line)
    if idx is not None and num is not None:
      if isinstance(num, str):
        num = NUMBERS[num]
      num_list.append((idx, num))

  nums = sorted(num_list, key=lambda x: x[0])

  addend = 10 * nums[0][1] + nums[-1][1]
  return addend, nums


def Part2(lines):
  """Part 2."""
  total = 0
  for line in lines:
    addend, _ = Calibration(line)
    total += addend

  return total


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
