#!/usr/bin/python3
# https://adventofcode.com/2021/day/01

DATA = 'data01.txt'
# DATA = 'testdata01.txt'

def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [int(i.strip()) for i in fh]
  return lines


def Pt1():
  lines = GetData(DATA)
  counter = 0
  prev = lines[0]
  for i in lines[1:]:
    if i > prev:
      counter += 1
    prev = i
  print(counter)


def Pt2():
  lines = GetData(DATA)
  prev = sum(lines[0:3])
  counter = 0
  for i in range(1, len(lines)-2):
    current = sum(lines[i:i+3])
    if current > prev:
      counter += 1
    prev = current
  print(counter)
    

Pt1()
Pt2()
