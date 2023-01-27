#!/usr/bin/python3
# file created 2023-Jan-26 15:52
"""https://adventofcode.com/2016/day/6"""

from collections import defaultdict
DATA = 'data201606.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Decode(lines, part):
  """Decode part 1 or part 2"""
  assert part in ['Part 1', 'Part 2']
  sortkey = -1 if part == 'Part 1' else 0

  width = len(lines[0])
  dicts_list = [defaultdict(lambda: 0) for _ in range(width)]
  for line in lines:
    for idx, c in enumerate(line):
      dicts_list[idx][c] += 1

  answer = ''
  for i in range(width):
    answer += sorted(dicts_list[i].items(),
                     key=lambda x: x[1])[sortkey][0]
  return answer


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Decode(lines, "Part 1")}')
  print(f'Part 2: {Decode(lines, "Part 2")}')


if __name__ == '__main__':
  main()
