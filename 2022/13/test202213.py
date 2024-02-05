#!/usr/bin/python3
"""Home brew unit test."""

from prog202213 import RightOrder
from prog202213 import L_LESS_THAN_R, L_GREATER_THAN_R, L_EQUALS_R


CASES = [(([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]), L_LESS_THAN_R),
         (([1, 1, 5, 1, 1], [1, 1, 3, 1, 1]), L_GREATER_THAN_R),
         (([[1], [2, 3, 4]], [[1], 4]), L_LESS_THAN_R),
         (([9], [[8, 7, 6]]), L_GREATER_THAN_R),
         (([[4, 4], 4, 4], [[4, 4], 4, 4, 4]), L_LESS_THAN_R),
         (([7, 7, 7, 7], [7, 7, 7]), L_GREATER_THAN_R),
         (([], [3]), L_LESS_THAN_R),
         (([[[]]], [[]]), L_GREATER_THAN_R),
         (([1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
           [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]), L_GREATER_THAN_R),
         (([1, 2, 3], [1, 2, 3, 4]), L_LESS_THAN_R),
         (([1, 2, 3, 4], [1, 2, 3]), L_GREATER_THAN_R),
         (([1], [[1]]), L_EQUALS_R),
         (([[1]], [1]), L_EQUALS_R),
         (([[1, 2, 3], 1], [[1, 2, 3], 1, 2]), L_LESS_THAN_R),
         (([[1, 2, 3], 1, 2], [[1, 2, 3], 1]), L_GREATER_THAN_R),
        ]

def testRightOrder():

  pass_count = 0
  fail_count = 0
  for case in CASES:
    print(case)
    args, expected = case
    left, right = args

    actual = RightOrder(left, right)
    if actual == expected:
      pass_count += 1
    else:
      fail_count += 1
      print(f'Test failed for {left} {right} '
            f'expected {expected} but got {actual}')

  print(f'{pass_count} tests pass and {fail_count} fail')


if __name__ == '__main__':
  testRightOrder()
