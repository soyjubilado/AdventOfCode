#!/usr/bin/env python3
"""unit tests for progYYYYDD.py"""

import sys
sys.path.insert(0, '../lib/')
from h_test import h_test


def test_my_func():
  """Test spring_conditions()"""
  testcases = [['#.#.###', [1, 1, 3]],
               ['.#...#....###.', [1, 1, 3]],
               ['.#.###.#.######', [1, 3, 1, 6]],
               ['####.#...#...', [4, 1, 1]],
               ['#....######..#####.', [1, 6, 5]],
               ['.###.##....#', [3, 2, 1]],
              ]
  return h_test(testcases, my_func)


def main():
  """main"""
  failures = 0

  failures += test_my_func()

  print(f'\nTotal failed tests: {failures}')


if __name__ == '__main__':
  main()
