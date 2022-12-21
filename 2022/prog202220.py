#!/usr/bin/python3
# file created 2022-Dec-20 18:47
"""https://adventofcode.com/2022/day/20"""

DATA = 'data202220.txt'
# DATA = 'testdata202220.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [int(i.strip()) for i in fh]
  return lines


class Number():
  """A linked list number."""
  def __init__(self, number):
    self.value = number
    self.next = None
    self.prev = None

  def __repr__(self):
    return f'{self.value}'

  def __str__(self):
    return f'{self.value}'


def BuildCircularList(lines):
  """Create a circular linked list from the input lines."""
  orig_list = []
  prev_num = None
  for n in lines:
    num = Number(n)
    if prev_num:
      prev_num.next = num
      num.prev = prev_num
    orig_list.append(num)
    prev_num = num
  orig_list[-1].next = orig_list[0]
  orig_list[0].prev = orig_list[-1]
  return orig_list


def RearrangeCircularList(orig_list):
  """Given a list of numbers, rearrange the linked list according to the
     rules of the game."""
  length = len(orig_list) - 1

  # rearrange numbers
  for n in orig_list[:]:
    if n.value % length == 0:
      continue

    distance = n.value % length

    # pull n out of the list
    n.prev.next = n.next
    n.next.prev = n.prev
    current = n

    # skip down the list n times
    for _ in range(distance):
      current = current.next

    # insert n into the list here
    after_n = current.next
    current.next = n
    n.prev = current
    n.next = after_n
    after_n.prev = n


def PrintCircularList(head):
  """Given a single node in the list, print out the list from there."""
  last = head.prev
  while head != last:
    print(f'{head}', end=', ')
    head = head.next
  print(f'{head}')


def GroveValues(head):
  """Return a list of the values at 1000, 2000, and 3000 past the zero."""
  # find zero
  current = head
  while current.value != 0:
    current = current.next

  grove = []
  # find the three grove values and save them
  for _ in range(3):
    for _ in range(1000):
      current = current.next
    grove.append(current.value)
  return grove


def Part1(lines):
  """Part 1"""
  orig_list = BuildCircularList(lines)
  RearrangeCircularList(orig_list[:])
  grove = GroveValues(orig_list[0])
  print(f'Part 1: {sum(grove)}')


def Part2(lines):
  """Part 2 is like Part 1"""
  magic_decryption_key = 811589153
  orig_list = BuildCircularList(lines)
  for i in orig_list:
    i.value *= magic_decryption_key
  for n in range(10):
    print(f'rearranging; {10 - n} times to go')
    RearrangeCircularList(orig_list[:])

  grove = GroveValues(orig_list[0])
  print(f'Part 2: {sum(grove)}')


def main():
  """main"""
  lines = GetData(DATA)
  Part1(lines)
  Part2(lines)


if __name__ == '__main__':
  main()
