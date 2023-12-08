#!/usr/bin/python3
# file created 2023-Dec-07 20:59
"""https://adventofcode.com/2023/day/8"""

from factor import factors
DATA = 'data202308.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetElementDict(lines):
  """Given lines 2-end, return a dictionary representing the element map."""
  the_dict = {}
  for l in lines:
    key, lr = l.split('=')
    left = lr.split(',')[0].replace('(', '')
    right = lr.split(',')[1].replace(')', '')
    the_dict[key.strip()] = (left.strip(), right.strip())
  return the_dict


def Directions(directions):
  """Iterator to give the next direction, repeating infinitely.
     Yields 0 for left and 1 for right, to allow indexing into the tuple.
  """
  num_items = len(directions)
  i = -1
  while True:
    i = (i + 1) % num_items
    yield 0 if directions[i] == 'L' else 1


def CyclesToZ(start, end_str, element_dict, direction_data):
  """Count steps to get from start to end.
  Args:
    start: (str) starting element.
    end_str: (str) what the target element ends with.
    element_dict: dictionary of elements and transitions.
    direction_data: first line of the data file.

  Returns:
    counter: number of steps
    element: full name of the ending element
  """
  direction = Directions(direction_data)
  counter = 0
  left_or_right = next(direction)
  element = start
  while not element.endswith(end_str):
    counter += 1
    next_element = element_dict[element][left_or_right]
    element = next_element
    left_or_right = next(direction)
  return counter, element


def LeastCommonFactor(a, b):
  """Least common factor of a and b."""
  if a < b:
    a, b = b, a
  if not a % b:
    return b
  return LeastCommonFactor(b, a % b)


def LeastCommonMultiple(a, b):
  """Least common multiple of a and b."""
  lcf = LeastCommonFactor(a, b)
  return (a * b)//lcf


def Part1(lines):
  """Part 1"""
  direction_data = lines[0]
  element_dict = GetElementDict(lines[2:])
  start = 'AAA'
  end_str = 'ZZZ'
  counter, _ = CyclesToZ(start, end_str, element_dict, direction_data)
  return counter


def Part2(lines):
  """The LCM solution only works due to easy input for this problem.
     This is not a general solution."""
  direction_data = lines[0]
  element_dict = GetElementDict(lines[2:])
  start_elements = [i for i in element_dict if i.endswith('A')]
  end_str = 'Z'
  running_lcm = 1
  for s in start_elements:
    counter, end = CyclesToZ(s, end_str, element_dict, direction_data)
    print(f'{s} -> {end} in {counter}')
    print(f'    {counter} factors to: {factors(int(counter))}')
    running_lcm = LeastCommonMultiple(running_lcm, counter)
  return running_lcm


def main():
  """main"""
  lines = GetData(DATA)
  print(f'part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
