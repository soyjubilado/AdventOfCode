#!/usr/bin/env python3
"""Unit tests for prog201507.py"""

from prog201507 import Op, ParseLine


def testOp():
  """Test Op()"""
  cases = [(('AND', 123, 456), 72),
           (('OR', 123, 456), 507),
           (('LSHIFT', 123, 2), 492),
           (('RSHIFT', 456, 2), 114),
           (('NOT', 123), 65412),
           (('NOT', 456), 65079),
           (('123',), 123),
          ]
  for c, expected in cases:
    actual = Op(*c)
    passing = 'pass' if actual == expected else 'fail'
    print(f'{passing}: {c} -> {actual} (expected {expected})')


def testParseLine():
  """Test ParseLine()"""
  cases = [('123 -> x', ('x', '123')),
           ('456 -> y', ('y', '456')),
           ('x AND y -> d', ('d', 'AND', 'x', 'y')),
           ('x OR y -> e', ('e', 'OR', 'x', 'y')),
           ('x LSHIFT 2 -> f', ('f', 'LSHIFT', 'x', '2')),
           ('y RSHIFT 2 -> g', ('g', 'RSHIFT', 'y', '2')),
           ('NOT x -> h', ('h', 'NOT', 'x')),
           ('NOT y -> i', ('i', 'NOT', 'y')),
           ('NOT ay -> i', ('i', 'NOT', 'ay')),
          ]
  for c, expected in cases:
    actual = ParseLine(c)
    passing = 'pass' if actual == expected else 'fail'
    print(f'{passing}: {c} -> {actual} (expected {expected})')


def main():
  """main()"""
  testOp()
  testParseLine()


if __name__ == '__main__':
  main()
