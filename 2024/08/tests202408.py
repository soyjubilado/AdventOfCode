#!/usr/bin/env python3
"""Simple unit tests for prog202408."""

from prog202408 import Antinodes

def testAntinodes():
  """This helped me find a bug in part1 really quickly."""
  cases = [[((1, 1), (2, 2)), {(0, 0), (3, 3)}],
           [((2, 2), (1, 1)), {(0, 0), (3, 3)}],
           [((2, 1), (1, 2)), {(3, 0), (0, 3)}],
           [((1, 2), (2, 1)), {(3, 0), (0, 3)}],
           [((1, 1), (1, 2)), {(1, 0), (1, 3)}],
           [((1, 2), (1, 1)), {(1, 0), (1, 3)}],
           [((1, 1), (2, 1)), {(0, 1), (3, 1)}],
           [((2, 1), (1, 1)), {(0, 1), (3, 1)}],
          ]
  for case, expected in cases:
    actual = set(Antinodes(*case))
    passing = 'PASS' if actual == expected else 'FAIL'
    print(f'{passing}: {case} -> {actual} (expected {expected})')


def main():
  """main"""
  testAntinodes()


if __name__ == '__main__':
  main()
