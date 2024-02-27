#!/usr/bin/python3
# file created 2024-Feb-25 08:09
# part one finished: 08:35
"""https://adventofcode.com/2023/day/14"""

from grid import GridWrap, MinMaxXY

DATA = 'data202314.txt'
# DATA = 'testdata202314.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def SlideRocks(grid, coords_list):
  """Given a grid and list of coordinates representing a row or column, from
     top to bottom or vice versa, or left to right or vice versa, slide all
     the rocks toward the origin."""
  for idx in range(len(coords_list)):
    orig = current = idx
    prev = idx-1
    if grid[coords_list[current]] != 'O':
      continue
    while prev >= 0 and grid[coords_list[prev]] == '.':
      current = prev
      prev -= 1
    if current != orig:
      grid[coords_list[current]] = 'O'
      grid[coords_list[orig]] = '.'
  return grid


def SlideNorth(grid):
  """Tilt north, all rocks slide to top."""
  _, max_x, _, max_y = MinMaxXY(grid)
  for x in range(max_x + 1):
    coords = [(x, y) for y in range(max_y + 1)]
    SlideRocks(grid, coords)
  return grid


def SlideWest(grid):
  """Tilt west, all rocks slide to left."""
  _, max_x, _, max_y = MinMaxXY(grid)
  for y in range(max_y + 1):
    coords = [(x, y) for x in range(max_x + 1)]
    SlideRocks(grid, coords)


def SlideSouth(grid):
  """Tilt south, all rocks slide to bottom."""
  _, max_x, _, max_y = MinMaxXY(grid)
  for x in range(max_x + 1):
    coords = [(x, y) for y in range(max_y, -1, -1)]
    SlideRocks(grid, coords)


def SlideEast(grid):
  """Tilt east, all rocks slide to right."""
  _, max_x, _, max_y = MinMaxXY(grid)
  for y in range(max_y + 1):
    coords = [(x, y) for x in range(max_x, -1, -1)]
    SlideRocks(grid, coords)


def Load(grid):
  """Sum of y distance to bottom for round rocks (O)"""
  _, _, _, max_y = MinMaxXY(grid)
  max_load = max_y + 1
  return sum([max_load - y for x, y in grid if grid[(x, y)] == 'O'])


def Part1(grid):
  """Part 1."""
  SlideNorth(grid)
  return Load(grid)


def RunOneCycle(grid):
  """Slide once north, west, south, east."""
  SlideNorth(grid)
  SlideWest(grid)
  SlideSouth(grid)
  SlideEast(grid)


def GuessCycleLength(loads):
  """Given a list of loads, guess the cycle length. Take the last 10 values in
     the list, find the previous occurrence in the list, and take the difference
     of the indices. This is a guess. Collect all the guesses and return the
     largest one.
  """
  indices = range(-1, -11, -1)
  guesses = []
  for i in indices:
    load_indices = [idx for idx, val in enumerate(loads) if val == loads[i]]
    guesses.append(load_indices[-1] - load_indices[-2])
  print(f'cycle length guesses: {guesses}')
  return max(guesses)


def FindCycle(grid, tilt_cycles=300):
  """Return an offset and a cycle."""
  loads = [0,]

  # generate a list of 300 loads, indexed on how many tilt cycles were run.
  # loads[1] is the load after one tilt cycle, loads[2] after 2, etc.
  for i in range(tilt_cycles):
    print(i, end=' ', flush=True)
    RunOneCycle(grid)
    loads.append(Load(grid))
  print()
  cycle_length = GuessCycleLength(loads)

  print(f'assuming a cycle length of {cycle_length}')
  some_value = loads[-1]
  prev_idx = loads.index(some_value)
  print(f'first index of {some_value} is {prev_idx}')

  # find where the values start to repeat every cycle_length times
  for idx, val in enumerate(loads):
    if val == some_value:
      if idx - prev_idx == cycle_length:
        cycle_start = idx
        print(f'cycle starts at index {cycle_start}')
        break
      prev_idx = idx

  return cycle_start, loads[cycle_start:cycle_start + cycle_length]


def Part2(grid):
  """Part 2"""
  offset, cycle = FindCycle(grid)
  print(f'{offset=}, {cycle=}')
  idx = (1000000000 - offset) % len(cycle)
  return cycle[idx]


def main():
  """main"""
  lines = GetData(DATA)
  grid = GridWrap(lines)
  print(f'Part 1: {Part1(grid)}')
  print(f'Part 2: {Part2(grid)}')


if __name__ == '__main__':
  main()
