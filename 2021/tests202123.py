#!/usr/bin/python3
# $Id: tests202123.py,v 1.5 2022/11/17 16:41:53 hjew Exp hjew $

from textwrap import dedent
from prog202123 import *

class FailedUnitTestError(Exception):
  pass

STATE1 = '''\
         #############
         #...........#
         ###A#D#A#B###
           #C#C#D#B#
           #########'''


def testLinesToState():
  print(f'\ntesting testLinesToState')
  lines = [l for l in dedent(STATE1).split('\n')]
  PrintLines(lines, depth=3)
  expected = set([((2, 1), 'A'),
                  ((2, 2), 'C'),
                  ((4, 1), 'D'),
                  ((4, 2), 'C'),
                  ((6, 1), 'A'),
                  ((6, 2), 'D'),
                  ((8, 1), 'B'),
                  ((8, 2), 'B'),
                 ])

  actual_state = LinesToState(lines)
  result = 'matches' if actual_state == expected else 'does not match'
  print(f'actual state {result} expected')
  print("\n".join([f'{s}' for s in sorted(actual_state)]))
  if actual_state != expected:
    raise FailedUnitTestError


STATE2 = '''\
         #############
         #.D.......A.#
         ###C#.#C#D###
           #A#B#B#D#
           #########'''

def testAlreadyHome():
  print(f'\ntesting testIsAlreadyHome')
  lines = [l for l in dedent(STATE2).split('\n')]
  PrintLines(lines, depth=3)
  state = LinesToState(lines)
  testcases = [ [((1, 0), 'D'), False],
                [((2, 1), 'C'), False],
                [((2, 2), 'A'), True],
                [((4, 2), 'B'), True],
                [((6, 2), 'B'), False],
                [((6, 1), 'C'), False],
                [((8, 2), 'D'), True],
                [((9, 0), 'A'), False],
                [((8, 1), 'D'), True],
              ]
  for case, expected in testcases:
    actual = AlreadyHome(case, state)
    passing = 'pass' if actual == expected else 'FAIL'
    print(f'{passing}: {case} got {actual} expected {expected}')

"""
STATE2 = '''\
         #############
         #.D.......A.#
         ###C#.#C#D###
           #A#B#B#D#
           #########'''
"""

def testForeignersOccupyHome():
  print(f'\ntesting ForeignersOccupyHome')
  lines = [l for l in dedent(STATE2).split('\n')]
  PrintLines(lines, depth=3)
  state = LinesToState(lines)
  testcases = [ [((1, 0), 'D'), False],
                [((2, 1), 'C'), True],
                [((2, 2), 'A'), True],
                [((4, 2), 'B'), False],
                [((6, 2), 'B'), False],
                [((6, 1), 'C'), True],
                [((8, 2), 'D'), False],
                [((9, 0), 'A'), True],
                [((8, 1), 'D'), False],
              ]
  for case, expected in testcases:
    actual = ForeignersOccupyHome(case, state)
    passing = 'pass' if actual == expected else 'FAIL'
    print(f'{passing}: {case} got {actual} expected {expected}')

"""
STATE2 = '''\
         #############
         #.D.......A.#
         ###C#.#C#D###
           #A#B#B#D#
           #########'''
"""

def testBlockedInTrench():
  print(f'\ntesting BlockedInTrench')
  lines = [l for l in dedent(STATE2).split('\n')]
  PrintLines(lines, depth=3)
  state = LinesToState(lines)
  testcases = [ [((1, 0), 'D'), False],
                [((2, 1), 'C'), False],
                [((2, 2), 'A'), True],
                [((4, 2), 'B'), False],
                [((6, 2), 'B'), True],
                [((6, 1), 'C'), False],
                [((8, 2), 'D'), True],
                [((9, 0), 'A'), False],
                [((8, 1), 'D'), False],
              ]
  for case, expected in testcases:
    actual = BlockedInTrench(case, state)
    passing = 'pass' if actual == expected else 'FAIL'
    print(f'{passing}: {case} got {actual} expected {expected}')


def testGetOccupiedDict():
  print(f'\ntesting GetOccupiedDict')
  lines = [l for l in dedent(STATE2).split('\n')]
  PrintLines(lines, depth=3)
  state = LinesToState(lines)
  expected = {(1, 0): 'D',
              (2, 1): 'C',
              (2, 2): 'A',
              (4, 2): 'B',
              (6, 2): 'B',
              (6, 1): 'C',
              (8, 2): 'D',
              (8, 1): 'D',
              (9, 0): 'A',
             }
  actual = GetOccupiedDict(state)
  passing = 'pass' if actual == expected else 'FAIL'
  print(f'{passing}: {state} \ngot\n {actual}'
        f'\nexpected\n {expected}')
  
"""
testLinesToState()
testForeignersOccupyHome()
testBlockedInTrench()
testAlreadyHome()
"""
testGetOccupiedDict()
