#!/usr/bin/python3
"""https://adventofcode.com/2021/day/07"""

DATA = 'data202107.txt'
DATA = 'testdata202107.txt'


def GetData(datafile):
  """Parse input."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def FuelCost(n):
  """Triangle numbers for part 2"""
  return n*(n+1)//2


def Part1():
  fuel = [int(i) for i in GetData(DATA)[0].split(',')]
  min_num = 0
  min_val = float('infinity')
  for i in range(max(fuel)):
    val_sum = sum([abs(i-j) for j in fuel])
    if val_sum < min_val:
      min_val = val_sum
      min_num = i
  print(f'Part 1: align on {min_num} for total fuel of {min_val}')


def Part2():
  fuel = [int(i) for i in GetData(DATA)[0].split(',')]
  min_num = 0
  min_val = float('infinity')
  for i in range(max(fuel)):
    val_sum = sum([FuelCost(abs(i-j)) for j in fuel])
    if val_sum < min_val:
      min_val = val_sum
      min_num = i
  print(f'Part 2: align on {min_num} for total fuel of {min_val}')


Part1()
Part2()
