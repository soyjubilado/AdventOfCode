#!/usr/bin/python3
# file created 2023-Jan-20 14:46
"""https://adventofcode.com/2016/day/5"""

import hashlib

DATA = 'data201605.txt'
# DATA = 'testdata201605.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines[0]


def ZeroLeadingHash(door_id):
  """Yield the next hash that starts with five zeros."""
  count = 1
  while True:
    door_index = door_id + str(count)
    md5sum = Md5Hash(door_index)
    if md5sum.startswith('00000'):
      print(f'{door_index} -> {md5sum}')
      yield md5sum
    count += 1


def Md5Hash(my_string):
  """Given a string, return the md5 hexadecimal hash."""
  hasher = hashlib.md5()
  hasher.update(bytes(my_string, 'utf-8'))
  return hasher.hexdigest()


def Part1(door_id):
  """Part 1"""
  pw = ''
  nextchar = ZeroLeadingHash(door_id)
  while len(pw) < 8:
    c = next(nextchar)[5]
    pw += c
  print(f'Part 1: {pw}')


def Part2(door_id):
  """Part 2"""
  pw = {}
  nextchar = ZeroLeadingHash(door_id)
  while len(pw) < 8:
    this_hash = next(nextchar)
    try:
      idx = int(this_hash[5])
    except ValueError:
      continue
    char = this_hash[6]
    if 0 <= idx < 8 and idx not in pw:
      pw[idx] = char
  print('Part 2: ', end='')
  print(''.join([pw[i] for i in range(8)]))


def main():
  """main"""
  door_id = GetData(DATA)
  Part1(door_id)
  Part2(door_id)


if __name__ == '__main__':
  main()
