#!/usr/bin/env python3
"""Brute force tool for Part 2"""

from prog202417 import Computer
TARGET = [2, 4, 1, 1, 7, 5, 0, 3, 4, 7, 1, 6, 5, 5, 3, 0]


def StartWithA(a):
  """Run the computer with a in the 'a' register."""
  prog = [2, 4, 1, 1, 7, 5, 0, 3, 4, 7, 1, 6, 5, 5, 3, 0]
  c = Computer(a, 0, 0)
  c.RunProg(prog)
  return c.output


def FindStart():
  """Find a number just below what will give a 16-digit answer."""
  magnitude = 0
  answer = []
  a = 1
  while len(answer) < 16:
    magnitude += 1
    a = 10 ** magnitude
    answer = StartWithA(a)

  answer = []
  a = 10 ** (magnitude - 1)
  incr = 10 ** (magnitude - 3)
  while len(answer) < 16:
    a += incr
    answer = StartWithA(a + incr)
  # print(f'{a + incr} -> {answer}')
  return a - incr


def Magnitude(n):
  """The m such that n // 10 ** m will give the first digit of n"""
  m = -1
  while n > 0:
    n = n // 10
    m += 1
  return m


def main():
  """main"""
  start = FindStart()
  magnitude = Magnitude(start)

  incr = 10 ** (magnitude - 3)
  answer = StartWithA(start)
  while len(answer) < 16 or answer[-3:] != TARGET[-3:]:
    start += incr
    answer = StartWithA(start)
  print(f'target: {TARGET}')
  print(f'{start} -> {answer}')
  start -= 100 * incr

  incr = 10 ** (magnitude - 6)
  answer = StartWithA(start)
  while answer[-6:] != TARGET[-6:]:
    start += incr
    answer = StartWithA(start)
  print(f'{start} -> {answer}')
  start -= 100 * incr

  incr = 10 ** (magnitude - 9)
  answer = StartWithA(start)
  while answer[-9:] != TARGET[-9:]:
    start += incr
    answer = StartWithA(start)
  print(f'{start} -> {answer}')
  start -= 100 * incr

  incr = 10 ** (magnitude - 12)
  answer = StartWithA(start)
  while answer[-12:] != TARGET[-12:]:
    start += incr
    answer = StartWithA(start)
  print(f'{start} -> {answer}')
  start -= 100 * incr
  magnitude = Magnitude(start)

  incr = 10 ** (magnitude - 13)
  answer = StartWithA(start)
  while answer[-14:] != TARGET[-14:]:
    start += incr
    answer = StartWithA(start)
  print(f'{start} -> {answer}')
  start -= 100 * incr
  magnitude = Magnitude(start)

  incr = 10 ** (magnitude - 14)
  answer = StartWithA(start)
  while answer != TARGET:
    start += incr
    answer = StartWithA(start)
  print(f'{start} -> {answer}')


if __name__ == '__main__':
  main()
