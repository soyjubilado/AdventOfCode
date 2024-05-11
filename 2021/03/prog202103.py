#!/usr/bin/python3
# https://adventofcode.com/2021/day/03

import math
DATA = 'data03.txt'
# DATA = 'testdata03.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def MostCommonBit(lines, position):
  threshold = math.ceil(len(lines)/2)
  ones = sum([int(i[position]) for i in lines])
  return '1' if ones >= threshold else '0'


def LeastCommonBit(lines, position):
  return '0' if MostCommonBit(lines, position) == '1' else '1'


def testMostCommonBit():
  tests = [[['111', '101', '001'], 0, 1],
           [['111', '101', '001'], 1, 0],
           [['111', '101', '001'], 2, 1],
           [['111', '101', '001', '010'], 0, 1],
           [['111', '101', '001', '010'], 1, 1],
           [['110', '100', '001', '010'], 2, 0],
          ]
  for case in tests:
    lines, position, expected = case
    actual = MostCommonBit(lines, position)
    passing = 'pass' if actual == expected else 'fail'
    print(f'{passing}: {lines} -> {actual} (expected {expected})')


def GetGasRate(lines_of_binary, MostLeastCommonBit):
  """
  Args:
    lines_of_binary (list): a list of binary strings
    MostLeastCommonBit (function): MostCommonBit or LeastCommonBit
  """
  lines = lines_of_binary[:]
  position = 0
  while len(lines) > 1:
    common_bit = MostLeastCommonBit(lines, position)
    new_lines = [i for i in lines if i[position] == common_bit]
    lines = new_lines
    position += 1
  return lines[0]


def Pt2():
  lines = GetData(DATA)

  o2rate = GetGasRate(lines, MostCommonBit)
  o2decimal = int(o2rate, 2)
  print(f'\noxygen: {o2rate} -> {o2decimal}')

  carbon = GetGasRate(lines, LeastCommonBit)
  carbondecimal = int(carbon, 2)
  print(f'carbon: {carbon} -> {carbondecimal}')

  print(f'Part 2: {o2decimal} x {carbondecimal} = {o2decimal * carbondecimal}')


def Pt1():
  lines = GetData(DATA)
  width = len(lines[0])
  gamma = ''.join([MostCommonBit(lines, i) for i in range(width)])
  epsilon = ''.join([LeastCommonBit(lines, i) for i in range(width)])
  print(f'\ngamma: {gamma}, epsilon: {epsilon}')
  print(f'Part 1: {int(gamma, 2) * int(epsilon, 2)}')


Pt1()
Pt2()
