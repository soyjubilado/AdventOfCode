#!/usr/bin/python3
# file created 2022-Dec-15 20:41
"""https://adventofcode.com/2022/day/16

Volcanic tunnels and pressure release valves. I reduced the problem by looking
at only the rooms with a working valve. For the sample problem, this was six,
and for my input it was 15. The total number of paths is N!, which is
reasonable for 6 but intractable for 15. As much as possible I reduced
the number of rooms by eliminating those that would take too long to reach
from the current position.

Basic algorithm:
  * Find all the high value rooms (working valves).
  * Map all these rooms, so you know the distance from any one to any other.
  * From room AA, recursively evaluate every path, and choosing the highest
    value path.
  * The value of a room is the flow rate of the valve times the number of
    seconds left on the clock when you open that valve. Once a valve has been
    opened, the room is removed from the list of candidates.

"""

DATA = 'data202216.txt'
# DATA = 'testdata202216.txt'
NO_PATH = float('inf')


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetValveDict(lines):
  """Parse through the input lines and produce a dictionary."""
  valves = {}
  for line in lines:
    tokens = line.split()
    name = tokens[1]
    rate = int(tokens[4].replace(';', '').split('=')[1])
    lead_to = [i.replace(',', '') for i in tokens[9:]]
    valves[name] = (rate, lead_to)
  return valves


def GetTargetRooms(valve_dict):
  """Return a list of the valuable rooms. Do not include start room AA."""
  target_rooms = []
  for room, datum in valve_dict.items():
    if datum[0] > 0:
      target_rooms.append(room)
  return target_rooms


def DistanceFrom(start, target, v, valve_dict):
  """How many hops from start to target."""
  visited = v[:]
  adjacent_rooms = [i for i in valve_dict[start][1] if i not in visited]
  if target in adjacent_rooms:
    # print(f'  found {target} adjacent to {start}')
    return 1, [start, target]

  if start not in visited:
    visited.append(start)
  # print(f'  adjacent_rooms to {start}: {adjacent_rooms}')
  cheapest = NO_PATH
  path = [start]
  for r in adjacent_rooms:
    v = visited[:]
    dist, path_add = DistanceFrom(r, target, v, valve_dict)
    if dist < cheapest:
      cheapest = dist
      path += path_add
  return cheapest + 1, path


def GetMapOfTargetRooms(target_rooms, valve_dict):
  """Generate a dictionary of the distance from every target room to every
     other target room, plus from the starting room AA.
     Returns a dictionary of dictionaries.
  """
  target_rooms = target_rooms[:] + ['AA']
  target_map = {room: {} for room in target_rooms}
  while target_rooms:
    start = target_rooms.pop()
    for t in target_rooms:
      distance, _ = DistanceFrom(start, t, [], valve_dict)
      target_map[start][t] = distance
      target_map[t][start] = distance
  return target_map


def FlowRate(room, valve_dict):
  """Flow rate of a given room"""
  rate, _ = valve_dict[room]
  return rate


def MaxPathValue(start, target_rooms, target_map, valve_dict, clock):
  """Recursive function to return the max value of starting at room N with
     a given amount of time left on the clock."""
  if start in target_rooms:
    target_rooms.remove(start)

  # Remove rooms that will be useless by the time we visit them
  worthless = []
  for room in target_rooms:
    if clock + 1 <= target_map[start][room]:
      worthless.append(room)
  for room in worthless:
    target_rooms.remove(room)

  # no more time
  if not clock:
    return 0, worthless + target_rooms

  # no more rooms to visit
  if not target_rooms:
    return FlowRate(start, valve_dict) * clock, worthless

  # recursively evaluate every remaining path with the remaining time
  sub_values_and_rooms = [MaxPathValue(room, target_rooms[:],
                                       target_map, valve_dict,
                                       clock - target_map[start][room] - 1)
                          for room in target_rooms]
  best_answer = max(sub_values_and_rooms)
  sub_values, rooms = best_answer

  return sub_values + (FlowRate(start, valve_dict) * clock), worthless + rooms


def Solve(valve_dict, clock=30, rooms_left=None):
  """Default args work for Part 1. For part 2, run once with clock=26, then take
     the list of unvisited rooms and run it *again* with clock=26, and add the
     two values together."""
  target_rooms = GetTargetRooms(valve_dict) if not rooms_left else rooms_left
  target_map = GetMapOfTargetRooms(target_rooms[:], valve_dict)
  answer, rooms_left = MaxPathValue('AA', target_rooms, target_map, valve_dict,
                                    clock)
  return answer, rooms_left


def main():
  """main"""
  lines = GetData(DATA)
  valve_dict = GetValveDict(lines)
  pt1_answer, rooms_left = Solve(valve_dict)
  print(f'Part 1: {pt1_answer}, rooms left: {rooms_left}')

  pt2_answer1, rooms_left = Solve(valve_dict, clock=26)
  print(f'After 26 secs, answer = {pt2_answer1} with rooms left: {rooms_left}')
  pt2_answer2, rooms_left = Solve(valve_dict, clock=26, rooms_left=rooms_left)
  print(f'After 26 secs, answer = {pt2_answer2} with rooms left: {rooms_left}')
  print(f'Part 2: {pt2_answer1} + {pt2_answer2} = {pt2_answer1 + pt2_answer2}')


if __name__ == '__main__':
  main()
