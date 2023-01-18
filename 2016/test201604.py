#!/usr/bin/env python3
"""Unit tests for prog201604.py"""

import unittest
from prog201604 import RotN


class TestProg201604(unittest.TestCase):

  def testRotN(self):
    self.assertEqual(RotN('a', 1), 'b')
    self.assertEqual(RotN('z', 1), 'a')
    self.assertEqual(RotN('a', 26), 'a')
    self.assertEqual(RotN('z', 26), 'z')
    self.assertEqual(RotN('z', 27), 'a')


if __name__ == '__main__':
  unittest.main()
