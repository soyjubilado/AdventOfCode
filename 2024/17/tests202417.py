#!/usr/bin/env python3
"""simple tests for prog202417."""

from prog202417 import Computer, GetComputer


def testGetComputer():
  """test GetComputer"""
  testLines = ['Register A: 729',
               'Register B: 0',
               'Register C: 0',
               '',
               'Program: 0,1,5,4,3,0']

  c = GetComputer(testLines)
  print(c)


def testComputer():
  """test Computer class and operations"""

  c = Computer(10, 0, 9)
  c.instr = 0
  c.RunProg([2, 6])
  expected = c.b == 1
  passing = 'PASS' if expected else 'FAIL'
  print(c)
  print(f'{passing} [2, 6]')

  c.a = 10
  c.instr = 0
  c.RunProg([5, 0, 5, 1, 5, 4])
  expected = c.output = [0, 1, 2]
  passing = 'PASS' if expected else 'FAIL'
  print(c)
  print(f'{passing} [5, 0, 5, 1, 5, 4]')

  c.a = 2024
  c.instr = 0
  c.output = []
  c.RunProg([0, 1, 5, 4, 3, 0])
  expected = c.output == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0] and c.a == 0
  passing = 'PASS' if expected else 'FAIL'
  print(c)
  print(f'{passing} [0, 1, 5, 4, 3, 0]')

  c.b = 29
  c.instr = 0
  c.RunProg([1, 7])
  expected = c.b == 26
  passing = 'PASS' if expected else 'FAIL'
  print(c)
  print(f'{passing} [1, 7]')

  c.b = 2024
  c.c = 43690
  c.instr = 0
  c.RunProg([4, 0])
  expected = c.b == 44354
  passing = 'PASS' if expected else 'FAIL'
  print(c)
  print(f'{passing} [4, 0]')


if __name__ == '__main__':
  testGetComputer()
  testComputer()
