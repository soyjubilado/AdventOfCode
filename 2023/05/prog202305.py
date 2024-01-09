#!/usr/bin/python3
# file created 2023-Dec-04 21:09
# solved 2024-Jan-09
"""https://adventofcode.com/2023/day/5"""

from collections import namedtuple
from sys import maxsize as MAX_INT


DATA = 'data202305.txt'
# DATA = 'testdata202305.txt'


TransformMap = namedtuple('transform_map', 'dest_start, src_start, range_len')


def GetData(datafile):
  """Read input into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


class Transformer:
  """Transformer object."""
  def __init__(self, src, dest):
    self.src = src
    self.dest = dest
    self.maps = []
    self.endpoints = None

  def AddMap(self, map_str):
    """Translate a map string into a range object and a destination start"""
    dest_start, src_start, range_len = [int(i) for i in map_str.split()]
    self.maps.append(TransformMap(dest_start, src_start, range_len))

  def Transform(self, num):
    """Given a number, return the number it transforms into."""
    t = self.IsInInterval(num)
    if t:
      answer = t.dest_start + num - t.src_start
    else:
      answer = num
    return answer

  def TransformRange(self, t_range_list):
    """(For part 2) Given a single range (start, length), return a single
       range that represents the transforms for input range.

       Assumes that the ranges have been cleaned up, and they do not
       cross transform map borders.
    """
    answers = []
    for t_range in t_range_list:
      first, length = t_range
      new_first = self.Transform(first)
      answers.append((new_first, length))
    return answers

  def IsInInterval(self, num):
    """If num is in any interval in self.maps, return the map tuple
       that corresponds to the interval where num is found. Otherwise
       return False."""
    for t in self.maps:
      if t.src_start <= num < t.src_start + t.range_len:
        return t
    return False

  def MakeRangesContiguous(self):
    """Check if all the maps in self are contiguous; if not, return a list
       of additional maps that would make them contiguous"""
    ranges = sorted(self.maps, key=lambda x: x.src_start)
    fixes = []
    for i in range(1, len(ranges)):
      r_prev = ranges[i-1]
      r_this = ranges[i]
      if r_prev.src_start + r_prev.range_len != r_this.src_start:
        fixes.append(FixRange(r_prev.src_start, r_prev.range_len,
                              r_this.src_start))
    if fixes:
      self.maps.extend(fixes)

  def __repr__(self):
    return f'<{self.src} to {self.dest}> {self.maps}'


def SplitRange(t_range, self_maps):
  """Given a transform range, and a list of transform maps, split it up so
     that no subrange crosses a range boundary in self.maps. Returns a list
     of ranges."""
  maps = sorted(self_maps, key=lambda x: x.src_start)
  start_points = [i.src_start for i in maps]
  last_map = maps[-1]

  # add one more point to mark the beginning of the last unmapped section
  start_points.append(last_map.src_start + last_map.range_len)

  start, length = t_range
  higher_points = [i for i in start_points if i > start]

  # starting past the last point
  if not higher_points:
    return [(start, length)]

  next_point = min(higher_points)

  # next point is past the t_range
  if start + length - 1 < next_point:
    return [(start, length)]

  # the current range goes past the next point
  answer = []
  this_point = start
  this_length = next_point - start
  answer.append((this_point, this_length))
  next_length = length - this_length
  next_t_range = (next_point, next_length)
  answer.extend(SplitRange(next_t_range, self_maps))
  return answer


def FixRange(prev_start, prev_len, next_start):
  """Given the starts of two adjacent maps, and the length of the first one,
     return the map that would fill the gap between the two"""
  fix_start = prev_start + prev_len
  fix_len = next_start - fix_start
  fix_dest = fix_start
  return TransformMap(fix_dest, fix_start, fix_len)


def ParseMaps(lines):
  """Parse the input into a dictionary of tranform maps."""
  seeds_str = lines[0].split(':')[1]
  seeds = [int(i) for i in seeds_str.split()]

  transformers = {}
  new_trans = None
  for current in lines[2:]:
    if current.endswith('map:'):
      title = current.split()[0].split('-')
      source, dest = title[0], title[2]
      new_trans = Transformer(source, dest)
    if current and current[0].isdigit():
      new_trans.AddMap(current)
    if not current.strip():
      assert new_trans.src not in transformers
      transformers[new_trans.src] = new_trans

  assert new_trans.src not in transformers
  transformers[new_trans.src] = new_trans

  return seeds, transformers


def FullTransform(transformers, src_type, dest_type, num):
  """Given a dictionary of transformers, source & destination types, and a
     single starting number, return what the number transforms into at the
     destination type."""
  next_num = transformers[src_type].Transform(num)
  next_type = transformers[src_type].dest
  while next_type != dest_type:
    next_num = transformers[next_type].Transform(next_num)
    next_type = transformers[next_type].dest
  return next_num


def FullTransformRange(transformers, src_type, dest_type, t_ranges):
  """Given a dictionary of transformers, source & destination types, and a
     list of ranges, return what the number transforms into at the
     destination type."""
  next_type = transformers[src_type].dest

  # split each range if necessary
  self_map = transformers[src_type].maps
  split_ranges = []
  for t_range in t_ranges:
    split_subranges = SplitRange(t_range, self_map)
    split_ranges.extend(split_subranges)

  # transform each range
  next_ranges = transformers[src_type].TransformRange(split_ranges)

  if next_type == dest_type:
    return next_ranges
  return FullTransformRange(transformers, next_type, dest_type, next_ranges)


def Part1(lines):
  """Solve part 1"""
  seeds, transformers = ParseMaps(lines)
  lowest = MAX_INT
  for seed in seeds:
    loc = FullTransform(transformers, 'seed', 'location', seed)
    if loc < lowest:
      lowest = loc
  return lowest


def Part2(lines):
  """Solve part 2"""
  seeds, transformers = ParseMaps(lines)
  seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

  # fix all the transformer maps to eliminate gaps
  for t in transformers:
    transformers[t].MakeRangesContiguous()

  output = FullTransformRange(transformers, 'seed', 'location', seed_ranges)

  return min([i[0] for i in output])


def main():
  """main"""
  lines = GetData(DATA)
  print(f'Part 1: {Part1(lines)}')
  print(f'Part 2: {Part2(lines)}')


if __name__ == '__main__':
  main()
