#!/usr/bin/env python3
"""Unit tests for prog201607.py"""

from prog201607 import ContainsAbba, AllAba, Flipped


def testContainsAbba():
  """Test ContainsAbba()"""
  testcases = [['abba', 'abba'],
               ['abab', False],
               ['cccc', False],
               ['cabbac', 'abba'],
               ['cccccabba', 'abba'],
               ['dxxdcccccabba', 'dxxd'],
               ['abbac', 'abba']
              ]
  for case, expected in testcases:
    actual = ContainsAbba(case)
    passing = 'pass' if actual == expected else 'fail'
    print(f'  {passing}: {case} -> {actual} (expected {expected})')


def testAllAba():
  """Test AllAba()"""
  testcases = [['abba', []],
               ['abab', ['aba', 'bab']],
               ['cccc', []],
               ['cabbac', []],
               ['cccccabba', []],
               ['dxdcdcccaba', ['dxd', 'dcd', 'cdc', 'aba']],
               ['ababcccc', ['aba', 'bab']],
               ['ccccabab', ['aba', 'bab']],
               ['ccababcc', ['aba', 'bab']],
              ]
  for case, expected in testcases:
    actual = AllAba(case)
    passing = 'pass' if actual == expected else 'fail'
    print(f'  {passing}: {case} -> {actual} (expected {expected})')


def testFlipped():
  """Test Flipped()"""
  testcases = [['aba', 'bab'],
              ]
  for case, expected in testcases:
    actual = Flipped(case)
    passing = 'pass' if actual == expected else 'fail'
    print(f'  {passing}: {case} -> {actual} (expected {expected})')


def main():
  """main"""
  print("testContainsAbba()")
  testContainsAbba()
  print("testAllAba()")
  testAllAba()
  print("testFlipped()")
  testFlipped()


if __name__ == "__main__":
  main()
