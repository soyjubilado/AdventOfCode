#!/usr/bin/python3
"""https://adventofcode.com/2021/day/23"""
# file created 2022-Mar-14 16:02
# $Id: prog202123.py,v 1.8 2022/11/17 16:41:32 hjew Exp hjew $
# https://adventofcode.com/2021/day/23
# Top row is goes from (0,0) to (0,WIDTH-3) aka (0,10)
# Columns are 2, 4, 6, 8, and go from 0 to DEPTH-1.

import argparse
import subprocess
import time
from heapq import heappush, heappop
from textwrap import dedent


DATA = 'data202123.txt'
# DATA = 'testdata202123.txt'
WIDTH = 13
HOME_COL = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
NO_STOPPING = set(HOME_COL.values())
COST_MULTIPLIER = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


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


def PodInTrench(pod):
  """Is a pod in a trench?"""
  return pod[0][1] != 0


def LinesToTupleSet(lines):
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
  return frozenset(state)


class State():
  """Class to define a state, defined by pod locations."""
  def __init__(self, lines=None, tuple_set=None, depth=None):

    if not tuple_set:
      self.state = LinesToTupleSet(lines)
      self.depth = len(lines) - 2
    elif not depth:
      raise Unimplemented
    else:
      self.state = frozenset(tuple_set)
      self.depth = depth
    self.width = WIDTH
    self.occupied = self.GetOccupiedDict()

  def __hash__(self):
    return hash(self.state)

  def __eq__(self, other):
    return self.state == other.state

  def __lt__(self, other):
    """There's no way to sort these."""
    return False

  def GetOccupiedDict(self):
    """Given a state, return a dict keyed on coordinates."""
    my_dict = {}
    for coord, pod in self.state:
      my_dict[coord] = pod
    return my_dict

  def PrintSelf(self, verbose=False):
    """Verify output."""
    lines = self.SelfToLines()
    print('\n'.join(lines))
    if verbose:
      print(f'depth: {self.depth}')
      print(f'width: {self.width}')

  def SelfToLines(self):
    """converts set of tuples to printable list of lines."""
    lines = []
    line1 = '#' * self.width
    lines.append(line1)

    line2 = '#'
    for x in range(0, self.width - 2):
      next_char = '.' if (x, 0) not in self.occupied else self.occupied[(x, 0)]
      line2 += next_char
    line2 += '#'
    lines.append(line2)

    # lines 3 to Depth - 2
    for y in range(1, self.depth):
      line_n = '  #'
      for x in range(2, self.width - 3):
        if x not in [2, 4, 6, 8]:
          next_char = '#'
        elif (x, y) in self.occupied:
          next_char = self.occupied[(x, y)]
        else:
          next_char = '.'
        line_n += next_char
      lines.append(line_n)

    # fix line 3
    lines[2] = lines[2].replace(' ', '#') + '##'

    lines.append('  #########')
    return lines

  def AllNextStates(self):
    """Return a dict of all the possible next states and the cost to get
       there."""
    all_next_states = {}
    for pod in self.state:
      next_states_dict = self.NextStatesForPod(pod)
      for s, cost in next_states_dict.items():
        all_next_states[s] = cost
    return all_next_states

  def NextStatesForPod(self, pod):
    """
    Args:
      pod: a single tuple, one of the ones in state

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
    state = self.state
    assert pod in state
    if (self.AlreadyHome(pod) or self.BlockedInTrench(pod) or
        self.BlockedOutside(pod) or self.ForeignersOccupyHome(pod)):
      return {}

    if PodInTrench(pod):
      return self.NextStatesFromTrench(pod)
    # else pod is on the top row, nothing blocking its path home
    return self.GoHome(pod)

  def NextStatesFromTrench(self, pod):
    """Assume pod is in trench, but not AlreadyHome(). Return a dict keyed on
    the new states that result from that particular pod moving to the top row,
    and the cost of reaching each of those states:
    {frozenset(new_state): cost_to_reach}
    """
    assert PodInTrench(pod)
    assert not self.AlreadyHome(pod)
    answer_dict = {}
    dest_cols = self.FreeColumns(pod)
    pod_col = pod[0][0]
    pod_row = pod[0][1]
    pod_type = pod[1]
    state_sans_pod = set(self.state.copy())
    state_sans_pod.remove(pod)
    for c in dest_cols:
      new_state_set = state_sans_pod.copy()
      new_state_set.add(((c, 0), pod_type))
      distance = pod_row + abs(pod_col - c)
      cost = distance * COST_MULTIPLIER[pod_type]
      answer_dict[State(tuple_set=new_state_set, depth=self.depth)] = cost
    return answer_dict

  def GoHome(self, pod):
    """Assumes the path is clear to go home.
    Args:
      pod: an amphipod ((x, y), 'Type')

    Returns:
      A dictionary with the next state as key, and the value is the cost to get
      to that state fro the current state.
    """
    depth = self.depth
    location, pod_type = pod
    x1, _ = location
    home_column = HOME_COL[pod_type]
    target_y = depth - 1
    while (home_column, target_y) in self.occupied and target_y > 0:
      target_y -= 1
    if target_y == 0:
      # target row can't be the top
      raise Exception

    distance = abs(x1 - home_column) + target_y
    cost = distance * COST_MULTIPLIER[pod_type]
    new_state_tuple_set = set(self.state.copy())
    new_state_tuple_set.remove(pod)
    new_state_tuple_set.add(((home_column, target_y), pod_type))
    return {State(tuple_set=new_state_tuple_set, depth=self.depth): cost}

  def FreeColumns(self, pod):
    """Given a pod *in a trench*, list all the columns on the top
       row that are a possible landing site."""
    state = self.state
    width = self.width
    assert pod in state
    answers = set([])
    max_index = width - 3
    pod_column = pod[0][0]
    assert pod_column in NO_STOPPING
    current = pod_column
    while (current <= max_index and (current, 0) not in self.occupied):
      if current not in NO_STOPPING:
        answers.add(current)
      current += 1
    current = pod_column
    while current >= 0 and (current, 0) not in self.occupied:
      if current not in NO_STOPPING:
        answers.add(current)
      current -= 1
    return answers

  def BlockedInTrench(self, pod):
    """True if the pod is in a trench but can't move because someone
       is in the same trench above him."""
    state = self.state
    assert pod in state
    location, _ = pod
    x, y = location
    if y == 0:
      return False
    for row in range(y-1, 0, -1):
      if (x, row) in self.occupied:
        return True
    return False

  def BlockedOutside(self, pod):
    """True if the pod is not in trench and someone is between
       him and his home trench."""
    state = self.state
    assert pod in state
    location, pod_type = pod
    x, y = location
    if y != 0: # not outside trench
      return False
    home_col = HOME_COL[pod_type]
    cols_between = NumbersBetween(home_col, x)
    for n in cols_between:
      if (n, 0) in self.occupied:
        return True
    return False

  def AlreadyHome(self, pod):
    """True if the pod is already home and no foreign pods are below."""
    state = self.state
    depth = self.depth
    assert pod in state
    location, pod_type = pod
    x, y = location
    home_col = HOME_COL[pod_type]
    if y == 0:
      return False
    if x != home_col:
      return False

    # so x is home column
    for row in range(depth-1, y-1, -1):
      occupant = self.occupied.get((x, row), pod_type)
      if occupant != pod_type:
        return False
    return True

  def ForeignersOccupyHome(self, pod):
    """True if this pod is on the top line, AND there are foreign pods in the
       home trench. That is, they are blocked from going home. If they are in
       any trench, return False becaue they are not being blocked in this
       manner."""
    state = self.state
    assert pod in state
    location, pod_type = pod
    _, y = location
    if y != 0:
      return False

    home_col = HOME_COL[pod_type]
    for row in range(self.depth-1, 0, -1):
      occupant = self.occupied.get((home_col, row), pod_type)
      if occupant != pod_type:
        return True
    return False


def GenCostDict(start_state, target_state, return_path=False):
  """Use shortest path algorithm to generate a dictionary of lowest cost to get
     to each state, and keep updating this dictionary until all the nodes
     surrounding the target have been visited.
  """
  cost_dict = {start_state: 0,}
  priority_q = [(0, start_state),]
  visited = set([])
  unvisited_target_neighbors = set(target_state.AllNextStates().keys())
  path_dict = {}

  while target_state not in visited or unvisited_target_neighbors:
    current_val, this_state = heappop(priority_q)
    if this_state in visited:
      continue
    visited.add(this_state)
    if this_state in unvisited_target_neighbors:
      unvisited_target_neighbors.remove(this_state)
    next_states_dict = {k:v for k, v in this_state.AllNextStates().items()
                        if k not in visited}
    for state, cost in next_states_dict.items():
      new_cost = current_val + cost
      if state in cost_dict and new_cost < cost_dict[state]:
        cost_dict[state] = new_cost
        path_dict[state] = this_state
      elif state not in cost_dict:
        cost_dict[state] = new_cost
        path_dict[state] = this_state
      else: # previous cost to that state was lower than current cost
        pass
      heappush(priority_q, (new_cost, state))
  # print(f'visited {len(visited)} nodes')
  if return_path:
    return cost_dict, path_dict
  return cost_dict


def TargetState(part):
  """Return target state for 'Part 1' or 'Part 2'"""
  if part == 'Part 1':
    target_lines = '''\
                   #############
                   #...........#
                   ###A#B#C#D###
                     #A#B#C#D#
                     #########'''
  elif part == 'Part 2':
    target_lines = '''\
                   #############
                   #...........#
                   ###A#B#C#D###
                     #A#B#C#D#
                     #A#B#C#D#
                     #A#B#C#D#
                     #########'''
  else:
    raise Unimplemented
  return State(dedent(target_lines).split('\n'))


def StartState(lines, part):
  """Given lines and 'Part 1' or 'Part 2' return the start state."""
  if part == 'Part 1':
    return State(lines)
  if part != 'Part 2':
    raise Unimplemented

  new_lines = lines[:3]
  new_lines.extend(["  #D#C#B#A#", "  #D#B#A#C#",])
  new_lines.extend(lines[3:])
  return State(new_lines)


def Solve(lines, part):
  """Solve Part 1 and return the answer."""
  target_state = TargetState(part)
  start_state = StartState(lines, part)
  cost_dict, path_dict = GenCostDict(start_state, target_state,
                                     return_path=True)
  return cost_dict[target_state], path_dict


def BetweenStates(start_state, end_state):
  """Given two states, return a set of all the in-between states."""
  states = []
  start_pod = [i for i in start_state.state if not i in end_state.state][0]
  end_pod = [i for i in end_state.state if not i in start_state.state][0]
  state_sans_pod = set(start_state.state)
  state_sans_pod.remove(start_pod)
  pod_type = start_pod[1]
  start_x, start_y = start_pod[0]
  end_x, end_y = end_pod[0]
  range_step = 1 if start_x < end_x else -1
  if start_y == 0:
    # do horizontal first
    for x in range(start_x, end_x, range_step):
      tuple_set = state_sans_pod.copy()
      tuple_set.add(((x, 0), pod_type))
      states.append(State(tuple_set=tuple_set, depth=start_state.depth))

    # do vertical part second
    for y in range(0, end_y):
      tuple_set = state_sans_pod.copy()
      tuple_set.add(((end_x, y), pod_type))
      states.append(State(tuple_set=tuple_set, depth=start_state.depth))
  else:
    # do vertical part first
    for y in range(start_y, 0, -1):
      tuple_set = state_sans_pod.copy()
      tuple_set.add(((start_x, y), pod_type))
      states.append(State(tuple_set=tuple_set, depth=start_state.depth))
    # horizontal part second
    for x in range(start_x, end_x, range_step):
      tuple_set = state_sans_pod.copy()
      tuple_set.add(((x, 0), pod_type))
      states.append(State(tuple_set=tuple_set, depth=start_state.depth))

  return states


def FilledStates(all_states):
  """Given a list of states, fill in the in-between states."""
  filled_states = []
  for i, s in enumerate(all_states[:-1]):
    filled_states.append(s)
    filled_states.extend(BetweenStates(s, all_states[i+1]))
  filled_states.append(all_states[-1])
  return filled_states


def Animate(path_dict, lines, part):
  """Animate the organizing of the amphipods."""
  start_state = StartState(lines, part)
  target_state = TargetState(part)
  current_state = target_state
  all_states = []
  while current_state != start_state:
    all_states.append(current_state)
    current_state = path_dict[current_state]
  all_states.append(start_state)
  all_states.reverse()
  filled_states = FilledStates(all_states)
  for s in filled_states:
    print(f'\033[1;1f', end='')
    s.PrintSelf()
    time.sleep(.1)


def main():
  """main"""
  parser = argparse.ArgumentParser()
  parser.add_argument('-2', '--part2', help='solve part 2', action='store_true')
  parser.add_argument('-a', '--animate', help='animate', action='store_true')
  args = parser.parse_args()
  lines = GetData(DATA)
  part = 'Part 2' if args.part2 else 'Part 1'

  if args.animate:
    subprocess.call('clear')
    print(f'\033[1;1f', end='')

  start_state = StartState(lines, part)
  start_state.PrintSelf()
  cost, path_dict = Solve(lines, part)

  if args.animate:
    Animate(path_dict, lines, part)

  print(f'{part}: {cost}')


if __name__ == '__main__':
  main()
