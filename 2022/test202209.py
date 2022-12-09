#!/usr/bin/python3

import unittest
from prog202209 import AreAdjacent, MoveHead, MoveTail


class TestProg202206(unittest.TestCase):

  def testAreAdjacent(self):
    self.assertTrue(AreAdjacent((0,0), (-1,1)))
    self.assertTrue(AreAdjacent((0,0), (0,1)))
    self.assertTrue(AreAdjacent((0,0), (1,1)))
    self.assertTrue(AreAdjacent((0,0), (-1,0)))
    self.assertTrue(AreAdjacent((0,0), (0,0)))
    self.assertTrue(AreAdjacent((0,0), (0,1)))
    self.assertTrue(AreAdjacent((0,0), (-1,-1)))
    self.assertTrue(AreAdjacent((0,0), (0,-1)))
    self.assertTrue(AreAdjacent((0,0), (1,-1)))
    self.assertTrue(AreAdjacent((1,1), (2,2)))
    self.assertFalse(AreAdjacent((0,0), (2,-1)))

  def testMoveHead(self):
    self.assertEqual(MoveHead((0,0), 'R'), (1,0))
    self.assertEqual(MoveHead((0,0), 'L'), (-1,0))
    self.assertEqual(MoveHead((0,0), 'U'), (0,1))
    self.assertEqual(MoveHead((0,0), 'D'), (0,-1))

  def testMoveTail(self):
    self.assertEqual(MoveTail((0,0), (0,0)), (0,0))
    self.assertEqual(MoveTail((0,0), (0,1)), (0,0))
    self.assertEqual(MoveTail((0,0), (0,-1)), (0,0))
    self.assertEqual(MoveTail((0,0), (1,0)), (0,0))
    self.assertEqual(MoveTail((0,0), (2,0)), (1,0))
    self.assertEqual(MoveTail((0,0), (2,2)), (1,1))
    self.assertEqual(MoveTail((0,0), (2,1)), (1,1))
    self.assertEqual(MoveTail((0,0), (1,2)), (1,1))


if __name__ == '__main__':
  unittest.main()
