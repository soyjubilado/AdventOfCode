#!/usr/bin/env python3
"""tests for 201802"""

from h_test import h_test
from prog201802 import DifferingLetters, CommonLetters


def test_DifferingLetters():
  """test for DifferingLetters()"""
  cases = [[('abcd', 'abce'), 1],
           [('abcd', 'abef'), 2],
          ]
  h_test(cases, DifferingLetters, unpack=True)


def test_CommonLetters():
  """test for CommonLetters()"""
  cases = [[('abcd', 'abce'), 'abc'],
           [('abcd', 'abef'), 'ab'],
          ]
  h_test(cases, CommonLetters, unpack=True)


if __name__ == '__main__':
  test_DifferingLetters()
  test_CommonLetters()
