#!/usr/bin/env python3
"""unit tests for prog202313"""

from grid import GridWrap
from h_test import h_test
from prog202313 import IndexOfHorizReflection, IndexOfVertReflection
from prog202313 import IsHorizReflection, IsVertReflection


example1 = ['#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',]

example1b = ['#.##.##.',
             '..#.#.#.',
             '##.....#',
             '##.....#',
             '..#.#.#.',
             '..##.##.',
             '#.#.#.#.',]

example2 = ['#...##..#',
            '#....#..#',
            '..##..###',
            '#####.##.',
            '#####.##.',
            '..##..###',
            '#....#..#',]

example2b = ['#...##..#',
             '#....#..#',
             '..##..###',
             '#####.##.',
             '..##..###',
             '#....#..#',]


def test_IsHorizReflection():
  """Test IsHorizReflection()"""
  testcases = [[(GridWrap(example1, 'example1'), 1), False],
               [(GridWrap(example1, 'example1'), 2), False],
               [(GridWrap(example1, 'example1'), 3), False],
               [(GridWrap(example1, 'example1'), 4), False],
               [(GridWrap(example1, 'example1'), 5), False],
               [(GridWrap(example2, 'example2'), 1), False],
               [(GridWrap(example2, 'example2'), 2), False],
               [(GridWrap(example2, 'example2'), 3), False],
               [(GridWrap(example2, 'example2'), 5), False],
               [(GridWrap(example2, 'example2'), 4), True],
               [(GridWrap(example2b, 'example2b'), 2), False],
               [(GridWrap(example2b, 'example2b'), 3), False],
               [(GridWrap(example2b, 'example2b'), 4), False],
              ]
  return h_test(testcases, IsHorizReflection, unpack=True)


def test_IsVertReflection():
  """Test IsVertReflection()"""
  testcases = [[(GridWrap(example1, 'example1'), 1), False],
               [(GridWrap(example1, 'example1'), 2), False],
               [(GridWrap(example1, 'example1'), 3), False],
               [(GridWrap(example1, 'example1'), 4), False],
               [(GridWrap(example1, 'example1'), 5), True],
               [(GridWrap(example1b, 'example1b'), 3), False],
               [(GridWrap(example1b, 'example1b'), 4), False],
               [(GridWrap(example1b, 'example1b'), 5), False],
               [(GridWrap(example1b, 'example1b'), 6), False],
               [(GridWrap(example2, 'example2'), 1), False],
               [(GridWrap(example2, 'example2'), 2), False],
               [(GridWrap(example2, 'example2'), 3), False],
               [(GridWrap(example2, 'example2'), 4), False],
               [(GridWrap(example2, 'example2'), 5), False],
              ]
  return h_test(testcases, IsVertReflection, unpack=True)


def test_IndexOfHorizReflection():
  """Test IndexOfHorizReflection()"""
  testcases = [[GridWrap(example1, 'example1'), [0]],
               [GridWrap(example2, 'example2'), [400]],
               [GridWrap(example2b, 'example2b'), [0]],
              ]
  return h_test(testcases, IndexOfHorizReflection, unpack=False)


def test_IndexOfVertReflection():
  """Test IndexOfVertReflection()"""
  testcases = [[GridWrap(example1, 'example1'), [5]],
               [GridWrap(example1b, 'example1b'), [0]],
               [GridWrap(example2, 'example2'), [0]],
              ]
  return h_test(testcases, IndexOfVertReflection, unpack=False)


def main():
  """main"""
  failures = 0
  failures += test_IsHorizReflection()
  failures += test_IsVertReflection()
  failures += test_IndexOfHorizReflection()
  failures += test_IndexOfVertReflection()
  print(f'\nTotal failed tests: {failures}')


if __name__ == '__main__':
  main()
