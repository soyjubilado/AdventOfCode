#!/usr/bin/python3
#file created 2021-Dec-16 20:54
"""https://adventofcode.com/2021/day/17"""

"""
Max starting vx will put x at edge of target area on first shot + 1: 222
Min starting vx is 0
Max starting vy is the one that puts it at the highest trajectory + 1: 122
Min starting vy will put y at lower boundary of target area (negative): -123
Max steps is around 244.

For both x and y, build a dictionary of the starting velocities and which steps
of that trajectory will land in the target area.

  {vx: [steps in target]}
  {vy: [steps in target]}

Reverse the dictionary for both (make a new dictionary keyed on the values).

For each step that is common to both dictionaries, the cartesian product of
those two lists are all valid starting velocities. NOTE: this may result in
some duplicates.

For example, if a trajectory has the torpedo in the target area at step
six for starting velocities vx in [2, 3] and vy in [4, 5], then the starting
velocities (2, 4), (2, 5), (3, 4), (3, 5) are all valid starting points.

The hardest part of this program was choosing the ranges to iterate over.

"""

from collections import defaultdict
from itertools import product


def StepsInTarget_X(vx, target_x, max_steps=250):
  """returns a list of what steps during which torpedo is in target area."""
  x_min, x_max = target_x
  x = 0
  in_target = []
  step = 0
  while x < x_max and step < max_steps:
    step += 1
    x += vx
    vx = vx - 1 if vx > 0 else 0
    if x >= x_min and x <= x_max:
      in_target.append(step)
  return in_target


def StepsInTarget_Y(vy, target_y):
  """returns a list of what steps during which torpedo is in target area."""
  y_min, y_max = target_y
  y = 0
  in_target = []
  step = 0
  while y > y_min:
    step += 1
    y += vy
    vy -= 1
    if y <= y_max and y >= y_min:
      in_target.append(step)
  return in_target


def TrajectoryHitsY(vy, target):
  y_min, y_max = target
  y = 0
  peak = 0
  while y > y_max:
    y += vy
    if y > peak:
      peak = y
    vy -= 1
  if y >= y_min:
    # print(f'landing y: {y}')
    return True, peak
  return False, peak


def Part1():
  target = (-10, -5)
  # target = (-122, -74)
  peakpeak = 0
  num_tries = 1000
  for vy in range(num_tries):
    hits, peak = TrajectoryHitsY(vy, target)
    if hits:
      peakpeak = peak
      print(f'{vy}: Peak={peak}')
  print(f'after {num_tries} tries largest peak seen is {peakpeak}')


def InvertDict(steps_for_n):
  """Given a dictionary starting velocities and number of steps in target,
     return a dictionary of number of steps in target and starting velocities"""
  inverted_d = defaultdict(lambda: [])
  for v in steps_for_n:
    for step in steps_for_n[v]:
      inverted_d[step].append(v)
  return inverted_d


def Part2():
  # target format (min, max)

  target_y = (-10, -5) # test
  target_x = (20, 30) # test

  target_y = (-122, -74)
  target_x = (185, 221)

  x_start_range = 0
  x_end_range = target_x[1] + 6
  y_start_range = target_y[0] - 6

  # Max starting velocity determined from part 1
  # This will be around abs(target_y[0]) or a little higher.
  y_end_range = abs(y_start_range)

  steps_for_vy = {}
  for vy in range(y_start_range, y_end_range):
    steps_for_vy[vy] = StepsInTarget_Y(vy, target_y)

  vy_steps = InvertDict(steps_for_vy)

  steps_for_vx = {}
  for vx in range(x_start_range, x_end_range):
    steps_for_vx[vx] = StepsInTarget_X(vx, target_x)

  vx_steps = InvertDict(steps_for_vx)

  accumulate = 0
  velocities = []
  for step in vy_steps:
    if step in vx_steps:
      velocities.extend(product(vx_steps[step], vy_steps[step]))

  print(len(set(velocities)))


if __name__ == '__main__':
  Part2()
