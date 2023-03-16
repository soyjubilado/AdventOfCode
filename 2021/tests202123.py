#!/usr/bin/python3
"""Unit tests for prog202123.py"""

import unittest
from textwrap import dedent
from prog202123 import LinesToState, AlreadyHome, ForeignersOccupyHome
from prog202123 import BlockedInTrench, GetOccupiedDict


class UnitTestFailure(Exception):
  """Failing unit test."""


class TestProg202123(unittest.TestCase):
  """Unit tests class."""
  STATE1 = '''\
           #############
           #...........#
           ###A#D#A#B###
             #C#C#D#B#
             #########'''

  def testLinesToState(self):
    """Test LinesToState"""
    lines = dedent(self.STATE1).split('\n')
    expected = set([((2, 1), 'A'),
                    ((2, 2), 'C'),
                    ((4, 1), 'D'),
                    ((4, 2), 'C'),
                    ((6, 1), 'A'),
                    ((6, 2), 'D'),
                    ((8, 1), 'B'),
                    ((8, 2), 'B'),
                   ])

    self.assertTrue(LinesToState(lines) == expected)


  STATE2 = '''\
           #############
           #.D.......A.#
           ###C#.#C#D###
             #A#B#B#D#
             #########'''

  def testAlreadyHome(self):
    """Test AlreadyHome"""
    lines = dedent(self.STATE2).split('\n')
    state = LinesToState(lines)
    testcases = [[((1, 0), 'D'), False],
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
      self.assertEqual(actual, expected)

  """
  STATE2 = '''\
           #############
           #.D.......A.#
           ###C#.#C#D###
             #A#B#B#D#
             #########'''
  """

  def testForeignersOccupyHome(self):
    """Test ForeignersOccupyHome"""
    lines = dedent(self.STATE2).split('\n')
    state = LinesToState(lines)
    testcases = [[((1, 0), 'D'), False],
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
      self.assertEqual(actual, expected)

  """
  STATE2 = '''\
           #############
           #.D.......A.#
           ###C#.#C#D###
             #A#B#B#D#
             #########'''
  """

  def testBlockedInTrench(self):
    """Test BlockedInTrench"""
    lines = dedent(self.STATE2).split('\n')
    state = LinesToState(lines)
    testcases = [[((1, 0), 'D'), False],
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
      self.assertEqual(actual, expected)


  def testGetOccupiedDict(self):
    """Test GetOccupiedDict"""
    lines = dedent(self.STATE2).split('\n')
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
    self.assertEqual(actual, expected)


if __name__ == '__main__':
  unittest.main()
