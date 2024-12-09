#!/usr/bin/python3
# file created 2024-Dec-09 07:55
"""https://adventofcode.com/2024/day/09"""

from collections import deque

DATA = 'data202409.txt'
# DATA = 'testdata202409.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def PositionAndPopdirection(line):
  """For Part 1, given the original line, figure out for each index whether
     that block will come from the left of the deque or the right."""
  num = iter(line)
  pos = 0
  direction = 'LEFT'
  while True:
    try:
      for _ in range(int(next(num))):
        yield pos, direction
        pos += 1
      direction = 'RIGHT' if direction == 'LEFT' else 'LEFT'
        
    except StopIteration:
      pass


def BuildDeque(line):
  """Deque built from every other item in the line starting at idx 0.
     Create a list of the number of IDs in that block, then extend
     the deque with that list."""
  disk_deque = deque([])
  for i in range(len(line)//2 + 1):
    idx = i
    num = int(line[idx * 2])
    sub_list = [idx for _ in range(num)]
    disk_deque.extend(sub_list)
  return disk_deque


def Part1(original_line):
  """Part 1."""
  big_deque = BuildDeque(original_line)
  pos_and_dir = PositionAndPopdirection(original_line)
  checksum = 0
  while big_deque:
    idx, direction = next(pos_and_dir)
    value = big_deque.pop() if direction == 'RIGHT' else big_deque.popleft()
    checksum += idx * value
  return checksum


def Part2(lines):
  """Part 2."""
  return None


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines[0])}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
