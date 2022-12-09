#!/usr/bin/python3
#file created 2022-Dec-08 20:55
"""https://adventofcode.com/2022/day/9"""

from collections import defaultdict
DATA = 'data202209.txt'
# DATA = 'testdata202209.txt'


def GetData(datafile):
  """Put input data into a list of lines."""
  lines = []
  with open(datafile, 'r') as fh:
    lines = [i.strip() for i in fh]
  return lines


def MoveHead(start, direction):
  """Given start coordinates and direction, return next coordinates."""
  direction_map = {'R': (1, 0),
                   'L': (-1, 0),
                   'U': (0, 1),
                   'D': (0, -1)}
  x1, y1 = start
  x2, y2 = direction_map[direction]
  return x1 + x2, y1 + y2


def AreAdjacent(tail, head):
  """True if two coordinates are adjacent."""
  x_tail, y_tail = tail
  x_head, y_head, = head
  if (abs(x_head - x_tail) > 1 or abs(y_head - y_tail) > 1):
    return False
  return True


def MoveTail(tail, head):
  """Per the puzzle instructions, how the tail follows the head."""
  x_head, y_head = head
  x_tail, y_tail = tail
  if AreAdjacent(tail, head):
    return tail

  # Add +1, 0, or -1 to the tail to get it closer to the head
  y_tail += 0 if y_head == y_tail else (y_head - y_tail)//abs(y_head - y_tail)
  x_tail += 0 if x_head == x_tail else (x_head - x_tail)//abs(x_head - x_tail)

  return x_tail, y_tail


def GetGraphDimensions(lines):
  """Get the min and max coordinates for purpose of drawing the field."""
  head = (0, 0)
  head_seen = [head]
  for line in lines:
    direction, steps = line.split()
    for _ in range(int(steps)):
      head = MoveHead(head, direction)
      head_seen.append(head)
  x_min = x_max = y_min = y_max = 0
  for x, y in head_seen:
    x_min = x if x < x_min else x_min
    x_max = x if x > x_max else x_max
    y_min = y if y < y_min else y_min
    y_max = y if y > y_max else y_max
  return x_min, y_min, x_max, y_max


def PrintRope(rope, dimensions):
  """Print a graphic representation of the rope on the field.
     "dimensions" is the tuple returned by GetGraphDimensions.
  """
  invert_rope = defaultdict(lambda: '.')
  for i in range(9, 0, -1):
    invert_rope[rope[i]] = str(i) # dups will be overwritten by smallest no.
  invert_rope[rope[0]] = 'H'

  x_min, y_min, x_max, y_max = dimensions
  for y in range(y_max, y_min - 1, -1):
    for x in range(x_min, x_max + 1):
      print(f'{invert_rope[(x, y)]}', end='')
    print()


def Solver(lines, length=10):
  """Solve for a rope of arbitrary length. Works for Part 1 and Part 2."""
  rope = [(0, 0) for _ in range(length)]
  tail_seen = [(0, 0)]

  for line in lines:
    direction, steps = line.split()
    for _ in range(int(steps)):
      rope[0] = MoveHead(rope[0], direction)
      for idx in range(1, length):
        rope[idx] = MoveTail(rope[idx], rope[idx-1])
      tail_seen.append(rope[-1])

  return len(set(tail_seen))


def main():
  lines = GetData(DATA)
  print(f'Part 1: {Solver(lines, 2)}')
  print(f'Part 2: {Solver(lines, 10)}')


if __name__ == '__main__':
  main()
