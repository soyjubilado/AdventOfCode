#!/usr/bin/python3
# file created 2024-Feb-26 18:59
"""https://adventofcode.com/2023/day/15"""

from collections import namedtuple

Lens = namedtuple('Lens', ['label', 'focal'])
DATA = 'data202315.txt'
# DATA = 'testdata202315.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Hash(my_str):
  """The HASH algorithm."""
  current_val = 0
  for char in my_str:
    current_val += ord(char)
    current_val *= 17
    current_val %= 256
  return current_val


def Part_1(lines):
  """Part 1"""
  return sum(Hash(i) for i in lines[0].split(','))


def remove_from_box(boxes, op):
  """Remove lens from box according to op."""
  label = op.split('-')[0]
  box = Hash(label)
  index_of_lens = -1
  for idx, lens in enumerate(boxes[box]):
    if lens.label == label:
      index_of_lens = idx
      break
  if index_of_lens >= 0:
    del boxes[box][index_of_lens]


def add_to_box(boxes, op):
  """Add lens to box according to op."""
  op_parts = op.split('=')
  label = op_parts[0]
  box = Hash(label)
  focal = int(op_parts[1])
  index_of_lens = -1
  for idx, lens in enumerate(boxes[box]):
    if lens.label == label:
      index_of_lens = idx
      break
  if index_of_lens >= 0:
    boxes[box][index_of_lens] = Lens(label, focal)
  else:
    boxes[box].append(Lens(label, focal))


def focusing_power(boxes):
  """Calculate focusing power."""
  total = 0
  for b in boxes:
    for idx, lens in enumerate(boxes[b]):
      total += (b + 1) * (idx + 1) * lens.focal
  return total


def Part_2(lines):
  """Part 2"""
  ops = lines[0].split(',')
  boxes = {i: [] for i in range(256)}
  for op in ops:
    if op.endswith('-'):
      remove_from_box(boxes, op)
    elif '=' in op:
      add_to_box(boxes, op)
    else:
      raise Exception
  return focusing_power(boxes)


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part_1(lines)}')
  print(f'Part 2: {Part_2(lines)}')


if __name__ == '__main__':
  main()
