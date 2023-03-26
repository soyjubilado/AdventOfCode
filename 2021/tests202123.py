#!/usr/bin/python3
"""Unit tests for prog202123.py"""

import unittest
from textwrap import dedent
from prog202123 import State, NumbersBetween, PodInTrench
# from prog202123 import LinesToState, AlreadyHome, ForeignersOccupyHome
# from prog202123 import BlockedInTrench, GetOccupiedDict, NumbersBetween
# from prog202123 import BlockedOutside, PodInTrench, NextStatesForPod
# from prog202123 import GoHome, FreeColumns, AllNextStates
# from prog202123 import StateToLines, PrintLines
# from prog202123 import Unimplemented


class UnitTestFailure(Exception):
  """Failing unit test."""


class TestProg202123(unittest.TestCase):
  """Unit tests class."""

  def testLinesToTupleSet(self):
    """Test LinesToState"""
    state1 = '''\
             #############
             #...........#
             ###A#D#A#B###
               #C#C#D#B#
               #########'''
    lines = dedent(state1).split('\n')
    s = State(lines=lines)
    expected = set([((2, 1), 'A'),
                    ((2, 2), 'C'),
                    ((4, 1), 'D'),
                    ((4, 2), 'C'),
                    ((6, 1), 'A'),
                    ((6, 2), 'D'),
                    ((8, 1), 'B'),
                    ((8, 2), 'B'),
                   ])

    self.assertTrue(s.state == expected)
    # test hashable
    _ = {s: 5}
    # test __eq__
    new_obj = State(lines=lines)
    self.assertTrue(s is not new_obj)
    self.assertTrue(s == new_obj)

  def testAlreadyHome(self):
    """Test AlreadyHome"""
    state2 = '''\
             #############
             #.D.......A.#
             ###C#.#C#D###
               #A#B#B#D#
               #########'''

    lines = dedent(state2).split('\n')
    s = State(lines=lines)
    # self.assertEqual(s.AlreadyHome(((1, 0), 'D'), state), False)
    self.assertEqual(s.AlreadyHome(((1, 0), 'D')), False)
    self.assertEqual(s.AlreadyHome(((2, 1), 'C')), False)
    self.assertEqual(s.AlreadyHome(((2, 2), 'A')), True)
    self.assertEqual(s.AlreadyHome(((4, 2), 'B')), True)
    self.assertEqual(s.AlreadyHome(((6, 2), 'B')), False)
    self.assertEqual(s.AlreadyHome(((6, 1), 'C')), False)
    self.assertEqual(s.AlreadyHome(((8, 2), 'D')), True)
    self.assertEqual(s.AlreadyHome(((9, 0), 'A')), False)
    self.assertEqual(s.AlreadyHome(((8, 1), 'D')), True)

  def testForeignersOccupyHome(self):
    """Test ForeignersOccupyHome"""
    state = '''\
            #############
            #.D.......A.#
            ###C#.#C#A###
              #A#B#B#D#
              #########'''
    lines = dedent(state).split('\n')
    s = State(lines=lines)
    self.assertEqual(s.ForeignersOccupyHome(((1, 0), 'D')), True)
    self.assertEqual(s.ForeignersOccupyHome(((2, 1), 'C')), False)
    self.assertEqual(s.ForeignersOccupyHome(((2, 2), 'A')), False)
    self.assertEqual(s.ForeignersOccupyHome(((4, 2), 'B')), False)
    self.assertEqual(s.ForeignersOccupyHome(((6, 2), 'B')), False)
    self.assertEqual(s.ForeignersOccupyHome(((6, 1), 'C')), False)
    self.assertEqual(s.ForeignersOccupyHome(((8, 2), 'D')), False)
    self.assertEqual(s.ForeignersOccupyHome(((9, 0), 'A')), True)
    self.assertEqual(s.ForeignersOccupyHome(((8, 1), 'A')), False)

  def testBlockedInTrench(self):
    """Test BlockedInTrench"""
    state2 = '''\
             #############
             #.D.......A.#
             ###C#.#C#D###
               #A#B#B#D#
               #########'''
    lines = dedent(state2).split('\n')
    s = State(lines=lines)
    self.assertEqual(s.BlockedInTrench(((1, 0), 'D')), False)
    self.assertEqual(s.BlockedInTrench(((2, 1), 'C')), False)
    self.assertEqual(s.BlockedInTrench(((2, 2), 'A')), True)
    self.assertEqual(s.BlockedInTrench(((4, 2), 'B')), False)
    self.assertEqual(s.BlockedInTrench(((6, 2), 'B')), True)
    self.assertEqual(s.BlockedInTrench(((6, 1), 'C')), False)
    self.assertEqual(s.BlockedInTrench(((8, 2), 'D')), True)
    self.assertEqual(s.BlockedInTrench(((9, 0), 'A')), False)
    self.assertEqual(s.BlockedInTrench(((8, 1), 'D')), False)

  def testGetOccupiedDict(self):
    """Test GetOccupiedDict"""
    state2 = '''\
             #############
             #.D.......A.#
             ###C#.#C#D###
               #A#B#B#D#
               #########'''
    lines = dedent(state2).split('\n')
    s = State(lines=lines)
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
    actual = s.occupied
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
    s = State(lines=lines)
    self.assertEqual(s.BlockedOutside(((1, 0), 'D')), True)
    self.assertEqual(s.BlockedOutside(((3, 0), 'C')), False)
    self.assertEqual(s.BlockedOutside(((2, 2), 'A')), False)
    self.assertEqual(s.BlockedOutside(((4, 2), 'B')), False)
    self.assertEqual(s.BlockedOutside(((6, 2), 'B')), False)
    self.assertEqual(s.BlockedOutside(((6, 1), 'C')), False)
    self.assertEqual(s.BlockedOutside(((8, 2), 'D')), False)
    self.assertEqual(s.BlockedOutside(((9, 0), 'A')), True)
    self.assertEqual(s.BlockedOutside(((8, 1), 'D')), False)

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
    s = State(lines=lines)
    self.assertEqual(s.NextStatesForPod(((2, 2), 'A')), {})
    self.assertEqual(s.NextStatesForPod(((1, 0), 'D')), {})
    self.assertEqual(s.NextStatesForPod(((9, 0), 'A')), {})
    self.assertEqual(s.NextStatesForPod(((8, 2), 'D')), {})
    self.assertEqual(s.NextStatesForPod(((4, 2), 'B')), {})
    self.assertEqual(s.NextStatesForPod(((3, 0), 'C')), {})

    new_states = s.NextStatesForPod(((4, 1), 'C'))
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
    state_next_1 = State(lines=dedent(state_1).split('\n'))
    self.assertTrue(state_next_1 in new_states)
    state_next_2 = State(lines=dedent(state_2).split('\n'))
    self.assertTrue(state_next_2 in new_states)

    new_states = s.NextStatesForPod(((6, 2), 'B'))
    self.assertEqual(len(new_states), 2)
    state_1 = '''\
              #############
              #.D.C...B.A.#
              ###.#C#.#.###
                #A#B#.#D#
                #########'''
    state_2 = '''\
              #############
              #.D.C.B...A.#
              ###.#C#.#.###
                #A#B#.#D#
                #########'''
    state_next_1 = State(lines=dedent(state_1).split('\n'))
    self.assertTrue(state_next_1 in new_states)
    state_next_2 = State(lines=dedent(state_2).split('\n'))
    self.assertTrue(state_next_2 in new_states)

  def testGoHome(self):
    """Test GoHome"""
    state = '''\
            #############
            #.D.C...B.A.#
            ###.#C#.#.###
              #A#B#.#D#
              #########'''
    lines = dedent(state).split('\n')
    s = State(lines=lines)
    ret_dict = s.GoHome(((3, 0), 'C'))

    self.assertEqual(len(ret_dict), 1)
    new_state = list(ret_dict.keys())[0]
    # print(new_state)
    self.assertTrue(((6, 2), 'C') in new_state.state)
    next_dict_for_pod = s.NextStatesForPod(((3, 0), 'C'))
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
    s = State(lines=dedent(state).split('\n'))
    pod = ((2, 1), 'A')
    free = s.FreeColumns(pod)
    self.assertEqual(free, {0, 1, 3, 5, 7, 9, 10, 11})

    state = '''\
            #############
            #.A.....C...#
            ###.#B#.#D###
              #A#B#C#D#
              #########'''
    s = State(lines=dedent(state).split('\n'))
    pod = ((4, 1), 'B')
    free = s.FreeColumns(pod)
    self.assertEqual(free, set({3, 5}))

    state = '''\
            #############
            #...A.C.....#
            ###.#B#.#D###
              #A#B#C#D#
              #########'''
    s = State(lines=dedent(state).split('\n'))
    pod = ((4, 1), 'B')
    free = s.FreeColumns(pod)
    self.assertEqual(free, set({}))

  def testLinesToState(self):
    """Test conversion from State to lines and back."""
    state_lines = '''\
                  #############
                  #...A.C.....#
                  ###.#B#.#D###
                    #A#B#C#D#
                    #########'''
    lines1 = dedent(state_lines).split('\n')
    s1 = State(lines=lines1)
    lines2 = s1.SelfToLines()
    s2 = State(lines=lines2)
    self.assertEqual(lines1, lines2)
    self.assertEqual(s1, s2)
    assert s1 is not s2

  def testAllNextStates(self):
    """Test AllNextStates"""
    state_lines = '''\
                  #############
                  #.....B.....#
                  ###A#.#C#D###
                    #A#B#C#D#
                    #########'''
    lines = dedent(state_lines).split('\n')
    s = State(lines)
    next_states = s.AllNextStates()
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
    self.assertEqual(list(next_states.keys())[0].state, expected)


if __name__ == '__main__':
  unittest.main()
