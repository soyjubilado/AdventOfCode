#!/usr/bin/python3
"""Unit tests for prog202123.py"""

import unittest
from textwrap import dedent
from prog202123 import LinesToState, AlreadyHome, ForeignersOccupyHome
from prog202123 import BlockedInTrench, GetOccupiedDict
from prog202123 import NumbersBetween, BlockedOutside


class UnitTestFailure(Exception):
  """Failing unit test."""


class TestProg202123(unittest.TestCase):
  """Unit tests class."""

  def testLinesToState(self):
    """Test LinesToState"""
    state1 = '''\
             #############
             #...........#
             ###A#D#A#B###
               #C#C#D#B#
               #########'''
    lines = dedent(state1).split('\n')
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

  def testAlreadyHome(self):
    """Test AlreadyHome"""
    state2 = '''\
             #############
             #.D.......A.#
             ###C#.#C#D###
               #A#B#B#D#
               #########'''

    lines = dedent(state2).split('\n')
    state = LinesToState(lines)
    self.assertEqual(AlreadyHome(((1, 0), 'D'), state), False)
    self.assertEqual(AlreadyHome(((2, 1), 'C'), state), False)
    self.assertEqual(AlreadyHome(((2, 2), 'A'), state), True)
    self.assertEqual(AlreadyHome(((4, 2), 'B'), state), True)
    self.assertEqual(AlreadyHome(((6, 2), 'B'), state), False)
    self.assertEqual(AlreadyHome(((6, 1), 'C'), state), False)
    self.assertEqual(AlreadyHome(((8, 2), 'D'), state), True)
    self.assertEqual(AlreadyHome(((9, 0), 'A'), state), False)
    self.assertEqual(AlreadyHome(((8, 1), 'D'), state), True)

  def testForeignersOccupyHome(self):
    """Test ForeignersOccupyHome"""
    state2 = '''\
             #############
             #.D.......A.#
             ###C#.#C#D###
               #A#B#B#D#
               #########'''
    lines = dedent(state2).split('\n')
    state = LinesToState(lines)
    self.assertEqual(ForeignersOccupyHome(((1, 0), 'D'), state), False)
    self.assertEqual(ForeignersOccupyHome(((2, 1), 'C'), state), True)
    self.assertEqual(ForeignersOccupyHome(((2, 2), 'A'), state), True)
    self.assertEqual(ForeignersOccupyHome(((4, 2), 'B'), state), False)
    self.assertEqual(ForeignersOccupyHome(((6, 2), 'B'), state), False)
    self.assertEqual(ForeignersOccupyHome(((6, 1), 'C'), state), True)
    self.assertEqual(ForeignersOccupyHome(((8, 2), 'D'), state), False)
    self.assertEqual(ForeignersOccupyHome(((9, 0), 'A'), state), True)
    self.assertEqual(ForeignersOccupyHome(((8, 1), 'D'), state), False)

  def testBlockedInTrench(self):
    """Test BlockedInTrench"""
    state2 = '''\
             #############
             #.D.......A.#
             ###C#.#C#D###
               #A#B#B#D#
               #########'''
    lines = dedent(state2).split('\n')
    state = LinesToState(lines)
    self.assertEqual(BlockedInTrench(((1, 0), 'D'), state), False)
    self.assertEqual(BlockedInTrench(((2, 1), 'C'), state), False)
    self.assertEqual(BlockedInTrench(((2, 2), 'A'), state), True)
    self.assertEqual(BlockedInTrench(((4, 2), 'B'), state), False)
    self.assertEqual(BlockedInTrench(((6, 2), 'B'), state), True)
    self.assertEqual(BlockedInTrench(((6, 1), 'C'), state), False)
    self.assertEqual(BlockedInTrench(((8, 2), 'D'), state), True)
    self.assertEqual(BlockedInTrench(((9, 0), 'A'), state), False)
    self.assertEqual(BlockedInTrench(((8, 1), 'D'), state), False)

  def testGetOccupiedDict(self):
    """Test GetOccupiedDict"""
    state2 = '''\
             #############
             #.D.......A.#
             ###C#.#C#D###
               #A#B#B#D#
               #########'''
    lines = dedent(state2).split('\n')
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

  def testNumbersBetween(self):
    """Test NumbersBetween"""
    self.assertEqual(NumbersBetween(0, 0), [])
    self.assertEqual(NumbersBetween(0, 2), [1])
    self.assertEqual(NumbersBetween(2, 0), [1])
    self.assertEqual(NumbersBetween(2, 1), [])
    self.assertEqual(NumbersBetween(1, 2), [])
    self.assertEqual(NumbersBetween(1, 4), [2, 3])
    self.assertEqual(NumbersBetween(4, 1), [2, 3])

  def testBlockedOutside(self):
    """Test BlockedOutside"""
    state3 = '''\
             #############
             #.D.C.....A.#
             ###.#.#C#D###
               #A#B#B#D#
               #########'''
    lines = dedent(state3).split('\n')
    state = LinesToState(lines)
    self.assertEqual(BlockedOutside(((1, 0), 'D'), state), True)
    self.assertEqual(BlockedOutside(((3, 0), 'C'), state), False)
    self.assertEqual(BlockedOutside(((2, 2), 'A'), state), False)
    self.assertEqual(BlockedOutside(((4, 2), 'B'), state), False)
    self.assertEqual(BlockedOutside(((6, 2), 'B'), state), False)
    self.assertEqual(BlockedOutside(((6, 1), 'C'), state), False)
    self.assertEqual(BlockedOutside(((8, 2), 'D'), state), False)
    self.assertEqual(BlockedOutside(((9, 0), 'A'), state), True)
    self.assertEqual(BlockedOutside(((8, 1), 'D'), state), False)


if __name__ == '__main__':
  unittest.main()
