#!/usr/bin/python3
#file created 2021-Dec-07 20:39
"""https://adventofcode.com/2021/day/8"""

from collections import defaultdict
DATA = 'data202108.txt'
# DATA = 'testdata202108.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def SplitLineIntoSets(line):
  ten_digits, nums = line.split(' | ')
  rosetta = []
  puzzle_nums = []
  for word in ten_digits.split():
    rosetta.append(frozenset(word))
  for word in nums.split():
    puzzle_nums.append(frozenset(word))
  return rosetta, puzzle_nums


def Solver(rosetta):
  """Given a set of ten circuits, determine which is which"""
  keys = {}
  keys[1] = [i for i in rosetta if len(i) == 2][0]
  keys[4] = [i for i in rosetta if len(i) == 4][0]
  keys[7] = [i for i in rosetta if len(i) == 3][0]
  keys[8] = [i for i in rosetta if len(i) == 7][0]
  keys[6] = [i for i in rosetta if len(i) == 6 and not keys[7].issubset(i) 
                                               and not keys[4].issubset(i)][0]
  keys[0] = [i for i in rosetta if len(i) == 6 and not keys[4].issubset(i)
                                               and keys[7].issubset(i)][0]
  keys[9] = [i for i in rosetta if len(i) == 6 and keys[4].issubset(i)
                                               and keys[7].issubset(i)][0]
  keys[3] = [i for i in rosetta if len(i) == 5 and keys[1].issubset(i)][0]
  keys[5] = [i for i in rosetta if len(i) == 5 and i.issubset(keys[6])][0]
  keys[2] = [i for i in rosetta if len(i) == 5 and not i.issubset(keys[6])
                                               and not keys[1].issubset(i)][0]
  anti_keys = {keys[i]: str(i) for i in keys}
  return anti_keys


def Part2(lines):
  total = 0
  for line in lines:
    print(line.split(" | ")[1], end=": ")
    rosetta, puzzle_nums = SplitLineIntoSets(line)
    solve_dict = Solver(rosetta)
    num_as_str = f'{"".join(solve_dict[n] for n in puzzle_nums)}'
    print(num_as_str)
    total += int(num_as_str)
  print(f'\nTotal for part 2: {total}')


def Part1(lines):
  size_map = defaultdict(lambda: 0)
  for line in lines:
    words = line.split(' | ')[1].split()
    for word in words:
      size_map[len(word)] += 1
  for n in [2, 3, 4, 7]:
    print(f'{n}: {size_map[n]}')
  answer = 0
  for i in [2, 3, 4, 7]:
    answer += size_map[i]
  print(answer)  


def main():
  lines = GetData(DATA)
  Part2(lines)


if __name__ == '__main__':
  main()
