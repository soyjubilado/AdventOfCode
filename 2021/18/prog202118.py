#!/usr/bin/python3
#file created 2021-Dec-17 20:48
"""https://adventofcode.com/2021/day/18

Create a parse tree to represent the snail number. This was fairly easy, took
about an hour. The idea for Explode was pretty good, but poor execution led
to some time spent debugging. If concerned about references, note the use of
"is" vs "==" is not the same.

Spent way too much time on part 2. There are only 10000 permutations.
"""

from itertools import permutations
from copy import deepcopy
DATA = 'data202118.txt'
DATA = 'testdata202118.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


class Snail(object):
  def __init__(self, left, right):
    # left and right are either type Snails or type ints
    self.left = left
    self.right = right
    self.parent = None
    for child in [self.left, self.right]:
      if isinstance(child, Snail):
        child.parent = self

  def PrintDebug(self):
    print(f'me: {self}')
    print(f'  my parent: {self.parent}')
    if self.parent and self.parent.left is self:
      print('  I am the left child')
    elif self.parent:
      print('  I am the right child')
    for child in [self.left, self.right]:
      if isinstance(child, Snail):
        child.PrintDebug()

  def AddRight(self, num, came_from):
    """Add number to the next digit on the right"""
    if came_from is self.left and isinstance(self.right, int):
      self.right += num
    elif came_from is self.left and isinstance(self.right, Snail):
      self.right.AddLeftDown(num)
    elif came_from is self.right and not self.parent:
      pass
    elif came_from is self.right:
      self.parent.AddRight(num, self)

  def AddLeftDown(self, num):
    if isinstance(self.left, int):
      self.left += num
    else:
      self.left.AddLeftDown(num)

  def AddLeft(self, num, came_from):
    """Add number to the next digit on the left"""
    if came_from is self.right and isinstance(self.left, int):
      self.left += num
    elif came_from is self.right and isinstance(self.left, Snail):
      self.left.AddRightDown(num)
    elif came_from is self.left and not self.parent:
      pass
    elif came_from is self.left:
      self.parent.AddLeft(num, self)

  def AddRightDown(self, num):
    if isinstance(self.right, int):
      self.right += num
    else:
      self.right.AddRightDown(num)

  def Explode(self, depth=0):
    if depth >= 4:
      self.parent.AddRight(self.right, self)
      self.parent.AddLeft(self.left, self)

      if self.parent.left is self:
        self.parent.left = 0
      elif self.parent.right is self:
        self.parent.right = 0
      else:
        raise Exception
      return True

    # depth is less than 4
    elif isinstance(self.left, Snail) and self.left.Explode(depth + 1):
      return True
    elif isinstance(self.right, Snail) and self.right.Explode(depth + 1):
      return True
    return False

  def Subsnail(self, value_ge_10):
    new_left = value_ge_10 // 2
    new_right = value_ge_10 // 2 + value_ge_10 % 2
    snail = Snail(new_left, new_right)
    snail.parent = self
    return snail

  def Split(self):
    """Return true if something split at this level or below.
       Splits must occur at leftmost possible branch."""
    if isinstance(self.left, int) and self.left >= 10:
      subsnail = self.Subsnail(self.left)
      self.left = subsnail
      return True
    elif isinstance(self.left, Snail) and self.left.Split():
      return True
    elif isinstance(self.right, int) and self.right >= 10:
      subsnail = self.Subsnail(self.right)
      self.right = subsnail
      return True
    elif isinstance(self.right, Snail) and self.right.Split():
      return True
    else:
      return False

  def Reduce(self):
    something_happened = True
    while something_happened:
      something_happened = False
      while self.Explode():
        something_happened = True
      if self.Split():
        something_happened = True

  def Magnitude(self):
    if isinstance(self.left, int):
      sub_mag_left = self.left
    else:
      sub_mag_left = self.left.Magnitude()
    if isinstance(self.right, int):
      sub_mag_right = self.right
    else:
      sub_mag_right = self.right.Magnitude()
    return (3 * sub_mag_left) + (2 * sub_mag_right)

  def Depth(self):
    if isinstance(self.left, int) and isinstance(self.right, int):
      return 1
    elif isinstance(self.left, Snail) and isinstance(self.right, Snail):
      return 1 + max(self.left.Depth(), self.right.Depth())
    elif isinstance(self.left, Snail):
      return 1 + self.left.Depth()
    elif isinstance(self.right, Snail):
      return 1 + self.right.Depth()
    else:
      raise Exception

  def __str__(self):
    return f'[{self.left},{self.right}]'


def CreateSnail(line):
  """Scan to find the highest level ',' and create snail from both sides"""
  ptr = 0
  stack = []
  for idx, c in enumerate(line):
    if c == '[':
      stack.append(c)
    elif c == ']':
      stack.pop()
    elif c == ',' and len(stack) == 1:
      break
  left = line[1:idx]
  right = line[idx+1:-1]
  if left.isdigit() and right.isdigit():
    return Snail(int(left), int(right))
  elif left.isdigit():
    return Snail(int(left), CreateSnail(right))
  elif right.isdigit():
    return Snail(CreateSnail(left), int(right))
  else:
    return Snail(CreateSnail(left), CreateSnail(right))


def AddSnails(snail1, snail2):
  s1 = deepcopy(snail1)
  s2 = deepcopy(snail2)
  new_snail = Snail(s1, s2)
  new_snail.Reduce()
  return new_snail


def testPt2():
  snail1 = CreateSnail('[2,8]')
  snail2 = CreateSnail('[6,4]')
  print(f'snail1: {snail1} magnitude: {snail1.Magnitude()}')
  print(f'snail2: {snail2} magnitude: {snail2.Magnitude()}')
  snail1_snail2 = AddSnails(snail1, snail2)
  snail2_snail1 = AddSnails(snail2, snail1)
  print(f'1 + 2 = {snail1_snail2} magnitude {snail1_snail2.Magnitude()}')
  print(f'2 + 1 = {snail2_snail1} magnitude {snail2_snail1.Magnitude()}')


def Pt2():
  lines = GetData(DATA)
  snail_array = []
  for line in lines:
    snail = CreateSnail(line)
    snail_array.append(snail)

  largest = 0
  largest_pair = None

  for snail1, snail2 in permutations(snail_array, 2):
    combined = AddSnails(snail1, snail2)
    this_mag = combined.Magnitude()
    if this_mag >= largest:
      largest = this_mag
      largest_pair = (snail1, snail2)
  print(f'largest seen for Part 2: {largest}')
  print(f'  {largest_pair[0]}')
  print(f'  {largest_pair[1]}', flush=True)

def Pt1():
  lines = GetData(DATA)
  snail_1 = CreateSnail(lines[0])
  for line in lines[1:]:
    snail_2 = CreateSnail(line)
    new_snail = AddSnails(snail_1, snail_2)
    new_snail.Reduce()
    snail_1 = new_snail
  print(f'final snail for Part 1: {snail_1}')
  print(f'magnitude: {snail_1.Magnitude()}')


if __name__ == '__main__':
  Pt1()
  Pt2()
