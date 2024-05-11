#!/usr/bin/python3
#file created 2021-Dec-21 21:11
"""https://adventofcode.com/2021/day/22

Algorithm for part 2:

For every new cuboid:
  If it intersects with an existing cuboid, break up the existing one.
  If it is "on" then keep it.
  If it is "off" then discard it.

Breaking up cuboids:
  Return a list of cuboids.
  Break along the x-axis, then the y-axis, then the z-axis.
"""

DATA = 'data202122.txt'
# DATA = 'testdata202122.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


class Cuboid(object):
  def __init__(self, x1, x2, y1, y2, z1, z2):
    for i in [x1, x2, y1, y2, z1, z2]:
      assert isinstance(i, int)
    self.x1 = min(x1, x2)
    self.x2 = max(x1, x2)
    self.y1 = min(y1, y2)
    self.y2 = max(y1, y2)
    self.z1 = min(z1, z2)
    self.z2 = max(z1, z2)

  def Intersects(self, other):
    if (self.x2 < other.x1 or
        self.x1 > other.x2 or
        self.y2 < other.y1 or
        self.y1 > other.y2 or
        self.z2 < other.z1 or
        self.z1 > other.z2):
      return False
    return True

  def Cleave(self, other):
    """Cleave self into sub-cuboids that don't intersect with other.
    Returns a list of up to 6 cuboids.
    """
    assert self.Intersects(other)
    retval = []

    x1 = self.x1
    x2 = self.x2
    y1 = self.y1
    y2 = self.y2
    z1 = self.z1
    z2 = self.z2
    if  x1 < other.x1 <= x2:
      retval.append(Cuboid(x1, other.x1 - 1, y1, y2, z1, z2))
      x1 = other.x1
    if x1 <= other.x2 < x2:
      retval.append(Cuboid(other.x2 + 1, x2, y1, y2, z1, z2))
      x2 = other.x2
    if  y1 < other.y1 <= y2:
      retval.append(Cuboid(x1, x2, y1, other.y1 - 1, z1, z2))
      y1 = other.y1
    if y1 <= other.y2 < y2:
      retval.append(Cuboid(x1, x2, other.y2 + 1, y2, z1, z2))
      y2 = other.y2
    if z1 < other.z1 <= z2:
      retval.append(Cuboid(x1, x2, y1, y2, z1, other.z1 - 1))
      z1 = other.z1
    if z1 <= other.z2 < z2:
      retval.append(Cuboid(x1, x2, y1, y2, other.z2 + 1, z2))
      z2 = other.z2
    return retval

  def Volume(self):
    """This is not really volume. Intentionally off by 1 in every axis."""
    return ((self.x2 - self.x1 + 1) *
            (self.y2 - self.y1 + 1) *
            (self.z2 - self.z1 + 1))

  def __str__(self):
    return (f'x({self.x1}..{self.x2}) '
            f'y({self.y1}..{self.y2}) '
            f'z({self.z1}..{self.z2})')


class RebootStep(object):

  def __init__(self, on_off, cuboid):
    self.on_off = on_off
    self.cuboid = cuboid

  def __str__(self):
    return f'{self.on_off}: {self.cuboid.__str__()}'


def LinesToInstructions(lines):
  instructions = []
  for line in lines:
    instr, coords = line.split()
    x_str, y_str, z_str = coords.split(',')
    x1, x2 = x_str.split('=')[1].split('..')
    y1, y2 = y_str.split('=')[1].split('..')
    z1, z2 = z_str.split('=')[1].split('..')
    cuboid = Cuboid(int(x1), int(x2), int(y1), int(y2), int(z1), int(z2))
    instructions.append(RebootStep(instr, cuboid))
  return instructions


def testCuboids():
  cu1 = Cuboid(-3, 3, -3, 3, -3, 3)
  cu2 = Cuboid(-2, 2, -2, 2, -2, 2)
  cu3 = Cuboid(-6, -4, -3, 3, -3, 3)
  cu4 = Cuboid(-6, -3, -3, 3, -3, 3)

  testcases = [[cu1, cu2, True],
               [cu2, cu1, True],
               [cu2, cu3, False],
               [cu3, cu2, False],
               [cu3, cu1, False],
               [cu1, cu3, False],
               [cu3, cu4, True],
               [cu4, cu3, True],
              ]
  for c_a, c_b, expected in testcases:
    actual = c_a.Intersects(c_b)
    passing = 'pass' if actual == expected else 'fail'
    print(f'{passing}: {c_a} intersects {c_b}? {actual} (expect {expected})')


def testCleave():
  cu1 = Cuboid(-3, 3, -3, 3, -3, 3)
  cu2 = Cuboid(-2, 2, -2, 2, -2, 2)
  print(f'cu1: {cu1}, volume: {cu1.Volume()}')
  print(f'cu2: {cu2}, volume: {cu2.Volume()}')
  cloven = cu1.Cleave(cu2)
  for c in cloven:
    print(f'  {c}, volume: {c.Volume()}')
  print(f'  sum: {sum([c.Volume() for c in cloven])}')


def ApplyRebootSteps(reboot_steps):
  cuboid_list = []

  for step in reboot_steps:
    # print(f'step: {step}')
    # save a list of the cuboids you remove later so we do not remove cuboids
    # as we are iterating through the list.
    removeables = []

    for c in cuboid_list:
      if c.Intersects(step.cuboid):
        removeables.append(c)
        cloven = c.Cleave(step.cuboid)
        cuboid_list.extend(cloven)

    for r in removeables:
      cuboid_list.remove(r)

    if step.on_off == 'on':
      cuboid_list.append(step.cuboid)

  return sum([c.Volume() for c in cuboid_list])
  


def main():
  lines = GetData(DATA)
  reboot_steps = LinesToInstructions(lines)

  reboot_area = Cuboid(-50, 50, -50, 50, -50, 50)
  pt1_steps = [s for s in reboot_steps if s.cuboid.Intersects(reboot_area)]

  cubes_on_pt_1 = ApplyRebootSteps(pt1_steps)
  cubes_on_pt_2 = ApplyRebootSteps(reboot_steps)
  print(f'Part 1 answer: {cubes_on_pt_1}')
  print(f'Part 2 answer: {cubes_on_pt_2}')


if __name__ == '__main__':
  main()
