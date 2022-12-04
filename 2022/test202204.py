#!/usr/bin/python3

import unittest
from prog202204 import *


class TestProg202204(unittest.TestCase):

  def testParseLineToNumbers(self):
    self.assertEqual(ParseLineToNumbers('1-2,3-4'), (1, 2, 3, 4))
    self.assertEqual(ParseLineToNumbers('11-22,33-44'), (11, 22, 33, 44))
    with self.assertRaises(ValueError):
      ParseLineToNumbers('1-a, 3-b')

  def testWhollyContained(self):
    self.assertEqual(WhollyContained(2, 4, 6, 8), False)
    self.assertEqual(WhollyContained(2, 3, 4, 5), False)
    self.assertEqual(WhollyContained(5, 7, 7, 9), False)
    self.assertEqual(WhollyContained(2, 8, 3, 7), True)
    self.assertEqual(WhollyContained(6, 6, 4, 6), True)
    self.assertEqual(WhollyContained(2, 6, 4, 8), False)

  def testOverlapAtAll(self):
    self.assertEqual(OverlapAtAll(2, 4, 6, 8), False)
    self.assertEqual(OverlapAtAll(2, 3, 4, 5), False)
    self.assertEqual(OverlapAtAll(5, 7, 7, 9), True)
    self.assertEqual(OverlapAtAll(2, 8, 3, 7), True)
    self.assertEqual(OverlapAtAll(6, 6, 4, 6), True)
    self.assertEqual(OverlapAtAll(2, 6, 4, 8), True)

  def testSolve(self):
    sample = ['2-4,6-8',
              '2-3,4-5',
              '5-7,7-9',
              '2-8,3-7',
              '6-6,4-6',
              '2-6,4-8',]
    self.assertEqual(Solve(sample, 'Part 1'), 2)
    self.assertEqual(Solve(sample, 'Part 2'), 4)
    with self.assertRaises(AssertionError):
      Solve([], 'Part 3')


if __name__ == '__main__':
  unittest.main()
