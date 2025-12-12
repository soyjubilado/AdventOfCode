#!/usr/bin/python3
# file created 2025-Dec-11 13:41
"""https://adventofcode.com/2025/day/11"""

from functools import lru_cache
DATA = 'data202511.txt'
# DATA = 'testdata202511.txt'


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


def PrintDict(my_dict):
  """Pretty print a dictionary."""
  print("\n".join([f'{k}: {v}' for k, v in my_dict.items()]))


def PathsToYou(og_ways_to_dict):
  """Closure to recursively find all the paths to 'you'."""

  ways_to_dict = og_ways_to_dict.copy()

  @lru_cache(maxsize=None)
  def PathsInnerFunc(device):
    """Inner function of closure."""
    if 'you' in ways_to_dict[device]:
      return 1
    if not ways_to_dict[device]:
      return 0
    return sum([PathsInnerFunc(i) for i in ways_to_dict[device]])

  return PathsInnerFunc


def Part1(device_dict):
  """Part 1."""
  ways_to_dict = WaysToDict(device_dict)
  return PathsToYou(ways_to_dict)('out')


def Part2(_lines):
  """Part 2."""
  return None


def main():
  """main"""
  lines = GetData(DATA)
  device_dict = DeviceDict(lines)
  print(f'Part 1: {Part1(device_dict)}')
  # print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
