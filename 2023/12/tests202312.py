#!/usr/bin/env python3
"""unit tests for prog202312.py"""

import sys
sys.path.insert(0, '../lib/')
from h_test import h_test
from prog202312 import spring_conditions, split_spring, count_matches


def test_spring_conditions():
  """Test spring_conditions()"""
  testcases = [['#.#.###', [1, 1, 3]],
               ['.#...#....###.', [1, 1, 3]],
               ['.#.###.#.######', [1, 3, 1, 6]],
               ['####.#...#...', [4, 1, 1]],
               ['#....######..#####.', [1, 6, 5]],
               ['.###.##....#', [3, 2, 1]],
              ]
  return h_test(testcases, spring_conditions)


def test_split_spring():
  """Test split_spring()"""
  testcases = [('.??..??...?##.', ['??', '??', '?##']),
               ('?#?#?#?#?#?#?#?', ['?#?#?#?#?#?#?#?']),
               ('????.#...#...', ['????', '#', '#']),
               ('????.######..#####.', ['????', '######', '#####']),
               ('?###????????', ['?###????????']),
              ]
  return h_test(testcases, split_spring)


def test_count_viable():
  """Test count_viable()"""
  testcases = [(('???.###', [1, 1, 3]), 1),
               (('.??..??...?##.', [1, 1, 3]), 4),
               (('?#?#?#?#?#?#?#?', [1, 3, 1, 6]), 1),
               (('????.#...#...', [4, 1, 1]), 1),
               (('????.######..#####.', [1, 6, 5]), 4),
               (('?###????????', [3, 2, 1]), 10),
               (('????#?.??.', [1, 1, 2]), 4),
               (('#??.?#...?', [1, 1, 1]), 2),
               (('???.?#?.??', [1, 1, 1]), 7),
               (('????#?#?..?#?', [4, 1]), 2),
               (('.???????.#', [2, 1, 1]), 10),
               (('?#??#??.#?', [1, 1, 1]), 1),
              ]
  return h_test(testcases, count_matches)


def main():
  """main"""
  failures = 0
  failures += test_spring_conditions()
  failures += test_split_spring()
  failures += test_count_viable()
  print(f'\nTotal failed tests: {failures}')


if __name__ == '__main__':
  main()
