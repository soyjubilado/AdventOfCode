#!/usr/bin/env python3
"""Unit tests for prog201609.py"""

import unittest
from prog201609 import Unpack, Length, ExtractParts


class Tests2016Day09(unittest.TestCase):
  """Class to test prog201609.py functions"""

  def testUnpack(self):
    """Test Unpack()"""
    self.assertEqual(Unpack('ADVENT'), 'ADVENT')
    self.assertEqual(Unpack('A(1x5)BC'), 'ABBBBBC')
    self.assertEqual(Unpack('(3x3)XYZ'), 'XYZXYZXYZ')
    self.assertEqual(Unpack('A(2x2)BCD(2x2)EFG'), 'ABCBCDEFEFG')
    self.assertEqual(Unpack('(6x1)(1x3)A'), '(1x3)A')
    self.assertEqual(Unpack('X(8x2)(3x3)ABCY'), 'X(3x3)ABC(3x3)ABCY')

  def testLength(self):
    """Test Length()"""
    self.assertEqual(Length('ADVENT'), 6)
    self.assertEqual(Length('A(1x5)BC'), 7)
    self.assertEqual(Length('(3x3)XYZ'), 9)
    self.assertEqual(Length('A(2x2)BCD(2x2)EFG'), 11)
    self.assertEqual(Length('(6x1)(1x3)A'), 3)
    self.assertEqual(Length('X(8x2)(3x3)ABCY'), 20)
    self.assertEqual(Length('(27x12)(20x12)(13x14)(7x10)(1x12)A'), 241920)
    self.assertEqual(Length('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)'
                            'TWO(5x7)SEVEN'), 445)

  def testExtractParts(self):
    """Test ExtractParts()"""
    self.assertEqual(ExtractParts("A(1x5)BC"), ('A', 5, 'B', 'C'))
    self.assertEqual(ExtractParts("(3x3)XYZ"), ('', 3, 'XYZ', ''))
    self.assertEqual(ExtractParts("A(2x2)BCD(2x2)EFG"),
                     ('A', 2, 'BC', 'D(2x2)EFG'))
    self.assertEqual(ExtractParts("(6x1)(1x3)A"), ('', 1, '(1x3)A', ''))
    self.assertEqual(ExtractParts("X(8x2)(3x3)ABCY"), ('X', 2, '(3x3)ABC', 'Y'))


if __name__ == '__main__':
  unittest.main()
