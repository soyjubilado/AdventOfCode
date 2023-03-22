#!/usr/bin/python3
"""https://adventofcode.com/2021/day/23"""
# file created 2022-Mar-14 16:02
# $Id: prog202123.py,v 1.8 2022/11/17 16:41:32 hjew Exp hjew $
# https://adventofcode.com/2021/day/23
# Top row is goes from (0,0) to (0,WIDTH-3) aka (0,10)
# Columns are 2, 4, 6, 8, and go from 0 to DEPTH-1.


DATA = 'data202123.txt'
#DATA = 'testdata202123.txt'

DEPTH = 3
WIDTH = 13
HOME_COL = {'A': 2, 'B': 4, 'C': 6, 'D': 8}


class Unimplemented(Exception):
  """Unimplemented feature."""


def GetData(datafile):
  """Return input data as a list of strings."""
  lines = []
  with open(datafile, 'r') as fh:
    # lines = [i.replace('\n', '').replace(' ', '#') for i in fh]
    lines = [i.rstrip() for i in fh]
  return lines


def NumbersBetween(a, b):
  """Return a list of numbers between a and b, exclusive."""
  if a == b:
    return []
  if a > b:
    a, b = b, a
  return list(range(a + 1, b))


def LinesToState(lines):
  """converts ascii lines to a set of tuples of occupied spaces.
  Args:
    lines: a list of strings
  Returns:
    state: a set of tuples {((x1,y1), 'A'), (x2,y2), 'B'), ...}
  """
  state = set({})
  for y, row_str in enumerate(lines):
    for x, char in enumerate(row_str):
      if char in HOME_COL:
        state.add(((x-1, y-1), char))
  return state


def StateToLines(state, depth=DEPTH, width=WIDTH):
  """converts set of tuples to printable list of lines."""
  occupied = dict(state)
  lines = []
  line1 = '#' * width
  lines.append(line1)

  line2 = '#'
  for x in range(1, width-1):
    next_char = '.' if (x, 0) not in occupied else occupied[(x, 0)]
    line2 += next_char
  line2 += '#'
  lines.append(line2)

  # lines 3 to Depth - 2
  for y in range(1, depth):
    line_n = '  #'
    for x in range(2, width - 3):
      if x not in [2, 4, 6, 8]:
        next_char = '#'
      elif (x, y) in occupied:
        next_char = occupied[(x, y)]
      else:
        next_char = '.'
      line_n += next_char
    lines.append(line_n)

  # fix line 3
  lines[2] = lines[2].replace(' ', '#') + '##'

  lines.append('  #########')
  return lines


def NextStatesForPod(pod, state, depth=DEPTH):
  """
  Args:
    pod: a single tuple, one of the ones in state
    state: set of tuples {((1,2), 'A'), ((2,2), 'B'), ...}

  Returns:
    a dictionary of states: {next_state: cost}
      next_state: set of tuples (like state)
      cost: int

  Return empty set early if:
    * pod is already home. (AlreadyHome)
    * pod is not home, but a foreigner is home. (ForeignersOccupyHome)
    * pod is in a trench, but there's someone above it. (BlockedInTrench)
    * pod is not home, but can't reach trench. (BlockedOutside)
  """
  assert pod in state
  if (AlreadyHome(pod, state) or BlockedInTrench(pod, state) or
      BlockedOutside(pod, state)) or ForeignersOccupyHome(pod, state):
    return {}

  if PodInTrench(pod):
    raise Unimplemented
  else:
    raise Unimplemented


def PodInTrench(pod):
  """Is a pod in a trench?"""
  coords, _ = pod
  _, y = coords
  return y != 0


def BlockedInTrench(pod, state):
  """
  Args:
    pod: a single tuple, one of the ones in state
    state: set of tuples {((1,2), 'A'), ((2,2), 'B'), ...}

  Returns:
    boolean: True if the pod is in a trench but can't move because someone
             is in the same trench above him.
  """
  assert pod in state
  occupied_dict = GetOccupiedDict(state)
  location, _ = pod
  x, y = location
  if y == 0:
    return False
  for row in range(y-1, 0, -1):
    if (x, row) in occupied_dict:
      return True
  return False


def BlockedOutside(pod, state):
  """
  Args:
    pod: a single tuple, one of the ones in state
    state: set of tuples {((1,2), 'A'), ((2,2), 'B'), ...}

  Returns:
    boolean: True if the pod is not in trench and someone is between
             him and his home trench.

  Status of this function: untested
  """
  assert pod in state
  occupied_dict = GetOccupiedDict(state)
  location, pod_type = pod
  x, y = location
  if y != 0: # not outside trench
    return False
  home_col = HOME_COL[pod_type]
  cols_between = NumbersBetween(home_col, x)
  for n in cols_between:
    if (n, 0) in occupied_dict:
      return True
  return False


def AlreadyHome(pod, state, depth=DEPTH):
  """
  Args:
    pod: a single tuple, one of the ones in state
    state: set of tuples {((1,2), 'A'), ((2,2), 'B'), ...}

  Returns:
    boolean: True if the pod is already home and no foreign pods are below.
  """
  assert pod in state
  occupied_dict = GetOccupiedDict(state)
  location, pod_type = pod
  x, y = location
  home_col = HOME_COL[pod_type]
  if y == 0:
    return False
  if x != home_col:
    return False

  # so x is home column
  for row in range(depth-1, y-1, -1):
    occupant = occupied_dict.get((x, row), pod_type)
    # print(f'({x}, {row}): {occupant}')
    if occupant != pod_type:
      return False
  return True


def ForeignersOccupyHome(pod, state, depth=DEPTH):
  """
  Args:
    pod: a single tuple, one of the ones in state
    state: set of tuples {((1,2), 'A'), ((2,2), 'B'), ...}

  Returns:
    boolean: True if this pod is on the top line, AND there are foreign
             pods in the home trench. That is, they are blocked from
             going home. If they are in any trench, return False
             becaue they are not being blocked in this manner.
  """
  assert pod in state
  occupied_dict = GetOccupiedDict(state)
  location, pod_type = pod
  _, y = location
  if y != 0:
    return False

  home_col = HOME_COL[pod_type]
  for row in range(depth-1, 0, -1):
    occupant = occupied_dict.get((home_col, row), pod_type)
    if occupant != pod_type:
      return True
  return False


def GetOccupiedDict(state):
  """Given a state, return a dict keyed on coordinates."""
  my_dict = {}
  for coord, pod in state:
    my_dict[coord] = pod
  return my_dict


def PrintLines(lines, depth=DEPTH, width=WIDTH):
  """Verify output."""
  print('\n'.join(lines))
  print(f'depth: {depth}')
  print(f'width: {width}')


def main():
  """main"""
  lines = GetData(DATA)
  global DEPTH
  DEPTH = len(lines) - 2
  PrintLines(lines)
  state = LinesToState(lines)
  # for k,v in sorted(state):
    # print(f'  {k}: {v}')
  for s in sorted(state):
    print(s)
  lines_redux = StateToLines(state)
  PrintLines(lines_redux)


if __name__ == '__main__':
  main()