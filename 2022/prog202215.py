#!/usr/bin/python3
# file created 2022-Dec-14 21:02
"""https://adventofcode.com/2022/day/15"""

DATA = 'data202215.txt'
# DATA = 'testdata202215.txt'


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetSensorsAndBeacons(lines):
  """Marshall the input lines into a list of tuples comprised of
     sensor and beacon coordinates."""
  sensors_beacons = []
  for line in lines:
    tokens = line.replace('=', ' ').replace(':', ' ').replace(',', ' ').split()
    s_x, s_y = int(tokens[3]), int(tokens[5])
    b_x, b_y = int(tokens[-3]), int(tokens[-1])
    sensors_beacons.append(((s_x, s_y), (b_x, b_y)))
  return sensors_beacons


def ManhattanDistance(pt1, pt2):
  """Return the Manhattan distance between two points."""
  x1, y1 = pt1
  x2, y2 = pt2
  return abs(x2 - x1) + abs(y2 - y1)


def TargetSegmentInclusive(sensor, target_row, distance):
  """Given a sensor, a target row, and the manhattan distance to the nearest
     beacon, return a sgment (start, finish) on the target row where a sensor
     cannot be. Segments are inclusive, so include both ends."""
  x, y = sensor
  remainder = distance - abs(target_row - y)
  if remainder < 0:
    return None
  start = x - remainder
  end = x + remainder
  return start, end


def SegmentsInTargetRow(sensors_and_beacons, target_row):
  """Given a list of sensors and their closest beacons, and a target row,
     return a list of segments on that target row where a beacon cannot be."""
  segments = []
  for sensor, beacon in sensors_and_beacons:
    distance = ManhattanDistance(sensor, beacon)
    sub_segment = TargetSegmentInclusive(sensor, target_row, distance)
    if sub_segment:
      segments.append(sub_segment)
  return sorted(segments)


def OverlapAtAll(first, second) -> bool:
  """The two ranges overlap at least partially."""
  one_s, one_f = first
  two_s, two_f = second
  return (one_s <= two_s <= one_f or
          one_s <= two_f <= one_f or
          two_s <= one_s <= two_f or
          two_s <= one_f <= two_f)


def MergeSegments(segments):
  """Given a sorted list of segments, merge as many as possible and return
     the hopefully smaller list of segments."""
  merged = []
  if len(segments) <= 1:
    return segments[:]
  current = segments[0]
  for next_seg in segments[1:]:
    if not OverlapAtAll(current, next_seg):
      merged.append(current)
      current = next_seg
    else:
      current = (min(current[0], next_seg[0]), max(current[1], next_seg[1]))
  merged.append(current)
  return merged


def Part1(sensors_and_beacons):
  """Number of impossible beacon locations on the target row."""
  target_row = 10 if DATA == 'testdata202215.txt' else 2000000
  segments = SegmentsInTargetRow(sensors_and_beacons, target_row)
  merged = MergeSegments(segments)
  num_points = sum([abs(b - a) + 1 for a, b in merged])
  beacons_in_row = [b for s, b in sensors_and_beacons if b[1] == target_row]
  answer = num_points - len(set(beacons_in_row))
  print(f'Part 1: {answer}')


def FoundX(segments, max_dimension):
  """For part 2, find a segment that starts inside the target range."""
  for segment in segments:
    segment_start = segment[0]
    if segment_start <= 0:
      continue
    if segment_start < max_dimension:
      return segment_start - 1
  return None


def Part2(sensors_and_beacons):
  """Part 2"""
  max_dimension = 20 if DATA == 'testdata202215.txt' else 4000000
  row = None
  for row in range(max_dimension):
    if not row % 100000:
      print(row)
    segments = MergeSegments(SegmentsInTargetRow(sensors_and_beacons, row))
    column = FoundX(segments, max_dimension)
    if column is not None:
      break
  tuning_frequency = 4000000 * column + row
  print(f'Part 2: at ({column}, {row}): {tuning_frequency}')


def main():
  """main"""
  lines = GetData(DATA)
  sensors_and_beacons = GetSensorsAndBeacons(lines)
  Part2(sensors_and_beacons)


if __name__ == '__main__':
  main()
