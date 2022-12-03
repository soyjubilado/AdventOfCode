#!/usr/bin/python3

import unittest
from prog202203 import Priority

class TestProg202203(unittest.TestCase):

  def testPriority(self):
    self.assertEqual(Priority('a'), 1)
    self.assertEqual(Priority('z'), 26)
    self.assertEqual(Priority('A'), 27)
    self.assertEqual(Priority('Z'), 52)
    with self.assertRaises(Exception):
      Priority('1')


if __name__ == '__main__':
  unittest.main()
