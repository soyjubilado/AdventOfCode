#!/usr/bin/python3
"""Unit tests for prog202123.py"""

import unittest
from textwrap import dedent
from prog202123 import LinesToState, AlreadyHome, ForeignersOccupyHome
from prog202123 import BlockedInTrench, GetOccupiedDict, NumbersBetween
from prog202123 import BlockedOutside, PodInTrench, NextStatesForPod
from prog202123 import GoHome, FreeColumns, AllNextStates
from prog202123 import StateToLines, PrintLines
# from prog202123 import Unimplemented


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
    state = '''\
            #############
            #.D.......A.#
            ###C#.#C#A###
              #A#B#B#D#
              #########'''
    lines = dedent(state).split('\n')
    state = LinesToState(lines)
    self.assertEqual(ForeignersOccupyHome(((1, 0), 'D'), state), True)
    self.assertEqual(ForeignersOccupyHome(((2, 1), 'C'), state), False)
    self.assertEqual(ForeignersOccupyHome(((2, 2), 'A'), state), False)
    self.assertEqual(ForeignersOccupyHome(((4, 2), 'B'), state), False)
    self.assertEqual(ForeignersOccupyHome(((6, 2), 'B'), state), False)
    self.assertEqual(ForeignersOccupyHome(((6, 1), 'C'), state), False)
    self.assertEqual(ForeignersOccupyHome(((8, 2), 'D'), state), False)
    self.assertEqual(ForeignersOccupyHome(((9, 0), 'A'), state), True)
    self.assertEqual(ForeignersOccupyHome(((8, 1), 'A'), state), False)

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

  def testPodInTrench(self):
    """Test PodInTrench"""
    self.assertEqual(PodInTrench(((1, 0), 'D')), False)
    self.assertEqual(PodInTrench(((3, 0), 'C')), False)
    self.assertEqual(PodInTrench(((2, 2), 'A')), True)
    self.assertEqual(PodInTrench(((4, 2), 'B')), True)
    self.assertEqual(PodInTrench(((6, 2), 'B')), True)
    self.assertEqual(PodInTrench(((6, 1), 'C')), True)
    self.assertEqual(PodInTrench(((8, 2), 'D')), True)
    self.assertEqual(PodInTrench(((9, 0), 'A')), False)
    self.assertEqual(PodInTrench(((8, 1), 'D')), True)

  def testNextStatesForPod(self):
    """Test NextStatesForPod"""
    state = '''\
            #############
            #.D.C.....A.#
            ###.#C#.#.###
              #A#B#B#D#
              #########'''
    lines = dedent(state).split('\n')
    state = LinesToState(lines)
    self.assertEqual(NextStatesForPod(((2, 2), 'A'), state), {})
    self.assertEqual(NextStatesForPod(((1, 0), 'D'), state), {})
    self.assertEqual(NextStatesForPod(((9, 0), 'A'), state), {})
    self.assertEqual(NextStatesForPod(((8, 2), 'D'), state), {})
    self.assertEqual(NextStatesForPod(((4, 2), 'B'), state), {})
    self.assertEqual(NextStatesForPod(((3, 0), 'C'), state), {})

    new_states = NextStatesForPod(((4, 1), 'C'), state)
    self.assertEqual(len(new_states), 2)
    state_1 = '''\
              #############
              #.D.C...C.A.#
              ###.#.#.#.###
                #A#B#B#D#
                #########'''
    state_2 = '''\
              #############
              #.D.C.C...A.#
              ###.#.#.#.###
                #A#B#B#D#
                #########'''
    state_next_1 = LinesToState(dedent(state_1).split('\n'))
    self.assertTrue(frozenset(state_next_1) in new_states)
    state_next_2 = LinesToState(dedent(state_2).split('\n'))
    self.assertTrue(frozenset(state_next_2) in new_states)

    new_states = NextStatesForPod(((6, 2), 'B'), state)
    self.assertEqual(len(new_states), 2)


  def testGoHome(self):
    """Test GoHome"""
    state = '''\
            #############
            #.D.C...B.A.#
            ###.#C#.#.###
              #A#B#.#D#
              #########'''
    lines = dedent(state).split('\n')
    state = LinesToState(lines)
    ret_dict = GoHome(((3, 0), 'C'), state, depth=3)
    self.assertEqual(len(ret_dict), 1)
    new_state = list(ret_dict.keys())[0]
    # print(new_state)
    self.assertTrue(((6, 2), 'C') in new_state)
    next_dict_for_pod = NextStatesForPod(((3, 0), 'C'), state)
    next_state_for_pod = list(next_dict_for_pod.keys())[0]
    self.assertEqual(new_state, next_state_for_pod)

  def testFreeColumns(self):
    """Test FreeColumns"""
    state = '''\
            #############
            #...........#
            ###A#B#C#D###
              #A#B#C#D#
              #########'''
    lines = dedent(state).split('\n')
    state = LinesToState(lines)
    pod = ((2, 1), 'A')
    free = FreeColumns(pod, state)
    self.assertEqual(free, {0, 1, 3, 5, 7, 9, 10, 11})

    state = '''\
            #############
            #.A.....C...#
            ###.#B#.#D###
              #A#B#C#D#
              #########'''
    lines = dedent(state).split('\n')
    state = LinesToState(lines)
    pod = ((4, 1), 'B')
    free = FreeColumns(pod, state)
    self.assertEqual(free, set({3, 5}))

    state = '''\
            #############
            #...A.C.....#
            ###.#B#.#D###
              #A#B#C#D#
              #########'''
    lines = dedent(state).split('\n')
    state = LinesToState(lines)
    pod = ((4, 1), 'B')
    free = FreeColumns(pod, state)
    self.assertEqual(free, set({}))

  def testLinesToState(self):
    """Test LinesToState and StateToLines"""
    state_lines = '''\
                  #############
                  #...A.C.....#
                  ###.#B#.#D###
                    #A#B#C#D#
                    #########'''
    lines1 = dedent(state_lines).split('\n')
    state1 = LinesToState(lines1)
    lines2 = StateToLines(state1)
    state2 = LinesToState(lines2)
    self.assertEqual(lines1, lines2)
    self.assertEqual(state1, state2)

  def testAllNextStates(self):
    """Test AllNextStates"""
    state_lines = '''\
                  #############
                  #.....B.....#
                  ###A#.#C#D###
                    #A#B#C#D#
                    #########'''
    lines = dedent(state_lines).split('\n')
    state = LinesToState(lines)
    # print('original:')
    # PrintLines(lines)
    # print('next states:')
    next_states = AllNextStates(state)
    self.assertEqual(len(next_states), 1)
    expected = {((2, 1), 'A'),
                ((2, 2), 'A'),
                ((4, 1), 'B'),
                ((4, 2), 'B'),
                ((6, 1), 'C'),
                ((6, 2), 'C'),
                ((8, 1), 'D'),
                ((8, 2), 'D'),
               }
    self.assertEqual(list(next_states.keys())[0], expected)


if __name__ == '__main__':
  unittest.main()
