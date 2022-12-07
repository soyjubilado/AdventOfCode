#!/usr/bin/python3

import unittest
from prog202206 import Solver, NoSolution


DATA = [
        ['bvwbjplbgvbhsrlpgdmjqwftvncz', 4, 5],
        ['bvwbj', 4, 5],
        ['nppdvjthqldpwncqszvftbrmjlhg', 4, 6],
        ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4, 10],
        ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4, 11],
        ['mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14, 19],
        ['bvwbjplbgvbhsrlpgdmjqwftvncz', 14, 23],
        ['nppdvjthqldpwncqszvftbrmjlhg', 14, 23],
        ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14, 29],
        ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14, 26],
       ]


class TestProg202206(unittest.TestCase):

  def testSolver(self):
    for line, width, expected in DATA:
      self.assertEqual(Solver(line, width), expected)
    with self.assertRaises(NoSolution):
      Solver('hello', 4)


if __name__ == '__main__':
  unittest.main()
