#!/usr/bin/python3
# file created 2025-Dec-10 08:25
"""https://adventofcode.com/2025/day/10"""

from functools import lru_cache
from itertools import combinations
from math import inf as INFINITY

DATA = 'data202510.txt'
# DATA = 'testdata202510.txt'


class Impossible(Exception):
  """Problem can't be solved."""


class Machine():
  """An elf machine has lights, buttons, joltages."""

  def __init__(self, lights, buttons, joltages):
    self.lights = lights
    self.buttons = buttons
    self.joltages = joltages

  def __str__(self):
    return f'[{self.lights}] {self.buttons} {self.joltages}'


  def min_lights(self):
    """Minimum buttons to achieve light pattern."""
    og_start = ['.' for _ in self.lights]
    for i in range(1, len(self.buttons)):
      for combo in combinations(self.buttons, i):
        if ToggleAllLights(og_start, combo) == self.lights:
          return combo
    raise Impossible

  def min_joltage(self):
    """Min number of buttons to achieve joltage pattern."""
    start = tuple([0 for _ in self.joltages])
    return MashButtons(start, self.joltages, self.buttons)


@lru_cache(maxsize=None)
def MashButtons(current_j, target_j, buttons):
  for b in buttons:
    if ApplyButton(current_j, b) == target_j:
      return 1

  exceeders = [b for b in buttons if ExceedTarget(current_j, target_j, b)]
  non_exceeders = tuple([b for b in buttons if b not in exceeders])
  if not non_exceeders:
    return INFINITY

  next_round = []
  for b in non_exceeders:
    next_current = ApplyButton(current_j, b)
    # print(next_current)
    next_round.append(MashButtons(next_current, target_j, non_exceeders))

  return 1 + min(next_round)


@lru_cache(maxsize=None)
def ExceedTarget(current, target, button):
  next_jolt = ApplyButton(current, button)
  for i in range(len(target)):
    if next_jolt[i] > target[i]:
      return True
  return False


@lru_cache(maxsize=None)
def ApplyButton(current_j, button):
  joltage = [i for i in current_j]
  for idx in button:
    joltage[idx] += 1
  return tuple(joltage)


def ToggleLights(og_lights, button):
  """Apply this one button to these lights."""
  light = og_lights[:]
  for idx in button:
    light[idx] = '.' if light[idx] == '#' else '#'
  return light


def ToggleAllLights(og_lights, buttons):
  """Apply all buttons to these lights."""
  lights = og_lights[:]
  for b in buttons:
    lights = ToggleLights(lights, b)
  return lights


def GetData(datafile):
  """Read input into a list of lines."""
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def tokens_to_buttons(tokens):
  """Convert middle part of string input to button tuples."""
  tokens = [i[1:-1] for i in tokens]
  buttons = tuple([tuple(int(i) for i in t.split(',')) for t in tokens])
  return buttons


def lights_buttons_joltage(line):
  """parse input string into lights, buttons, joltages."""
  tokens = line.split()
  lights = list(tokens[0][1:-1])
  buttons = tokens_to_buttons(tokens[1:-1])
  joltages = tuple([int(i) for i in tokens[-1][1:-1].split(',')])

  return Machine(lights, buttons, joltages)


def Part1(machines):
  """Part 1."""
  return sum([len(m.min_lights()) for m in machines])


def ReportReduction(mach):
  """Report whether joltage can be reduced."""
  len_joltage = len(mach.joltages)
  indices = {i: 0 for i in range(len_joltage)}
  for b in mach.buttons:
    for i in b:
      indices[i] += 1
  solos = [i for i, v in indices.items() if v==1]
  if not solos:
    print(f'Not reducible: {mach}')
  else:
    print(f'Reducible: {mach}')
    for i in solos:
      print(f'button: {[b for b in mach.buttons if i in b]}')
  print(indices)
  print('------------------------')
  

def Part2(machines):
  """Part 2."""
  for m in machines:
    ReportReduction(m)
  """
  total = 0
  for m in machines:
    joltage = m.min_joltage()
    print(f'{m}: {joltage}')
    total += joltage
  return total
  """


def main():
  """main"""
  lines = GetData(DATA)
  machines = [lights_buttons_joltage(line) for line in lines]
  print(f'Part 1: {Part1(machines)}')
  print(f'Part 2: {Part2(machines)}')


if __name__ == '__main__':
  main()
