#!/usr/bin/python3
#file created 2021-Dec-11 20:58
"""https://adventofcode.com/2021/day/12"""

from collections import defaultdict
DATA = 'data202112.txt'
# DATA = 'testdata202112.txt'

def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def GetVertexDictionary(lines):
  """Dictionary of vertex connectivity.
     key: vertex
     value: vertices that connect to this vertex
  """
  my_dict = defaultdict(lambda: [])
  for line in lines:
    a, b = line.split('-')
    my_dict[a].append(b)
    my_dict[b].append(a)
  return my_dict


class SpelunkerPt1(object):
  """Recursive tree solver for Part 1."""

  def __init__(self, vertex_dict):
    self.vdict = vertex_dict
    self.paths = []
    self.small_caves = set([i for i in vertex_dict if i.islower()])

  def NumPaths(self, vert, path_to_here):
    """Number of paths from this vertex to the end.
       0 if this leads to a duplicate small cave.
    """
    path_plus_here = path_to_here[:]
    path_plus_here.append(vert)
    if vert == 'end':
      self.paths.append(path_plus_here)
      return 1
    elif vert in self.small_caves and vert in path_to_here:
      return 0
    return sum([self.NumPaths(i, path_plus_here) for i in self.vdict[vert]])


class SpelunkerPt2(SpelunkerPt1):
  """Same as part 1 but with different rules."""

  def NumPaths(self, vert, path_to_here, cave_dupes=False):
    path_plus_here = path_to_here[:]
    path_plus_here.append(vert)
    if vert == 'end':
      self.paths.append(path_plus_here)
      return 1
    if path_to_here and vert == 'start':
      return 0
    elif vert in self.small_caves and vert in path_to_here and cave_dupes:
      return 0
    elif vert in self.small_caves and vert in path_to_here and not cave_dupes:
      cave_dupes = True
    return sum([self.NumPaths(i, path_plus_here, cave_dupes) for i in
                self.vdict[vert]])


def main():
  lines = GetData(DATA)
  vdict = GetVertexDictionary(lines)
  spelunker1 = SpelunkerPt1(vdict)
  print(f"Number of paths in Part 1: {spelunker1.NumPaths('start', [])}")
  spelunker2 = SpelunkerPt2(vdict)
  print(f"Number of paths in Part 2: {spelunker2.NumPaths('start', [])}")


if __name__ == '__main__':
  main()
