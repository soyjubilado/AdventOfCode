#!/usr/bin/python3
# https://adventofcode.com/2021/day/02

DATA = 'data02.txt'
# DATA = 'testdata02.txt'

def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines

def Pt1():
  lines = GetData(DATA)
  x = y = 0
  for line in lines:
    direction, amt = line.split()
    print(f'{direction}, {amt}')
    if direction == 'down':
      y += int(amt)
    elif direction == 'up':
      y -= int(amt)
    elif direction == 'forward':
      x += int(amt)
  print(x * y)

def Pt2():
  lines = GetData(DATA)
  x = y = 0
  aim = 0
  for line in lines:
    direction, amt = line.split()
    print(f'{direction}, {amt}')
    if direction == 'down':
      # y += int(amt)
      aim += int(amt)
    elif direction == 'up':
      # y -= int(amt)
      aim -= int(amt)
    elif direction == 'forward':
      x += int(amt)
      y += int(amt) * aim
    print(f'x: {x}, y: {y}, aim: {aim}')
  print(x * y)


Pt1()
