#!/usr/bin/python3
#file created 2021-Dec-18 21:02
"""https://adventofcode.com/2021/day/19"""

DATA = 'data202119.txt'
# DATA = 'testdata202119.txt'


def GetData(datafile):
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def ListToCoords(list_of_lines):
  """From one set of lines from scanner input, create a set of coords.
     The first line of list_of_lines is the scanner name '--- scanner 0 ---'
  """
  ret_val = []
  name = ' '.join(list_of_lines[0].split()[1:3])
  for line in list_of_lines[1:]:
    x, y, z = [int(i) for i in line.split(',')]
    ret_val.append((x, y, z))
  return name, ret_val


class Scanner(object):
  def __init__(self, name, beacons):
    self.name = name
    self.beacons = beacons
    self.transform = None

  def __str__(self):
    retval = self.name + '\n'
    for i in self.beacons:
      retval += f'{i}\n'
    return retval


def GroupScanners(lines):
  """Given line input, return a list of lists of coordinates.
     uses ALL the lines, including labels like '--- scanner 0 ---'
  """
  split_idx = lines.index('') # assumes clean input!
  scanners = []
  while split_idx:
    subgroup = lines[0:split_idx]
    name, list_of_coords = ListToCoords(subgroup)
    new_scanner = Scanner(name, list_of_coords)
    scanners.append(new_scanner)
    lines = lines[split_idx + 1:]
    try:
      split_idx = lines.index('')
    except ValueError:
      break
  name, list_of_coords = ListToCoords(lines)
  new_scanner = Scanner(name, list_of_coords)
  scanners.append(new_scanner)
  return scanners


def FlippedScans(list_of_coords):
  """Given a list of 3-D coordinates, return a list of 48 lists, each a
  different variation of those coordinates. There's only supposed to be 24, but
  I couldn't figure out which ones were valid transformations of 3-d coordinates
  and which ones were impossible mirror images. The 48 are generated by:
  reordering (x, y, z) (six combinations) and flipping the sign on one or more
  of x, y, z (eight combinations).
  """
  retval = []
  for a, b, c in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), 
                  (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]:
    group1 = []
    group2 = []
    group3 = []
    group4 = []
    group5 = []
    group6 = []
    for xx, yy, zz in list_of_coords:
      x = xx*a
      y = yy*b
      z = zz*c
      group1.append((x, y, z))
      group2.append((x, z, y))
      group3.append((y, x, z))
      group4.append((y, z, x))
      group5.append((z, x, y))
      group6.append((z, y, x))
    retval.append(group1)
    retval.append(group2)
    retval.append(group3)
    retval.append(group4)
    retval.append(group5)
    retval.append(group6)
  return retval


def Transform(list_of_coords, coord_t):
  """Given a list of coordinates, and a transform, add the transform to each
  item in the list and return the new list."""
  retval = []
  a, b, c = coord_t
  for x, y, z in list_of_coords:
    retval.append((x+a, y+b, z+c))
  return retval


def GetIntersectionYTransform(g0, g1):
  """Find intersection and transform between two groups. g1 already flipped.
     Will return None, None if no intersection > 12 is found.
  """
  ret_intersection = None
  ret_transform = None
  for x0, y0, z0 in g0:
    for x1, y1, z1 in g1:
      transform = (x0-x1, y0-y1, z0-z1)
      g1_new = Transform(g1, transform)
      intersection = set(g0).intersection(set(g1_new))
      if len(intersection) >= 12:
        ret_transform = transform
        ret_intersection = intersection
        return ret_intersection, ret_transform
  return ret_intersection, ret_transform


def FindBeaconsYTransform(g0, g1):
  """Find intersection and transform between two groups. g1 not flipped.
     Tries GetIntersectionYTransform on all flipped versions of g1.
  """
  for flipped_g1 in FlippedScans(g1):
    intersection, transform = GetIntersectionYTransform(g0, flipped_g1)
    if intersection:
      return flipped_g1, transform
  return None, None


def Part1():
  lines = GetData(DATA)
  scanners = GroupScanners(lines)
  found_scanners = scanners[0:1]
  recent_found_scanners = scanners[0:1]
  unfound_scanners = scanners[1:]

  count = 0
  transforms = []
  while unfound_scanners and count < 1000:
    count += 1
    just_found = []
    for unfound in unfound_scanners:
      fallen = False
      for found in recent_found_scanners:
        flipped_g, transform = FindBeaconsYTransform(found.beacons,
                                                     unfound.beacons)
        if flipped_g:
          unfound.beacons = Transform(flipped_g, transform)
          transforms.append(transform)
          print(f'matched {unfound.name} with {found.name}')
          break
      else:
        print(f'fell through: {unfound.name}')
        fallen = True
      if not fallen:
        found_scanners.append(unfound)
        just_found.append(unfound)
    for i in found_scanners:
      if i in unfound_scanners:
        unfound_scanners.remove(i)
    recent_found_scanners = just_found
    print(f'\nremaining unfound scanners: '
          f'{", ".join([i.name for i in unfound_scanners])}')
    print(f'\nall found scanners: '
          f'{", ".join([i.name for i in found_scanners])}\n')
  #endwhile

  beacons = set([])
  for scanner in found_scanners:
    beacons.update(scanner.beacons)
  print(f'part 1: {len(beacons)} beacons')
  transforms.append((0, 0, 0))
  with open('scanner_locations.py', 'w') as fh:
    fh.write(f'#!/usr/bin/python3\n\n')
    fh.write(f'SCANNER_LOCATIONS = [\n')
    for t in transforms:
      fh.write(f'  {t},\n')
    fh.write(f'  ]\n')


def Part2():

  def Distance(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)

  from scanner_locations import SCANNER_LOCATIONS
  from itertools import combinations
  pairs = combinations(SCANNER_LOCATIONS, 2)
  max_dist = 0
  max_pair = None
  for a, b in pairs:
    pair_distance = Distance(a, b)
    if pair_distance > max_dist:
      max_dist = pair_distance
      max_pair = (a, b)
  print(f'max distance is {max_dist} between {max_pair}')


if __name__ == '__main__':
  Part1()
  Part2()
