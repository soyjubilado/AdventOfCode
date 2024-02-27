#!/usr/bin/env python3
"""unit tests for prog202314.py"""

import sys
sys.path.insert(0, '../lib/')
from h_test import h_test
from grid import Grid
from prog202314 import *

example1 = ['O....#....',
            'O.OO#....#',
            '.....##...',
            'OO.#O....O',
            '.O.....O#.',
            'O.#..O.#.#',
            '..O..#O..O',
            '.......O..',
            '#....###..',
            '#OO..#....',]

tilt_north1 = ['OOOO.#.O..',
               'OO..#....#',
               'OO..O##..O',
               'O..#.OO...',
               '........#.',
               '..#....#.#',
               '..O..#.O.O',
               '..O.......',
               '#....###..',
               '#....#....',]


def test_SlideNorth():
  """Test SlideNorth()""" 
  testcases = [[GridWrap(example1[:]), GridWrap(tilt_north1)],]
  return h_test(testcases, SlideNorth)


def main():
  """main"""
  failures = 0
  failures += test_SlideNorth()
  print(f'\nTotal failed tests: {failures}')


if __name__ == '__main__':
  main()
