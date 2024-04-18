#!/usr/bin/python3
"""unit tests for prog201505"""

from h_test import h_test
from prog201505 import ThreeVowels, DoubleLetter, BadWords, IsNicePt1
from prog201505 import MoreThan2Nonconsecutive, TwoLettersTwice, PairSepSingle
from prog201505 import IsNicePt2


def testThreeVowels():
  """test ThreeVowels()"""
  cases = [('hello', False),
           ('hello mellow', True),
           ('a hello mellow', True),
           ('aeio', True),
          ]
  return h_test(cases, ThreeVowels)


def testDoubleLetter():
  """test DoubleLetter()"""
  cases = [('hell', True),
           ('llo melow', True),
           ('a hello melow', True),
           ('aeio', False),
          ]
  return h_test(cases, DoubleLetter)


def testBadWords():
  """test BadWords()"""
  cases = [('hello', False),
           ('helloab', True),
           ('cdhello', True),
           ('aeio', False),
           ('helloxy', True),
          ]
  return h_test(cases, BadWords)


def testIsNicePt1():
  """test IsNicePt1()"""
  cases = [('ugknbfddgicrmopn', True),
           ('aaa', True),
           ('jchzalrnumimnmhp', False),
           ('haegwjzuvuyypxyu', False),
           ('dvszwmarrgswjxmb', False),
          ]
  return h_test(cases, IsNicePt1)


def testMoreThan2Nonconsecutive():
  """test MoreThan2Nonconsecutive()"""
  cases = [([1, 2, 3], True),
           ([1, 3], True),
           ([1, 2, 3, 5], True),
           ([1, 2, 3, 4, 5], True),
           ([1, 2], False),
           ([3, 4], False),
           ([1], False),
           ([], False),
          ]
  return h_test(cases, MoreThan2Nonconsecutive)


def testTwoLettersTwice():
  """test TwoLettersTwice()"""
  cases = [('xyxy', True),
           ('aabcdefgaa', True),
           ('aaa', False),
          ]
  return h_test(cases, TwoLettersTwice)


def testPairSepSingle():
  """test PairSepSingle()"""
  cases = [('xyx', True),
           ('abcdefeghi', True),
           ('aaa', True),
          ]
  return h_test(cases, PairSepSingle)


def testIsNicePt2():
  """test IsNicePt2()"""
  cases = [('qjhvhtzxzqqjkmpb', True),
           ('xxyxx', True),
           ('uurcxstgmygtbstg', False),
           ('ieodomkazucvgmuy', False),
          ]
  return h_test(cases, IsNicePt2)


def main():
  """main"""
  failures = 0
  failures += testThreeVowels()
  failures += testDoubleLetter()
  failures += testBadWords()
  failures += testIsNicePt1()
  failures += testMoreThan2Nonconsecutive()
  failures += testTwoLettersTwice()
  failures += testPairSepSingle()
  print(f'\nTotal failed tests: {failures}')

if __name__ == '__main__':
  main()
