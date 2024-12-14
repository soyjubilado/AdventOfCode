#!/usr/bin/env python3
"""Tests for prog202412"""

from prog202412 import Grid, Neighbors, Coord, SplitGroup


def TestResult(testcase, actual, expected):
  """Build string for test result."""
  passing = 'PASS' if actual == expected else 'FAIL'
  addendum = f'(expected {expected})' if passing == 'FAIL' else ''
  return f'{passing}: {testcase} -> {actual} {addendum}'


def testNeighbors():
  """Test that the optional grid argument works."""
  print('Testing Neighbors()\n')
  lines = ['xxx',
           'xxx',
           'xxx']
  grid = Grid(lines)
  testcase = Coord(0, 0)
  actual = f'{Neighbors(testcase)}'
  expected = '[XY(x=-1, y=0), XY(x=1, y=0), XY(x=0, y=1), XY(x=0, y=-1)]'
  print(TestResult(testcase, actual, expected))

  actual = f'{Neighbors(testcase, grid)}'
  expected = '[XY(x=1, y=0), XY(x=0, y=1)]'
  print(TestResult(testcase, actual, expected))

def testSplitGroup():
  """Test SplitGroup()"""
  print('\nTesting SplitGroup()\n')

  testcase = [Coord(0, 1), Coord(0, 2), Coord(0, 4), Coord(0, 6), Coord(0, 7)]
  actual = f'{SplitGroup(testcase, "left")}'
  expected = ('[[XY(x=0, y=1), XY(x=0, y=2)], '
              '[XY(x=0, y=4)], [XY(x=0, y=6), XY(x=0, y=7)]]')
  print(TestResult(testcase, actual, expected))

  actual = f'{SplitGroup(testcase, "right")}'
  expected = ('[[XY(x=0, y=1), XY(x=0, y=2)], '
              '[XY(x=0, y=4)], [XY(x=0, y=6), XY(x=0, y=7)]]')
  print(TestResult(testcase, actual, expected))

  actual = f'{SplitGroup(testcase, "upper")}'
  expected = ('[[XY(x=0, y=1)], [XY(x=0, y=2)], '
              '[XY(x=0, y=4)], [XY(x=0, y=6)], [XY(x=0, y=7)]]')
  print(TestResult(testcase, actual, expected))

  actual = f'{SplitGroup(testcase, "lower")}'
  expected = ('[[XY(x=0, y=1)], [XY(x=0, y=2)], '
              '[XY(x=0, y=4)], [XY(x=0, y=6)], [XY(x=0, y=7)]]')
  print(TestResult(testcase, actual, expected))
  print()

  testcase = [Coord(1, 0), Coord(2, 0), Coord(4, 0), Coord(6, 0), Coord(7, 0)]
  actual = f'{SplitGroup(testcase, "left")}'
  expected = ('[[XY(x=1, y=0)], [XY(x=2, y=0)], '
              '[XY(x=4, y=0)], [XY(x=6, y=0)], [XY(x=7, y=0)]]')
  print(TestResult(testcase, actual, expected))

  actual = f'{SplitGroup(testcase, "right")}'
  expected = ('[[XY(x=1, y=0)], [XY(x=2, y=0)], '
              '[XY(x=4, y=0)], [XY(x=6, y=0)], [XY(x=7, y=0)]]')
  print(TestResult(testcase, actual, expected))

  actual = f'{SplitGroup(testcase, "upper")}'
  expected = ('[[XY(x=1, y=0), XY(x=2, y=0)], '
              '[XY(x=4, y=0)], [XY(x=6, y=0), XY(x=7, y=0)]]')
  print(TestResult(testcase, actual, expected))

  actual = f'{SplitGroup(testcase, "lower")}'
  expected = ('[[XY(x=1, y=0), XY(x=2, y=0)], '
              '[XY(x=4, y=0)], [XY(x=6, y=0), XY(x=7, y=0)]]')
  print(TestResult(testcase, actual, expected))

testNeighbors()
testSplitGroup()
