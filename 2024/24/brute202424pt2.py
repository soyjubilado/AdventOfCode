#!/usr/bin/python3
"""Brute force code for https://adventofcode.com/2024/day/24
   This is wildly inefficient, and had to be run twice for me to get a solution
   (some wires showed up twice, and I banned them for the second run). It will
   take around 40 minutes to run on my computer (1400 Mhz AMD Ryzen, # of cores
   is irrelevant since there's no multithreading.
"""
import operator
from itertools import combinations


LOGFILE = 'log.txt'
DATA = 'data202424.txt'
# DATA = 'testdata202424.txt'


def Log(msg):
  """Log a message."""
  with open(LOGFILE, 'a') as fh:
    fh.write(msg)
    fh.write('\n')


class NoSuchTag(Exception):
  """Try to look up a tag not in the circuit."""


class NoPairFound(Exception):
  """Exhausted all the possibilities and found nothing."""


def Binary(n):
  """Return a string representing the binary version of the integer n."""
  return format(n, 'b')


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def Circuit(lines):
  """From the input lines, create a dictionary representing the circuit."""
  circuit = {}
  for l in lines:
    if ':' in l:
      k, v = l.split(':')
      circuit[k] = int(v.strip())
    elif '->' in l:
      tokens = l.split()
      circuit[tokens[-1]] = tokens[:3]
  return circuit


def Op(x):
  """Map the proper operator to the description."""
  return {'XOR': operator.xor,
          'AND': operator.and_,
          'OR': operator.or_}[x]


def EvalTag(tag, circuit):
  """Evaluate a given tag, recursively through the circuit."""
  if not tag in circuit:
    raise NoSuchTag
  if isinstance(circuit[tag], int):
    return circuit[tag]
  a, op, b = circuit[tag]
  return Op(op)(EvalTag(a, circuit), EvalTag(b, circuit))


def WiresInvolved(tag, circuit):
  """List all the wires involved in evaluating this z register."""
  if any([tag.startswith(i) for i in ['x', 'y']]):
    return [tag]
  if not tag in circuit:
    return []
  if isinstance(circuit[tag], int):
    return [tag]
  a, _, b = circuit[tag]
  return [tag] + WiresInvolved(a, circuit) + WiresInvolved(b, circuit)


def Add(x, y, circuit):
  """Use the circuit to add two binary numbers. The numbers are strings.
     eg. '1111', '0001111'.
  """
  x_items = list(reversed([int(i) for i in x]))
  y_items = list(reversed([int(i) for i in y]))
  for _ in range(45 - len(x_items)):
    x_items.append(0)
  for _ in range(45 - len(y_items)):
    y_items.append(0)
  for i in range(45):
    x = f'x{i:02}'
    y = f'y{i:02}'
    circuit[x] = x_items[i]
    circuit[y] = y_items[i]
  return Part1(circuit)


def NotXY(n):
  """True if n doesn't start with x or y."""
  return not any([n.startswith(i) for i in ['x', 'y']])


def NotXYZ(n):
  """True if n doesn't start with x or y."""
  return not any([n.startswith(i) for i in ['x', 'y', 'z']])


def N_DigitsWork(n, circuit):
  """Test addition of n digits in the circuit. Use the following tests:
     all zeros: 0 + 0 = 0
     all zeros and ones: 00000 + 11111 = 11111
     ones and zeros: 11111 + 00000 = 11111
     carry one: 1111 + 1 = 10000
  """
  testcases = [[[0, 0], 0],
               [[2**n - 1, 0], 2**n - 1],
               [[0, 2**n - 1], 2**n - 1],
               [[(2**(n-1))-1, 1], 2**(n-1)],]
  testcases = testcases[:-1] if n == 0 else testcases # special case 0

  for case, expected in testcases:
    x, y = case
    actual = Add(Binary(x), Binary(y), circuit)
    passing = 'PASS' if actual == expected else 'FAIL'
    # print(f'{passing}: {case} -> {actual} (expected {expected})')
    if passing == 'FAIL':
      return False
  return True


def Part1(circuit):
  """Part 1."""
  keys = [k for k in circuit if k.startswith('z')]
  answer_list = []
  for k in sorted(keys, reverse=True):
    answer_list.append(str(EvalTag(k, circuit)))
  return int(''.join(answer_list), 2)


def SafeToN(circuit):
  """Check where this circuit breaks."""
  n = 0
  safe_wires = set()
  while n < 46 and N_DigitsWork(n, circuit):
    # print(f'okay with n == {n}')
    zed = f'z{n:02}'
    involved = [i for i in WiresInvolved(zed, circuit) if NotXY(i)]
    new_wires = [i for i in involved if i not in safe_wires]
    safe_wires = safe_wires.union(new_wires)
    n += 1

  if n == 46:
    print('Success!')
    return 46, safe_wires, new_wires

  zed = f'z{n:02}'
  involved = [i for i in WiresInvolved(zed, circuit) if NotXY(i)]
  new_wires = [i for i in involved if i not in safe_wires]

  return n, safe_wires, new_wires


def GetSwaps(og_location, circuit):
  """Keep mutating the circuit until it goes further."""
  # In previous runs, if a tag shows up more than once, add it here
  # and re-run from the beginning.
  # forbidden = ['tfs', 'kkq']
  forbidden = []

  # The number of wires involved in the previous (good) tag should be less
  # than the correct answer for the current tag. All the previous x/y wires
  # should be there, and none of the succeding x/y wires.
  prev_involved = len(WiresInvolved(f'z{og_location - 1:02}', circuit))
  pre_x = [f'x{n:02}' for n in range(og_location + 1)]
  pre_y = [f'y{n:02}' for n in range(og_location + 1)]
  post_x = [f'x{n:02}' for n in range(og_location + 2, 47)]
  post_y = [f'y{n:02}' for n in range(og_location + 2, 47)]


  # If it were possible to shorten the list of candidates, this could be
  # way more efficient.
  candidates = [c for c in circuit if NotXY(c) and c not in forbidden]
  if og_location == 46:
    raise Exception    # shouldn't happen

  for n, c in combinations(candidates, 2):
    circuit[n], circuit[c] = circuit[c], circuit[n]
    try:
      result = SafeToN(circuit)
      involved = WiresInvolved(f'z{og_location:02}', circuit)
    except RecursionError:
      # Some bad combinations will lead to infinite recursion; keep going.
      result = [og_location]
      involved = []

    involvement_ok = len(involved) > prev_involved

    good_xy = (all(x in involved for x in pre_x) and
               all(y in involved for y in pre_y) and
               not any(x in involved for x in post_x) and
               not any(y in involved for y in post_y))

    if (not result or result[0] > og_location) and involvement_ok and good_xy:
      print(f'swapping {n} and {c} moves us forward')
      return [n, c]

    # This pair didn't work; put them back!
    circuit[n], circuit[c] = circuit[c], circuit[n]

  raise NoPairFound


def PreSwap(circuit):
  """If previous runs got you closer, pre-swapping some of the tags will
     save some time for the current run. This mutates the circuit.
  """
  # example:
  # preswap = [('frn', 'z05'), ('wnf', 'vtj'),
  #            ('z21', 'gmq'), ('wtt', 'z39')]
  preswap = []
  swaps = []
  for a, b in preswap:
    circuit[a], circuit[b] = circuit[b], circuit[a]
    swaps.extend([a, b])
  return swaps


def Part2(circuit):
  """Part 2."""
  swaps = []
  # swaps.extend(PreSwap(circuit))

  location = 0
  while location < 46:
    location, _, _ = SafeToN(circuit)
    print(f'now safe to n == {location}; swaps so far: {swaps}')
    if location == 46:
      break
    swaps.extend(GetSwaps(location, circuit))
    print(swaps)
    Log(', '.join(swaps))

  return ','.join(sorted(swaps))


def Part3(circuit):
  """There's no part 3; this is for insight and debugging."""
  for i in range(46):
    involved = WiresInvolved(f"z{i:02}", circuit)
    print(f'{i}: {WiresInvolved(f"z{i:02}", circuit)}')
    pre_x = [f'x{n:02}' for n in range(i + 1)]
    pre_y = [f'y{n:02}' for n in range(i + 1)]
    post_x = [f'x{n:02}' for n in range(i + 2, 47)]
    post_y = [f'y{n:02}' for n in range(i + 2, 47)]
    good_xy = (all(x in involved for x in pre_x) and
               all(y in involved for y in pre_y) and
               not any(x in involved for x in post_x) and
               not any(y in involved for y in post_y))
    print(f'    pre_x: {pre_x}')
    print(f'    pre_y: {pre_y}')
    print(f'    post_x: {post_x}')
    print(f'    post_y: {post_y}')
    print(f'    good_xy: {good_xy}')


def main():
  """main"""
  lines = GetData(DATA)
  circuit = Circuit(lines)
  # print(f'Part 1: {Part1(circuit.copy())}')
  print(f'Part 2: {Part2(circuit.copy())}')
  # print(f'Part 3: {Part3(circuit.copy())}')


if __name__ == '__main__':
  main()
