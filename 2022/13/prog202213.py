#!/usr/bin/python3
#file created 2022-Dec-12 20:59
"""https://adventofcode.com/2022/day/13"""

import json
from functools import cmp_to_key

DATA = 'data202213.txt'
DATA = 'testdata202213.txt'

L_LESS_THAN_R = -1
L_GREATER_THAN_R = 1
L_EQUALS_R = 0


def Nop(*args, **kwargs):
  """A null function."""


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetPairs(lines):
  """Given the input, separate the lines into pairs of packets."""
  pairs = []
  num_pairs = (len(lines) + 1) // 3

  for i in range(num_pairs):
    idx = (i * 3)
    pairs.append((json.loads(lines[idx]), json.loads(lines[idx+1])))
  return pairs


def RightOrder(left, right, depth=0, print=Nop):
  """Recursively decide if the left is smaller than the right."""
  assert isinstance(left, list)
  assert isinstance(right, list)
  spaces = '  ' * depth
  print(f'{spaces}- Compare {left} vs {right}')
  depth += 1
  spaces = '  ' * depth
  for l, r in zip(left, right):
    l_to_send = l
    r_to_send = r
    if isinstance(l, int) and isinstance(r, int):
      print(f'{spaces}- Compare {l} vs {r}')
      if l < r:
        return L_LESS_THAN_R
      if l > r:
        return L_GREATER_THAN_R

    # One or both are lists; turn the int into a list too.
    else:
      if isinstance(l, int):
        l_to_send = [l]
        r_to_send = r
      elif isinstance(r, int):
        l_to_send = l
        r_to_send = [r]

      print(f'{spaces}- Compare {l} vs {r}')
      right_order_output = RightOrder(l_to_send, r_to_send, depth)
      if right_order_output in (L_LESS_THAN_R, L_GREATER_THAN_R):
        return right_order_output

  # if you got here, you ran through the whole zip.
  if len(left) < len(right):
    print(f'{spaces}- Left side exhausted')
    return L_LESS_THAN_R
  if len(left) > len(right):
    print(f'{spaces}- Right side is exhausted')
    return L_GREATER_THAN_R
  print(f'{spaces}- Both sides the same')
  return L_EQUALS_R


def Part1(lines):
  """Solve Part 1."""
  pairs = GetPairs(lines)
  running_sum = 0
  for idx, pair in enumerate(pairs):
    left, right = pair
    right_order_output = RightOrder(left, right)
    if right_order_output in (L_LESS_THAN_R, L_EQUALS_R):
      running_sum += idx + 1

  print(f'Part 1: {running_sum}')


def Part2(lines):
  """Solve Part 2."""
  all_packets = [[[2]], [[6]]]
  for line in lines:
    if line:
      all_packets.append(json.loads(line))
  all_packets.sort(key=cmp_to_key(RightOrder))

  decoder_key = 1
  for idx, packet in enumerate(all_packets):
    if packet in [[[2]], [[6]]]:
      decoder_key *= idx + 1
  print(f'Part 2: {decoder_key}')


def main():
  """main"""
  lines = GetData(DATA)
  Part1(lines)
  Part2(lines)


if __name__ == '__main__':
  main()
