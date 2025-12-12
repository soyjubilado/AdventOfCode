#!/usr/bin/python3
# file created 2025-Dec-11 13:41
"""https://adventofcode.com/2025/day/11"""

from functools import lru_cache
DATA = 'data202511.txt'
# DATA = 'testdata202511_a.txt'
# DATA = 'testdata202511_b.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def DeviceDict(lines):
  """Parse input into a dictionary of devices."""
  my_dict = {}
  for line in lines:
    k, devs = line.split(':')
    my_dict[k] = devs.strip().split()
  return my_dict


def WaysToDict(device_dict):
  """Basically a reverse of device_dict: for each device, which other
     devices point to it. Adds device 'out' at the end."""

  all_keys = device_dict.keys()
  my_dict = {k: [] for k in all_keys}
  for k in all_keys:
    other_keys = [kk for kk in all_keys if kk != k]
    for ok in other_keys:
      if k in device_dict[ok]:
        my_dict[k].append(ok)
  my_dict['out'] = [k for k in all_keys if 'out' in device_dict[k]]
  return my_dict


def PathsToStart(og_ways_to_dict, start_pt, req1, req2):
  """Closure to recursively find all the paths to start_pt. If req1
     and req2 are given, require the paths to go through them."""

  ways_to_dict = og_ways_to_dict.copy()
  check1 = check2 = lambda x: True

  if req1:
    check1 = lambda dev: dev == req1
  if req2:
    check2 = lambda dev: dev == req2

  @lru_cache(maxsize=None)
  def PathsInnerFunc(device, seen1=False, seen2=False):
    """Inner function of closure."""
    seen1 = seen1 or check1(device)
    seen2 = seen2 or check2(device)

    if start_pt in ways_to_dict[device]:
      if seen1 and seen2:
        return 1
      return 0

    if not ways_to_dict[device]:
      return 0

    return sum([PathsInnerFunc(i, seen1, seen2) for i in ways_to_dict[device]])

  return PathsInnerFunc


def Part1(device_dict):
  """Part 1."""
  ways_to_dict = WaysToDict(device_dict)
  return PathsToStart(ways_to_dict, 'you', '', '')('out')


def Part2(device_dict):
  """Part 2."""
  ways_to_dict = WaysToDict(device_dict)
  return PathsToStart(ways_to_dict, 'svr', 'fft', 'dac')('out')


def main():
  """main"""
  lines = GetData(DATA)
  device_dict = DeviceDict(lines)
  print(f'Part 1: {Part1(device_dict)}')
  print(f'Part 2: {Part2(device_dict)}')


if __name__ == '__main__':
  main()
